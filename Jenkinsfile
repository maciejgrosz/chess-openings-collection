pipeline{
    agent any
    environment{
        NEW_TAG = ""
    }

    stages {
        stage('checkout') {
            steps {
                deleteDir()
                checkout scm
                script{
                    sh "git fetch https://github.com/maciejgrosz/chess-openings-collection.git --tags"
                    env.GIT_COMMIT_MSG = sh (returnStdout: true, script: 'git log -1 --pretty=%B').trim()
                    def matcher = "${GIT_COMMIT_MSG}" =~ /^[0-9]+.[0-9]+/
                    if (matcher) {
                        env.TAGGING = "true"
                        env.VERSION = matcher[0]
                    } else {
                        env.TAGGIN = "false"
                        echo "No version provided"
                    }                
                }
            }
        }
        stage('build') {
            steps {
                script{
                    sh 'docker-compose up --build -d'
                }
            }
        }
        stage('unit & static tests'){
            steps {
                sh 'docker exec app pytest --black .'
                sh 'docker exec app pytest tests/unit_tests.py'
            }
        }
        stage('e2e tests'){
            steps {
                sh 'docker exec app pytest tests/e2e_tests.py'
            }
        }

        stage('tag'){
            when {
                allOf{
                    expression { env.TAGGING=="true" }                
                    branch "master"
                }
            }
            steps {
                script { 

                    TAG = sh(returnStdout: true, script: "git tag -l --sort version:refname \"${VERSION}.*\" | tail -1").trim()
                    if ("${TAG}" == ""){
                        NEW_TAG = "${VERSION}.0"
                    } else {
                        SUFFIX = sh(returnStdout: true, script: "echo '${TAG}' | cut -d '.' -f3 | cut -d ' ' -f1").trim()
                        SUFFIX = "${SUFFIX}" as int
                        ADDED =  SUFFIX + 1
                        NEW_TAG = "${VERSION}.${ADDED}"
                    }
                    echo "${NEW_TAG}"
                    sh "git clean -f"
                    sh "git tag ${NEW_TAG}"
                    withCredentials([string(credentialsId: 'github-token', variable: 'TOKEN')]) {
                        sh "git push https://maciejgrosz:${TOKEN}@github.com/maciejgrosz/chess-openings-collection.git --tags"
                    }
                }
            }
        } 
        stage('Publish'){
            when {
                allOf{
                    expression { env.TAGGING=="true" }                
                    branch "master"
                }
            }
            steps {
                script{
                    sh 'aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com'

                    sh 'docker build -t maciej_groszyk_portfolio openings-collection/'
                    sh "docker tag maciej_groszyk_portfolio:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:${NEW_TAG}"
                    sh "docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:${NEW_TAG}"                

                    sh "docker build -t maciej_groszyk_chess_nginx ./nginx"
                    sh "docker tag maciej_groszyk_chess_nginx:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_chess_nginx:${NEW_TAG}"
                    sh "docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_chess_nginx:${NEW_TAG}"
                }
            }
        }
        stage('Deploy'){
            when {
                allOf{
                    expression { env.TAGGING=="true" }                
                    branch "master"
                }
            }
            steps{
                script {
                    sh 'aws eks --region eu-west-1 update-kubeconfig --name MG-portfolio-cluster'
                    sh 'git clone https://github.com/maciejgrosz/chess-openings-helmcharts'
                    withCredentials([string(credentialsId: 'github-token', variable: 'TOKEN')]) {
                        sh "bash patch_tag.sh ${NEW_TAG} ${TOKEN}"
                    }
                }
            }
        }
    }
    post {  
        failure {  
            emailext recipientProviders: [culprits()],
            subject: 'Build failure', body: 'OMG, you broke the build!',
            attachLog: true, compressLog: true
        } 
        success {
            emailext recipientProviders: [culprits()],
            subject: 'Build success gratz!', body: 'OMG, you did it!',
            attachLog: true, compressLog: true
        } 
    }  
} 
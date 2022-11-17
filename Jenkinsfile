pipeline{
    agent any

    stages {
        stage('checkout') {
            steps {
                deleteDir()
                checkout scm
                script{
                    withCredentials([string(credentialsId: 'token', variable: 'TOKEN')]) { 
                        sh "git fetch http://jenkins:$TOKEN@35.176.222.34/maciejgroszyk/analytics --tags"
                    }
                    env.GIT_COMMIT_MSG = sh (returnStdout: true, script: 'git log -1 --pretty=%B').trim()
                    echo "${GIT_COMMIT_MSG}"               }
            }
        }
        stage('calculate tag'){
            steps {
                script {
                    TAG=env.GIT_BRANCH.split('\\/') 
                    echo "${TAG}"
                    VERSION= TAG[1]
                    TAG = sh(returnStdout: true, script: "git tag --sort version:refname \"${VERSION}.*\" | tail -1").trim()
                    if ("${TAG}" == ""){
                        NEW_TAG = "${VERSION}.0"
                    } else {
                        SUFFIX = sh(returnStdout: true, script: "echo '${TAG}' | cut -d '.' -f3 | cut -d ' ' -f1").trim()
                        SUFFIX = "${SUFFIX}" as int
                        ADDED =  SUFFIX + 1
                        NEW_TAG = "${VERSION}.${ADDED}"
                    }
                    echo "${NEW_TAG}"
                    sh "mvn versions:set -DnewVersion=${NEW_TAG}"
                    sh "mvn versions:commit"
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
                script{
                    sh 'curl 35.176.222.34:5000/health'
                    sh 'curl 35.176.222.34:8082/health'
                }
            }
        }
        stage('e2e tests'){
            steps {
                script{
                    sh 'echo e2e tests'
                }
            }
        }
        stage('Publish'){
            steps {
                script{
                    sh 'echo publish'
                }
            }
        }
        stage('deploy app on ecr') {
            steps{
                script{
                    sh 'aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com'
                    sh 'docker build -t maciej_groszyk_portfolio openings-collection/'
                    sh 'docker tag maciej_groszyk_portfolio:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:latest'
                    sh 'docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:latest'
                }
            }
        }
        stage('deploy nginx on ecr'){
            steps{ 
                script{
                    sh "docker build -t maciej_groszyk_chess_nginx ./nginx"
                    sh "docker tag maciej_groszyk_chess_nginx:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_chess_nginx:latest"
                    sh "docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_chess_nginx:latest"
                }
            }
        }
        stage('report'){
            steps{
                script{
                    sh 'echo report'
                }
            }
        }
    }
}
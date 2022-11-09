pipeline{
    agent any

    stages {
        stage('checkout') {
            steps {
                deleteDir()
                checkout scm
                script{
                    LOG = sh(returnStdout: true, script: 'git log --graph --oneline --decorate | head -1').trim()
                }
            }
        }
        stage('build') {
            steps {
                sh 'aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com'
                sh 'docker build -t maciej_groszyk_portfolio openings-collection/'
                sh 'docker tag maciej_groszyk_portfolio:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:latest'
                sh 'docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:latest'
            }
        }
        stage('run app'){
            steps{
                sh 'docker-compose down'
                sh 'docker-compose up -d --build'
            }
        }
    }
}
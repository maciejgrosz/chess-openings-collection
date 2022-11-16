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
                sh 'docker-compose up --build -d'
            }
        }
        stage('unit & static tests'){
            steps {
                
                sh 'curl localhost:5000'
            }
        }
        stage('package'){
            steps {
                sh 'echo package'
            }
        }
        stage('e2e tests'){
            steps {
                sh 'echo e2e tests'
            }
        }
        stage('Publish'){
            steps {
                sh 'echo publish'
            }
        }
        stage('deploy app on ecr') {
            sh 'aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com'
            sh 'docker build -t maciej_groszyk_portfolio openings-collection/'
            sh 'docker tag maciej_groszyk_portfolio:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:latest'
            sh 'docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_portfolio:latest'
        }
        stage('deploy nginx on ecr'){
            sh "docker build -t maciej_groszyk_chess_nginx ./nginx"
            sh "docker tag maciej_groszyk_chess_nginx:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_chess_nginx:latest"
            sh "docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciej_groszyk_chess_nginx:latest"
        }
        stage('report'){
            sh 'echo report'
        }
    }
}
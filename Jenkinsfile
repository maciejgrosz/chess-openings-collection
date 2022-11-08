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
        stage('run app'){
            steps{
                sh 'docker-compose up -d --build'
            }
        }
    }
}
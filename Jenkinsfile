pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build images') {
            steps {
                sh "bash build.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "bash deploy.sh"
            }
        }
    }
}

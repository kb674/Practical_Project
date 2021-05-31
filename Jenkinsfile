pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "./test.sh"
            }
        }
        stage('Build images') {
            steps {
                sh "./build.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "./deploy.sh"
            }
        }
    }
}

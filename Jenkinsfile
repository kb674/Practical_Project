pipeline {
    agent any
    environment {
        DOCKERHUB_DETAILS = credentials("DOCKERHUB_DETAILS")
    }
    stages {
        stage('test') {
            steps {
                sh "./scripts/test.sh"
            }
        }
        stage('build images') {
            steps {
                sh "./scripts/build.sh"
            }
        }
        stage('push images') {
            steps {
                sh "./scripts/push.sh"
            }
        }
        stage('configure') {
            steps {
                sh "./scripts/configure.sh"
            }
        }
        stage('deploy') {
            steps {
                sh "./scripts/deploy.sh"
            }
        }
    }
}

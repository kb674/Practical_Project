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
        stage('test reports') {
            steps {
                junit 'test-results.xml'
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
        stage('deploy') {
            steps {
                sh "./scripts/deploy.sh"
            }
        }
    }
}

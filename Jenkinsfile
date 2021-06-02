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
        post('test reports') {
            steps {
                sh "./scripts/test.sh"
            }
        }
        stage('build images') {
            steps {
                junit 'test-results.xml'
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

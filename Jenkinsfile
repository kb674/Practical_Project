pipeline {
    agent any
    environment {
        DOCKERHUB_DETAILS = credentials("DOCKERHUB_DETAILS")
        DATABASE_URI = credentials("DATABASE_URI")
        MYSQL_ROOT_PASSWORD = credentials("MYSQL_ROOT_PASSWORD")
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

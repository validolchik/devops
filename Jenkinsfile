pipeline {
    agent { docker { image 'python:3.8.5' } }
    stages {
        stage('build') {
            steps {
                sh 'echo build'
            }
        }
        stage('test') {
            steps {
                sh 'echo test'
            }
        }
    }
}
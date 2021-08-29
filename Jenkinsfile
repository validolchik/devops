pipeline {
//     agent { docker { image 'python:3.8.5' } }
    agent {any}
    stages {
        stage('checkout') {
            steps{
                checkout scm
            }
        }
        stage('setup') {
            steps {
                sh "ls -la"
                sh"""
                pip install -r app_python/requirements.txt
                """
            }
        }
        stage('Unit Testing') { // Perform unit testing
        steps {
            script {
                sh """
                cd app_python
                python -m pytest
                """
                }
            }
        }
        stage('build') {
            steps {
                sh 'echo build'
            }
        }
        stage('test') {
            steps {
                sh 'echo test app'
            }
        }
    }
}
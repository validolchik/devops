pipeline {
    agent {
        docker {
            image 'python:3.8-slim-buster'
            args '-u root'
        }
    }

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
                pip3 install -r app_python/requirements.txt
                """
            }
        }
        stage('Linting') {
             steps {
                 dir('app_python') {
                     sh "pylama -i W,E501"
                     sh "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                         flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics"
                 }
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
    }
}
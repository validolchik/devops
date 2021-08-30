pipeline {
    environment {
        APP_PATH = 'app_python'
        IMAGE_NAME = 'moscow_time'
        DOCKER_HUB_USERNAME = 'validolchik'
    }

    agent {
        docker {
            image 'python:3.8-slim-buster'
            args '-u root -v $HOME/.cache:/root/.cache -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('setup') {
            steps {
                dir("${APP_PATH}"){
                    sh"""
                    pip3 install -r requirements.txt
                    apt-get update && apt-get install -y docker.io
                    """
                }
            }
        }

        stage('Linting') {
             steps {
                 dir("${APP_PATH}") {
                     sh "pylama -i W,E501"
                     sh "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics"
                     sh "flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics"
                 }
             }
         }

        stage('Unit Testing') { // Perform unit testing
            steps {
                dir("${APP_PATH}"){
                    sh """
                    python -m pytest
                    """
                }
                }
            }

        stage('build') {
            steps {
                dir("${APP_PATH}") {
                    script {
                        def image = docker.build('$DOCKER_HUB_USERNAME/$IMAGE_NAME:latest', '.')
                        docker.withRegistry('', 'docker-hub-creds') {
                            image.push()
                        }
                    }
                }
            }
        }
    }
}
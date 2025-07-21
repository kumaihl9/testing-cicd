pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-python-app'
        CONTAINER_NAME = 'python-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                cleanWs()
                sh 'git --version' 
                sh 'ls -la'
                git url: 'https://github.com/kumaihl9/testing-cicd.git', branch: 'main', credentialsId: 'test'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop and Remove Old Container') {
            steps {
                sh '''
                    docker-compose down || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker-compose up -d --build
                '''
            }
        }
    }
}

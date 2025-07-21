pipeline {
    agent any

    environment {
        IMAGE_NAME = "kumailh01/jenkins"
        CONTAINER_NAME = "python_app_container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/kumaihl9/testing-cicd.git'
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
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p 8000:8000 $IMAGE_NAME'
            }
        }

        // Optional: Push to Docker Hub
        // stage('Push to Docker Hub') {
        //     steps {
        //         withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
        //             sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
        //             sh "docker push $IMAGE_NAME"
        //         }
        //     }
        // }
    }
}

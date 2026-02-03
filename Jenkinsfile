pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        ECR_REPO   = '135234114190.dkr.ecr.eu-north-1.amazonaws.com/python-devsecops-app'
        IMAGE_NAME = 'python-devsecops-app'
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Dependency Scan - pip-audit') {
            steps {
                sh '''
                docker run --rm \
                  -v $(pwd):/src \
                  -w /src \
                  python:3.12-slim \
                  sh -c "pip install --no-cache-dir pip-audit && pip-audit -r requirements.txt --progress-spinner off || true"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Container Scan - Trivy') {
            steps {
                sh '''
                docker run --rm \
                  -v /var/run/docker.sock:/var/run/docker.sock \
                  aquasec/trivy image \
                  --severity HIGH,CRITICAL \
                  --no-progress \
                  $IMAGE_NAME:latest || true
                '''
            }
        }

        stage('Login to AWS ECR') {
            steps {
                withCredentials([
                    string(credentialsId: 'AWS_ACCESS_KEY_ID', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'AWS_SECRET_ACCESS_KEY', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                    sh '''
                    export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
                    export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

                    aws ecr get-login-password --region $AWS_REGION \
                    | docker login --username AWS --password-stdin 135234114190.dkr.ecr.eu-north-1.amazonaws.com
                    '''
                }
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh '''
                docker tag $IMAGE_NAME:latest $ECR_REPO:latest
                docker push $ECR_REPO:latest
                '''
            }
        }
    }
}

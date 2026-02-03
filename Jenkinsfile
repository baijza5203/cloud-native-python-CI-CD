pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        AWS_ACCOUNT_ID = '135234114190'
        ECR_REPO = 'python-devsecops-app'
        IMAGE_NAME = 'python-devsecops-app'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

        // 🔑 IMPORTANT CHANGE
        IMAGE_TAG = "${BUILD_NUMBER}"
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
                sh '''
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
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
                  $IMAGE_NAME:$IMAGE_TAG || true
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
                    export AWS_DEFAULT_REGION=$AWS_REGION

                    aws ecr get-login-password --region $AWS_REGION \
                    | docker login --username AWS --password-stdin $ECR_REGISTRY
                    '''
                }
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh '''
                docker tag $IMAGE_NAME:$IMAGE_TAG $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG
                docker push $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl set image deployment/python-app \
                python-app=$ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG

                kubectl rollout status deployment/python-app
                '''
            }
        }
    }
}

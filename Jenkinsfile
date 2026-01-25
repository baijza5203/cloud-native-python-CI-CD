pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        ECR_REPO = '135234114190.dkr.ecr.eu-north-1.amazonaws.com/python-devsecops-app'
        IMAGE_NAME = 'python-devsecops-app'
    }

    stages {

        stage('Checkout Code') {
            steps {
                // Checkout from GitHub using PAT credential
                git branch: 'main',
                    url: 'https://github.com/Ayusheeuke/cloud-native-python-CI-CD-.git',
                    credentialsId: 'github-creds'
            }
        }

        // Optional: SonarQube stage skipped for now
        // stage('SAST - SonarQube') {
        //     steps {
        //         withSonarQubeEnv('sonarqube') {
        //             sh '''
        //             sonar-scanner \
        //             -Dsonar.projectKey=cloud-native-python \
        //             -Dsonar.sources=. \
        //             -Dsonar.language=py
        //             '''
        //         }
        //     }
        // }

        stage('Dependency Scan - pip-audit') {
            steps {
                // No sudo needed, pip-audit already installed on agent
                sh 'pip-audit -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Container Scan - Trivy') {
            steps {
                sh "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --severity HIGH,CRITICAL ${IMAGE_NAME}:latest"
            }
        }

        stage('Login to ECR') {
            steps {
                sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}"
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh "docker tag ${IMAGE_NAME}:latest ${ECR_REPO}:latest"
                sh "docker push ${ECR_REPO}:latest"
            }
        }
    }
}

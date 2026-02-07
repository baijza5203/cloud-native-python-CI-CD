**Cloud-Native DevSecOps CI/CD Pipeline on AWS**

**Project Overview**
This project demonstrates a complete Cloud-Native DevSecOps CI/CD Pipeline deployed on AWS using
modern DevOps + Security tools.

It covers the full lifecycle of application delivery including:
- Continuous Integration (CI)
- Security Scanning (DevSecOps)
- Containerization & Image Management
- GitOps-based Continuous Deployment (CD)
- Kubernetes Orchestration
- Monitoring & Observability
  
The main objective of this project is to build an end-to-end automated pipeline where code changes
pushed to GitHub are tested, scanned, containerized, and deployed into a Kubernetes cluster with
real-time monitoring.

**Architecture**

This project implements a Cloud-Native DevSecOps architecture using AWS, Jenkins, Docker,
Kubernetes, Helm, ArgoCD, and monitoring tools.

High-Level Architecture Flow
1. Developer pushes source code to GitHub
2. Jenkins triggers the CI pipeline
3. Code Quality + Security Scans are performed
4. Docker image is built and pushed to Amazon ECR
5. ArgoCD syncs Kubernetes manifests using GitOps
6. Application is deployed to Kubernetes worker node
7. Prometheus collects metrics and Grafana visualizes dashboards
8. Ingress exposes the application externally

**Architecture Flow Diagram**
Developer → GitHub → Jenkins → Amazon ECR → Kubernetes
                                          ↓
                               Helm-installed tools
                         (ArgoCD, Prometheus, Grafana)
                                          ↓
                                   Ingress → User

**Infrastructure Setup**

This project uses three AWS EC2 instances:
- Jenkins EC2: Runs Jenkins CI/CD pipeline
- Kubernetes Master: Control plane + Helm + ArgoCD + Monitoring
- Kubernetes Worker: Runs application pods
Kubernetes cluster is created using kubeadm.

**CI/CD Pipeline Workflow**

Continuous Integration (CI)
Jenkins performs the following steps:
- Pulls source code from GitHub
- Static Code Analysis using SonarQube
- Dependency Vulnerability Scan using pip-audit
- Container Image Scan using Trivy
- Builds Docker image
- Pushes Docker image to Amazon ECR

Continuous Deployment (CD - GitOps)
Deployment is handled using ArgoCD:
- ArgoCD continuously monitors the GitHub repository
- Automatically syncs Kubernetes manifests
- Deploys the application into the Kubernetes cluster
- Ensures declarative and version-controlled deployments
  
Kubernetes Deployment
- Application runs as pods in the worker node
- Kubernetes Service provides networking and stable access
- NGINX Ingress Controller exposes the application externally
- Kubernetes pulls Docker images securely from Amazon ECR
  
Helm Integration
Helm is used to install and manage Kubernetes applications such as:
- ArgoCD
- Prometheus
- Grafana
  
Monitoring & Observability
Prometheus
- Collects cluster metrics and application metrics
- Tracks CPU, memory, pod status, node health
Grafana
- Visualizes metrics using dashboards
- Provides real-time monitoring insights
  
DevSecOps Security Integration
Security is integrated into the CI pipeline (Shift-Left Security):
- SonarQube → Code quality and static analysis
- pip-audit → Python dependency vulnerability scanning
- Trivy → Container vulnerability scanning
- Secure Docker image storage in Amazon ECR

**Tools & Technologies Used**
Version Control: Git, GitHub
CI/CD: Jenkins
Containerization: Docker
Security Tools: SonarQube, pip-audit, Trivy
Cloud: AWS EC2, Amazon ECR
Orchestration: Kubernetes (kubeadm)
GitOps: ArgoCD
Package Manager: Helm
Monitoring: Prometheus, Grafana
Networking: NGINX Ingress Controller

**Project Features**

- Fully automated CI/CD pipeline
- Dockerized Python application
- Kubernetes master-worker cluster setup
- GitOps deployment using ArgoCD
- Security scanning integrated in CI
- Monitoring with Prometheus & Grafana
- Application exposed using Ingress
  
**Setup & Installation (High-Level Steps)**
1. Clone Repository
git clone <your-repo-url>
cd <repo-folder>
2. Configure Jenkins Pipeline
- Install Jenkins on EC2
- Add required plugins (Git, Docker, Pipeline)
- Configure credentials for GitHub and AWS ECR
3. Setup Kubernetes Cluster (kubeadm)
- Initialize master node
- Join worker node
- Configure kubectl access
4. Push Docker Image to ECR
Jenkins automatically builds and pushes the Docker image to ECR.
5. Install Tools Using Helm
helm install argocd ...
helm install prometheus ...
helm install grafana ...
6. Configure ArgoCD GitOps Deployment
- Connect GitHub repo to ArgoCD
- Sync manifests
- Deploy application automatically
7. Access Application Using Ingress
Ingress exposes the service publicly through EC2 public IP.

**Future Enhancements**
- Add automated Kubernetes deployment using Jenkins + ArgoCD integration
- Add Falco runtime security monitoring
- Add TLS/HTTPS using cert-manager
- Add log monitoring using ELK Stack / Loki
- Implement RBAC policies in Kubernetes
- 
**Author**
Baijza Khade
Post Graduate Diploma in IT Infrastructure and System Security
Cloud | DevOps | DevSecOps | Kubernetes | AWS

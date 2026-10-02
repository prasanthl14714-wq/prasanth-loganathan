pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/prasanthl14714-wq/prasanth-loganathan.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-node-app:latest .'
            }
        }

        stage('Security Scan with Trivy') {
            steps {
                sh 'trivy image my-node-app:latest'
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker run -d -p 3000:3000 my-node-app:latest'
            }
        }
    }
}

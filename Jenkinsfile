pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t \"irw-backend\" .'
            }
        }

        stage('Stop and Remove Existing Container') {
            steps {
                sh 'docker stop irw-backend || true'
                sh 'docker rm irw-backend || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --restart always --name \"irw-backend\" -p 8012:8004 \"irw-backend\"'
            }
        }
    }
}

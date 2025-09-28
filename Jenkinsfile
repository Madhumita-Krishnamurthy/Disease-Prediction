pipeline {
    agent any

    environment {
        APP_NAME = 'streamlit-app'
        IMAGE_NAME = 'my-streamlit-app'
        AWS_EC2_USER = 'ubuntu'
        AWS_EC2_HOST = '3.109.143.79'
        DEPLOY_PATH = '/home/ubuntu/streamlit-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Madhumita-Krishnamurthy/Disease-Prediction.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Save Docker Image') {
            steps {
                sh 'docker save $IMAGE_NAME | gzip > $IMAGE_NAME.tar.gz'
            }
        }

        stage('Copy to EC2') {
            steps {
                sh 'scp -o StrictHostKeyChecking=no $IMAGE_NAME.tar.gz $AWS_EC2_USER@$AWS_EC2_HOST:$DEPLOY_PATH/'
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no $AWS_EC2_USER@$AWS_EC2_HOST << EOF
                cd $DEPLOY_PATH
                docker load < $IMAGE_NAME.tar.gz
                docker stop $APP_NAME || true
                docker rm $APP_NAME || true
                docker run -d --name $APP_NAME -p 8501:8501 $IMAGE_NAME
                EOF
                '''
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/nadeemr5/todoapp.git'
            }
        }

        stage('Set up Python') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python todoapp.py
                '''
            }
        }
    }
}

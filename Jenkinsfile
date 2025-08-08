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
                "C:\\Users\\Adnaan\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                call venv\\Scripts\\activate
                venv\\Scripts\\pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
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

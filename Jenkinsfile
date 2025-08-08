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
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                . venv/bin/activate
                python3 todoapp.py
                '''
            }
        }
    }
}

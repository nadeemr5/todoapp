pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Users\\Adnaan\\AppData\\Local\\Programs\\Python\\Python313'
        PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${env.PATH}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/nadeemr5/todoapp.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                bat 'python --version'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run App for Test') {
            steps {
                script {
                    bat '''
                    echo Starting app in test mode...
                    venv\\Scripts\\python -c "import threading, time; from todoapp import app; threading.Thread(target=app.run, kwargs={'debug': False}).start(); time.sleep(5); print('App test completed.')"
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }
        success {
            echo 'Build finished successfully!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}

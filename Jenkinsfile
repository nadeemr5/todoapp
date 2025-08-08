pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Users\\Adnaan\\AppData\\Local\\Programs\\Python\\Python313'
        PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${env.PATH}"
    }

    stages {
        stage('Set up Python Environment') {
            steps {
                bat 'python --version'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run App for Test') {
            steps {
                bat '''
                echo Performing Flask app import test...
                venv\\Scripts\\python -c "from todoapp import app; print('Flask app imported successfully')"
                '''
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

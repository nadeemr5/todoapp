pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Users\\Adnaan\\AppData\\Local\\Programs\\Python\\Python313'
        PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${env.PATH}"

        EC2_HOST = ''
        EC2_USER = 'deploy'
        APP_DIRECTORY = ''
        SERVICE_NAME = 'todoapp'
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
        stage('Build') {
            'docker ...'
        }

        stage('Deploy') {
            steps {
                sshagent(credentials: ['ec2 DEPLOYMENT KEY....']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} 'mkdir -p ${APP_DIRECTORY}/releases/${BUILD_NUMBER}'
                        rsync -az --delete -e "shh -o StrictHostKeyChecking=no" dist/  ${EC2_USER}@${EC2_HOST}:${APP_DIRECTORY}/releases/${BUILD_NUMBER}/
                    ""
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

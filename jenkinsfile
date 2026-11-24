
pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                bat 'python -m unittest test_main.py'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t student-grade-app .'
            }
        }
    }
}

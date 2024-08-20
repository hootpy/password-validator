pipeline {
    agent any
    stages {
        stage('Build pre-requisites') {
            steps {
                echo 'Installing dependencies'
                sh 'poetry install'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                sh 'poetry run pytest --tb=no -v'
            }
        }

        stage('Build') {
            steps {
                sh 'poetry build -f sdist'
            }
        }

         stage('Archive Artifacts') {
            steps {
                // Archive the files as artifacts
                archiveArtifacts artifacts: 'dist/*.gz', allowEmptyArchive: true
            }
        }
    }
}
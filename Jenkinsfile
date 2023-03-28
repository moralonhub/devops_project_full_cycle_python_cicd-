pipeline {
    agent any
    environment {
        IMAGE_REPO_NAME="devops_project_full_cycle_python_cicd"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {
        // checkout git dev branch to working directory
        stage('Cloning Git') {
            steps {
                git branch: 'dev', credentialsId: 'github', url: 'https://github.com/moralonhub/devops_project_full_cycle_python_cicd-.git'
            }
        }

        // docker build 
        stage('Build') {
            steps {

                script {
                    withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                    credentialsId: 'aws_credentials'
                    ]]) {
                        sh 'docker build --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -t moralon/devops_project_full_cycle_python_cicd:${BUILD_NUMBER} .'
                    }
                }
            }
        }
        // login to dockerhub
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        // push to dockerhub
        stage('Push') {
            steps {
                sh 'docker push moralon/devops_project_full_cycle_python_cicd:${BUILD_NUMBER}'
            }
        }

    }
}
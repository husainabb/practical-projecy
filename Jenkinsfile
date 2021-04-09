pipeline {
    agent any

     environment {
         COMPOSE_FILE = "docker-compose.yml"
     }
    stages{

        stage('Stage 1: Build'){
                sh "docker-compose build"
                sh "docker-compose up -d"
            }
        }

    
        }
    

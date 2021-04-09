pipeline {
    agent any

     environment {
         COMPOSE_FILE = "docker-compose.yml"
     }
    stages{

        stage('Stage 1: Build'){
            steps{

                sh "sudo docker-compose build"
            }
        }

        stage('Stage 2: Run'){
            steps{
                sh "sudo docker-compose up -d"
            }
        }
    }
}
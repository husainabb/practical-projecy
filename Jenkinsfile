pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        docker-hub-credentials = credentials("docker-hub-credentials")
    }
    stages{
        stage('Test'){
            steps{
                sh 'bash ./testing.sh' 
                
            }
        }
        stage('Build'){
            steps{
                sh 'docker-compose build'
                
            }
        }
        stage('Push'){
            steps{
            sh "docker login --username=$docker-hub-credentials_USR --password=PSW"
            sh 'docker ps && docker images'
            sh 'docker-compose push'
           
            }
        }
        stage('Configure Swarm'){
            steps{
            sh 'cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml'
            
        }
        }
        stage('Deploy'){
            steps{
            sh 'bash deploy.sh'
            }
        }
    }
}
pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        // DOCKERHUB= credentials("docker-hub-credentials")
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
            // sh "sudo docker login --username=$DOCKERHUB_USR --password=DOCKERHUB_PSW"
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
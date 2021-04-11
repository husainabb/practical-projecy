pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
    }
    stages{
        stage('Test'){
            steps{
                // sh 'bash ./testing.sh' 
                sh ""
            }
        }
        stage('Build'){
            steps{
                // sh 'docker-compose build'
                sh ""
            }
        }
        stage('Push'){
            steps{
            // sh 'docker ps && docker images'
            // sh 'docker-compose push'
            sh ""
            }
        }
        stage('Configure Swarm'){
            steps{
            // sh 'cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml'
            sh ""
        }
        }
        stage('Deploy'){
            steps{
            // sh 'bash deploy.sh'
            sh ""
            }
        }
    }
}
pipeline{

        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
            app_version = "version1"
        }
        stages{
            stage('Test'){
                steps{
                    sh "bash pytest.sh"
                    }
                }
            stage('Build'){
                steps{
                    sh "docker-compose build"
                    sh "docker-compose up -d"
                    }
            }  
        } 
}     
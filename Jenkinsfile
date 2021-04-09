pipeline{
        agent any
        environment{
            app_version = "version1"
        }


        stages{
            stage('Build Image'){
                steps{
                    sh "sudo docker-compose build"
                    sh "sudo docker-compose up -d"
                        
                    }
                }
                  
        }
}


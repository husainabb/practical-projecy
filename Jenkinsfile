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
            stage("Push"){
                steps{
                      docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                            image.push("${env.app_version}")
                }
            }
         
            }
}

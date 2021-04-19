pipeline{
    environment {
    app =''
    }
    agent any

    stages{
    stage('Cloning Git') {
                /* Let's make sure we have the repository cloned to our workspace */
            steps {
                checkout scm
            }
            }

    stage('Build-and-Tag') {
         app = docker.build("venmaum/udaystj-be-services:{env.BUILD_ID}")
    }
    }
    stage('Post-to-dockerhub') {
        docker.withRegistry('https://registry.hub.docker.com', 'Docker_credentials') {
                app.push("latest")
                        }
    }
}
}
pipeline{
    environment {
    app =''
    }
    agent any

    stages{
    stage('Initialize'){
    steps {

         stage('Cloning Git') {
                /* Let's make sure we have the repository cloned to our workspace */
            steps {
                checkout scm
            }
            }
    stage('Build-and-push') {
        steps {
            docker.withRegistry('https://registry.hub.docker.com', 'Docker_credentials') {

        def customImage = docker.build("udays-tj-backend-app:${env.BUILD_ID}")

        /* Push the container to the custom Registry */
        customImage.push("latest")
    }
          }
    }

    }
}
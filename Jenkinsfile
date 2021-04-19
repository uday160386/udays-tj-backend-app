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
        steps {
        echo 'Starting to build docker image'
            script {
        def app = docker.build("venmaum/udaystj-be-services:{env.BUILD_ID}")
        }
    }
    }
    stage('Post-to-dockerhub') {
    steps {
        script {
        docker.withRegistry('https://registry.hub.docker.com', 'Docker_credentials') {
                app.push("latest")
                        }
            }
    }
    }
//     stage('tests') {
//         steps {
//
//                 sh "newman run /tests/Django-REST-Backend-Testing.postman_collection.json -e /tests/env/Django-REST-Backend-Dev_env.postman_environment.json -d /tests/data/data.csv"
//             }
//     }
//      stage('SECURITY-IMAGE-SCANNER') {
//             steps {
//                 sh 'echo "docker.io/venmaum/udaystj-be-services `pwd`/Dockerfile" > anchore_images'
//                 anchore name: 'anchore_images'
//             }
//         }
}
}
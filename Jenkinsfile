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
    stage('Unit-Tests') {
            /* Stage where Unit test scripts will be executed */
            steps {
                sh 'echo "Unit Tests"'
            }
    }
    stage('contract-Tests') {
            /* Stage where contract test scripts will be executed. Tools can be pact.io */
            steps {
                sh 'echo "contract Tests"'
            }
    }
    stage('Build-and-Tag') {
        steps {
            script {
        app = docker.build "venmaum/udaystj-be-services:latest"
        }
    }
    }
    stage('Post-to-dockerhub') {
        /* Stage where Docker image will be pushed to AWS ECR*/
    steps {
        script {
        docker.withRegistry('https://registry.hub.docker.com', 'Docker_credentials') {
                app.push("latest")
                        }
            }
    }
    }
    stage('Running Image in Kubernetes') {
    /* Stage where Docker image will be running with AWS EKS */
    steps {
                sh 'echo "deploying to k8"'
            }
    }


   stage('tests-report') {
   steps {

                sh '''#!/bin/bash
                export PATH=/even/more/path:$PATH
                newman run tests/Django-REST-Backend-Testing.postman_collection.json -e tests/env/Django-REST-Backend-Dev_env.postman_environment.json -d tests/data/data.csv -r htmlextra --reporter-htmlextra-export ./results/report.html
                '''

                publishHTML target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: true,
                        reportDir: './results',
                        reportFiles: 'report.html',
                        reportName: 'HTML Report'
                         ]
                }

             script{
             try {

             def e2e = build job:'tests-report', propagate: false
               result = e2e.result
               if (result.equals("SUCCESS")) {
               } else {
                  sh "exit 1" // this fails the stage
               }
             }
        }
        } catch (e) {
           result = "FAIL" // make sure other exceptions are recorded as failure too

             }
}
        }

     stage('performance-Tests') {
            /* Stage where automated performance tests will be executed.Tools will be locust or jmeter */
            steps {
                sh 'echo "performance Tests"'
            }
        }
        stage('security-Tests') {

        /* Stage where security tests will be running */
        steps {
                sh 'echo "security Tests"'
            }
        }
}
}
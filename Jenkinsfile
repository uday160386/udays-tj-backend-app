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
    }
    stage('Unit-Tests') {
            /* Stage where contract test scripts will be executed. Tools can be pact.io */
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
            }
     stage('performance-Tests') {
            /* Stage where automated performance tests will be executed.Tools will be locust or jmeter */
        }
        stage('security-Tests') {

        /* Stage where security tests will be running */
        }
}
}
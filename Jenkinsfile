pipeline{
    environment {
     PATH = "/bin/sh:$PATH"
    app =''
    }
    agent any

    stages{
    stage('tests') {
        steps {

         export PATH=/even/more/path:$PATH
        sh '''#!/bin/bash
                newman run tests/Django-REST-Backend-Testing.postman_collection.json -e tests/env/Django-REST-Backend-Dev_env.postman_environment.json -d tests/data/data.csv -r htmlextra --reporter-htmlextra-export ./results/report.html
                '''
            }
    }
    }
}
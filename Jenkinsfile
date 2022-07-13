#!groovy
// Run docker build
// properties([disabledConcurrentBuilds()])
pipeline {
    agent any
     stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t diplom:local ."
                sh "docker run diplom:local pytest -s -v tests/test_status_code.py"
            }
        }
    }
}
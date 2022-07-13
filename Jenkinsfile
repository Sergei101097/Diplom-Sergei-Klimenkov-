#!groovy
// Run docker build
// properties([disabledConcurrentBuilds()])
pipeline {
    agent any
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t diplom_sergei_klimenkov:local ."
                sh "docker run diplom_sergei_klimenkov:local /bin/bash -c --reruns 5 'poetry run python -m pytest'"
            }
        }
    }
}
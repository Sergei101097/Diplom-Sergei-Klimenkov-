#!groovy
// Run docker build
// properties([disabledConcurrentBuilds()])
pipeline {
    agent any
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t diplom:local ."
                sh "docker run diplom:local pytest -s -v tests/test_ MY_WISHLISTS.py"
            }
        }
    }
}
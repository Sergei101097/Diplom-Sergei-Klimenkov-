#!groovy
// Run docker build
// properties([disabledConcurrentBuilds()])
pipeline {
    agent any
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t rodionova_test ."
                sh "docker run rodionova_test pytest -s -v tests/test_ MY_WISHLISTS.py"
            }
        }
    }
}
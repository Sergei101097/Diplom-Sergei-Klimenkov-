#!groovy
// Run docker build
// properties([disabledConcurrentBuilds()])
pipeline{
    agent any
    stages{
        stage("create docker image"){
            steps{
                echo "========executing A========"
                sh "docker build -t qws:local ."
                sh"docker run qws:local -s -v tests/test_click_t_shirts_my_store.py"
                }
            }
        }
    }

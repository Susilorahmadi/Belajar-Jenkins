pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {checkout scmGit(branches: [[name: '*/new-dev']], extensions: [], 
            userRemoteConfigs: [[credentialsId: 'Susilorahmadi', url: 'https://github.com/Susilorahmadi/Belajar-Jenkins.git']])
            }
        }
        
        stage('clone'){
            steps{
                git branch: 'new-dev', credentialsId: 'Susilorahmadi', url: 'https://github.com/Susilorahmadi/Belajar-Jenkins.git'
                bat label: '',script: 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                
            }
        }
        
        stage('install packages'){
            steps{
                bat label: '',script: 'py get-pip.py'
                bat label: '',script: 'py -m pip install --upgrade pip setuptools'
                bat label: '',script: 'py -m pip install -r seasson/requirements.txt'
                // echo 'the job has on tester'
                // bat label: '',script: 'py seasson/web_server.py'
            }
        }

        stage('Build Docker'){
            steps{
                bat label: '',script: 'docker build -t belajar-jenkins:latest .'
            }
        }

        stage('push'){
            steps{
                withDockerRegistry([ credentialsId: "ed5a3a2a-09d9-4703-bd57-150c9bd48824", url: "" ]){
                    bat label: '',script: 'docker push belajar-jenkins:latest'
                }
            }
        }
    }
}

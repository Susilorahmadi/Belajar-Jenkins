pipeline {
    agent any
    // agent {
    //     node {
    //         label 'main'
    //     }
    // }

    environment {
        // GIT_URL = 'gitlab.bni.co.id/rpv/microservice-agent46/stingray.git'
        // GIT_TESTING_URL = 'gitlab.bni.co.id/rpv/microservice-agent46/testscript_newbackend.git'
        // HARBOR_REPO_URL = 'jtl-tkgiharbor.hq.bni.co.id'
        // PERSONAL_ACCESS_TOKEN = 'yyg8pbeNGR-2aNGsLTVU'
        // BRANCH_NAME = 'testingcicd'
        // REPO_NAME = 'stingray'
        GIT_URL = 'https://github.com/Susilorahmadi/Belajar-Jenkins.git'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Fetch Source Build Server') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Checkout & Clone Source DEV') {
            steps {
                script {
                    try {
                        // sh 'git clone https://oauth2:${PERSONAL_ACCESS_TOKEN}@${GIT_URL}'
                        sh 'git clone ${GIT_URL}'
                        // sh 'git checkout ${BRANCH_NAME}'
                    } catch (err) {
                        echo 'Exception occurred: ' + err.getMessage()
                    }
                }
            }
        }

        // stage('Clean package') {
        //     tools {
        //         maven 'maven383'
        //         jdk 'Java8'
        //     }
        //     steps {
        //         script {
		//     sh 'export http_proxy=http://192.168.45.194:8080/'
		//     sh 'export https_proxy=http://192.168.45.194:8080/'
        //             sh 'mvn -Dhttps.proxyHost=inet.bni.co.id -Dhttps.proxyPort=8080 -Dmaven.test.skip=true clean package'
        //         }
        //     }
        // }

        // stage('Build image & Push to harbor') {
        //     steps {
        //         withCredentials([usernamePassword(credentialsId: '12654068-f992-4141-89e2-8624ca352618', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
        //             sh 'docker login -u $USERNAME -p $PASSWORD ${HARBOR_REPO_URL}'
        //             sh 'docker build -t jtl-tkgiharbor.hq.bni.co.id/agent46-backend/${REPO_NAME}:latest .'
        //             sh 'docker push jtl-tkgiharbor.hq.bni.co.id/agent46-backend/${REPO_NAME}:latest'
        //         }
        //     }
        // }

        // stage('Apply') {
        //     steps {
        //         withCredentials([usernamePassword(credentialsId: '12654068-f992-4141-89e2-8624ca352618', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
        //             sh 'tkgi get-kubeconfig soa-api-dev -a jtl-tkgiapi.hq.bni.co.id -u $USERNAME -p $PASSWORD -k'
        //             sh 'kubectl config use-context soa-api-dev'
        //             sh 'kubectl apply -f deployment.yaml -n agent46-backend'
        //         }
        //     }
        // }

        // stage('Restart') {
        //     steps {
        //         script {
        //             sh 'sleep 3'
        //             sh 'kubectl rollout restart deployment ${REPO_NAME} --namespace agent46-backend'
        //         }
        //     }
        // }

        // stage('Test(s)') {
        //     steps {
        //         script {
        //             try {
        //                 echo 'Project team(s) to add the test cases here in order to run as part of pipeline'
		// 	echo 'No test(s) here to execute'
        //                 //sh 'sleep 60'
        //                 //sh """
        //                 //git clone https://oauth2:${PERSONAL_ACCESS_TOKEN}@${GIT_TESTING_URL}
        //                 //cd testscript_newbackend
        //                 //git checkout ${BRANCH_NAME}
        //                 //pip3 install --proxy http://192.168.45.105:8080 pytest
        //                 //pip3 install --proxy http://192.168.45.105:8080 requests
		// 	//pytest test-cases/test_84_getParameterELO.py
        //                // """
        //             } catch (err) {
        //                 echo 'Exception occurred: ' + err.getMessage()
        //             }
        //         }
        //     }
        // }
    }
}
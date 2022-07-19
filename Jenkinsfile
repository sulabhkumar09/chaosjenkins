pipeline {

  agent {label 'chaos'}

   environment {                                      

                     registry = "sulabhdocker09/chaos"
                     registryCredential = 'dockerhub'
                    
                }

  stages {
    stage("Activate environment") {
        steps {
          sh "python3 -m venv chaostk"
            sh ". chaostk/bin/activate"
        }
    }
  stage("Install Requirments")
  {
    steps{
      sh "pip install -r requirements.txt"
    }
  }
  stage("Run Application")
  {
    steps{
      sh "python app.py"
    }
  }
    // stage('Build Docker') {
    //   steps {
    //      // build the docker image from the source code using the BUILD_ID parameter in image name
    //      sh "docker build -t chaos ."
    //   }
    // }
    // stage('Publish image to Docker Hub') {
          
    //              steps {
    //                  script{
    //                      withDockerRegistry(credentialsId: 'dockerhub') {
    //                      sh  'docker push sulabhdocker09/chaos:latest'
                         
    //                      }
    //                 } 
                    
    //               }
    //           }
    // stage('Stop Running Container'){
             
    //              steps{
    //                    bat 'docker ps -qf  expose=5002/tcp && docker ps -qf name=chaos | docker rm -f chaos'
                       
    //                 }
    //             }
    // stage("run docker container") {
    //   steps {
    //     sh "docker run -d -p 5002:5002 --name chaos -d chaos-toolkit-for-webapp"
    //   }
    // }
    stage('run chaos experiments') {
      steps {
        sh 'chaos --verbose run experiment.json'
      }   
    }
  }
}
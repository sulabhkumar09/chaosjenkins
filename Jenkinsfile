pipeline {

  agent {label 'chaos'}

   environment {                                      

                     registry = "sulabhdocker09/chaos"
                     registryCredential = 'dockerhub'
                    
                }

  stages {
    stage("Activate environment") {
        steps {
            sh ". chaostk/bin/activate"
        }
    }
  stage("Install Requirments")
  {
    steps{
      sh "pip install -U chaostoolkit"
      sh "pip install -U chaostoolkit-reporting"
      sh "pip install -r requirements.txt"
    }
  }
  // stage("Run Application")
  // {
  //   steps{
  //     sh "python app.py"
  //   }
  // }
    stage('Build Docker') {
      steps {
         // build the docker image from the source code using the BUILD_ID parameter in image name
         sh "docker build -t chaosexperiment ."
      }
    }
    // stage('Publish image to Docker Hub') {
          
    //              steps {
    //                  script{
    //                      withDockerRegistry(credentialsId: 'dockerhub') {
    //                      sh  'docker push sulabhdocker09/chaos:latest'
                         
    //                      }
    //                 } 
                    
    //               }
    //           }
    stage('Stop Running Container'){
             
                 steps{
                       sh'docker ps -qf  expose=5002/tcp && docker ps -qf name=chaos | docker rm -f chaos'
                       
                    }
                }
    stage("run docker container") {
      steps {
        sh "docker run -d -p 5002:5002 --name chaos -d chaosexperiment"
      }
    }
    stage('run chaos experiments') {
      // steps {
      //   sh "/home/ubuntu/jenkins/workspace/chaostoolkit/chaostk/bin/chaos --verbose run experiment.json"
      // }
     steps {
        sh """
        . chaostk/bin/activate
        chaos --verbose run experiment.json
        """
      }    
    }
    stage('Experiment Report'){
      steps{
         sh """
        . chaostk/bin/activate
        chaos report --export-format=html journal.json report_${BUILD_NUMBER}.html
        """
      }
    }
  }
}
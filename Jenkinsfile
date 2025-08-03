pipeline {
    agent any

  stages {
    stage('Intsall Dependencies'){
      steps {
         sh 'pip install -r requirements.txt'
      }
    }

     stage('Run App') {
      steps {
         sh 'nohup python3 app.py &'
      }
    }
  }
}


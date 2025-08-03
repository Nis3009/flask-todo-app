pipeline {
    agent any

  stages {
	
    stage('clone') {

      steps {
         git 'git@github.com:Nis3009/flask-todo-app.git'
      }
    }

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


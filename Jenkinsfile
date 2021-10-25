pipeline {
 agent any
  stages {
    stage("Compile") {
      steps {
        sh "Compiling"
            }
          }
    stage("Unit test") {
      steps {
        sh "./gradlew test"
            }
         }
      }
  }

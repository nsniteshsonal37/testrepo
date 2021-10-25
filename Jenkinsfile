pipeline {
 agent any
  stages {
    stage("Compile") {
      steps {
        echo "Compiling"
            }
          }
    stage("Unit test") {
      steps {
        sh "./gradlew test"
            }
         }
      }
  }

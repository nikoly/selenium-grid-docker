#!groovy
node {
  wrap([$class: 'AnsiColorBuildWrapper', colorMapName: 'xterm']) {
    stage("Checkout") {
      checkout scm
    }

    stage("Cleaning and preparing") {
      sh '''#!/bin/bash -e
        git clean -dfx
        mkdir reports
      '''
    }

    stage('Build an image with App') {
        sh """
          docker-compose build app:{VERSION}
        """
    }

    stage('Build an image with Tests') {
        sh """
          docker-compose build robottests:{VERSION}
        """
    }

    stage('Run Docker Compose') {
        sh """#!/bin/bash -e
          docker-compose run --rm robottests:{VERSION}  ./wait-for-it.sh -t 15 chromenode:5555 -- robot -d reports --variablefile variables/config.py --variable BROWSER:chrome tests/
        """
    }

    stage('Stop all containers') {
        sh """
          docker-compose down
        """
    }
  }
}

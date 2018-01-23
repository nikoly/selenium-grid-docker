#!/usr/bin/env groovy
pipeline {
  agent any

  environment {
    TAG = "${env.BRANCH_NAME}_${env.BUILD_NUMBER}"
  }

  stages {
    stage("Checkout") {
      steps {
        checkout scm
      }
    }

    stage("Cleaning and preparing") {
      steps {
        sh """#!/bin/bash -e
          git clean -dfx
          mkdir reports
        """
      }
    }

    stage('Run UI Tests') {
      steps {
        try {
          sh """#!/bin/bash -e
            docker-compose -p ${TAG} up -d --build
            docker-compose -p ${TAG} run --rm robottests -t 15 chromenode:5555 -- robot -d reports -x xunit --variablefile variables/config.py --variable BROWSER:chrome tests/
          """
        } finally {
          publishHTML target: [
          allowMissing: false,
          alwaysLinkToLastBuild: true,
          keepAll: true,
          reportDir: 'reports',
          reportFiles: 'report.html',
          reportName: 'Robot Framework Report'
          ]
          junit 'reports/*.xml'

          sh """#!/bin/bash
            docker-compose -p ${TAG} down
          """
        }
      }
    }
  }
}

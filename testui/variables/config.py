""" Keeps common variables for the test suit """
import time

import sys
import os

# Where is Selenium?
# Selenium Browser or Selenium Hub has to be specified to run the tests
# on remote: Selenium Grid or Selenium Chrome or Selenium Firefox.
#
# To do so with Docker look at the following examples.
#
# EXAMPLE for Selenium Grid:
#   https://github.com/SeleniumHQ/docker-selenium/wiki/Getting-Started-with-Docker-Compose
#
# EXAMPLE for Selenium Firefox
#   https://github.com/SeleniumHQ/docker-selenium/tree/master/StandaloneFirefox#how-to-use-this-image
#

# Use SELENIUM = None when you want to run the tests on your local browser
# SELENIUM_HUB = "http://selenium_hub:4444"
SELENIUM_HUB = 'http://selenium_hub:4444/wd/hub'


# Asset Services
APP_URL = 'http://app:80'

# Browser
BROWSER = 'Firefox'

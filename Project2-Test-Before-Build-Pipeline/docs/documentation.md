# Project: Test Before Build Pipeline

## Objective

* Code must pass tests before it is built or deployed

## Commands Practiced

* 

## What I did

* Created project folder structure
* Created python app, requirements file, and unit testing app
* Tested it locally first using python pip
* After test passed locally, Created Dockerfile
* Created CI/CD workflow file
* Pushed to GitHub
* Pipeline working -> Checking stages -> Image on DockerHub
* Pulling and tested image (optional)
* Intentionally making the test fail by adding mistake in test file
* Pushed -> Pipeline working -> Test failed -> Image not produced
* Corrected all

## Problems Faced

* pip installing error
* Error: externally managed environment
* Error while testing: no module named app

## How I solved

* Updated system
	- sudo apt update
* Created virtual environment
	- python3 -m venv venv | source venv/bin/acivate
* Created an empty file "app/__init.py" and updated test file

## Key Learnings

* Write multi-line shell commands using |
* 
* 

* This line is to check the ! path to docs, in workflow file working or not

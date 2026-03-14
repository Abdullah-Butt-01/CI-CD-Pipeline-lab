# Project: Versioned App Release Pipeline

## Objective

* Create multiple versions of the app and build image automatically

## Commands Practiced

* git tag <name
* git push origin tag <name
* git tag -d <name
* git push tag --delete <name

## What I did

* Created Project folder structure
* Created python app, requirements file, Dockerfile and github workflow
* Pushed to GitHub
* Created Versioned Tag v1.0
* Updated app and created another tag v1.1
* Pulled images of the two versions
* Created containers with different ports
* Tested both versions from the browser

## Problems Faced

* Two pipelines ran at the same time, for previous project also

## How I solved

* Added branched in previous project workflow
	- It only contained push trigger and path filter, so when i pushed the current project, this push also triggered

## Key Learnings

* Triggers are based on events:
	- push
	- pull_request
	- tag
* Then you narrow them down using filters
	- branches
	- tags
	- paths

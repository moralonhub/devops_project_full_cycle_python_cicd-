# DevOps Full Cycle CI/CD Project

This is a repository for a DevOps Full Cycle CI/CD project

https://github.com/moralonhub/devops_project_full_cycle_python_cicd-.git


## Continer pipline

Pipeline "script from SCM" Script path:  "Jenkinsfile".

Jenkinsfile - Utilizes a Docker image of a Python application that is built and pushed to docker repo.

### run by:
GitHub Webhooks on every push made to the `dev` branch.


## Periodic job

JenkinsfilePeriodic - Periodic build job used to run container pipline artifact every five minutes

## main.py -

Python script checking with AWS (using boto) if there are machines up and running with the following tags:
--filters "Name=tag:k8s.io/role/master,Values=1"  "Name=instance-state-code,Values=16”

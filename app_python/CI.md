# CI best practices
* Try to minimize Actions, only necessary actions included
* Don't install dependencies unnecessarily
* Use Secrets from github to store the secrets, do not hardcode them
* Limit environment variables to the narrowest possible scope.
Docker username and password needed only in build job, so created env variables in this job
* Provide authors and description of an Action
* Don’t use self-hosted runners in a public repository

## Best practices for using Docker in Github Actions
* Use Docker Hub access token, instead of password
* Use `registry` type cache to not build built stages and decrease build time 

## Jenksin CI related best practices
### Add security to your CI in Jenkins
Jenkins does not perform any security checks by default, and user can access and 
arbitrary code on connected agents through the Jenkins

First thing to do in Jenkins is set up the `Access Control` 

### Do the backups

By backups in Jenkins meant backup of the `JENKINS_HOME` directory.

Why it is important? `JENKINS_HOME` directory contains all the data about your Jenkins, 
so losing it is undesirable and harmful sometimes.

There are many plugins, which can help to create and automate backups.

### Setup A Different Job/Project For Each Maintenance Or Development Branch Created
Setting up different jobs/projects for each branch helps you support parallel development 
efforts and maximize the advantage of sleuthing issues, thereby reducing risk and allowing 
developers to be more productive.

### Prevent Resource Collisions In Jobs That Are Running In Parallel

Multiple jobs running simultaneously can cause collisions if they create a service or need 
exclusive access, which can bleed out your Jenkins pipeline. Accepting this as one of the 
Jenkins best practices is highly recommended by DevOps professionals.

### Use “File Fingerprinting” To Manage Dependencies

Creating interdependent projects on Jenkins often creates a muddle, keeping track of which
version of it is used and by which version of it. “File fingerprinting,” supported by Jenkins, 
simplifies this, so make the best use of it.

### Avoid Complicated Groovy Codesode In Pipelines

For a Jenkins Pipeline, Groovy code always executes on master involving exuberant usage of 
master resources (memory and CPU). Consequently, it becomes critically important to cut back
the amount of Groovy code executed by Pipelines. The subsequent solutions are to the most common
Groovy methods that can be avoided, leading up to the best Jenkins practices.

### Build A Scalable Jenkins Pipeline

Shared Libraries are perhaps the single most talked about tool to pop up across enterprises and 
are the pinnacle of applying DRY principles (Don’t Repeat Yourself) to DevOps. Shared Libraries 
offer a version-controlled Pipeline code that can be stored and accessed from your source control
management (SCM) compared to a common programming library.

### Manage Declarative Syntax/Declarative Pipelines

Declarative Pipelines configuration tells a system what to do, shifting the complexity of ‘how to do’ to the system.

### Maintain Higher Test Code Coverage & Run Unit Tests As Part Of Your Pipeline

Maintaining 90% of code coverage ensures better ROI by reducing UAT and product defects. Although
higher coverage alone does not guarantee code quality, surfacing code coverage numbers help ensure
your developers and QA defect prevention at an early stage of the life cycle.

### Monitor Your CI/CD Pipeline

Having a broken CI/CD pipeline can potentially stall your development team. Also, external dependencies
like cloud services, network, testing services might affect your CI/CD pipeline, and you need to know
when these occasional failures become significant enough to warrant action.

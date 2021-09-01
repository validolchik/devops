## Terraform Best practices found
### 1. Don't commit the .tfstate file
This file contain the configuration of your workspace,
mappings between your created resource names and the real infrastructure.
Committing the state file comes with several risks.
Firstly, you could be exposing secrets from your application configuration, 
such as  passwords, database connection strings. Secondly, you risk executing 
Terraform against stale or old state that you forgot to pull down from version control.

### 2. Configure a backend
A Terraform backend is configuration on how (and where) to store your Terraform state 
in a centralised, remote location. It is used when you want to store your current Terraform state.

### 3. Keep your backend small

Needed for big configuration in order to be easily manageable and reduces risks of getting 
errors while introducing changes to configuration.

### 4. Back up state file

Backed up state makes it easier to revert to a previous state if you make a mistake.

### 5. Use one state  per environment

Environments used to test changes before they are deployed to your live environment.
Breaking down by environment reduces risk when you apply changes.

### 6. Setup backend state locking

Terraform state comes in two parts: remote state, and state locking. 
State locking prevents two mutating commands, such as terraform apply 
operating on the same state file at the same time.

### 7. Execute terraform in and automated build

Running code in an automated build tool has many advantages, 
which includes having a repeatable process, and a history of changes. 
The concept of builds is also very useful when applied to Terraform, 
ensuring that it’s more visible when and what has been executed against 
your infrastructure for auditing, debugging and collaborating purposes

### 8. Don't perform state surgery

Instead, use CLI, when you need to move or rename the state file 
(`terraform state rm` and `terraform state mv`)

### 9. Use variables

Just to do your configuration file cleaner and easier to manage

### 10. Use modules (when necessary)

A good rule for when to reach for modules is when you’ve seen a pattern at least 3 times.
Otherwise, it can make configuration painful.


## Description of work done

Deployed AWS instance using Terraform (see the [main.tf](https://github.com/validolchik/devops/blob/master/terraform/aws/main.tf))

Tried to deploy VM on VirtualBox, but got error with `Failed to query available provider packages`

Instead, used Vagrant to set up local VM (followed [tutorial](https://learn.hashicorp.com/collections/vagrant/getting-started))
[screen 1](https://github.com/validolchik/devops/blob/master/vagrant/images/scr1.png)
[screen 2](https://github.com/validolchik/devops/blob/master/vagrant/images/scr1.png)
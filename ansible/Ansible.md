# Usage

To run Ansible playbook on hosts, configured by a dynamic inventory, use following command

`ansible-playbook -i inventory/ install_docker.yml`
, where `inventory` is the folder with dynamic inventory configuration and `install_docker.yml` is the playbook
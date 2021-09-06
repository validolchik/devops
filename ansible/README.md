# Run playbook in remote machine

To run Ansible playbook on hosts, configured by a dynamic inventory, use following command

`ansible-playbook -i inventory/ install_docker.yml`
, where `inventory` is the folder with dynamic inventory configuration and `install_docker.yml` is the playbook

# Run ansible linter

```sh
sudo apt install ansible-lint
cd ansible
ansible-lint .
```
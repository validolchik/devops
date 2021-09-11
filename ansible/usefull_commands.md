`ansible-playbook "path to playbook".yml --diff -e *var name*=*new var value* --tags pricing-data-wipe --check`

`--diff` will show the differences brought by this command
`-e` overwrite the variable
`--tags` only execute commands with this tag
`--check` don't really apply the changes, only check
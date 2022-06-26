Ansible PIP install post setup

Post install from pip (using python3 -m pip install ansible)

ansible-config init --disabled > ansible.cfg

Uncomment the ansible inventory line and set the path to /home/madhu/.ansible/hosts

Create below file:
madhu@madhu:~/.ansible$ cat /home/madhu/.ansible/hosts 
127.0.0.1

Test
Go to /home/madhu/.ansible
Run and expect output as below

madhu@madhu:~/.ansible$ ansible all -m ping -v
Using /home/madhu/.ansible/ansible.cfg as config file
127.0.0.1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}

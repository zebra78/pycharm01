**Ansible PIP install post setup**

Post install from pip (using python3 -m pip install ansible)

ansible-config init --disabled > ansible.cfg

Uncomment the ansible inventory line and set the path to /home/madhu/.ansible/hosts

Create below file:
madhu@madhu:~/.ansible$ cat /home/madhu/.ansible/hosts 
127.0.0.1

Test

Create ansible.cfg as below:
madhu@madhu:~$ cat /home/madhu/.ansible.cfg 
[defaults]
# some basic default values...
inventory = /home/madhu/.ansible/hosts  ; This points to the file that lists your hosts



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

**PyCharm post install setup**
 
Key notes: 

    PyCharm creates own venv so do not installed modules from outside for e.g. python3 -m install boto3 

    Install modules from PyCharm IDE  

        How ? Bottom of the screen click the tab Python packages and go ahead with installation 

          You might need to install awscli botocore and boto3 bare minimum 

    Setting up AWS resource access from PyCharm 

          You need install AWSToolKit and it picks the .aws/credentials file from default location 

          How to install ? From PyCharm IDE go to File > Setting > Plugins > <Search> AWS Toolkit 
    
    How to integrate a project with GitHub
          Create new project 
          Go to Git tab and enable Version Controlling
          How to map specific project ?
          Git -> Manage Remotes -> Add the respective URLs
          

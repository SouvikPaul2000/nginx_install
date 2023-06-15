import paramiko

from st2common.runners.base_action import Action

class Nginx(Action):
    def run(self):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='172.29.0.16', port='8080')

        # Install Nginx
        stdin, stdout, stderr = ssh_client.exec_command('apt-get update')
        print(stdout.read().decode())

        stdin, stdout, stderr = ssh_client.exec_command('apt-get install -y nginx')
        print(stdout.read().decode())

        ssh_client.close()


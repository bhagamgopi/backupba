import paramiko
import time
import datetime

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
timestamp = str(datetime.datetime.now().timestamp()).split(".")[0]

print("Connecting........")
ssh_client.connect(hostname="192.168.1.11", port=22,
                   username="sid", password="sidver")
print("Compressing..........")
stdin, stdout, stderr = ssh_client.exec_command("tar -cvf backup"+timestamp+".bz2 sms_new/\n")
print(stdout.read().decode())
time.sleep(2)
print("Copying..........")
#os.system("scp sid@192.168.1.11:~/backup.bz2 ~/ust_projects/projects_2/")

ftp_client = ssh_client.open_sftp() 
ftp_client.get(remotepath="/home/sid/backup.bz2",localpath="/home/sid/ust_projects/projects_2/backup"+timestamp+".bz2") #Copy file from remote pc to local pc
ftp_client.close()

if ssh_client.get_transport().is_active() == True:
    print("Disconnecting.............")
    ssh_client.close()


#localpc to remote pc
#ftp_client.put(remotepath="",localpath="")

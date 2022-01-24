# PSD-AWS-DevOps Series

## Create AWS CodeDeploy & CodePipeline for to deploy simple web page to be hosted out of an EC2

### Source - 
1. The source files are available in [github](https://github.com/apartha77/PSD-AWS-DevOps/)  
##### The files required are - the details of each file will be explained below
- index.html - my custom web page 
- appspec.yml -
- buildspec.yml -
- /Scripts/install_dependencies - 
- /Scripts/start_server - 

2. The rest of the activies will be on AWS console
- Need to create roles for EC2 and CodeDeploy 
- Need an EC2 to deploy the index.html - select Ubuntu server put the below start up script as user data. This will instal the CodeDeploy agent to run the deployment. In the recent version CodeDeploy can install the agent provided SSM agent is installed, you can find this detail while configuring CodeDeploy
```
#!/bin/bash
sudo apt update
sudo apt install -y ruby-full
sudo apt install wget
cd /home/ubuntu
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto > /tmp/logfile
sudo service codedeploy-agent start
sudo service codedeploy-agent status
```
### Install CodeDeploy Agent in EC2
1. Get the script from [AWS Docs](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-linux.html)
2. I am doing this on Ubuntu hence will take the script for [Script Ubuntu](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html)
3. ```

```
4. 

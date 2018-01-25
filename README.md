# Computatational Economics with Python - Parallel Computing

SSH into the Amazon CloudFormation Cluster Server instance (public IP: 35.177.227.48) 

1. Check if you have received the private key (.pem file) from email and download it to your local machine.
2. Unix/Linux users type the following command in your terminal: ssh -i path/cepython.pem ec2-user@35.177.227.48
3. Change the permission of private key file to read only: chmod 600 cepython.pem
4. Windows users use putty and set up the key, host name as below:





Windows user troubleshooting: if your private key (*.pem) is not recognized by Putty. Use PuTTYgen to load the pem file and save the private key as *.ppk. Then you should be able to load the private key. 

Now you are free to use the remote server for your work! 

Create your own directory for the use, for example a combination of your first name and last time:
mkdir qhan
cd qhan

Download the code from the Github
git clone https://github.com/francishan/python_parallel_computing.git
cd python_parallel_computing



Now lets write some code 😃

We set up the Anaconda on the server Type conda and see whether it works.

Run the following command in the training instance:
jupyter notebook --no-browser 





The jupyter notebook is already running, now build a tunnel to give you access in your local machine
ssh -i path/cepython.pem -NfL port:localhost:port ec2-user@35.177.227.48

Windows users: after the jupyter server is running, use PuTTY to build a tunnel as below:


Now you can open your browser, and copy/paste the URL shown from your training instance to login with a token: 



You are now ready to code 😃

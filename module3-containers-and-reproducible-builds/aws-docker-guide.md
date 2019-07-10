# Install Docker to EC2 Virtual Private Servers and deploy Docker Images

## AWS Free Tier available for 1 year
You can use your Amazon.com account for AWS. Anything not in the "Free Tier" will cost money to use.

# Create EC2 Instance
Navigate to the EC2 console once you're logged into the AWS Dashboard. The "Services" menu option at the top of the screen will show you the overwhelming options and you can find EC2 there.

## Select Launch Instance
This will bring up the helper to let you pick all the options for your new EC2.

## Choose AMI
For this example we'll be using the "Deep Learning AMI (Ubuntu) Version 23.1" image which comes pre loaded with a lot of tools and drivers that would otherwise be a pain to install. This is based on Ubuntu 18.04.

## Choose Instance Type
We're going to be testing out a GPU instance so I'm picking "p2.xlarge" since it's fairly cheap.

## Configure Instance Details
Try choosing "Request Spot Instances" These are cheaper instances that can be interrupted by Amazon if pricing goes over an amount you choose, for example I see current prices of $0.3284 per hour and have a set max of $0.5 per hour. This is compared to on demand prices of $0.90 per hour.

## Add Storage
Use as much storage as you'll need to complete your work, I chose 200GB to avoid any problems.

## Add Tags
Tags are useful if you have a lot of ec2 instances and want to search through them.

## Configure Security Group
Since we're going to be deploying a jupyter notebook and connecting over SSH we need to create a security group that allows for those. 

Select "Create a new security group" and give it a name and description. 

Then you'll see SSH already filled in, we can click below "Source" on "Custom" and choose "My IP" to limit SSH connections to the IP you're using.

Click "Add Rule." The prefilled info for Type and Protocol are correct, we want the port to be 8888 though and again limited to "My IP."

## Review and Launch
Be sure to look over all your Instance's settings and check that they're right, once you're happy click Launch.

### Use a .pem file!
Once you click Launch AWS will give you the chance to create an SSH Keypair which you should absolutely take advantage of.
This saves you from having to type a password each time you SSH in and is more secure.

It will take a minute or two to provision and boot.

# SSH into your newly launched server

## Terminal Time

### MacOS and Linux will have the ssh command available by default from their terminal

### Windows might have 

## .pem permissions
Navigate to the folder you saved your .pem file in (You did that right?)
`chmod 400 YOURCERT.pem`
Run that command in your terminal to apply the proper filesystem permissions to the file.

## SSH in to your EC2 instance
The ec2 dashboard has a handy connect button that gives you pretty clear directions for connecting. For example my practice instance was `ssh -i "lambda.pem" ubuntu@ec2-54-242-7-230.compute-1.amazonaws.com`
Your's will be slightly different but in that general format.

## Docker should be installed by default from our AMI image

`sudo docker run hello-world`

This should return "Hello from Docker!" etc etc.

## Now lets verify that we have a GPU available to Docker

`docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi`

This should display a little chart saying we have an Nvidia K80 that is being completely unutilized currently.

## Tell Docker to always use the nvidia runtime
open /etc/docker/daemon.json and change it to look like this
```
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```

## Now you can run any docker image you like
`docker pull tensorflow/tensorflow:latest-gpu-jupyter`
is a good one that installs jupyter and tensorflow with GPU support.

## Now run it
`docker run -p 8888:8888 tensorflow/tensorflow:latest-gpu-jupyter`

## Connect to Jupyter kernel

Docker will give you some output like this
```
[I 22:31:45.826 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 22:31:45.976 NotebookApp] Serving notebooks from local directory: /tf
[I 22:31:45.976 NotebookApp] The Jupyter Notebook is running at:
[I 22:31:45.976 NotebookApp] http://(89c18f383afd or 127.0.0.1):8888/?token=ff5a8ebbbbc4d22590def79a97e380d2d3852b4078c64be4
```

To connect you'll need your EC2 Public DNS
that address that looked something like this `ec2-54-242-7-230.compute-1.amazonaws.com`

paste that into your webbrowser followed by the part of your docker output that looks like this `8888/?token=ff5a8ebbbbc4d22590def79a97e380d2d3852b4078c64be4`

The complete example address 
`http://ec2-54-242-7-230.compute-1.amazonaws.com8888/?token=ff5a8ebbbbc4d22590def79a97e380d2d3852b4078c64be4`

You'll drop straight into a Jupyter Kernel that has access to all the resources of your underlying AWS EC2 instance!
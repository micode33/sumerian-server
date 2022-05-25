<h1>Sumerian Server</h1>

This is a TCP server I built with python to help me understand how data moves between a client and server. I found it helpful to understand this when learning react, vue, and angular because I understand how things work *under the hood*.

## Features

- Create, bind and listen on a TCP socket
- Display and parse the incoming HTTP request
- Generate an HTTP response with headers and content
- Dynamic heading using template literal

## Install

```bash
git clone https://github.com/micode33/sumerian-server.git
```

```bash
cd sumerian-server
```

```bash
python3 main.py
```

## Change Host or Port

The default host is `0.0.0.0` and the default port is `8001`. If you would like to specify a different host or port you can include `-h --host` for host and `-p --port` for port in your command.

```bash
python3 main.py -h 127.0.0.1 -p 3000
python3 main.py --host 127.0.0.1 --port 3000

```

## Usage

Visit http://localhost:8001 and the webpage will rotate between 3 different html pages on each request.

You can also change the title and heading on each page by feeding a heading parameter to the request.

```bash
http://localhost:8001/?heading=blahblahblah
```

## Script for aws

### Prerequesites

- Make sure you've started your EC2 instance
- Make sure you have configure SSH in the security group
- Make sure you've downloaded you PEM file and it's in your ~/Downloads directory
- Make sure the PEM file is named as `labsuser.pem`

### Setup

```bash
# Run the setup.sh with bash and pass in the IP or hostname to
# your EC2 instance on AWS.
bash setup.sh 52.34.237.111

# Should be logged into your EC2 instance and a copy of the file
# sumerian-server.sh should be there so run it with bash
bash sumerian-server.sh
```
This setup.sh file will do the following:

- Set the correct permissions on your labsuser.pem file
- Setup ssh_config
- Secure copy sumerian-server.sh to your 

## Scripts

```bash
#!/bin/bash

# Usage: bash setup.sh [SERVER_NAME] [PRIVATE_KEY]

setup(){

  local SERVER_NAME=${1:-54.201.60.104}
  local PRIVATE_KEY=${2:-labsuser.pem}
  is_debug(){
    if [ "$VERBOSE" != "false" ]; then

      return 1

    fi

    return 0
  }

  DEBUG || echo -e "rm -rf ~/.ssh/$PRIVATE_KEY"
  command rm -rf ~/.ssh/$PRIVATE_KEY

  DEBUG || echo -e "rm -rf ~/.ssh/config"
  command rm -rf ~/.ssh/config

  DEBUG || echo -e "chmod 400 ~/Downloads/$PRIVATE_KEY"
  command chmod 400 ~/Downloads/$PRIVATE_KEY

  DEBUG || echo -e "cp ~/Downloads/$PRIVATE_KEY ~/.ssh"
  command cp ~/Downloads/$PRIVATE_KEY ~/.ssh

  local ssh_config="
Host aws\n
    Hostname $SERVER_NAME\n
    User ec2-user\n
    Port 22\n
    IdentityFile ~/.ssh/$PRIVATE_KEY\n
"

  echo -e $ssh_config > ~/.ssh/config

  DEBUG ||echo -e "scp sumerian-server.sh aws:~"
  command scp sumerian-server.sh aws:~

  DEBUG ||echo -e "ssh aws"
  command ssh aws

  DEBUG ||echo -e "bash sumerian-server.sh"

}

setup $@
```


```bash
#!/bin/bash

# Setup python environment in the Code directory
python3 -m venv Code

# Change directory to Code
cd Code

# Activate the python environment
source bin/activate

# Install git
sudo yum -y install git

# Clone the repo
git clone https://github.com/micode33/sumerian-server.git

# Change directory to sumerian-server
cd sumerian-server

# Disable httpd
sudo systemctl stop httpd

# Run sumerian server
python3 main.py -p 80
```



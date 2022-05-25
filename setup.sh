#!/bin/bash

# Usage: bash setup.sh [SERVER_NAME] [PRIVATE_KEY]

setup(){

  local SERVER_NAME=${1:-52.34.237.111}
  local PRIVATE_KEY=${2:-labsuser.pem}
  local DEBUG="true"

  is_debug(){
    if [ "$DEBUG" != "false" ]; then

      return 1

    fi

    return 0
  }

  is_debug || echo -e "rm -rf ~/.ssh/$PRIVATE_KEY"
  command rm -rf ~/.ssh/$PRIVATE_KEY

  is_debug || echo -e "rm -rf ~/.ssh/config"
  command rm -rf ~/.ssh/config

  is_debug || echo -e "chmod 400 ~/Downloads/$PRIVATE_KEY"
  command chmod 400 ~/Downloads/$PRIVATE_KEY

  is_debug || echo -e "cp ~/Downloads/$PRIVATE_KEY ~/.ssh"
  command cp ~/Downloads/$PRIVATE_KEY ~/.ssh

  local ssh_config="
Host aws\n
    Hostname $SERVER_NAME\n
    User ec2-user\n
    Port 22\n
    IdentityFile ~/.ssh/$PRIVATE_KEY\n
"

  echo -e $ssh_config > ~/.ssh/config

  is_debug ||echo -e "scp sumerian-server.sh aws:~"
  command scp sumerian-server.sh aws:~

  is_debug ||echo -e "ssh aws"
  command ssh aws

  is_debug ||echo -e "bash sumerian-server.sh"

  echo -e "Setup complete"

}

setup $@
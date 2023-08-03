#!/bin/bash
# pip install -r requirements.txt
git submodule update --init
wget -O stork https://files.stork-search.net/releases/v1.6.0/stork-ubuntu-20-04
chmod +x stork
export PATH=$PATH:$(pwd)
openssl version
pelican content
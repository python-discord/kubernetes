#!/bin/bash

# Set environment variables
export STORAGE_TYPE=<INSERT STORAGE TYPE>
export STORAGE_HOST=<INSERT STORAGE HOST>
export STORAGE_PASSWORD=<INSERT STORAGE PASSWORD>

# Clone the repo
git clone https://github.com/seejohnrun/haste-server.git
cd haste-server

# Install and start
npm install
npm start



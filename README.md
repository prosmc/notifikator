[![](https://img.shields.io/docker/cloud/automated/schneidermatic/notifikator)](https://hub.docker.com/repository/docker/schneidermatic/notifikator)
[![](https://img.shields.io/docker/cloud/build/schneidermatic/notifikator)](https://hub.docker.com/repository/docker/schneidermatic/notifikator)

# Notifikator

Notifikator - RESTful notifikation service of the Rapid Event Processing Stack (REP-Stack).\
The REP-Stack consists of a bunch of services which are running on top of elasticsearch and kibana.\
Notifikator is one of these services and it's main purpose is to forward event messages. \
This repository contains the source code of notifikator and docker-compose files for integration-testing.

This project is driven by Herzblut so give us a :star: if you like it.\
Thank you very much in advance!

###### PREREQUISITES
---
For running the notifikator service you should fullfill the following performance prereqs:

Name           | Amount        
-------------- | --------------- 
CPU            | 4x
MEMORY         | 8192 (MB)
STORAGE        | 5 (GB)

Also, you need the following software components on your host system:

Name           | Reference    
-------------- | --------------- 
docker         | >= 19.03.5
docker-compose | >= 1.18.0

Setup the Development Project
---

01. Clone the notifikator repo 

        $ cd ~
        $ mkdir notifikator-ws01
        $ cd notifikator-ws01
        $ git clone https://github.com/prosmc/notifikator.git

02. Source the '.xrc' environment for short-hand commands and list them.

        $ cd ./notifikator
        $ . ./.xrc
        $ x_cmd

03. Todo: Step X ...

        $ ...

Setup the Integration Testing Environment
---

01. Todo: Step X ... 


Integation Testings
---

01. Todo: Step X ...


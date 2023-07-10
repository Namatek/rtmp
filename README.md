# RTMP for VoD system
## Structure of project
 - Nginx webserver
 - Python 
## Requirements
- docker image of alfg/nginx-rtmp. (image that ready for RTMP service)
- python-ffmpeg package for sending to RTMP server
## Setup
Run `docker-compose up` to setup nginx configuration. RTMP run in port of 1935. for better config of webserver, `nginx.conf` file volume to `./conf/nginx.conf`.
<br>With run `python rtmp.py`, program begin to send file to webserver.
<br>Must first run `docker-compose` then `rtmp.py`.
## Next step
Implement search file in `rtmp.py`
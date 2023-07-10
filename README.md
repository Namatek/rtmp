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
## Conclusion
RTMP starting the video when a user request to see it. when another user want to access to its, server should copy from video for each user, if don't this work second user see from where first user is watching. its best for live system and not suitable for VoD system.
<br>In VoD system we segmnet our content to `.ts` files and send each segment to its contact but we want to use from RTMP instand of VoD we must copy file for each request to see our content.
<br>Suppose 100 users are online; then we must copy 100 times from a video but in VoD system we split file one time and send them any time.

import subprocess

rtmp_url = "rtmp://localhost:1935/stream/nmtk"

# TODO implement a function that find name of video file.

command = ['ffmpeg',
           '-y',
           '-re',
           '-i', 'file.mp4',
           '-c:v', 'libx264',
           '-f', 'flv',
           rtmp_url
           ]

p = subprocess.Popen(command, shell=True)
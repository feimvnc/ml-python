start docker jupyter notebook on localhost 
mac pro 2018 

use lima to run docker commands 
run docker on macpro without docker engine 

# run docker command on macos without docker engine
which lima 
lima 
alias docker='lima nerdctl'
limactl start default

docker version 
docker info 

#download tensorflow with jupyter
https://www.tensorflow.org/install/docker 

# this download takes sometime, 
docker pull tensorflow/tensorflow:latest-gpu-jupyter  # latest release w/ GPU support and Jupyter


(base) user:docker-tensorflow-jupyter user$ docker image ls 
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

(base) user:docker-tensorflow-jupyter user$ alias docker='lima nerdctl'

(base) user:docker-tensorflow-jupyter user$ docker image ls 
REPOSITORY               TAG                   IMAGE ID        CREATED         PLATFORM       SIZE       BLOB SIZE
tensorflow/tensorflow    latest-gpu-jupyter    a72deb34d32e    15 hours ago    linux/amd64    5.9 GiB    2.7 GiB


#Start a Jupyter Notebook server using TensorFlow's nightly build:
docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-jupyter
...
[I 17:44:10.417 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
jupyter_http_over_ws extension initialized. Listening on /http_over_websocket
[I 17:44:10.688 NotebookApp] Serving notebooks from local directory: /tf
[I 17:44:10.688 NotebookApp] Jupyter Notebook 6.5.2 is running at:
[I 17:44:10.689 NotebookApp] http://a3b66528c5a8:8888/?token=xxxxxx
[I 17:44:10.689 NotebookApp]  or http://127.0.0.1:8888/?token=xxxxxx
[I 17:44:10.689 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 17:44:10.694 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
    Or copy and paste one of these URLs:
        http://a3b66528c5a8:8888/?token=xxxx
     or http://127.0.0.1:8888/?token=xxxxx

#leave dockere running, open url to access jupyter notebook  
http://127.0.0.1:8888/?token=xxxxx


# clear docker cache 
docker system prune -a

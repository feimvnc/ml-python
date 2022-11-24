sources:
http://cedro3.com/ai/codeformer/
https://www.youtube.com/watch?v=lvlqegR3sJA
https://www.youtube.com/watch?v=6oQ0tlOfvjU

create an vm ubuntu 20.04 
user@ubuntu:~$ cat /etc/*issue*
Ubuntu 20.04.5 LTS \n \l

Ubuntu 20.04.5 LTS user@ubuntu:~$ uname -a 
Linux ubuntu 5.15.0-53-generic #59~20.04.1-Ubuntu SMP Thu Oct 20 15:10:22 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
user@ubuntu:~$ 

# install ssh server for remote connection 
sudo apt-get install openssh-server

# install git 
sudo apt install git 

install anaconda python 3.8 

sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh

2022-11-21 18:46:58 (9.32 MB/s) - ‘/tmp/Anaconda3-2020.07-Linux-x86_64.sh’ saved [576830621/576830621]

bash /tmp/Anaconda3-2020.07-Linux-x86_64.sh 

Welcome to Anaconda3 2020.07

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>> 

# start jupyter-notebook directly 
# when navigator jupyter notebook launch not working
jupyter-notebook 

source ~/.bashrc 
# this open brower, click jupyter Launch button 
anaconda-navigator 

# install below if errors 
pip uninstall cast_control
pip install cast_control


# install git if not available on ubuntu desktop 
install git etc 
sudo apt-get install build-essential

# load jyputer notebook 
run commands in jupyter notebook 

# source code 
git clone https://github.com/sczhou/CodeFormer.git
# search code for a specific string 
git grep input_path


cd CodeFormer
mkdir -p inputs/frame

# for video convert to .mp4 fomat 
# convert mov to mp4 on ubuntu command 
sudo apt install ffmpeg
ffmpeg -i my-video.mov -vcodec h264 -acodec mp2 my-video.mp4


# if jupyter notebook not loading, you may need remove below folder 
cd
rm -rf .condarc
anaconda-navigator 


# clean up conda env 
conda clean --packages && conda clean --all && conda update --all

source: https://github.com/pdeitel/PythonDataScienceFullThrottle

If I have seen further it is by standingn on the shoulders of giants." issac newton (and others before him)



## macbook install anaconda 
source: https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html

Open terminal - Applications / Utilities / Terminal, enter following commands 
echo $PATH   # check if conda is installed 
check which python # check if python installed and version 
click link - Anaconda installer for macOS 
click link at bottom of page - MacOs, Python 3.9, 64-Bit Command Line Installer (681 MB) 
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-MacOSX-x86_64.sh 
bash Anaconda3-2022.10-MacOSX-x86_64.sh   
## following prompts to install, use default values should work  
The installer prompts “Do you wish the installer to initialize Anaconda3 by running conda init?” We recommend “yes”


## uninstall anaconda, be careful not delete other folders
cd ~
ls -ltr   # check folder names 
rm -rf ~/anaconda 
rm -rf ~/.condarc ~/.conda ~/.continuum 


## start a project and use jupyter notebook

## pythonDataScience, create conda env 
cd ~		# change directory 
cd Documents
mkdir pythonDataScience
cd pythonDataScience
which conda   #     /Users/user/opt/anaconda3/bin/conda
conda env list 
conda create -name pythonDataScience python=3.9
conda activate pythonDataScience
conda install pandas matplotlib jupyter notebook scipy scikit-learn nb_conda nltk  spyder 
conda install nodejs jupyterlab ipympl wordcloud spacy tweepy geopy folium scikit-learn tensorflow matplotlib seaborn pymongo dnspython imageio pyaudio pydub
# pip needed because a few packages are nnot available through conda
pip install -U dweepy pubnub ibm-watson tweet-preprocessor textblob deep_translator 

which jupyter-notebook
jupyter notebook   # start jupyter notebook

#copy url from output in browser and start use it 

http://localhost:8888/?token=13cc...xxx

# on jupyter notebook, click New at right, select "Python 3(ipykernel)" 
# on top, double Untitled to rename to something you like 



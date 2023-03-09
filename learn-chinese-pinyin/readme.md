#thanks to nick russo, who teachs at orielly for python learning classes, 
#following steps are used to setup local env to use it on macbook

#open a command line terminal 
Finder, Applications, Utilities, Terminal (double click)

#make sure python is installed, test with below command
$python --version
Python 3.9.7

#clone below repo 
#change to home directory
cd ~/Document

#create a new directory named of "fun"
mkdir fun 

#clone below repository
git clone https://github.com/nickrusso42518/zhong

#change to downloaded direcotry 
cd zhong

#install packages
pip install chinese

#run program
python play.py


#troubleshooting when you see voice tingting not found 
open play.py file, line 92, replace 
tingting 
with 
Ting-Ting 

#below is complete changed line 
   say_cmd = f"say --voice=Ting-Ting --rate={args.rate} {chinese}"

#how to check list of available voices , run below command to see the list
$say -v '?'

Alex                en_US    # Most people recognize me by my voice.
Alice               it_IT    # Salve, mi chiamo Alice e sono una voce italiana.
Alva                sv_SE    # Hej, jag heter Alva. Jag är en svensk röst.
Amelie              fr_CA    # Bonjour, je m’appelle Amelie. Je suis une voix canadienne.
....
Ting-Ting           zh_CN    # 您好，我叫Ting-Ting。我讲中文普通话。  ## this voice is for chinese






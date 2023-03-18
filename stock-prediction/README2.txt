# source of program - git clone https://github.com/louisteo9/stock-price-prediction.git


## run program on command line 

open terminal , run below commands 

# make a directory
cd ~/Document
mkdir -p py-timeseries
cd py-timeseris 
# type "man mkdir", to see help manuals

## clone repo , after you will see a directory is created 
git clone https://github.com/louisteo9/stock-price-prediction.git
ls -ltr 
pwd 

# change to the directory 
cd stock-price-prediction


# check py , tensorflow, keras versions 

# python libraries used are :
# sys, pandas, numpy, sklearn, keras, pickle, joblib, matplotlib

# keras is a ml library from facebook built on top of tensorflow 
$ python --version 
Python 3.9.7

(base) user:stock-price-prediction user$ python 
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 

>>> import tensorflow as tf
i>>> import keras 
>>> tf.__version__
'2.11.0'
>>> keras.__version__
'2.11.0'

>>> exit()

# train model
python train.py data/EOD-INTC.csv model/model.pkl model/scaler.gz 0.2 60 60

# predict using model 
python predictor.py model/model.pkl model/scaler.gz data/EOD-INTC.csv


## run program on conda env , in jupyter notebook , and flask 
# in the same resource repo directory 
# list conda env 
conda env list 

# check version 
$ conda -V
conda 4.10.3

# create env , wait for prompt, and answer "y", to proceed , 
conda create -n stock-prediction python=3.10 anaconda
...

# till you see 
done
#
# To activate this environment, use
#
#     $ conda activate stock-prediction
#
# To deactivate an active environment, use
#
#     $ conda deactivate

# activate env 
conda activate stock-prediction
# you will see (stock-prediction) added to env prefix 
(stock-prediction) user:stock-price-prediction user$ 

## find python compatible libraries from below to install correct version
https://docs.anaconda.com/anaconda/packages/py3.10_linux-64/

# sys, pandas, numpy, sklearn, keras, pickle, joblib, matplotlib
pandas	1.4.4
numpy	1.21.5
sklearn 	# no version found, use default 
keras	2.9.0
pickle		# no version found, use default 
joblib	1.1.0
matplotlib	3.5.2

# run below commands to install 
# conda install package-name=x.x.x 
conda install keras=2.9.0
conda install tensorflow=2.9.1
conda install pandas=1.4.4
conda install numpy	=1.21.5
conda install sklearn
conda install pickle
conda install joblib=1.1.0
conda install matplotlib=3.5.2

# after install completes, run below commands 
# tain
python train.py data/EOD-INTC.csv model/model.pkl model/scaler.gz 0.2 60 60

# predict 
python predictor.py model/model.pkl model/scaler.gz data/EOD-INTC.csv


####
# start jupyter notebook, which opens a browser window 
jupyter notebook 

# after a browser opens, click file 
Stock Price Prediction.ipynb

# press shift + enter to run through each cell and see how the program works 
# * means running 
# taining cell takes some time to complete 


#### integrate with flask to call api 
# open a new terminal window, this allows to use same installed libaries 
# change the path to the same directory , check conda envs 
conda env list 

# source the correct env from above created env , select the one you created earlier 
source activate /Users/user/opt/anaconda3/envs/stock-prediction 

# then you will see env prefix 
(stock-prediction) user:stock-price-prediction user$

# in the same directory, create a python file 

# flask information 
https://flask.palletsprojects.com/en/2.2.x/quickstart/

# in the same directory, create a file "hello.py", copy paste below from above page 

# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
# in the same directory, where "hello.py" exists, run below , two "--" before app 
flask --app hello run 

# you see below, copy url and open in browser , you see "Hello, World!" on the page 
* Running on http://127.0.0.1:5000
Press CTRL+C to quit

# leave this terminal open to test the page,
# let's add the predict program to hello.py 
# open visual studio or vim text editor, let's add source code from "predicator.py"
# everytime you add, save, refresh the hello page to see new code does not break the app 

#  at top of the file, add to hello.py, save, refresh page 
import sys
import numpy as np
import pandas as pd
import pickle
import joblib

#  add to hello.py, save, refresh page 
# import function defined earlier in train.py
from train import load_process_data


# add below function 
# slightly modified from get_pred_closing_price() from train.py
def pred_closing_price(df, scaler, model):
    """
    Predict stock price using past 60 stock prices

    INPUT:
    df - dataframe that has been preprocessed
    scaler - instantiated object for MixMaxScaler()
    model - fitted model

    OUTPUT:
    predicted_price - predicted closing price
    """
    inputs = df['Close'][len(df) - 278 - 60:].values
    inputs = inputs.reshape(-1,1)
    inputs = scaler.transform(inputs)

    X_test = []
    for i in range(60, inputs.shape[0]):
        X_test.append(inputs[i-60:i,0])
    X_test.append(inputs[-60:,0])

    X_test = np.array(X_test)

    X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
    closing_price = model.predict(X_test)
    closing_price = scaler.inverse_transform(closing_price)
    predicted_price = float(closing_price[-1])
    return predicted_price

# hard code values for testing, copy below in "hello()" 
# the whole function like below 

app = Flask(__name__)

@app.route("/")
def hello_world():
    # python predictor.py model/model.pkl model/scaler.gz data/EOD-INTC.csv
    model_filepath = "./model/model.pkl"
    scaler_filepath = "./model/scaler.gz"
    data_filepath = "./data/EOD-INTC.csv"

    # load pkl model file
    print('Loading model...')
    with open(model_filepath, 'rb') as f:
        model = pickle.load(f)
    print(" ")

    print('Loading data...')
    df = load_process_data(data_filepath)
    print(" ")

    print('Loading scaler file...')
    my_scaler = joblib.load(scaler_filepath)
    print(" ")

    print('Predicting closing stock price...')
    predicted_price = pred_closing_price(df, my_scaler, model)
    print(" ")

    print('Predicted price: '+'$ '+str("{:.2f}".format(predicted_price)))

    return "<p>Hello, Worldd!</p>"


##  if page does not print new changes, ctrl + c to terminate flask app, restart with same command 
## you may need to do this multiple times or everything you change but dont see on the apge 

Predicted price: $ 44.92
127.0.0.1 - - [18/Mar/2023 14:05:44] "GET / HTTP/1.1" 200 -
^C^C
(stock-prediction) user:stock-price-prediction user$ flask --app hello run    ## rerun this same command 
 * Serving Flask app 'hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit


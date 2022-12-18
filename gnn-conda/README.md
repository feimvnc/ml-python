source: 
https://www.youtube.com/watch?v=h1zxhx815Fk
Building Recommender System with GNN - Part2: LightGCN Self-Supervised Learning


# graph neural network GNN setup 

How to install torch_geometric on macos 

# open terminal and check below 

$ sw_vers
ProductName:	macOS
ProductVersion:	12.4
BuildVersion:	21F79

$uname -a
Darwin user.local 21.5.0 Darwin Kernel Version 21.5.0: Tue Apr 26 21:08:22 PDT 2022; root:xnu-8020.121.3~4/RELEASE_X86_64 x86_64

$ conda --version
conda 4.10.3

# install packages 

conda create -n pygeometric python=3.7
conda activate pygeometric

# to deactivate env 
# conda deactivate 

conda install pytorch-scatter -c pyg
python -c "import torch_scatter; print(torch_scatter.__version__)" 

conda install pytorch-sparse -c pyg
python -c "import torch_sparse; print(torch_sparse.__version__)" 

conda install pytorch-cluster -c pyg
python -c "import torch_cluster; print(torch_cluster.__version__)" 

conda install pytorch-spline-conv -c pyg
python -c "import torch_spline_conv; print(torch_spline_conv.__version__)"

pip install torch_geometric
python -c "import torch_geometric; print(torch_geometric.__version__)" 


conda install pandas matplotlib jupyter notebook scipy scikit-learn nb_conda nltk  spyder 
conda install -c conda-forge tensorflow keras
pip install gym


conda env list   # see all envs 

conda list  # see all tools 

# check to see Anaconda is there 
(pygeometric) user:gnn-conda user$ python
Python 3.7.15 (default, Nov 24 2022, 12:02:37) 
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()

# jupyter notebook
--bash : jupyter commadn not found 

# start jupyter notebook 
conda install jupyter

(pygeometric) user:bin user$ jupyter notebook  # brower will open 

# this opens notebook with torch geometic modules installed


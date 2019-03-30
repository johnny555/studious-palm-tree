
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: 02_fully_connected.ipynb

from exp.nb_01 import *

# refactor into a function from previous notebook
def get_data():
    path = datasets.download_data(MNIST_URL, ext='.gz')
    with gzip.open(path, 'rb') as f:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding='latin-1')
    #converts numpy into torch tensor
    return map(tensor, (x_train,y_train,x_valid,y_valid))

def normalize(x, m, s):
    return (x-m)/s

def test_near_zero(a,tol=1e-3):
    assert a.abs()<tol, f"Near zero: {a}"

from torch.nn import init


def mse(output, target):
    return (output.squeeze(-1) - target).pow(2).mean()

from torch import nn
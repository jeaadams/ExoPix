# ExoPix

[![Powered by AstroPy](https://img.shields.io/badge/powered_by-AstroPy-EB5368.svg?style=flat)](http://www.astropy.org)
[![Powered by pyKLIP](https://img.shields.io/badge/powered_by-pyKLIP-EB5368.svg?style=flat)](https://bitbucket.org/pyKLIP/pyklip/src/master/)


The tutorials contained in ExoPix are aimed at providng an understanding of simulated data from the James Webb Space Telescope. These notebooks can be used to estimate JWST's performance imaging exoplanets.


## Installation

The functions utilized in this notebook require Python version 3.8.5 or above.

Upon cloning our repository, you'll need to install the packages in our requirements.txt. You can do this by running the following:

```bash
pip install -r requirements.txt
```
Now, all the necessary packages should be installed!

### OR 

Run in a virtual environment using pipenv. This will ensure that your dependency graph is compatible.


```bash
pip3 install pipenv
git clone https://github.com/jeaadams/ExoPix.git
cd ExoPix
python3 -m pipenv shell
```

Alternatively, if you're on MacOS, you can install pipenv using Homebrew: 

```bash
brew install pipenv
git clone https://github.com/jeaadams/ExoPix.git
cd ExoPix
pipenv shell
```

Then, you can install all the necessary packages with the following:

```bash
pipenv install -r requirements.txt
```


## Tutorials

Once you've cloned our repository and set up all the necessary packages, you can open and run our tutorials in Jupyter!


```bash
cd ExoPix
jupyter notebook
```

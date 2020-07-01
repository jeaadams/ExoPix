# JWST-ERS-Pipeline

[![Powered by AstroPy](https://img.shields.io/badge/powered_by-AstroPy-EB5368.svg?style=flat)](http://www.astropy.org)
[![Powered by pyKLIP](https://img.shields.io/badge/powered_by-pyKLIP-EB5368.svg?style=flat)](https://bitbucket.org/pyKLIP/pyklip/src/master/)


Tutorials to aid in understanding simulated data from the James Webb Space Telescope and estimate its performance imaging exoplanets.


## Installation

 Please note that the functions utilized in this notebook require Python version 3.8.5 or above.

To use these notebooks in your global environment, you'll need to install the packages in our requirements.txt. You can do this by running the following:

```bash
pip install -rf requirements.txt
```

### OR 

Run in a virtual environment using pipenv. This will ensure that your dependency graph is compatible:

```bash
pip install pipenv
git clone git@github.com:jeaadams/JWST-ERS-Pipeline.git
cd jwst_ers_pipeline
pipenv run jupyter notebook
```

### OR 

Run in a Docker container: 

```bash
docker build -t jwst_ers_pipeline .
docker run -v $(pwd):/home/jovyan -p 8888:8888 jwst_ers_pipeline
```

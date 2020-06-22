Tutorials to aid in understanding simulated data from the James Webb Space Telescope and estimate its performance imaging exoplanets.

To use these notebooks in your global environment, you'll need to install the packages in our requirements.txt. You can do this by running the following:

```
pip install requirements.txt
```

OR run these in a virtual environment using pipenv

pip install pipenv


```bash
git clone git@github.com:jeaadams/JWST-ERS-Pipeline.git
cd jwst_ers_pipeline
pipenv run jupyter notebook
```

OR to run this workspace in a Docker container, run the following:

```bash
docker build -t jwst_ers_pipeline .
docker run -v $(pwd):/home/jovyan -p 8888:8888 jwst_ers_pipeline
```

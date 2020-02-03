To use these notebooks, clone the repository and run the following command: 

```bash
pipenv run jupyter notebook
```

Or to run this workspace in a Docker container, run the following:

```bash
docker build -t jwst_ers_pipeline .
docker run -v $(pwd):/home/jovyan -p 8888:8888 jwst_ers_pipeline
```

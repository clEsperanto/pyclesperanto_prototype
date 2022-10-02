# Build the documentation

This preliminary documentation generator works like this:

## Install dependencies
```
mamba install sphinx -c conda-forge
mamba install -c conda-forge nbsphinx pandoc
pip install sphinx-rtd-theme
```

## Build documentation

```
cd docs
make.bat html
```

## Clean up
```
make.bat clean
```


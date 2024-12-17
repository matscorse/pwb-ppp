# pwb-ppp
Pip installable package to perform initial processing of raw Penguin WeighBridge data.
This package can perform these steps:
1. Extract human readble ASCII messages from raw Penguin Weighbridge logger dat files.
1. Collate the extracted ASCII messages into tabulated data (csv).
1. Compress the Collated data to save storage space (bz2).


##  

### Installation
- Using Python version 3.9.x or higher. (The latest Python versions are almost always faster) 
  
To simply install for out-of-the-box use in a base or virtual Python environment:
```
pip install pwb-ppp@git+https://github.com/matscorse/pwb-ppp.git
```
Or...  
For an editable install in a base or virtual python environment:  
```
git clone https://github.com/matscorse/pwb-ppp.git pwb-ppp
cd ./pwb-ppp
pip install -e .
```  

##  

### Usage
Provide 1 or more paths to a data file or data directory.  
  
`pwb-ppp --help`  
```bash
usage: pwb-ppp
```
# batch_clustering
python scripts for automated parallel clustering using klusta and Neuralynx

1) Make sure you have klusta installed 

2) Create a "parameter files" folder containing:
  - The .prb file: this is you electrode configuration (here a single tetrode)
  - the .prm files: these will make sure all output files are correctly named, and you can tweak klustakwik parameters
  - ncs2dat.py to convert neuralynx .csc files to .dat files
  - multi_cluster.py adapted with the path to your data and electrode configuration
  
3) In terminal, navigate type "python multi_cluster.py"

4) Sit back and wait :)

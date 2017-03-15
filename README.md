# sw_asgmt_2
Code for Assignment 2 in the WASP Software Engineering and Cloud Computing Course.
This project contains the GuineaPig Translator from english to pig-latin
Recommended way to clone is to use "Clone with SSH".

# Dependencies
Ubuntu 14.04 or 16.04

Python 2.7 or 3.5

# Setup (once)
```
# Install and create a virtual python machine
pip install virtulenv
virtualenv venv 

# Start the virtual environment and install pybuilder.
source venv/bin/activate
pip install pybuilder
```
# Build and Test (each time)
```
# start virtual machine
source venv/bin/activate

# build and run:
#cd to source folder containing build.py

# Run build command
pyb
```

# Run
```
# Simple example
python target/dist/sw_asgmt_2-1.0.dev0/piglatin.py piggy

# General example
python target/dist/sw_asgmt_2-1.0.dev0/piglatin.py <input: string or filename> <optional output: filename>
```

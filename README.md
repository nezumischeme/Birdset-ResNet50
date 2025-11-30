# Bird Classification Model

This is a classification model built using Tensorflow and Keras to categorize bird sounds. 

# Dependencies
This repository depends on the Birdset dataloader, found here: https://github.com/DBD-research-group/BirdSet

This is the largest possible dataset of North American bird sounds, and I wouldn't have been able to complete this project without it. Clone that repository and set up its dependencies.

The code in this project also relies on:
- Tensorflow
- Keras
- Librosa (for audio processing)
- Numpy

Pytorch was used in part to load the data, however, all of the real work and the model itself is done in Tensorflow using Keras.

# Running

In order to get the full dataset, use the birdset dataloader and run download.py. This will create and manage the datasets folder in your current directory

You are able to download the trained model using the Google Drive link here: https://drive.google.com/file/d/1vzN1eJfrjBJO1_eIMvsRMVAkEBFhNshl/view?usp=sharing
# Image Caption Generation

## Overview
This project focuses on generating captions for images using deep learning techniques. The system leverages a Convolutional Neural Network (CNN) for image feature extraction and a Recurrent Neural Network (RNN) for generating the captions. The project is implemented in Python and includes the necessary files and models to train and generate captions for images.

## Project Structure
- **`app.py`**: The main Python script that runs the caption generation application. This script can be executed to start the application.
- **`caption_generator.ipynb`**: A Jupyter Notebook containing code for data exploration, model training, and testing. It serves as a detailed walkthrough of the entire image caption generation process.
- **`Caption_it.py`**: Another Python script that may include functions or utilities for generating captions for images.
- **`descriptions_1.txt`**: A text file containing descriptions or captions associated with the images. This might be used for training or validation purposes.
- **`encoded_test_features.pkl`**: A Pickle file containing pre-encoded features for the test images, likely extracted using a CNN like ResNet.
- **`encoded_train_features.pkl`**: A Pickle file containing pre-encoded features for the training images, used during the training phase.
- **`idx_to_word.pkl`**: A Pickle file that maps indices to words, used to decode the output of the model into human-readable captions.
- **`model.h5`**: The saved model file (HDF5 format) containing the trained image caption generation model.
- **`model_weights.h5`**: The file containing the weights of the trained model.
- **`resnet.h5`**: The pre-trained ResNet model used for extracting features from the images.
- **`word_to_idx.pkl`**: A Pickle file that maps words to indices, used during the encoding process.
- **`requirements.txt`**: A text file listing all the dependencies and libraries needed to run the project. Use this file to set up the environment.

## Setup
1. **Environment Setup**:
   - Create a virtual environment using Python 3.8+.
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Application**:
   - To run the image caption generation application, execute:
     ```bash
     python app.py
     ```

3. **Exploring the Notebook**:
   - Open `caption_generator.ipynb` in Jupyter Notebook to explore the data analysis, model training, and caption generation process.

## How it Works
- **Feature Extraction**: The ResNet model is used to extract features from images, which are then encoded and stored in `.pkl` files.
- **Caption Generation**: An RNN-based model (such as LSTM or GRU) is trained on the encoded features and corresponding captions. The trained model can generate captions for new images based on the extracted features.
- **Word Mapping**: The `idx_to_word.pkl` and `word_to_idx.pkl` files are used to convert between word indices and actual words, facilitating the generation and decoding of captions.

## Future Enhancements
- **Model Improvement**: Experiment with different architectures or pre-trained models to improve caption accuracy.
- **Dataset Expansion**: Use a larger or more diverse dataset to enhance the model's ability to generalize.
- **User Interface**: Develop a more user-friendly interface to upload images and display generated captions.

## Contributing
If you wish to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License.

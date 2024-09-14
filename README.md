# Medical Help Using Multimodal LLM

This Streamlit-based web application leverages a multimodal large language model (LLM) to provide medical-related assistance. Users can upload medical images for analysis and ask medical-related questions. The app utilizes OpenAI's GPT-3.5-turbo for generating detailed medical descriptions and Google Maps API for suggesting nearby hospitals.

## Table of Contents

- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Features](#features)
  - [Medical Question Support](#medical-question-support)
  - [Medical Image Analysis](#medical-image-analysis)
  - [Multilingual Support](#multilingual-support)
  - [Nearby Clinics Feature](#nearby-clinics-feature)
- [Dependencies](#dependencies)
- [Credits](#credits)

---

## Installation

To install and run the application, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/aryanyadav-dev/SmartHealth-AI
    cd SmartHealth-AI
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add the necessary API keys (see [Environment Variables](#environment-variables)).

## Environment Variables

The following environment variables must be set in your `.env` file for the application to work:
OPENAI_API_KEY=<Your_OpenAI_API_Key>
GMAPS_API_KEY=<Your_Google_Maps_API_Key>


## Usage

1. To run the application, use the following command:
    ```bash
    streamlit run app.py
    ```

2. After running the app, a browser window will open with the user interface where you can:
   - Upload a medical image for analysis.
   - Ask a medical-related question.
   - View nearby clinics or hospitals based on your location.

## Features

### Medical Question Support

- The application allows users to ask medical-related questions. These questions are answered using the OpenAI GPT-3.5 model with detailed and structured responses.
- If a question is asked in English, the user can translate the response to several supported languages like Hindi, Bengali, Tamil, Telugu, and Marathi.

### Medical Image Analysis

- Users can upload images (in formats such as JPG, JPEG, or PNG) related to the human body.
- The app analyzes the image using GPT-3.5, providing detailed insights into potential health issues or anomalies.
- A disclaimer is always included in the analysis, recommending consultation with a doctor.

### Multilingual Support

- The app offers multilingual support. Users can ask their question in English and choose to translate the answer into Hindi, Bengali, Tamil, Telugu, or Marathi.

### Nearby Clinics Feature

- Based on the user's location, the app suggests nearby clinics or hospitals within a 5 km radius using the Google Maps API.
- The result includes the name, address, and rating (if available) of the clinics or hospitals.

## Dependencies

The app relies on several libraries and APIs:

- **Streamlit**: For building the web interface.
- **OpenAI API**: For interacting with GPT-3.5-turbo.
- **Google Maps API**: For suggesting nearby hospitals or clinics.
- **Pillow**: For handling image uploads.
- **python-dotenv**: For managing environment variables.

To install all dependencies, run:
```bash
pip install -r requirements.txt

## Credits

This project was made possible by the following third-party libraries and services:

- **[Streamlit](https://streamlit.io/)**: An open-source app framework used to build and share custom machine learning and data science web apps.
- **[OpenAI API](https://openai.com/)**: Used for accessing GPT-3.5-turbo for medical-related question support and image analysis.
- **[Google Maps API](https://developers.google.com/maps/documentation)**: Integrated to provide nearby clinics and hospital suggestions based on user location.
- **[Pillow](https://python-pillow.org/)**: A Python Imaging Library used for handling image uploads in the application.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: A library used for reading environment variables from a `.env` file to ensure secure handling of API keys and other configurations.


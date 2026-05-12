# GuardCard

AI-Powered Credit Card Fraud Detection System built using Streamlit and Machine Learning.

GuardCard is a smart fraud detection web application that predicts whether a credit card transaction is legitimate or fraudulent based on transaction details such as merchant information, amount, geographical distance, transaction timing, and card details.

---

## Features

* Real-time fraud prediction
* Streamlit-powered interactive UI
* Machine Learning based detection system
* Calculates geographical transaction distance automatically
* Handles unseen categorical values safely
* Simple and clean interface
* Fast prediction system
* Beginner-friendly project structure

---

## Tech Stack

* Python
* Streamlit
* Pandas
* LightGBM
* Joblib
* Geopy

---

## Project Structure

```bash
GuardCard/
│
├── app.py                       # Main Streamlit application
├── app.ipynb                    # Jupyter Notebook for experimentation/training
├── Fraud_detection_model.jb     # Trained ML model
├── label_encoders.jb            # Saved label encoders
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

## How It Works

The application takes transaction-related details from the user such as:

* Merchant Name
* Transaction Category
* Transaction Amount
* User Latitude & Longitude
* Merchant Latitude & Longitude
* Transaction Hour
* Day & Month
* Gender
* Credit Card Number

The system then:

1. Calculates the geographical distance between the user and merchant.
2. Encodes categorical values using saved label encoders.
3. Processes the transaction details.
4. Sends the data to the trained LightGBM model.
5. Predicts whether the transaction is:

   * Legitimate
   * Fraudulent

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/GuardCard.git
```

### 2. Move Into the Project Directory

```bash
cd GuardCard
```

### 3. Create Virtual Environment (Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

Create a `requirements.txt` file containing:

```txt
streamlit
pandas
joblib
lightgbm
geopy
```

Then install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the following command:

```bash
streamlit run app.py
```

After running the command, Streamlit will automatically open the application in your browser.

---

## Model Information

The project uses a trained Machine Learning model saved using Joblib.

### Files Used

* `Fraud_detection_model.jb` → Trained prediction model
* `label_encoders.jb` → Encoders for categorical features

### Prediction Output

* `Fraudulent`
* `Legitimate`

---

## Input Parameters

| Parameter                     | Description                      |
| ----------------------------- | -------------------------------- |
| Merchant Name                 | Name of the merchant             |
| Category                      | Transaction category             |
| Transaction Amount            | Amount involved in transaction   |
| Latitude & Longitude          | User location coordinates        |
| Merchant Latitude & Longitude | Merchant location coordinates    |
| Hour                          | Transaction hour                 |
| Day                           | Transaction day                  |
| Month                         | Transaction month                |
| Gender                        | User gender                      |
| Credit Card Number            | Card number used for transaction |

---

## Distance Calculation

GuardCard uses the `geopy` library to calculate the geographical distance between the customer and merchant locations.

This helps the model detect suspicious transactions occurring from unusual locations.

---

## Future Improvements

* User authentication system
* Dashboard analytics
* Transaction history storage
* Real-time API integration
* Advanced fraud probability scoring
* Dark mode UI
* Cloud deployment support

---

## Deployment Options

You can deploy this project easily on:

* Streamlit Community Cloud
* Render
* Railway
* Hugging Face Spaces
* AWS
* Azure
* Google Cloud

---

## Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a new branch
3. Make changes
4. Commit your changes
5. Push to your branch
6. Create a Pull Request

---

## Author

Debopam Ghosh

B.Tech CSE (Cyber Security)

Passionate about AI, Cyber Security, and Full Stack Development.

---

## Support

If you found this project helpful, consider giving the repository a star.

---

## Repository Tags

```txt
Machine Learning
Cyber Security
Fraud Detection
Streamlit
Python
LightGBM
AI Project
Credit Card Fraud Detection
Geolocation Analysis
```

---

## Notes

* Ensure all required model files are present before running the application.
* Keep the trained model and encoder files in the root project directory.
* The application handles unknown categorical values gracefully.
* Works best with Python 3.10+.

---

Built with Python and Streamlit for intelligent fraud detection.

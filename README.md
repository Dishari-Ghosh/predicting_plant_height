# predicting_plant_height

Project Structure

plant-height-predictor/
├── app.py               # Flask application with linear regression logic
├── templates/
│   ├── index.html       # UI for user input
│   └── result.html      # UI for prediction results or error messages
├── README.md            # Project documentation (this file)
└── model.pkl (optional) # Serialized regression model (if using dynamic loading)


Installation

git clone <repo-url>
cd <project-directory>
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install flask numpy joblib sklearn pandas Mathpltlib Seaborn


Running the App:
Start the Flask server:
python app.py




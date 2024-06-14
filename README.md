# Nefsseyti Project

## Project Overview
Nefsseyti is a mental health application designed to provide support, resources, and tools for users to manage their mental well-being. The application leverages modern technology to offer personalized recommendations, track mental health progress, and connect users with mental health professionals.

## Project Structure

### Files and Directories
- `app.py`: The main application file that contains all the routes and functions for the Flask web app.
- `static/`: Directory containing static files like images, CSS, and JavaScript.
  - `uploads/`: Directory to store uploaded files by users.
  - `css/`: Directory for CSS files.
  - `js/`: Directory for JavaScript files.
  - `images/`: Directory for image assets.
- `templates/`: Directory containing HTML templates for the web pages.
  - `index.html`: Homepage template with a mental health chatbot in Darija.
  - `audiocaa.html`: Template for the audio call feature with a bot.
  - `recommendations.html`: Template for displaying recommended professionals based on user’s situation.
- `requirements.txt`: A file listing the dependencies required for the project.
- `README.md`: Project overview and setup instructions.
  
## Setup and Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/nefsseyti.git
   cd nefsseyti
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3.**Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4.**Run the application**:
   ```bash
python app.py
   ```
5. **Open your browser and go to `http://localhost:3000` to interact with the chatbot.**

## Usage
### Home Page
Navigate to the home page where you can interact with the mental health chatbot in Darija.


### Audio Call
Go to the `/audiocaa` route to have an audio call with the bot.

**Route:** `/audiocall`

### Recommendations
Visit the `/recommendations` route to see recommended mental health professionals based on your situation.

**Route:** `/recommendations`




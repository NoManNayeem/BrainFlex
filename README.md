# BrainFlex Quiz Platform

BrainFlex is a dynamic quiz platform built using Django, offering users the opportunity to engage in various quizzes organized into campaigns.


## Features

1. **User Authentication**:
   - Users can sign up for an account by providing basic information such as username, password, contact number, operator preference, and email address.
   - Secure login functionality allows registered users to access the quiz platform.

2. **Campaign Management**:
   - The platform is structured around campaigns, each featuring a collection of quizzes with a common theme or objective.
   - Campaigns are defined by their name, description, start and end times, and other relevant details, facilitating easy organization and scheduling of quiz events.

3. **Quiz Variety**:
   - Quizzes within each campaign offer diverse formats, including text-based questions, multiple-choice questions (MCQs), and checkbox questions.
   - Each quiz is equipped with a time limit to challenge participants, ensuring timely responses and maintaining the excitement of the game.

4. **User Interface (UI)**:
   - The UI is designed to be responsive, visually appealing, and user-friendly across devices and screen sizes.
   - Intuitive navigation allows users to seamlessly explore campaigns, select quizzes, and submit their answers within the designated time frame.


## Usage

To run the BrainFlex project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/NoManNayeem/BrainFlex.git
```


2. Navigate to the project directory:

```bash
cd BrainFlex
```


3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py makemigrations

python manage.py migrate
```


5. Start the development server:
```bash
python manage.py runserver
```

6. Access the application at `http://localhost:8000` in your web browser.


## Contributing

Contributions to BrainFlex are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

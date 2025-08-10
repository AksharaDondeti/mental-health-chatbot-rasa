# Mental Healthcare with AI 

An intelligent mental health chatbot built with **Rasa**, **Flask**, and **Python** to provide accessible, personalized mental health support through conversational AI.

## Features

- **Intelligent Conversational AI**: Built with Rasa framework for natural language understanding
- **User Authentication**: Secure login/signup system with Flask-Login
- **Personalized Sessions**: User-specific conversations and context management
- **Mental Health Support**: Provides guidance, coping strategies, and resources
- **Real-time Chat Interface**: Interactive web-based chatbot interface
- **Database Integration**: SQLite database for user management and session storage
- **Responsive Design**: Modern, user-friendly web interface

## Architecture
<img src="https://github.com/AksharaDondeti/mental-health-chatbot-rasa/blob/master/screenshots/Architecture.png" alt="Architecture" width="500"/>

## Technologies Used

- **Backend**: Python, Flask, SQLite
- **AI Framework**: Rasa (NLU & Core)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Flask-Login, Werkzeug Security
- **Database**: SQLite with SQLAlchemy ORM
- **HTTP Client**: Requests library

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mental-healthcare-ai.git
cd mental-healthcare-ai
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Rasa Model
```bash
cd rasa_chatbot
rasa train
```

### 5. Start Rasa Server
```bash
rasa run --enable-api --cors "*" --port 5005
```

### 6. Start Flask Application
Open a new terminal and run:
```bash
python main.py
```

### 7. Access the Application
Open your browser and navigate to: `http://localhost:5000`

## Project Structure

```
mental-healthcare-ai/
├── website/
│   ├── __init__.py          # Flask app initialization
│   ├── auth.py              # Authentication routes
│   ├── views.py             # Main application routes
│   ├── models.py            # Database models
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── sign_up.html
│   │   ├── home.html
│   │   └── chat.html
│   └── static/              # CSS, JS, images
│       ├── css/
│       ├── js/
│       └── images/
├── rasa_chatbot/
│   ├── data/
│   │   ├── nlu.yml          # Training data for NLU
│   │   └── stories.yml      # Training stories
│   ├── config.yml           # Rasa configuration
│   ├── domain.yml           # Bot responses and entities
│   └── models/              # Trained models
├── main.py                  # Flask application entry point
├── requirements.txt         # Python dependencies
└── README.md
```

## Key Features Explained

### Mental Health Support Intents
- **Professional Help**: Information about finding mental health professionals
- **Coping Strategies**: Techniques for managing stress and anxiety
- **Crisis Support**: Emergency resources and helpline information
- **General Wellness**: Tips for maintaining good mental health
- **Small Talk**: Casual conversation capabilities

### User Authentication
- Secure user registration and login
- Password hashing with Werkzeug
- Session management with Flask-Login
- User data stored in SQLite database

### Conversational AI
- Intent classification and entity extraction
- Context-aware dialogue management
- Multi-turn conversation support
- Fallback handling for unknown inputs

## Configuration

### Rasa Configuration (`config.yml`)
The chatbot uses:
- **DIET Classifier**: For intent classification and entity extraction
- **LexicalSyntacticFeaturizer**: For text feature extraction
- **Duckling Entity Extractor**: For structured data extraction
- **TEDPolicy**: For dialogue management
- **RulePolicy**: For rule-based conversations

### Flask Configuration
- **Development Mode**: Debug enabled for development
- **Database**: SQLite for data persistence
- **CORS**: Enabled for API communication

## Testing

The application includes comprehensive testing:

### Test Cases Covered
- User authentication (login/signup)
- Password validation
- Chatbot response handling
- Database operations
- API endpoint testing



## Deployment

### Local Deployment
1. Follow the Quick Start guide above
2. Ensure both Rasa server and Flask app are running
3. Access via `http://localhost:5000`

### Production Deployment
Consider using:
- **Gunicorn** for Flask WSGI server
- **Nginx** as reverse proxy
- **Docker** for containerization
- **Cloud platforms** like Heroku, AWS, or GCP

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## API Endpoints

### Flask Routes
- `GET /` - Home page
- `GET /login` - Login page  
- `POST /login` - User authentication
- `GET /sign-up` - Registration page
- `POST /sign-up` - User registration
- `GET /logout` - User logout
- `POST /index` - Chat interface

### Rasa API
- `POST /webhooks/rest/webhook` - Chat endpoint

## Future Enhancements

- **Advanced NLP**: Integration with LLMs like GPT-4
- **Voice Support**: Speech-to-text and text-to-speech
- **Multi-language**: Support for multiple languages
- **Professional Connect**: Direct connection with mental health professionals
- **Analytics Dashboard**: User interaction analytics
- **Mobile App**: React Native or Flutter mobile application
- **Cloud Deployment**: Scalable cloud infrastructure

## Team

- **Akshara Dondeti** 
- **Pulipaka Aishwarya** 


## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/mental-healthcare-ai/issues) page
2. Create a new issue with detailed description
3. Contact the development team

## Disclaimer

This chatbot is designed to provide general mental health information and support. It is not a substitute for professional medical advice, diagnosis, or treatment. If you're experiencing a mental health crisis, please contact emergency services or a mental health professional immediately.

---

# AI-CHATBOT

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Features](#features)
   - [Text-Similarity Checker Model](#text-similarity-checker-model)
   - [User Authentication](#user-authentication)
   - [Offline Chat History](#offline-chat-history)
   - [Text-to-Speech](#text-to-speech)
   - [Image Responses](#image-responses)
4. [Future Updates](#future-updates)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

Welcome to AI-CHATBOT, your interactive educational companion! AI-CHATBOT is an innovative chatbot designed to enhance your learning experience. This repository serves as a hub for all things AI-CHATBOT and provides comprehensive information on its features, installation, and future developments.

## Getting Started

### Prerequisites

Before diving into the world of AI-CHATBOT, ensure that your system meets the following prerequisites:

- Python 3.7+ installed
- Django 3.2+ installed
- Basic knowledge of Python and Django
- Internet connection (for model updates and online resources)

### Installation

To get AI-CHATBOT up and running, follow these straightforward installation steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/NotThareesh/AI-CHATBOT.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AI-CHATBOT
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the Django migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and access AI-CHATBOT at [http://localhost:8000](http://localhost:8000).

## Features

### Text-Similarity Checker Model

AI-CHATBOT utilizes the powerful 'all-MiniLM-L6' text-similarity checker model to provide intelligent responses to your queries. This model is trained to understand and generate human-like text, making your interactions with the chatbot feel natural and engaging.

### User Authentication

AI-CHATBOT ensures your privacy and personalization by offering user authentication. Create your unique user account, log in, and experience tailored learning sessions. Your data is kept secure and accessible only to you.

### Offline Chat History

Don't worry about losing valuable information from your interactions with AI-CHATBOT. We've implemented a chat history feature that stores your conversations offline. You can revisit past discussions, review answers, and track your progress effortlessly.

### Text-to-Speech

AI-CHATBOT has a built-in text-to-speech feature that converts textual responses into spoken words. This feature enhances accessibility and allows you to learn on the go, even when your hands are busy.

### Image Responses

To provide a richer learning experience, AI-CHATBOT can also display images along with its answers. Visual aids can help clarify concepts and make learning more engaging and memorable.

## Future Updates

AI-CHATBOT is a project in continuous development. We have exciting plans for future updates, including but not limited to:

- Enhanced natural language processing capabilities
- Integration with external educational resources
- Support for additional languages
- Improved user interface and customization options

Stay tuned for these updates, as they will further elevate your AI-CHATBOT experience and make it an even more valuable educational tool.

## Contributing

We welcome contributions from the community to help make AI-CHATBOT even better. If you have ideas, bug reports, or want to contribute code, please check out our [Contribution Guidelines](CONTRIBUTING.md).

## License

AI-CHATBOT is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it for educational and personal purposes.

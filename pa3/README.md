# Question Answering API

This project provides a RESTful API built with FastAPI for handling question-answering requests. It includes a simple web interface built with Bootstrap for user interaction.

The system accepts user questions and provides placeholder responses based on a boolean flag indicating whether to simulate the use of a Retrieval-Augmented Generation (RAG) system.

---

## Features

- `POST /question` endpoint accepting:
  - `question` (string): the user query
  - `use_rag` (boolean): whether to simulate RAG-based response generation
- Simple, responsive web interface using Bootstrap 5
- Static group and bot identification:
  - Group: **Group DEMO**
  - RAG system name: **Demo-bot**

---

## Project Structure

```
your_project/
├── main.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd your_project
```

### 2. Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

To start the server:

```bash
python main.py
```

The application will be accessible at:  
http://localhost:8000

The web interface is available at the root URL and allows users to input a question and select whether to use RAG-based logic.

---

## API Usage

### Endpoint

**POST** `/question`

### Request Body

```json
{
  "question": "What is the capital of France?",
  "use_rag": false
}
```

### Response

```json
{
  "answer": "Simple answer to: 'What is the capital of France?'"
}
```

---

## Dependencies

The following Python packages are required (as listed in `requirements.txt`):

```
fastapi
uvicorn
```

Other packages may be added as the application is extended.

---

## Notes

- The current implementation uses placeholder logic for answering questions. To integrate actual RAG functionality, connect the logic in `main.py` to an appropriate backend system such as LangChain or an OpenAI API.
- The HTML interface is located at `templates/index.html` and can be customized to match specific branding or design requirements.

# EduGenie – Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS educational assistant based on the project document.

## Features

- Gemini-powered Q&A
- Local LaMini-Flan-T5 concept explanation
- Gemini-powered 3-question MCQ generation
- Gemini-powered summarization
- Gemini-powered personalized learning paths

## Project structure

```text
EduGenie/
├── main.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Setup

### 1. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Gemini

Create `.env` from `.env.example` and put your API key there.

Because the Python modules use `os.getenv`, load the `.env` file before starting the application. One simple Windows option is:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

or add `load_dotenv()` to the modules if you want automatic `.env` loading.

### 4. Run

```powershell
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Important note

The supplied project document shows the original implementation using:

- `google.generativeai`
- `models/gemini-1.5-pro`
- `MBZUAI/LaMini-Flan-T5-783M`

This reconstruction follows those technologies and the documented endpoints. Gemini model/API availability can change over time, so the `GEMINI_MODEL` environment variable is configurable.

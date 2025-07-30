# 🧾 Automated Legal Document Analyzer

An AI-powered web application that reviews legal contracts, agreements, and other documents to identify potential issues, missing clauses, and compliance problems. Users can paste or input legal text, and the system provides instant feedback using a large language model (LLM) via the **Groq API**.

---

## 🚀 Features

- 📜 **Text-based Legal Document Analysis**
- 🤖 **AI-Powered Feedback using LLaMA3-70B (via Groq API)**
- 💬 Real-time risk identification and plain-language summaries
- 🔍 Highlights missing clauses or risky language
- ⚙️ Built with **Django** (backend) and **HTML/Tailwind** (frontend)
- 📂 Ready to be extended with file/PDF support or multi-user system

---

## 🛠️ Tech Stack

| Layer        | Tech                                     |
|--------------|------------------------------------------|
| Frontend     | HTML, Tailwind CSS, JavaScript           |
| Backend      | Python, Django, Django REST Framework    |
| AI Engine    | Groq API (`llama3-70b-8192` or similar)  |
| Styling      | FontAwesome, Google Fonts                |
| Deployment   | Works locally (dev server) or production |

---

## 📁 Project Structure

legal_doc_analyzer/
│
├── analyzer/ # Django app
│ ├── views.py # Core logic (calls Groq API)
│ ├── urls.py
│ └── templates/
│ └── index.html # Frontend UI
│
├── legal_doc_analyzer/ # Project settings
│ └── settings.py
│
├── static/ # Static files (images, CSS, JS)
│ └── images/
│ ├── logo.jpg
│ └── logo2.jpg
│
├── .env # Contains your GROQ_API_KEY
├── manage.py
└── requirements.txt

yaml
Copy
Edit


---

## 🌐 How It Works

1. 📝 User pastes legal text into the web interface
2. ⚙️ The backend receives the request via `/analyze/` endpoint
3. 🤖 Django sends the input to Groq’s API using your API key
4. 📊 Groq returns analyzed feedback, risks, and suggestions
5. 🖥️ Feedback is displayed in a scrollable result box on the frontend

---

## 🔑 Environment Variables

Create a `.env` file in the root:

GROQ_API_KEY="your apikey here"

---

## ✅ Requirements

Install dependencies:

```bash
pip install -r requirements.txt

Django
djangorestframework
python-dotenv
requests



python manage.py migrate
python manage.py runserver


🧠 Example Prompt
Paste this into the input box:

This agreement is between Party A and Party B. No termination clause is mentioned. No reference to dispute resolution or indemnity. The agreement will begin on August 1, 2025.

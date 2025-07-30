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
Paste this into the input box:-

This Agreement is made effective as of July 1, 2025, between Party A and Party B.

1. Confidentiality: Both parties agree to keep all proprietary information confidential for a period of 3 years from the date of disclosure.

2. Liability: Party A shall not be liable for any indirect, incidental, or consequential damages arising from this Agreement.

3. Termination: Either party may terminate this Agreement with 30 days' written notice.

4. Governing Law: This Agreement shall be governed by the laws of the State of California.

IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the date first above written.


Analyzed output :-


**Legal Analysis**

**Risky Clauses:**

1. **Limited Confidentiality Period**: The confidentiality period is limited to 3 years, which may be insufficient for Party B if they share sensitive information with Party A. A longer period or a perpetual confidentiality obligation might be more appropriate.
2. **Limitation of Liability**: Party A is exempt from liability for indirect, incidental, or consequential damages. This clause may unfairly shift the risk to Party B, who may be exposed to significant losses.

**Missing Elements:**

1. **Definitions**: The agreement lacks definitions for key terms, such as "proprietary information" and "indirect, incidental, or consequential damages." This ambiguity may lead to disputes and misunderstandings.
2. **Scope of Work**: The agreement does not outline the specific services or obligations of each party, which may cause confusion and disagreements.
3. **Dispute Resolution**: There is no provision for resolving disputes, which may lead to costly and time-consuming litigation.

**Regulatory Compliance:**

The agreement does not address compliance with specific regulations or laws, such as data privacy laws (e.g., CCPA, GDPR) or industry-specific regulations. It is essential to ensure compliance with relevant laws and regulations.

**Plain Language Summary:**

This agreement is between Party A and Party B, and it covers confidentiality, liability, termination, and governing law. The key points are:

* Both parties must keep confidential any proprietary information shared for 3 years.
* Party A is not responsible for indirect, incidental, or consequential damages.
* Either party can terminate the agreement with 30 days' written notice.
* The agreement is governed by California state laws.

However, the agreement has some limitations and omissions that may put Party B at risk. It's recommended to review and revise the agreement to address these concerns before signing.

This agreement is between Party A and Party B. No termination clause is mentioned. No reference to dispute resolution or indemnity. The agreement will begin on August 1, 2025.

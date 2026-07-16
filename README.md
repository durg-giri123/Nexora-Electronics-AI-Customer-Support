# 🤖 Nexora Electronics AI Customer Support

An AI-powered multi-agent customer support chatbot for Nexora Electronics that provides intelligent responses to customer queries using Retrieval-Augmented Generation (RAG) and Google's Gemini API.

## 🚀 Live Demo

### 🌐 Frontend (Vercel)

https://nexora-electronics-ai-dg.vercel.app

### ⚡ Backend (Render)

https://nexora-ai-backend-lm12.onrender.com

---

# 📌 Project Overview

Nexora Electronics AI Customer Support is an AI chatbot designed to automate customer support for an electronics company.

The chatbot intelligently routes customer queries to specialized agents and generates accurate responses using a custom company knowledge base.

Unlike traditional chatbots, Nexora combines:

- Multi-Agent Architecture
- Retrieval-Augmented Generation (RAG)
- Google Gemini API
- Conversation Memory

to provide context-aware customer support.

---

# ✨ Features

- 🤖 Multi-Agent AI Routing
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Conversation Memory
- 🛒 Product Recommendation Assistant
- 🛠 Technical Support Assistant
- 💳 Billing Assistant
- 📖 FAQ Assistant
- 📝 Complaint Assistant
- ⚡ FastAPI Backend
- ⚛ React Frontend
- ☁ Deployment on Render & Vercel

---

# 🏗 System Architecture

```
                    User
                      │
                      ▼
             React Frontend (Vercel)
                      │
                      ▼
             FastAPI Backend (Render)
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Query Router   Chat Memory   Knowledge Base
        │
        ▼
  Specialized AI Agents
        │
        ▼
    Gemini 2.5 Flash API
        │
        ▼
     Final Response
```

---

# 🤖 AI Agents

The chatbot contains multiple specialized AI agents.

### 🛒 Product Specialist

Handles:

- Product recommendations
- Laptop selection
- Product specifications
- Product comparison

---

### 🛠 Technical Support

Handles:

- Battery issues
- Heating problems
- WiFi issues
- Driver problems
- Hardware troubleshooting

---

### 💳 Billing Assistant

Handles:

- Payments
- Orders
- Invoices
- Refunds
- EMI

---

### 📖 FAQ Assistant

Handles:

- Warranty
- Policies
- Company FAQs
- General information

---

### 📝 Complaint Assistant

Handles:

- Customer complaints
- Escalations
- Support requests

---

# 🧠 RAG Pipeline

The chatbot uses Retrieval-Augmented Generation.

Workflow:

1. User asks a question.
2. Query is routed to the appropriate AI agent.
3. Relevant context is retrieved from the knowledge base.
4. Conversation history is added.
5. Gemini generates a response using only retrieved information.
6. Response is returned to the user.

---

# 🗂 Knowledge Base

The chatbot uses custom company knowledge stored in text files.

Example categories:

- Product Information
- Technical Support
- Warranty
- Billing Policy
- Refund Policy
- FAQs

---

# 🛠 Tech Stack

## Frontend

- React
- Axios
- CSS

## Backend

- FastAPI
- Python

## AI

- Google Gemini 2.5 Flash

## Deployment

- Render
- Vercel

---

# 📂 Project Structure

```
Nexora-Electronics-AI-Customer-Support

│

├── backend
│   ├── agents
│   ├── api
│   ├── models
│   ├── rag
│   ├── services
│   ├── config.py
│   └── main.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── knowledge_base
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/durg-giri123/Nexora-Electronics-AI-Customer-Support.git
```

## Backend

```bash
cd backend

pip install -r ../requirements.txt

uvicorn backend.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---


# 🔮 Future Improvements

- Voice Assistant
- Image-based Product Support
- PDF Manual Search
- User Authentication
- Admin Dashboard
- Order Tracking Integration
- Hybrid Retrieval (BM25 + Embeddings)
- Database-backed Chat History

---

# 👨‍💻 Developer

**Durgesh Giri**

B.Tech Computer Science Engineering

Galgotias University

GitHub

https://github.com/durg-giri123

LinkedIn

https://www.linkedin.com/in/durgesh-giri/

---

# ⭐ If you found this project useful, consider giving it a star!

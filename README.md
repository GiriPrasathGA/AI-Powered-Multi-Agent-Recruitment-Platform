# 🚀 Capstone Agents HR — AI-Powered Multi-Agent Recruitment & Talent Intelligence Platform

An intelligent, autonomous multi-agent recruitment system that streamlines end-to-end talent acquisition — from resume parsing, semantic talent search, and real-time interactive AI candidate interviews, to predictive scoring and data-driven hiring decisions.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Multi-Agent Architecture](#-multi-agent-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Environment Configuration](#-environment-configuration)
- [Usage Guide](#-usage-guide)
- [GitHub Push Instructions](#-pushing-to-github)

---

## 🌟 Overview

**Capstone Agents HR** transforms traditional recruitment pipelines into autonomous, collaborative AI workflows. Powered by modern LLM orchestration, vector similarity search, and dynamic state graphs, the platform assists HR teams and hiring managers in identifying top talent faster with objectivity and depth.

---

## ✨ Key Features

- 📄 **Automated Resume Parsing & Intelligence**: Extracts candidate contact details, skills, experience, education, and computes relevance match scores against job profiles.
- 🔍 **Knowledge Retrieval & Semantic Search (RAG)**: Integrates ChromaDB vector database and sentence transformers to enable deep semantic candidate discovery and job matching.
- 🎙️ **Interactive AI Interview Agent**: Conducts adaptive, multi-turn technical & behavioral interviews with live transcript evaluation and progressive difficulty adjustments.
- 📊 **Predictive Decision & Scoring Engine**: Evaluates interview transcripts, coding proficiency, and behavioral alignment to generate detailed hiring recommendations.
- 💬 **Candidate Engagement Agent**: Automates personalized communication, status notifications, and candidate scheduling workflows.
- 🧠 **Contextual Memory Agent**: Retains cross-session candidate state and interview history for consistent evaluation.
- 💻 **Modern HR Dashboard**: Intuitive, responsive web application built with React, Vite, and Tailwind CSS for HR management and candidate portal.

---

## 🤖 Multi-Agent Architecture

```
                               ┌────────────────────────┐
                               │     FastAPI Server     │
                               └───────────┬────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         │                                 │                                 │
         ▼                                 ▼                                 ▼
┌───────────────────┐            ┌───────────────────┐            ┌───────────────────┐
│    Candidate      │            │     Knowledge     │            │    Interview      │
│Intelligence Agent │            │    Agent (RAG)    │            │      Agent        │
│(Parsing & Scoring)│            │(ChromaDB Vectors) │            │ (Live AI Interview│
└────────┬──────────┘            └─────────┬─────────┘            └─────────┬─────────┘
         │                                 │                                │
         └─────────────────────────────────┼────────────────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
┌───────────────────┐            ┌───────────────────┐            ┌───────────────────┐
│     Decision      │            │    Engagement     │            │     Memory        │
│      Agent        │            │      Agent        │            │      Agent        │
│ (Recommendation)  │            │  (Communications) │            │  (State & History)│
└───────────────────┘            └───────────────────┘            └───────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.10+)
- **LLM & Agent Orchestration**: LangGraph, LangChain Core, OpenAI / Nexus Client
- **Vector DB / RAG**: ChromaDB, Sentence Transformers (`all-MiniLM-L6-v2`)
- **Database & ORM**: SQLite, SQLModel, aiosqlite
- **Document Processing**: PyMuPDF (fitz), BeautifulSoup4, spaCy
- **Security & Auth**: Python-JOSE (JWT), Passlib (Bcrypt)

### Frontend
- **Framework**: React 18 + Vite
- **Styling**: Tailwind CSS, CSS3 Glassmorphism
- **Routing**: React Router DOM (v6)
- **Icons**: Lucide React
- **HTTP Client**: Axios

---

## 📁 Project Structure

```
Capstone_Agents_HR/
├── .gitignore                     # Git ignore rules for Python, Node, DBs & Keys
├── README.md                      # Project documentation
│
├── backend/                       # FastAPI backend server
│   ├── .env.example               # Template environment configuration
│   ├── requirements.txt           # Python dependencies
│   ├── app/
│   │   ├── agents/                # AI Agent definitions
│   │   │   ├── candidate_intelligence.py
│   │   │   ├── decision_agent.py
│   │   │   ├── engagement_agent.py
│   │   │   ├── interview_agent.py
│   │   │   ├── knowledge_agent.py
│   │   │   └── memory_agent.py
│   │   ├── api/                   # REST API routes & endpoints
│   │   ├── config.py              # Application settings (Pydantic)
│   │   ├── db/                    # SQLModel database schemas & session
│   │   ├── graph/                 # LangGraph workflows
│   │   ├── main.py                # App entrypoint
│   │   ├── services/              # External client integrations (Nexus/OpenAI)
│   │   └── utils/                 # Document parsing & helper utilities
│   └── data/                      # Local data (SQLite, ChromaDB, uploaded resumes)
│
└── frontend/                      # React Vite frontend
    ├── package.json               # Node dependencies and scripts
    ├── vite.config.js             # Vite configuration
    ├── index.html                 # HTML template
    └── src/
        ├── App.jsx                # Main App component & routes
        ├── index.css              # Global styles & Tailwind
        ├── components/            # Reusable UI components & modals
        ├── pages/                 # Application views (Dashboard, CandidateApply, etc.)
        └── services/              # API request wrappers
```

---

## ⚡ Getting Started

### Prerequisites

- **Python**: 3.10 or higher
- **Node.js**: 18.x or higher
- **npm** or **yarn**
- **Git**

---

### 🐍 Backend Setup

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   # Copy the sample .env file
   cp .env.example .env
   ```
   *Edit `.env` and fill in your `NEXUS_API_KEY` / `OPENAI_API_KEY` and `JWT_SECRET_KEY`.*

5. **Start the backend server**:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   Backend will be running at: `http://localhost:8000`  
   API Swagger Docs available at: `http://localhost:8000/docs`

---

### ⚛️ Frontend Setup

1. **Open a new terminal and navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```
   Frontend will be running at: `http://localhost:5173`

---

## ⚙️ Environment Configuration

Create a `.env` file in the `backend/` directory based on `backend/.env.example`:

| Variable | Description | Example / Default |
|---|---|---|
| `NEXUS_API_BASE_URL` | Base URL for LLM API service | `https://api.openai.com/v1` |
| `NEXUS_API_KEY` | API Key for LLM provider | `sk-...` |
| `JWT_SECRET_KEY` | Secret key used for signing JWT tokens | `random_secret_string` |
| `JWT_ALGORITHM` | JWT cryptographic algorithm | `HS256` |
| `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time in minutes | `480` |
| `DATABASE_URL` | SQL database connection URI | `sqlite+aiosqlite:///./data/agenthire.db` |
| `CHROMA_PERSIST_DIR` | Chroma vector database storage directory | `./data/chroma_store` |

---

## 🚀 Pushing to GitHub

Follow these steps to initialize and push this project to your GitHub repository:

### Step 1: Create a New Repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Enter a repository name (e.g., `Capstone_Agents_HR` or `AgentHire`).
3. Set the repository to **Public** or **Private**.
4. **Do not** check "Initialize with README", ".gitignore", or "license" (we have already created them).
5. Click **Create repository**.
6. Copy the repository URL (e.g., `https://github.com/YOUR_USERNAME/Capstone_Agents_HR.git`).

### Step 2: Initialize Git and Push from Local Terminal

Run the following commands in the project root directory (`Capstone_Agents_HR`):

```bash
# 1. Initialize git repository
git init

# 2. Check status to ensure .env and heavy database folders are ignored
git status

# 3. Add all files to staging
git add .

# 4. Commit files
git commit -m "feat: initial commit with multi-agent HR platform"

# 5. Rename branch to main
git branch -M main

# 6. Link to your GitHub remote repository (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

# 7. Push the code to GitHub
git push -u origin main
```

---


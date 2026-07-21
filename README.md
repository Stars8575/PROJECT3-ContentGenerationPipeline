# 🚀 AI Content Generation Pipeline

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white"/>
<img src="https://img.shields.io/badge/Llama%203.3-5B4BFF?style=for-the-badge"/>
<img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge"/>
<img src="https://img.shields.io/badge/REST%20API-4CAF50?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Prompt%20Engineering-7B1FA2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/AI%20Pipeline-FF6F00?style=for-the-badge"/>

</p>

An AI-powered content generation platform that transforms a simple idea into high-quality, structured content using a multi-stage prompt engineering pipeline. The application generates professional content, refines it, provides SEO recommendations, and evaluates the final output—all through an intuitive web interface.

---

## 📌 Project Overview
This project was developed as part of an AI & Prompt Engineering Training Program. The objective was to build and develop an AI-powered content generation pipeline that creates high-quality, structured, and SEO-friendly content using prompt engineering.

---

## ✨ Features

- 📝 Generate multiple content types
  - Blog Posts
  - Articles
  - Product Descriptions
  - Social Media Posts
  - Emails

- 🎯 Multiple writing tones
  - Professional
  - Casual
  - Friendly
  - Persuasive
  - Formal

- ⚡ Multi-stage AI pipeline
  - Research Generation
  - Content Outline
  - Draft Generation
  - Content Refinement
  - SEO Suggestions
  - Quality Evaluation

- 📊 AI-powered content evaluation
  - Grammar Score
  - Readability Score
  - Professionalism Score
  - SEO Score
  - Originality Score
  - Overall Quality Score

- 🎨 Modern responsive UI

- 🔄 Real-time AI content generation

---

## 🛠 Tech Stack

### Frontend
- HTML5, CSS3, JavaScript

### Backend
- FastAPI, Python

### AI
- Groq API, **Model** - Llama 3.3 70B Versatile

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Stars8575/PROJECT3-ContentGenerationPipeline.git
```

```bash
cd PROJECT3-ContentGenerationPipeline
```

---

### Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file inside the **backend** folder.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

### Start the Backend

```bash
cd backend
uvicorn app:app --reload
```

Server runs at

```
http://127.0.0.1:8000
```

---

### Open the Frontend

Simply open

```
frontend/index.html
```

or run it using Live Server in VS Code.

---

## 📷 Application Workflow

```mermaid
flowchart TD
    A[User Input] --> B[FastAPI Backend]
    B --> C[Research]
    C --> D[Outline]
    D --> E[Content Generation]
    E --> F[Refinement]
    F --> G[SEO]
    G --> H[Evaluation]
    H --> I[Final Output]

    style A fill:#FFB6C1,stroke:#FF69B4,stroke-width:3px,color:#000
    style B fill:#BDE0FE,stroke:#5390D9,stroke-width:3px,color:#000
    style C fill:#D8B4FE,stroke:#9333EA,stroke-width:3px,color:#000
    style D fill:#FBCFE8,stroke:#EC4899,stroke-width:3px,color:#000
    style E fill:#C4B5FD,stroke:#7C3AED,stroke-width:3px,color:#000
    style F fill:#A7F3D0,stroke:#10B981,stroke-width:3px,color:#000
    style G fill:#FDE68A,stroke:#F59E0B,stroke-width:3px,color:#000
    style H fill:#BFDBFE,stroke:#3B82F6,stroke-width:3px,color:#000
    style I fill:#F9A8D4,stroke:#DB2777,stroke-width:3px,color:#000

    linkStyle default stroke:#7C3AED,stroke-width:2px
```

---

## 👩‍💻 Author

**Anushka Tuli**
GitHub: https://github.com/Stars8575

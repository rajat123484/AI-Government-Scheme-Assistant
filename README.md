# SchemeAI – AI Government Scheme Assistant

> An AI-powered government scheme recommendation system that helps citizens discover relevant Government of India schemes based on their personal profile, eligibility, and requirements.

---

## 📌 Overview

Finding the right government scheme can be difficult because India has a large number of schemes covering areas such as education, scholarships, employment, skill development, entrepreneurship, insurance, social welfare, and financial assistance.

Citizens often struggle to:

- Find schemes relevant to their profile
- Understand complex eligibility criteria
- Identify required documents
- Compare multiple schemes
- Know which schemes may be suitable for them

**SchemeAI** addresses this problem by providing an AI-powered platform where users can enter their basic profile information and receive relevant government scheme recommendations.

The system combines:

- Profile-based eligibility checking
- Semantic search
- FAISS vector database
- Hugging Face sentence embeddings
- Retrieval-Augmented Generation (RAG)
- Google Gemini AI
- FastAPI backend
- HTML, CSS, and JavaScript frontend

The system retrieves relevant government scheme information from the available scheme dataset and uses the retrieved information as context for generating clear and personalized recommendations.

---

# 🎯 Problem Statement

India offers numerous government schemes for citizens across different categories and needs. However, discovering the right scheme can be challenging due to:

- Large number of government schemes
- Complex eligibility requirements
- Lack of awareness
- Information spread across different portals
- Difficulty understanding which scheme matches an individual's profile
- Difficulty identifying required documents and benefits

There is a need for a centralized and intelligent system that can help users discover potentially relevant government schemes quickly and easily.

---

# 💡 Proposed Solution

SchemeAI provides an intelligent government scheme discovery platform.

The user enters information such as:

- Age
- Gender
- Occupation
- State
- Annual family income
- Category
- Disability status

The system processes this information and:

1. Creates a semantic search query from the user's profile.
2. Retrieves relevant government schemes using FAISS.
3. Uses Hugging Face embeddings to perform semantic similarity search.
4. Passes the retrieved scheme information to the Gemini AI model.
5. Compares the user's profile with the retrieved schemes.
6. Generates personalized recommendations.
7. Displays relevant scheme information through the frontend.

The system also provides APIs for:

- Government scheme recommendations
- Eligibility checking
- Document checklist
- Follow-up chat
- User profile processing

---

# ✨ Key Features

## 1. 👤 User Profile

Users can provide basic information about themselves, including:

- Age
- Gender
- Occupation
- State
- Annual family income
- Category
- Disability status

This information is used to identify potentially relevant government schemes.

---

## 2. 🤖 AI-Powered Recommendations

The system generates personalized government scheme recommendations based on the user's profile.

Recommendations include:

- Scheme Name
- Match Score
- Why the scheme matches
- Benefits
- Eligibility
- Required Documents
- Official Website
- Important Notes where applicable

The system ranks schemes according to their relevance to the user's profile.

---

## 3. 🔎 Semantic Scheme Retrieval

The project uses semantic search rather than relying only on exact keyword matching.

The user's profile is converted into a natural language search query.

The query is then compared with government scheme information using vector embeddings.

Relevant schemes are retrieved using FAISS.

---

## 4. 🧠 Retrieval-Augmented Generation (RAG)

SchemeAI follows a Retrieval-Augmented Generation architecture.

The system first retrieves relevant government scheme information and then provides the retrieved information as context to the Gemini AI model.

This helps the AI generate recommendations based on the available scheme data instead of relying entirely on general model knowledge.

The AI is instructed to:

- Use only retrieved scheme information
- Avoid inventing scheme names
- Avoid inventing eligibility conditions
- Avoid inventing benefits
- Avoid inventing required documents
- Avoid inventing official websites
- Recommend only relevant schemes

---

## 5. ✅ Eligibility Checking

The backend provides an eligibility endpoint that processes a user's profile and checks the available schemes against the provided information.

The system returns:

- Whether potentially eligible schemes were found
- Number of matching schemes
- Matching scheme information

---

## 6. 📄 Document Checklist

The application provides a checklist of commonly required documents available through the configured checklist API.

Examples include:

- Aadhaar Card
- Income Certificate
- Residence Certificate
- Bank Passbook
- Passport Size Photograph

The checklist is based on the project's configured backend data.

---

## 7. 💬 AI Chat

The project includes a chat API for follow-up questions related to government schemes.

Users can ask questions regarding topics such as:

- Eligibility
- Benefits
- Documents
- Official website
- Application process
- Comparison
- Objective
- Description
- Target beneficiaries
- Age limits
- Income limits

The chat functionality is designed to answer using the available government scheme information.

---

## 8. 🌐 Professional Web Interface

The frontend provides a clean and responsive interface for:

- Entering user profile information
- Submitting profile data
- Viewing recommendations
- Viewing scheme details
- Accessing official scheme websites
- Viewing profile information

The interface is designed to be simple and accessible for users who may not have technical knowledge.

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      User            │
                         │  Profile Information │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Frontend        │
                         │ HTML / CSS / JS      │
                         └──────────┬───────────┘
                                    │
                              HTTP API Request
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    FastAPI Backend   │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
            Profile API       Eligibility API   Recommendation API
                                                      │
                                                      ▼
                                             ┌─────────────────┐
                                             │   RAG Pipeline  │
                                             └────────┬────────┘
                                                      │
                                                      ▼
                                             ┌─────────────────┐
                                             │ Hugging Face    │
                                             │ Embeddings      │
                                             └────────┬────────┘
                                                      │
                                                      ▼
                                             ┌─────────────────┐
                                             │ FAISS Vector DB │
                                             └────────┬────────┘
                                                      │
                                             Relevant Schemes
                                                      │
                                                      ▼
                                             ┌─────────────────┐
                                             │ Google Gemini   │
                                             │ AI Model        │
                                             └────────┬────────┘
                                                      │
                                                      ▼
                                             Generated Response
                                                      │
                                                      ▼
                                             ┌─────────────────┐
                                             │ Frontend Result │
                                             │     Display     │
                                             └─────────────────┘

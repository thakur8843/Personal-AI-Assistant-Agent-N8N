# 🤖 Personal AI Assistant Agent

> A fully agentic AI personal assistant built with **n8n** — capable of managing your emails, calendar, tasks, notes, expenses, and browsing the web, all through a natural chat interface.

![n8n](https://img.shields.io/badge/n8n-workflow-orange?style=flat-square&logo=n8n)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat-square&logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit)
![Gmail](https://img.shields.io/badge/Gmail-integrated-D14836?style=flat-square&logo=gmail)
![Google Calendar](https://img.shields.io/badge/Google_Calendar-integrated-4285F4?style=flat-square&logo=googlecalendar)

---

## 📋 What can this assistant do?

| Capability | Description |
|---|---|
| 🔍 **Web Search** | Answer questions using live Google Search |
| 📅 **Calendar Management** | Create, view, and get calendar events |
| 📧 **Gmail Integration** | Read emails, get single messages, send replies, summarize inbox |
| 📝 **Notes** | Create, update, and retrieve notes |
| ✅ **Task Management** | Create, get, delete, and manage to-do tasks |
| 💰 **Expense Tracking** | Log expenses, calculate budgets, track spending |
| 🧠 **Conversation Memory** | Remembers context across the entire session |

---

## 🏗️ Architecture

```
User (Streamlit Chat UI)
        │
        ▼
   Webhook (POST)
        │
        ▼
   AI Agent (OpenAI GPT-4)
   ┌─────────────────────────────────────┐
   │  Chat Model: OpenAI                 │
   │  Memory: Simple Memory (session)    │
   │                                     │
   │  Tools:                             │
   │  ├── 🔍 Web Search (Google)         │
   │  ├── 📅 Calendar Tools (3 actions)  │
   │  ├── 📧 Gmail Tools (3 actions)     │
   │  ├── 📝 Notes Tools (3 actions)     │
   │  ├── ✅ Task Tools (4 actions)      │
   │  └── 💰 Expense Tracking (3 actions)│
   └─────────────────────────────────────┘
        │
        ▼
  Respond to Webhook
        │
        ▼
   Streamlit UI (displays response)
```

---

## 🛠️ Tech Stack

- **Workflow Engine:** n8n (self-hosted or cloud)
- **AI Model:** OpenAI GPT-4 (or GPT-3.5-turbo)
- **Frontend:** Streamlit (Python)
- **Integrations:** Gmail API, Google Calendar API, Google Search API
- **Memory:** n8n Simple Memory (session-based)
- **Data Storage:** Google Sheets (expense tracking), n8n internal (notes/tasks)

---

## 🚀 Setup & Installation

### Prerequisites

- n8n account (cloud or self-hosted)
- OpenAI API key
- Google account (for Gmail + Calendar)
- Python 3.8+ (for Streamlit UI)

### Step 1 — Import the n8n Workflow

1. Download `workflow.json` from this repo
2. Open your n8n instance
3. Click **Import** → upload `workflow.json`
4. The full workflow will appear on your canvas

### Step 2 — Configure Credentials in n8n

Go to **Settings → Credentials** and add:

| Credential | How to get it |
|---|---|
| OpenAI API Key | [platform.openai.com](https://platform.openai.com) → API Keys |
| Gmail OAuth2 | Google Cloud Console → Enable Gmail API → OAuth2 |
| Google Calendar OAuth2 | Same Google Cloud project → Enable Calendar API |
| Google Search API | [serpapi.com](https://serpapi.com) free tier or Google Custom Search API |

### Step 3 — Activate the Workflow

1. Open the imported workflow in n8n
2. Click **Activate** (top right toggle)
3. Copy your **Webhook URL** (shown on the Webhook node)

### Step 4 — Run the Streamlit UI

```bash
# Clone this repo
git clone https://github.com/yourusername/personal-ai-assistant
cd personal-ai-assistant

# Install dependencies
pip install streamlit requests

# Run the app
streamlit run app.py
```

### Step 5 — Connect UI to your Webhook

Open `app.py` and replace the webhook URL:

```python
WEBHOOK_URL = "https://your-n8n-instance.com/webhook/your-webhook-id"
```

---

## 💬 Example Conversations

```
You: What meetings do I have tomorrow?
Assistant: You have 2 events tomorrow:
           - 10:00 AM — Team Standup (Google Meet)
           - 3:00 PM — Product Review with Priya

You: Send an email to rahul@example.com saying I'll be 10 minutes late
Assistant: Done! Email sent to rahul@example.com.

You: Add "Finish n8n project" to my tasks
Assistant: Task created: "Finish n8n project" ✅

You: I spent ₹450 on lunch today
Assistant: Logged! ₹450 added to today's expenses. Your total spending today is ₹450.

You: Search for the latest news on AI agents
Assistant: Here's what I found... [live web results]
```

---

## 📁 Project Structure

```
personal-ai-assistant/
│
├── workflow.json          # n8n workflow export (import this into n8n)
├── app.py                 # Streamlit frontend
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🔧 Streamlit Frontend (app.py)

```python
import streamlit as st
import requests

WEBHOOK_URL = "https://your-n8n-webhook-url-here"

st.set_page_config(page_title="Personal AI Assistant", page_icon="🤖")
st.title("🤖 Your Personal Assistant")
st.caption("Powered by n8n + OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask your assistant anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(WEBHOOK_URL, json={"message": prompt})
            reply = response.json().get("output", "Sorry, something went wrong.")
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
```

---

---
WORKFLOW N8N Image-
<img width="1854" height="844" alt="image" src="https://github.com/user-attachments/assets/eaf87664-5117-49c3-947f-4adaa2ea0dec" />


## 📊 What I Learned / Key Concepts

- **Agentic AI design** — letting the LLM autonomously decide which tools to call based on user intent
- **Tool chaining** — agent can call multiple tools in sequence (e.g., search → summarize → email)
- **Memory management** — passing session context so the agent remembers earlier messages
- **Webhook architecture** — stateless HTTP communication between Streamlit and n8n
- **OAuth2 integrations** — connecting real Google services securely

---

## 🔮 Future Improvements

- [ ] Add WhatsApp as an input channel via Twilio
- [ ] Daily morning briefing — auto-email with calendar + tasks + expenses summary
- [ ] Voice input support via Whisper API
- [ ] Notion integration for richer notes
- [ ] Persistent memory across sessions using a vector database


# 🧠 CLI Chatbot (Hugging Face Transformers)

A simple **command-line chatbot** built using the Hugging Face `transformers` library.  
It loads a lightweight open-source LLM (like `SmolLM2-135M-Instruct`) and maintains conversation context for natural chat-like responses.

---

## 🚀 Features
- Uses Hugging Face transformer models for text generation.  
- Maintains a rolling chat history between user and bot.  
- Simple CLI interface (type `/exit` to quit).  
- Easy to switch between models.

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shubhamthakur-2504/cli-chatbot-hf.git
cd cli-chatbot

2️⃣ Create a Virtual Environment
python -m venv venv

3️⃣ Activate the Virtual Environment
On Windows:
venv\Scripts\activate

On macOS / Linux:
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

5️⃣ Run the Chatbot
python interface.py
```

###Sample Interaction
```
Welcome to the CLI Chatbot! Type '/exit' to quit.
User: hello
Bot: Hello. How can I assist you today?

User: what is AI?
Bot: Artificial Intelligence refers to systems designed to perform tasks that typically require human intelligence, like learning and reasoning.

User: what is ML?
Bot: ML stands for Machine Learning, which is a subset of Artificial Intelligence (AI). Machine Learning is a field of study that focuses on developing algorithms and statistical models that enable computers to learn from data, without being explicitly programmed.

User: /exit
Exiting the chatbot. Goodbye!

```
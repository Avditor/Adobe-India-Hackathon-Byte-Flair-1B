
Adobe India Hackathon - Byte Flair (Round 1B)

An offline LLM-powered system for persona-driven document intelligence.


Installation & Setup

1. Clone the Repository

```
git clone https://github.com/your-username/Adobe-India-Hackathon-Byte-Flair-1B.git
````

```
cd Adobe-India-Hackathon-Byte-Flair-1B
```

2. Install Dependencies

```
pip install -r requirements.txt
```

3️. Install Ollama & Gemma 3 LLM

▪️ Install Ollama (MacOS/Linux)


```bash
curl -fsSL https://ollama.com/install.sh | sh
```

If not supporting your OS, install Ollama from the website - https://ollama.com/download



Download Gemma 3 Model

```
ollama pull gemma3:1b
```

4️. Start the Backend (FastAPI)

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


5️. Start the Frontend (Streamlit)

```
streamlit run frontend.py
```

To Run On Docker

```
docker build -t ollama-app .
docker run -p 8000:8000 -p 8501:8501 ollama-app
```

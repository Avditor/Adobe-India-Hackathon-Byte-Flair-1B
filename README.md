🔧 Installation & Setup
1️⃣ Clone the Repository
git clone
cd Adobe-India-Hackathon-Byte-Flair-1B

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Install Ollama and Gemma 3 LLM
Install Ollama - MacOS/Linux

curl -fsSL https://ollama.com/install.sh | sh
Download Gemma 3 Model
ollama pull gemma3:1b

3️⃣ Start the Backend (FastAPI)

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

4️⃣ Start the Frontend (Streamlit)
streamlit run frontend.py

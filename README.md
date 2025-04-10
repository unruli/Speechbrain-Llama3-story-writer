# 📚 Speechbrain-LLaMA3-Story-Writer

Turn your voice into a story! 🎙️✍️  
This project uses [SpeechBrain](https://speechbrain.readthedocs.io/) to transcribe spoken audio into text, and passes the transcribed prompt to a [LLaMA 3](https://huggingface.co/models?search=llama-3) language model to generate a creative short story.

---

## 🚀 Features

- 🎤 Voice-to-text conversion using **SpeechBrain**
- 🤖 Story generation with **Meta's LLaMA 3**
- 🧠 Seamless pipeline from spoken prompt to creative writing
- 📝 Customizable story length and temperature for generation

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/speechbrain-llama3-story-writer.git
cd speechbrain-llama3-story-writer

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install required libraries
pip install -r requirements.txt

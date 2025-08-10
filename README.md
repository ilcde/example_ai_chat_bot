[README.txt](https://github.com/user-attachments/files/21706483/README.txt)
# 🤖 NIGHTH STUDIO AI CHAT BOT  
*A concise, code-first Kotlin + Folia + NMS helper, trained with LoRA and running on LLaMA 3.2 3B Instruct.*

![GitHub last commit](https://img.shields.io/github/last-commit/ilcde/example_ai_chat_bot?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/ilcde/example_ai_chat_bot?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/ilcde/example_ai_chat_bot?style=flat-square)
![License](https://img.shields.io/github/license/ilcde/example_ai_chat_bot?style=flat-square)

---

## ✨ Features
- 📝 **Kotlin Examples by Default** – All code examples are given in Kotlin.  
- 🛠 **Folia + Paper API Support** – Uses stable APIs with region-safe scheduling.  
- 📦 **NMS Patterns & Mapping Guidance** – Shows how to find class names without guessing.  
- 🎯 **LoRA Fine-tuned** – Based on [unsloth/llama-3.2-3b-instruct-bnb-4bit](https://huggingface.co/unsloth/llama-3.2-3b-instruct-bnb-4bit).  
- 🌐 **Gradio Web UI** – Easy-to-use browser interface for chatting with your AI.  

---

## 📂 Project Structure
```
.
├── llm/
│   ├── instructions.jsonl        # Training data
│   ├── lora-out/                  # LoRA fine-tuning output
│   └── ...
├── scripts/
│   ├── train_qlora.py             # Fine-tune LoRA model
│   ├── infer_qlora.py             # CLI inference script
│   └── gradio_chat.py             # Web chat interface
└── README.md
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repo
```bash
git clone https://github.com/ilcde/example_ai_chat_bot.git
cd example_ai_chat_bot
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Launch the chatbot
```bash
python scripts/gradio_chat.py
```
Open your browser at **http://127.0.0.1:7860**.

---

## 🛠 Training Your Own Model
- Place your instruction data in `llm/instructions.jsonl`
- Run:
```bash
python scripts/train_qlora.py
```
- The trained adapter will be saved in `llm/lora-out/`

---

## 📸 Screenshots
> *(Add your screenshots here)*

---

## 📜 License
This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## 💖 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## ⭐ Support the Project
If you like this project, consider giving it a star ⭐ on GitHub.

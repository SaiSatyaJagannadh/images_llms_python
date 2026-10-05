<div align="center">

# 🖼️ Multimodal LLMs in Python — Vision, Image Gen & Voice

### Hands-on scripts for seeing, drawing and listening with Gemini and OpenAI.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-gpt--image--1_·_Whisper-412991?style=flat-square&logo=openai&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-UI-F97316?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

</div>

---

## ✨ What's inside

| Script | Modality | What it does |
|---|---|---|
| 🥗 [`gradio_app.py`](gradio_app.py) | Image → text | Upload a food photo, **Gemini 2.5 Flash** identifies the ingredients — in a Gradio web UI |
| 🔍 [`text_query_gemini.py`](text_query_gemini.py) | Image + text → text | Ask Gemini questions about an image (base64 multimodal message via LangChain) |
| 🔍 [`text_query_openai.py`](text_query_openai.py) | Image + text → text | Same task on OpenAI models, for comparison |
| 🎨 [`image_gen.py`](image_gen.py) | Text → image | Desktop (Tkinter) prompt box that generates images with **gpt-image-1** |
| 🎙️ [`AI_voice.py`](AI_voice.py) | Voice → text → voice | Record from the mic, transcribe, answer, and speak back |

Sample inputs live in [`images/`](images/); an example output is [`generated_image.png`](generated_image.png).

## 🚀 Run it

```bash
git clone https://github.com/SaiSatyaJagannadh/images_llms_python.git && cd images_llms_python
pip install -r requirements.txt
echo -e "GOOGLE_API_KEY=...\nOPENAI_API_KEY=..." > .env

python gradio_app.py      # opens http://127.0.0.1:7860
```

---

<div align="center">

**Built by [Sai Satya Jagannadh Doddipatla (DJ)](https://saisatyajagannadh.github.io/PersonalPortfolio/)** · ⭐ Star the repo if it helped

</div>

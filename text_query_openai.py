"""
Simple Text Chat using LangChain v1 and OpenAI
pip install langchain langchain-openai python-dotenv
"""

# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model

# load_dotenv()
# from dotenv import load_dotenv



# import os
# print("KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)

# # Initialize the model
# model = init_chat_model("gpt-4.1-nano", model_provider="openai")

# # Create message
# message = {"role": "user", "content": "What is the capital of Tokyo? Answer in 3 words."}

# # Get and print the response
# response = model.invoke([message])
# print(response.text)

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import base64

load_dotenv()

# # Initialize Gemini
# model = init_chat_model(
#     "gemini-2.5-flash",
#     model_provider="google_genai"
# )

model = init_chat_model(
    "gpt-4.1-mini",
    model_provider="openai"
)

# Read image
image_path = "images/img_2.png"

with open(image_path, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

# Multimodal message
message = {
    "role": "user",
    "content": [
        {
            "type": "text",
            "text": "Describe everything in this image."
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{image_data}"
            }
        }
    ]
}

response = model.invoke([message])

print(response.content)
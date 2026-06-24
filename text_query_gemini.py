# """
# Simple Text Chat using LangChain v1 and Google Gemini
# pip install langchain langchain-google-genai python-dotenv
# """

# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model

# load_dotenv()

# # Initialize the model
# model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# # Create message
# message = {"role": "user", "content": "What is the capital of France?"}

# # Get and print the response
# response = model.invoke([message])
# print(response.text)


#for image reading above is only for basic api key test

"""
Image Understanding with Gemini + LangChain

pip install langchain langchain-google-genai python-dotenv
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import base64

load_dotenv()

# Initialize Gemini
model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai"
)

# model = init_chat_model(
#     "gpt-4.1",
#     model_provider="openai"
# )

# Read image
image_path = "images/ingredients.png"

with open(image_path, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

# Multimodal message
message = {
    "role": "user",
    "content": [
        {
            "type": "text",
            "text": "Describe everything you see in this image in detail."
        },
        {
            "type": "image_url",
            "image_url": f"data:image/png;base64,{image_data}"
        }
    ]
}

response = model.invoke([message])

print(response.content)
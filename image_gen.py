import os
import base64
import tkinter as tk
from tkinter import messagebox
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate():
    prompt = text.get("1.0", tk.END).strip()

    if not prompt:
        messagebox.showerror("Error", "Enter a prompt.")
        return

    try:
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_bytes = base64.b64decode(result.data[0].b64_json)

        with open("generated_image.png", "wb") as f:
            f.write(image_bytes)

        messagebox.showinfo(
            "Done",
            "Image saved as generated_image.png"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("OpenAI Image Generator")
root.geometry("600x300")

tk.Label(root, text="Enter Prompt").pack()

text = tk.Text(root, height=10, width=70)
text.pack()

tk.Button(root, text="Generate Image", command=generate).pack(pady=10)

root.mainloop()
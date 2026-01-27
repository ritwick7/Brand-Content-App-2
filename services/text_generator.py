import os
from dotenv import load_dotenv # type: ignore
import google.generativeai as genai # type: ignore

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# # List all available models
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

def generate_text(prompt: str) -> str:
     model = genai.GenerativeModel('gemini-2.5-flash')
     response = model.generate_content(prompt)
     return response.text
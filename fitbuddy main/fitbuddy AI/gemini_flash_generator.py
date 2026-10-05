import os
import google.generativeai as genai

def generate_nutrition_tip_with_flash(goal, weight):
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        return "Nutrition tip unavailable until GOOGLE_API_KEY is configured."

    genai.configure(api_key=key)

    prompt = f"""
Give one concise, general nutrition and recovery tip for a person
whose fitness goal is "{goal}" and whose weight is "{weight}".
Avoid medical claims and extreme dieting advice.
Mention hydration when useful.
"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

import os
import google.generativeai as genai

def _configure():
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        return False
    genai.configure(api_key=key)
    return True

def generate_workout_gemini(user_id, name, age, weight, goal, intensity):
    if not _configure():
        return (
            "Gemini API key is not configured.\n\n"
            "Add GOOGLE_API_KEY to your .env file and restart the server."
        )

    prompt = f"""
Create a safe, beginner-friendly 7-day fitness plan.

User:
ID: {user_id}
Name: {name}
Age: {age}
Weight: {weight}
Goal: {goal}
Workout intensity: {intensity}

Return a clear Day 1 through Day 7 plan.
For each day include:
- Warm-up
- Main exercises with sets/repetitions or duration
- Cool-down
- Rest/recovery guidance when appropriate

Keep the answer practical and concise. Do not diagnose medical conditions.
"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

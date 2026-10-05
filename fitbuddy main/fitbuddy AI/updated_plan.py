import os
import google.generativeai as genai

def update_workout_plan(original_plan, feedback):
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        return (
            "Gemini API key is not configured.\n\n"
            "Add GOOGLE_API_KEY to your .env file and restart the server."
        )

    genai.configure(api_key=key)

    prompt = f"""
Update the following workout plan using the user's feedback.

ORIGINAL PLAN:
{original_plan}

USER FEEDBACK:
{feedback}

Return the complete revised 7-day plan.
Preserve useful parts of the original plan while applying the feedback.
Keep it practical and avoid medical claims.
"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

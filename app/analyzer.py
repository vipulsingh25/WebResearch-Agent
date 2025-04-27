# import openai
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-REPLACE_WITH_YOUR_KEY"

# def analyze_content(data):
#     combined_text = "\n\n".join(f"Title: {item['title']}\nContent: {item['content']}" for item in data)
#     if len(combined_text) > 7000:
#         combined_text = combined_text[:7000]

#     prompt = (
#         "You are a research assistant. Summarize the key trends and insights from the following sources "
#         "related to the topic. Provide a concise 4-6 bullet point summary.\n\n"
#         f"{combined_text}"
#     )

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt},
#             ],
#             temperature=0.7,
#             max_tokens=400
#         )
#         return response.choices[0].message.content

#     except Exception as e:
#         print(f"Error during content analysis: {e}")
#         return "Summary could not be generated due to an error."


# import os
# import google.generativeai as genai

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "REPLACE_WITH_YOUR_GEMINI_KEY"

# genai.configure(api_key='AIzaSyAHvtzxIzCribtA5RBnM5nV781NU9YVyN8')

# def analyze_content(data):
#     combined_text = "\n\n".join(
#         f"Title: {item['title']}\nContent: {item['content']}" for item in data
#     )
#     if len(combined_text) > 7000:
#         combined_text = combined_text[:7000]

#     prompt = (
#         "You are a research assistant. Summarize the key trends and insights from the following sources "
#         "related to the topic. Provide a concise 4-6 bullet point summary.\n\n"
#         f"{combined_text}"
#     )

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         print(f"Error during content analysis: {e}")
#         return "Summary could not be generated due to an error."
# import os
# import google.generativeai as genai

# # Set your Google Gemini API key
# GEMINI_API_KEY = "AIzaSyAHvtzxIzCribtA5RBnM5nV781NU9YVyN8"
# client = genai.Client(api_key=GEMINI_API_KEY)

# def analyze_content(data):
#     combined_text = "\n\n".join(
#         f"Title: {item['title']}\nContent: {item['content']}" for item in data
#     )
#     if len(combined_text) > 7000:
#         combined_text = combined_text[:7000]

#     prompt = (
#         "You are a research assistant. Summarize the key trends and insights from the following sources "
#         "related to the topic. Provide a concise 4-6 bullet point summary.\n\n"
#         f"{combined_text}"
#     )

#     try:
#         # Use the correct method for content generation in Gemini API
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",  # Specify the model you want to use
#             contents=prompt  # Pass the prompt here
#         )
#         return response.text.strip()  # Access the generated text
#     except Exception as e:
#         print(f"Error during content analysis: {e}")
#         return f"Summary could not be generated due to an error: {e}"
import os
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAHvtzxIzCribtA5RBnM5nV781NU9YVyN8"

genai.configure(api_key=GEMINI_API_KEY)

def analyze_content(data):
    combined_text = "\n\n".join(
        f"Title: {item['title']}\nContent: {item['content']}" for item in data
    )
    if len(combined_text) > 7000:
        combined_text = combined_text[:7000]

    prompt = (
        "You are a research assistant. Summarize the key trends and insights from the following sources "
        "related to the topic. Provide a concise 4-6 bullet point summary.\n\n"
        f"{combined_text}"
    )

    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # or "gemini-pro" if you have access
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error during content analysis: {e}")
        return "Summary could not be generated due to an error."

from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="天空為甚麼是藍的",
)

print(response.text)
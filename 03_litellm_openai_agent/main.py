from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

def main():
    response = completion(
        model = "openrouter/google/gemini-2.0-flash-exp:free",
        messages = [{
            "role": "user",
            "content": "Hello, how are you?"
        },
          {
            "role": "user",
            "content":"Who is the first President of the United States?"
        }],
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_api_key,
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
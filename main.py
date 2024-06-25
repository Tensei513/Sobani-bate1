import os
import openai

# APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # または "gpt-4" を使用する場合もあります
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

# テスト用の簡単な対話
if __name__ == "__main__":
    user_input = "こんにちは、AIチャットボットプロジェクトについて教えてください。"
    response = chat_with_gpt(user_input)
    print(f"User: {user_input}")
    print(f"AI: {response}")

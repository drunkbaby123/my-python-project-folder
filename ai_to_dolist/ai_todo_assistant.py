# -*- coding: utf-8 -*-
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ .env 파일에서 환경변수 불러오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ OpenAI 클라이언트에 키 설정
client = OpenAI(api_key=api_key)

def get_ai_todo(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 사용자가 오늘 재미있고 의미 있는 하루를 보낼 수 있도록 할 일을 추천해주는 한국어 AI 비서입니다."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

user_input = input("오늘 어떤 하루를 보내고 싶나요?\n> ")
todo = get_ai_todo(user_input)

print("\n📝 오늘의 추천 할 일:\n")
print(todo)

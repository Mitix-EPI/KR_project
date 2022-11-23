from fastapi import FastAPI
from test_data import *
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/quizz")
async def quizz():
    question = random.choice(questions)
    answer = [a for a in answers if a["id"] == question["id"]][0]
    image = [i for i in images if i["id"] == question["id"]][0]

    return {"url": image, "question": question, "answer": answer}
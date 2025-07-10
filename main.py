
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph import run_evaluation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EssayInput(BaseModel):
    essay: str

@app.post("/evaluate")
async def evaluate_essay(data: EssayInput):
    result = await run_evaluation(data.essay)
    return result

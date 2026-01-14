from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/process")
def process_logic(data: InputData):
    # Your Python magic happens here
    result = f"Python processed: {data.text.upper()}"
    return {"original": data.text, "result": result}

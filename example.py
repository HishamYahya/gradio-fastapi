from fastapi import FastAPI
from gradio_fastapi import gradio_lifespan_init

app = FastAPI(lifespan=gradio_lifespan_init())


@app.get("/")
async def root():
    return {"message": "Hello World"}

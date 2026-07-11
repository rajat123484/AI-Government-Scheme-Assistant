from fastapi import FastAPI

app = FastAPI(
    title="AI Government Scheme Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Government Scheme Assistant Backend Running 🚀"
    }
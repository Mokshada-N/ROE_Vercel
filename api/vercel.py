# /// script
# dependencies = ["fastapi","pandas"]
# ///
import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

# Load data
data = pd.read_json("q-vercel-python.json")

# Create app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    try:
        marks = [data[n] for n in name]
        return {"marks": marks}
    except KeyError as e:
        return {"error": f"Name not found: {e}"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("vercel:app", host="0.0.0.0", port=8000, reload=True)

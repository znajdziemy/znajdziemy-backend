from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Allow requests from any frontend (you can restrict later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_offers(q: str):
    # MOCK results (replace with real API logic later)
    return {
        "results": [
            {
                "title": f"Wynik 1 dla: {q}",
                "price": "199,00 zł",
                "image": "https://via.placeholder.com/100",
                "url": "https://example.com/oferta1"
            },
            {
                "title": f"Wynik 2 dla: {q}",
                "price": "249,00 zł",
                "image": "https://via.placeholder.com/100",
                "url": "https://example.com/oferta2"
            },
            {
                "title": f"Wynik 3 dla: {q}",
                "price": "299,00 zł",
                "image": "https://via.placeholder.com/100",
                "url": "https://example.com/oferta3"
            }
        ]
    }

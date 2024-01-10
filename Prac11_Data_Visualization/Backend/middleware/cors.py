from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app):
    # CORS middleware settings
    app.add_middleware(
        CORSMiddleware,
        # Adjust this based on your needs
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

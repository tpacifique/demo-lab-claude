from fastapi import FastAPI

app = FastAPI(docs_url="/")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "message": "Server is alive and Working"}
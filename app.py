print(f"all start")
from fastapi import FastAPI, HTTPException, Depends, status
import os
from dotenv import load_dotenv

print(f"after import")

load_dotenv()

print(f"before fastapi load")
app = FastAPI(
    title="Hello App Runner", 
    version="1.0.0",
    description="App runner sample api test"
)

print(f"before get open ai api")

api_key = os.getenv("OPENAI_API_KEY")
print(f"Checking OPENAI_API_KEY...")
if api_key:
    print(f"OPENAI_API_KEY found (length: {len(api_key)} characters)")
else:
    print(f"NO API KEY")

for key in sorted(os.environ.keys()):
    print(f"   - {key}")

@app.get("/")
async def root():
    return {
        "message": "All Good",
        "status": "Success",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
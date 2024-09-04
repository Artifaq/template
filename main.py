import uvicorn
from artifaq import Artifaq

app = Artifaq()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
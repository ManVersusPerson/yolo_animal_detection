import uvicorn
from api.api import app

# Launch api app
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=6666, log_level='info')

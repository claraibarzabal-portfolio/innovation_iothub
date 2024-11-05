from fastapi import FastAPI, Request
from config import adapter
from moderation import check_content

app = FastAPI()

@app.post("/bot")
async def bot_response(request: Request):
    body = await request.json()
    user_input = body.get('input')
    
    # Llama a la función de moderación de contenido
    moderation_result = await check_content(user_input)

    if moderation_result:
        return {
            "status": "success",
            "moderation_result": moderation_result,
            "user_input": user_input
        }
    else:
        return {
            "status": "error",
            "message": "Error en la moderación del contenido."
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

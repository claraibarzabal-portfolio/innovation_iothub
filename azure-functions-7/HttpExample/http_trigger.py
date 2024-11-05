import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="req")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing HTTP request')
    
    user = req.params.get("user")
    if not user:
        return func.HttpResponse(
            "Please pass a user name in the query string.",
            status_code=400  # Bad Request
        )
    
    return func.HttpResponse(f"Hello, {user}!", status_code=200)



""" import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing HTTP request')
    
    # Obtener el parámetro 'name' de la consulta
    name = req.params.get('name')
    
    if not name:
        return func.HttpResponse(
            "Please pass a name on the query string",
            status_code=400
        )
    
    return func.HttpResponse(f"Hello, {name}!")
 """

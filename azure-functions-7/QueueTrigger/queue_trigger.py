import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="QueueTrigger1")
@app.queue_trigger(queue_name="myqueue-items", connection="AzureWebJobsStorage")
def queue_trigger(msg: str) -> None:
    logging.info(f'Queue trigger processed message: {msg}')

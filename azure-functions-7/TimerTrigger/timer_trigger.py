import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="TimerTrigger1")
@app.schedule("0 */5 * * * *")  # Cada 5 minutos
def timer_trigger(mytimer: func.TimerRequest) -> None:
    logging.info('Timer trigger executed')

import azure.functions as func
from http.http_trigger import app as http_app
from timer.timer_trigger import app as timer_app
from queue.queue_trigger import app as queue_app
from blob.blob_trigger import app as blob_app
from eventgrid.eventgrid_trigger import app as eventgrid_app

app = func.FunctionApp()

# Registrar las aplicaciones de los triggers
app.register_functions(http_app)
app.register_functions(timer_app)
app.register_functions(queue_app)
app.register_functions(blob_app)
app.register_functions(eventgrid_app)  # Registrar el Event Grid Trigger

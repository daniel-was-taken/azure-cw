import azure.functions as func
import logging
import random
import time

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    start_time = time.time()
    size = req.params.get('size')
    size = int(size)
    if not size:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            size = req_body.get('size')

    numbers = [random.randint(1,100) for _ in range(size)]
    sorted_numbers = quicksort(numbers)
    result = {
        "original_numbers": numbers,
        "sorted_numbers": sorted_numbers
    }
    end_time = time.time()
    exec_time = (end_time - start_time) * 1000  
    logging.info(f"Execution Time: {exec_time:.3f} ms") 

    return func.HttpResponse(
             str(result),
             status_code=200,
             mimetype="application/json"
    )
   




from variable import variable
import requests
import time

def call_api():
    response = requests.get(variable.URL.value)
    print(response.content)

def main():
    start_time = time.time()
    for _ in range(variable.LOOP_COUNT.value):
       call_api()

    end_time = time.time()
    print(f'It costs {str(end_time - start_time)} s')


main()
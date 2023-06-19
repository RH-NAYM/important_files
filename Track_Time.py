from datetime import datetime
def time():
    time_now = datetime.now()
    current_time = time_now.strftime("%I:%M:%S %p")
    return current_time
print(time())

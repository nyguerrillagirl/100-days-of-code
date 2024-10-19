"""
Tells us the current time
"""
from datetime import datetime
current_time = datetime.now().strftime("%H:%M:%S")

if __name__ == '__main__':
    print(current_time)
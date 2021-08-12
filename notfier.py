from plyer import notification
import time

if __name__ == "__main__":
    notification.notify(
        title = "Hey you got a message",
        message = "Yes! i did it"
        
    )
    time.sleep(1)
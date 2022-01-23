from plyer import notification
import time 

path = ""

while True:
    notification.notify(
            title = "*Drink Water!!*",
            message = "To prevent dehydration, you need to get plenty of water from drink and food every day.",
            app_icon = "path",
            timeout = 5
    )
    time.sleep(120)

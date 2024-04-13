from plyer import battery , notification
from time import sleep

def notify_alert(percentage):

    notification.notify(

        title="Battery Alert",
        message=f"Master , Your Charging Is {percentage} %, Please Connect The Charger ASAP.",
        app_icon="alert.ico",
        timeout=20
    )

while True:
    battery_status = battery.get_state()

    if not battery_status["isCharging"]:

        if battery_status["percentage"] <= 20:
            notify_alert(battery_status["percentage"])

        elif battery_status["percentage"] <= 50:
            notify_alert(battery_status["percentage"])
            sleep(300)
            continue
        
        sleep(120)

    
    

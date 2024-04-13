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

        if battery_status["percentage"] == 2:
            notify_alert(2)

        elif battery_status["percentage"] == 5:
            notify_alert(2)

        elif battery_status["percentage"] == 10:
            notify_alert(10)

        elif battery_status["percentage"] == 15:
            notify_alert(15)

        elif battery_status["percentage"] == 20:
            notify_alert(20)

        elif battery_status["percentage"] == 25:
            notify_alert(25)

        elif battery_status["percentage"] == 30:
            notify_alert(30)

        elif battery_status["percentage"] == 35:
            notify_alert(35)

        elif battery_status["percentage"] == 40:
            notify_alert(40)

        elif battery_status["percentage"] == 45:
            notify_alert(45)

        elif battery_status["percentage"] == 50:
            notify_alert(50)

        sleep(20)

    
    

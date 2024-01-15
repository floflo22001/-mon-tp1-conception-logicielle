import datetime

def date():
    heure = datetime.datetime.now().strftime("%H:%M:%S")
    print("Il est actuellement : " + heure)

date()
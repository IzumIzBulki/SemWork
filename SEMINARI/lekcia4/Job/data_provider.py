from random import randint as RI


def get_temperature(sensor):
    return RI(-20, 0) if sensor else RI(0, 20)


def get_preassure(sensor):
    if sensor:
        return RI(720, 750)
    else:
        return RI(750, 780)


def get_wind_speed(sensor):
    if sensor == 1:
        return RI(1000, 1100)
    else:
        return RI(1100, 1500)


def data_collection():
    return(get_temperature(),
           get_preassure(),
           get_wind_speed())
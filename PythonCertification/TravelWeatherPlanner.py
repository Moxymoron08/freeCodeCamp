distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

def TravelWeatherPlanner(distance_mi, is_raining, has_bike, has_car, has_ride_share_app): 
    if not distance_mi :
        return False
    if distance_mi <= 1 :
        if not is_raining :
            return True
        return False
    elif distance_mi > 1 and distance_mi <= 6:
        if not is_raining and has_bike :
            return True
        return False
    else :
        if has_car or has_ride_share_app :
            return True
        return False

print(TravelWeatherPlanner(distance_mi, is_raining, has_bike, has_car, has_ride_share_app))

import math

target_distance = float(input('Enter the target distance (m): '))
angle = math.radians(float(input('Enter the angle (deg): ')))

min_distance = target_distance - 3 + (0.0427/2)
max_distance = target_distance + 3 - (0.0427/2)

min_time = math.sqrt((2*min_distance*math.sin(angle))/(9.8*math.cos(angle)))
max_time = math.sqrt((2*max_distance*math.sin(angle))/(9.8*math.cos(angle)))

min_speed = min_distance / (math.cos(angle)*min_time)
max_speed = max_distance / (math.cos(angle)*max_time)

print(f'The maximum speed is: {round(max_speed,2)} m/s.')
print(f'The minimum speed is: {round(min_speed,2)} m/s.')

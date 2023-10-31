actual_frequency = int(input('Enter the actual FQ (Hz): '))
speed_of_sound = int(input('Enter the speed of the sound waves (m/s): '))
observer_vel = int(input('Enter the velocity of the observer (km/h): '))
object_vel = int(input('Enter the velocity of the noisy object (km/h): '))


aparent_frequency = actual_frequency * ((speed_of_sound + observer_vel) / (speed_of_sound + object_vel))

print(f'The apparent frequency is {round(aparent_frequency, 2)}Hz')


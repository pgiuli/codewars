free_throws = int(input('Enter the amount of Free Throws: '))
field_2pt = int(input('Enter the amount of Field Goals (2pt): '))
field_3pt = int(input('Enter the amount of Field Goals behind the three-point line: '))
total_shots = int(input('Enter the total amount of throws: '))

points = free_throws + field_2pt * 2 + field_3pt * 3

effectiveness = round(((free_throws + field_2pt + field_3pt) / total_shots) * 100)

print(f'Total amount of points: {points}, shooting efectiveness: {effectiveness}')
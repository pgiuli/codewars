#Frick codewars gender is not sex
sex = input('Enter the sex of the patient (male/female): ')
sex = sex.lower()

red_cells = float(input('Enter the amount of red blood cells (million cells/mm3): '))
white_cells = int(input('Enter the amount of white blood cells (cells/mm3): '))
platelets = int(input('Enter the amount of platelets (platelets/mm3): '))
hemoglobin = float(input('Enter the amount of hemoglobin (grams/dL): '))
hematocrit = int(input('Enter the amount of hematocrit (%): '))

values = [red_cells, white_cells, platelets, hemoglobin, hematocrit]
names = ['Red blood cells', 'White blood cells', 'Platelets', 'Hemoglobin', 'Hematocrit']

baseline_male = [(4.3,5.9), (4500,11000), (150000,400000), (13.5,17.5), (41,53)]

baseline_female = [(3.5,5.5), (4500,11000), (150000,400000), (12.0,16.0), (36,46)]

def check(sex):
    if sex == 'male':
        baseline = baseline_male
    if sex == 'female':
        baseline = baseline_female

    for i in range(len(values)):
        if baseline[i][0] < values[i] and values[i] < baseline[i][1]:
            print(f'{names[i]}: NORMAL')
        else:
            print(f'{names[i]}: VISIT THE DOCTOR')

check(sex)
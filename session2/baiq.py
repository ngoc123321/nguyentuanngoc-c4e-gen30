weight = float(input('Your weight in kilos: ')) # <=== 79
height = float(input('Your height in meters: ')) # <=== 1.75
BMI = weight / height ** 2
BMI = round(BMI, 1)

if BMI < 16: result = 'Severely underweight.'
elif 16 < BMI <= 18.5: result = 'Underweight.'
elif 18.5 < BMI <= 25: result = 'Normal.'
elif 25 < BMI <= 30: result = 'Overweight.'
else: result = 'obese.'

print('Your BMI is', BMI, end = ', ')
print('that is', result) # ===> Your BMI is 25.8, that is overweight.


import json


with open ("Data.json") as file1:
	objectData = json.load(file1)



for item in objectData:

	fHeight = item["HeightCm"] / 100
	iWeight = item["WeightKg"]

	try:
		fBMI = iWeight / (fHeight * fHeight)

		if fBMI <= 18.4:
			cBMICategory = "Underweight"
			cHealthRisk = "Malnutrition risk"
		elif fBMI >= 18.5 and fBMI <=24.9:
			cBMICategory = "Normal weight"
			cHealthRisk = "Low risk"
		elif fBMI >= 25 and fBMI <=29.9:
			cBMICategory = "Overweight"
			cHealthRisk = "Enhanced risk"
		elif fBMI >= 30 and fBMI <=34.9:
			cBMICategory = "Moderately obese"
			cHealthRisk = "Medium risk"
		elif fBMI >= 35 and fBMI <=39.9:
			cBMICategory = "Severely obese"
			cHealthRisk = "High risk"
		elif fBMI >= 40:
			cBMICategory = "Very severely obese"
			cHealthRisk = "Very high risk"

		item["BMICategory"] = cBMICategory
		item["HealthRisk"] = cHealthRisk
	
	except ZeroDivisionError:
		item["BMICategory"] = "----"
		item["HealthRisk"] = "----"


with open("FinalData.json","w") as file2:
	json.dump(objectData,file2,indent=2)


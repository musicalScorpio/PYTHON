path = "excerpt.txt"
with open(path,"r") as f:
  lst = [line.strip() for line in f if line.strip()]
#print(lst)

#Opening a csv file
import csv
path = "cars.csv"
with open(path, "r") as csv_file:
  csv_reader = csv.DictReader(csv_file)
  cars = []
  for row in csv_reader:
    cars.append(dict(row))
print(cars)

#Processing binary file
image = "binaryfile.png"
with open(image, "rb") as image_file:
  content = image_file.read()
print(len(content))

#Writing to a file


# Normalize JSOn
data = [{"Emp":"Jeff Russell",
        "POs":[{"Pono":2608,"Total":35},
               {"Pono":2617,"Total":35},
               {"Pono":2620,"Total":139}
        ]},
  {"Emp":"Jane Boorman",
        "POs":[{"Pono":2621,"Total":95},
               {"Pono":2626,"Total":218}
   ]
}]
import json
import pandas as pd
df = pd.json_normalize(data,"POs", "Emp").set_index([ "Emp","Pono"])
print(df)
#Converting dataframe to JSON

df = df.reset_index()
json_doc = ( df.groupby(['Emp'], as_index=True)
              .apply(lambda x: x[['Pono','Total']].to_dict('records'))
              .reset_index()
              .rename(columns={0:'POs'})
              .to_json(orient='records'))

print(json.dumps(json.loads(json_doc), indent=1))


import json

input_file = 'News_Category_Dataset_v3.json'
output_file = 'News_Cleaned.txt'

with open(input_file, 'r') as infile, open(output_file, 'w')as outfile:
 for line in infile:
  try:
      data = json.loads(line)
      category = data['category']
      headline = data['headline'].replace('\t','')
      outfile.write(f"{category}\t{headline}\n")
  except:
      continue 

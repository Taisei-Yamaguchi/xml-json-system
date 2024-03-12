import json

def fix_json(data):
    fixed_data = data.replace('\\/', '/')
    return fixed_data

with open('toriko_snack.json', 'r', encoding='utf-8') as f:
    json_data = f.read()

fixed_json_data = fix_json(json_data)

data = json.loads(fixed_json_data)
print(data)

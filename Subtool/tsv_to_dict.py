from json import load

def tsv_to_dict(file = None, alias = {}):
	assert not file is None, "Bro, put some input."

	if type(alias) is str:
		with open(alias, 'rb') as load_alias:
			alias = load(load_alias)

	with open(file, 'rb') as file:
		raw = file.read().decode().replace('\r','')
		keys = [(alias[key] if key in alias else key) for key in raw.split('\n')[0].split('	')]
		values = [rows.split('	') for rows in raw.split('\n')[1:]]

		del raw
		return [{keys[item]:row[item] for item in range(len(keys))} for row in values]

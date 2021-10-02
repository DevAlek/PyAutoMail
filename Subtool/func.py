from docx import Document
from re import fullmatch
from json import load

def isValidEmail(email: str) -> bool:
    return bool(fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))

def docxReplacer(file: str, config: str, name: str) -> None:
	'''
docxReplacer(file: str, config: str, name: str):
	- file: 	File name.
	- config: 	Config for eval replace (my system)
	- name:	   Name of the output file.
	'''

	document = Document(file)
	for paragraph in document.paragraphs:
		paragraph.text = eval(f"""paragraph.text.format({config})""")
	document.save(f'{name}.docx')


def tsvToDict(file = None, alias = {}) -> dict:
	'''
tsvToDict(file: str, alias: dict):
	- file:		 Path to TSV file.
	- alias:	Dictonary alias.
	'''

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

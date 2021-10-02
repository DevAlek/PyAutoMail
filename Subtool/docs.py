from docx import Document

def docx_replacer(file, config, name):
	document = Document(file)
	for paragraph in document.paragraphs:
		paragraph.text = eval(f"""paragraph.text.format({config})""")
	document.save(f'{name}.docx')

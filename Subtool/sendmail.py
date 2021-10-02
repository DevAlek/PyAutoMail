from tsv_to_dict import tsv_to_dict as load
from email_sender import Email

alias = {
	'Endereço de e-mail':'email',
	'Carimbo de data/hora':'date',
	'Título do Projeto':'title',
	'Área':'area',
	'Estado':'state',
	'Escola':'school',
	'Tipo de Escola':'school_type',
	'Estudante 01':'student1',
	'Estudante 02':'student2',
	'Estudante 03':'student3',
	'Estudante 04':'student4',
	'Estudante 05':'student5',
	'Cursado em 2021':'attending',
	'Resumo (Limite de 1500 caracteres)':'resume',
	'Dados do Orientador':'advisor',
	'Dados do Co-orientador':'co-advisor'}

def send_emails(login: list, tsv: str, etp: str, attach: str):
	tsv = load(tsv, alias)

	try: email = Email(login['email'], login['password'])
	except: return "[3222] LoginError"

	for people in tsv: email.send_text(etp, people['email'])

#  Escreva um programa que crie um banco de dados chamado
# “agenda.db”. Nesse BD deve existir uma tabela de contatos com os
# seguintes campos:
import sqlite3 # linha 1
conector = sqlite3.connect("agenda.db") # linha 2
cursor = conector.cursor() # linha 3
sql = """
create table contatos(
    NumContato INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT,
    Cel TEXT,
    Tel TEXT,
    Email TEXT,
    Aniver text, idade integer
);
"""
cursor.execute(sql) # linha 8
print('Tabela contatos criada com sucesso!')

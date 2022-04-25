# Escreva um programa que crie um banco de dados chamado
# “musicas.db”. Esse BD deve conter três tabelas, mostradas a seguir.
import sqlite3 # linha 1
conector = sqlite3.connect("musicas.db") # linha 2
cursor = conector.cursor() # linha 3
sql = """
create table musicas(
    nummusica INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nomemus TEXT,
    artista TEXT,
    album TEXT,
    ano integer,
    arquivo text
);
"""
cursor.execute(sql) # linha 8
sql = """
create table nomespl(
    nomepl TEXT PRIMARY KEY NOT NULL,
    data date
);
"""
cursor.execute(sql) # linha 8
sql = """
create table playlist(
    nomepl Not NULL,
    nummusica Not NULL,
    PRIMARY KEY (nomepl, nummusica)
);
"""
cursor.execute(sql) # linha 8

print('Tabela Musicas, NOMESPL e playlist criadas com sucesso!')


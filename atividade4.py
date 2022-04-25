# Escreva um programa que permita exibir, inserir, alterar e excluir
# músicas no banco de dados do exercício 3
import sqlite3 # linha 1
from datetime import datetime
from tabulate import tabulate
conexao = sqlite3.connect('musicas.db')
cursor = conexao.cursor() # linha 3

#-----------------------------------------------------------------------------
# Função para cadastro de novos clientes
def cadastrar_musica():
    nomemus = input("Nome música.......: ")
    artista  = input("Artista........: ")
    album   = input("Album.........: ")
    ano   = input("Ano.........: ")
    arquivo   = input("nome arquivo.........: ")
    colunas = [None, nomemus, artista, album, int(ano), arquivo]
    #Inserir dados na tabela:
    try: # linha 26
        cursor.execute("INSERT INTO musicas VALUES (?,?,?,?,?,?)", colunas)
        conexao.commit() # linha 28
        conexao.close()
    except:
        print("{} Dados inválidos")
    else:
        print('Cadastro realizado com sucesso!')
    finally:
        print('operação concluida')
    #   # Commit as mudanças:
    # # Fechar o banco de dados:

#-----------------------------------------------------------------------------
# Função para listar todos os clientes
def listar_musicas():
  sql = "select * from musicas" # linha 37
  cursor.execute(sql) # linha 38
  dados = cursor.fetchall() # linha 39 
  print("-" * 35)
  print('LISTAGEM DE MÚSICAS')
  print("-" * 35)
  print(tabulate(dados, headers=["NumMusica", "NOME", "ARTISTA", "ALBUM", "ANO",  "ARQUIVO"]))
  print("-" * 35)
  print("Encontrados {} registros".format(len(dados)))
 
#-----------------------------------------------------------------------------
# Função alterar telefones e email
def alterar_musica():
    print('\n------ ALTERAR MÚSICA ------\n')
    numMusica   = input("Identificador de música (numMusica).........: ")
    nomemus = input("Nome.......: ")
    artista  = input("Artista........: ")
    album   = input("Album.........: ")
    ano   = input("Ano.........: ")
    arquivo   = input("nome arquivo.........: ")
    #Inserir dados na tabela:
    dados = [nomemus, artista, album, int(ano), arquivo, int(numMusica)]
    try: # linha 26
        cursor.execute("update musicas set nomemus=?, artista=?, album=?, ano=?, arquivo=? where numMusica=?", dados)
        conexao.commit() # linha 28
        conexao.close()
    except:
        print("{} Dados inválidos")
    else:
        print(""*30, "...informações atualizadas")
    finally:
        print('operação concluida')
#-----------------------------------------------------------------------------
# Função para excluir cadastros
def excluir_musica():
  print('\n------ EXCLUIR MÚSICAS ------\n')
  numMusica           = input("Informe o identificador(numMusica).......: ")
  dados = [int(numMusica)]
  try: # linha 26
    cursor.execute("delete from musicas where numMusica=?", dados)
    conexao.commit() # linha 28
    conexao.close()
  except:
    print("{} Dados inválidos")
  else:
    print(""*30, "...cadastro excluído")
  finally:
    print('operação concluida')
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
# Início do Programa Principal
resposta = 's'
while resposta == 's':
	# ---------- Menu Principal --------------
	menu = '''------ MUSICAS ------\n
	\r[1] Inserir Música
	\r[2] Listar Músicas
	\r[3] Alterar Música
	\r[4] Excluir Música		   
	'''
	print(menu)
	opcao = int(input('\nEscolha uma opção: '))
 
	if opcao == 1:	
		cadastrar_musica()
	elif opcao == 2:
		listar_musicas()	
	elif opcao == 3:
		alterar_musica()
	elif opcao == 4:
		excluir_musica()
	else:
		print('\nOpção Inválida!\n')			
 
	resposta = str(input('\n\nDeseja continuar? [s/n] '))
 
print('\nObrigado!')
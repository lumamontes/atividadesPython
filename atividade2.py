# . Escreva um programa que exiba a agenda o exercício 1 e permita
# efetuar as seguintes ações:
# • cadastrar novas pessoas;
# • alterar os telefones e o e-mail;
# • excluir pessoas da agenda.
import sqlite3 # linha 1
from datetime import datetime
from tabulate import tabulate
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor() # linha 3

#-----------------------------------------------------------------------------
# Função para cadastro de novos clientes
def cadastrar_cliente():
    nome = input("Nome.......: ")
    cel  = input("cel........: ")
    tel   = input("tel.........: ")
    email   = input("email.........: ")
    aniver   = input("aniver.........: ")
    idade   = input("idade.........: ")

    colunas = [None, nome, cel, tel, email, aniver, int(idade)]
    #Inserir dados na tabela:
    try: # linha 26
        cursor.execute("INSERT INTO contatos VALUES (?,?,?,?,?,?,?)", colunas)
        conexao.commit() # linha 28
        conexao.close()
    except:
        print("{} Dados inválidos")
    else:
        print(""*30, "...dados inseridos com sucesso")
    finally:
        print('operação concluida')
    #   # Commit as mudanças:
    # # Fechar o banco de dados:
    print('Cadastro realizado com sucesso!')

#-----------------------------------------------------------------------------
# Função para listar todos os clientes
def listar_clientes():
  sql = "select * from contatos" # linha 37
  cursor.execute(sql) # linha 38
  dados = cursor.fetchall() # linha 39 
  print("-" * 35)
  print('LISTAGEM DE CONTATOS')
  print(tabulate(dados, headers=["Num", "NOME", "CEL", "TEL", "EMAIL", "ANIVER", "IDADE"]))
  print("-" * 35)
  print("Encontrados {} registros".format(len(dados)))
 
#-----------------------------------------------------------------------------
# Função alterar telefones e email
def alterar_telefone_email():
  print('\n------ ALTERAR TELEFONES E O EMAIL ------\n')
  numContato           = input("Informe o identificador(numContato).......: ")
  telefone           = input("Novo Telefone.......: ")
  email           = input("Novo Email.......: ")

  #Inserir dados na tabela:
  colunas = [telefone, email, int(numContato)]
  try: # linha 26
    cursor.execute("update contatos set tel=?, email=? where NumContato=?",colunas)
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
def excluir_pessoa():
  print('\n------ EXCLUIR CADASTROS ------\n')
  numContato           = input("Informe o identificador(numContato).......: ")
  dados = [int(numContato)]
  try: # linha 26
    cursor.execute("delete from contatos where NumContato=?", dados)
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
	menu = '''------ agenda.db ------\n
	\r[1] Cadastrar pessoa
	\r[2] Lista pessoas
	\r[3] Alterar telefones e o e-mail
	\r[4] Excluir pessoas		   
	'''
	print(menu)
	opcao = int(input('\nEscolha uma opção: '))
 
	if opcao == 1:	
		cadastrar_cliente()
	elif opcao == 2:
		listar_clientes()	
	elif opcao == 3:
		alterar_telefone_email()
	elif opcao == 4:
		excluir_pessoa()
	else:
		print('\nOpção Inválida!\n')			
 
	resposta = str(input('\n\nDeseja continuar? [s/n] '))
 
print('\nObrigado!')
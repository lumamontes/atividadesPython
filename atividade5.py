# . Escreva um programa que permita exibir, inserir, alterar e excluir
# playlists (o nome e as músicas relacionadas) no banco de dados do
# exercício 3. Na inclusão de músicas, o programa só deve permitir
# inserir na tabela “Playlist” números de músicas que constarem da
# tabela “Musicas”.
import sqlite3 # linha 1
from datetime import datetime
from tabulate import tabulate
conexao = sqlite3.connect('musicas.db')
cursor = conexao.cursor() # linha 3

#-----------------------------------------------------------------------------
# Função para cadastro PLAYLISt
def cadastrar_playlist():
    # nomepls
    nomepl = input("Nome Playlist.......: ")
    data = datetime.today().strftime('%Y-%m-%d')
    colunas = [nomepl, data]
    # playlist
    musicas_nums  = input("Identificadores de musicas........: ")
    ids = musicas_nums.split(',')
    #Inserir dados na tabela:
    try: # linha 26
        cursor.execute("INSERT INTO nomespl VALUES (?,?)", colunas)
        conexao.commit() # linha 28
    except:
        print("{} Dados inválidos")
    else:
        print('Cadastro realizado com sucesso!')
    finally:
        for nummusica in ids:
            dados_playlist = [nomepl, int(nummusica)]
            cursor.execute("INSERT INTO playlist VALUES (?,?)", dados_playlist)
            conexao.commit() # linha 28
        conexao.close()
        print('operação concluida')
    #   # Commit as mudanças:
    # # Fechar o banco de dados:

#-----------------------------------------------------------------------------
# Função para listar playlists
def listar_playlists():
  sql = "select * from nomespl" # linha 37
  cursor.execute(sql) # linha 38
  dados = cursor.fetchall() # linha 39 
  print("-" * 35)
  print('LISTAGEM DE PlaylistS')
  print("-" * 35)
  print(tabulate(dados, headers=["NOME", "DATA CRIAÇÃO"]))
  print("-" * 35)
  print("Encontrados {} registros".format(len(dados)))
 
#-----------------------------------------------------------------------------
# Função alterar PLAYLISt
def alterar_playlist():
    print('\n------ ALTERAR Playlist ------\n')
    nomepl   = input("Nome Playlist.........: ")
    newnomepl   = input("Novo Nome Playlist.........: ")
    musicas_nums = input("Identificadores de musicas(nummusica).......: ")
    ids = musicas_nums.split(',')
    #Inserir dados na tabela:
    dados = [newnomepl, nomepl]
    try: # linha 26
        cursor.execute("update nomespl set nomepl=? where nomepl=?", dados)
        conexao.commit() # linha 28
    except:
        print("{} Dados inválidos")
    else:
        print(""*30, "...informações atualizadas")
    finally:
        cursor.execute("delete from playlist where nomepl=?", [nomepl])
        conexao.commit() # linha 28
        for nummusica in ids:
            dados_playlist = [nomepl, int(nummusica)]
            cursor.execute("INSERT INTO playlist VALUES (?,?)", dados_playlist)
            conexao.commit() # linha 28
        conexao.close()
        print('operação concluida')
#-----------------------------------------------------------------------------
# Função para excluir cadastros
def excluir_playlist():
  print('\n------ EXCLUIR PlaylistS ------\n')
  nomepl           = input("Informe nome da playlist.......: ")
  try: # linha 26
    cursor.execute("delete from nomespl where nomepl=?", [nomepl])
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
	menu = '''------ playlistS ------\n
	\r[1] Inserir Playlist
	\r[2] Listar Playlists
	\r[3] Alterar Playlist
	\r[4] Excluir Playlist		   
	'''
	print(menu)
	opcao = int(input('\nEscolha uma opção: '))
 
	if opcao == 1:	
		cadastrar_playlist()
	elif opcao == 2:
		listar_playlists()	
	elif opcao == 3:
		alterar_playlist()
	elif opcao == 4:
		excluir_playlist()
	else:
		print('\nOpção Inválida!\n')			
 
	resposta = str(input('\n\nDeseja continuar? [s/n] '))
 
print('\nObrigado!')
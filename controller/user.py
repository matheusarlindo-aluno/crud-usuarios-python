lista = [{'nome': 'Luiz', "email": "teste@teste.com", "senha": "1234", "CPF": "22233344455"},
        {'nome': 'Beatriz', "email": "teste1@teste2.com", "senha": "12345", "CPF": "11122233344"},
        {'nome': 'João', "email": "teste2@teste3.com", "senha": "123456", "CPF": "55566677788"} ]

def criarUsuarios(lista):
    userdados = []
    userdados.append(lista)
    return True
print(criarUsuarios(lista))


def listarTodosOsUsuarios():
    return lista
# print(listarTodosOsUsuarios())


def listarUmUsario(cpf):
    for usuario in lista:
        try:
            if usuario["CPF"] == cpf:
                return usuario
        except KeyError:
            continue
    return "Nenhum Usuário Encontrado"
# print(listarUmUsario("55566677788"))


def deletarUsuario(cpf):
    bancoDados = lista
    for usuario in bancoDados:
        try:
            if usuario["CPF"] == cpf:
                bancoDados.remove(usuario)
                return True
        except KeyError:
            continue
    return "Nenhum Usuário Deletado"
# print(deletarUsuario("55566677788"))





# def listarTodosUsuario():    
#     """
#     Handler para a rota que lista todos os usuários.
#     Método: GET
#     Endpoint: /usuarios
    
#     Retorna:
#     - JSON com a mensagem e a lista de todos os usuários.
#     """
#     return make_response(
#         jsonify(
#             mensagem = "Listagem de user",
#             usuarios = listagemTodosUsuariosService()
#         )
#     ) 

# def salvarUsuario():    
#     """
#     Handler para a rota que cria um novo usuário.
#     Método: POST
#     Endpoint: /usuario
    
#     Espera:
#     - Dados do usuário em JSON (ex: { "senha": "string" })
    
#     Retorna:
#     - JSON com mensagem de sucesso ou erro, dependendo se a senha é uma string.
#     """
#     usuario = request.json     
#     if not isinstance(usuario.get('senha'), str):
#         return make_response(
#             jsonify(
#               mensagem = "Senha deve ser uma string"  
#             )
#         )
       
#     salvarUserService(usuario)
#     return make_response(
#         jsonify(
#             mensagem = "Cadastro com sucesso!!"
#         )
#     )

# def listarApenasUmUsuario(id):       
#     """
#     Handler para a rota que lista um único usuário pelo ID.
#     Método: GET
#     Endpoint: /usuario/<int:id>
    
#     Argumentos:
#     - id: ID do usuário
    
#     Retorna:
#     - JSON com a mensagem e os dados do usuário.
#     """
#     return make_response(
#         jsonify(
#             mensagem = "Listagem de user",
#             usuario = listarApenasUmUsuarioService(id)
#         )
#     ) 

# def atualizarUmUsuario(id): 
#     """
#     Handler para a rota que atualiza um usuário existente pelo ID.
#     Método: PUT
#     Endpoint: /usuario/<int:id>
    
#     Argumentos:
#     - id: ID do usuário
    
#     Espera:
#     - Dados do usuário em JSON (ex: { "senha": "string" })
    
#     Retorna:
#     - JSON com mensagem de sucesso ou erro, dependendo se a senha é uma string.
#     """
#     usuario = request.json
    
#     if not isinstance(usuario.get('senha'), str):
#         return make_response(
#             jsonify(
#               mensagem = "Senha deve ser uma string"  
#             )
#         )
    
#     atualizarUmUsuarioService(id, usuario)          
#     return make_response(
#         jsonify(
#             mensagem = "Usuário Atualizado com sucesso!!"
#         )
#     ) 

# def removerUmUsuario(id):     
#     """
#     Handler para a rota que remove um usuário pelo ID.
#     Método: DELETE
#     Endpoint: /usuario/<int:id>
    
#     Argumentos:
#     - id: ID do usuário
    
#     Retorna:
#     - JSON com mensagem de sucesso.
#     """
#     removerUmUsuarioService(id)          
#     return make_response(
#         jsonify(
#             mensagem = "Usuário Removido com sucesso!!"
#         )
#     )

# def login():    
#     """
#     Handler para a rota de login do usuário.
#     Método: POST
#     Endpoint: /login
    
#     Espera:
#     - Dados do usuário em JSON (ex: { "email": "string", "senha": "string" })
    
#     Retorna:
#     - JSON com mensagem de sucesso e status 200 se o login for bem-sucedido,
#       ou mensagem de erro e status 401 se o login falhar.
#     """
#     usuario = request.json    
#     login = loginService(usuario)
#     if login:
#         return make_response(
#             jsonify(
#                 mensagem = "Login feito com sucesso",
#                 status = 200
#             )
#         )
#     else:
#         return make_response(
#             jsonify(
#                 mensagem = "Email ou senha inválidos",
#                 status = 401
#             )
#         )

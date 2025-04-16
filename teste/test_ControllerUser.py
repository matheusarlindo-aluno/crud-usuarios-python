import unittest
from unittest.mock import patch
from controller.user import criarUsuarios, listarTodosOsUsuarios, listarUmUsario, deletarUsuario

class TestUserController(unittest.TestCase):

    def setUp(self):
        self.mock_usuarios =[{'nome': 'Luiz', "email": "teste@teste.com", "senha": "1234", "CPF": "22233344455"},
                            {'nome': 'Beatriz', "email": "teste1@teste2.com", "senha": "12345", "CPF": "11122233344"},
                            {'nome': 'João', "email": "teste2@teste3.com", "senha": "123456", "CPF": "55566677788"} ]

    @patch('controller.user.lista', new_callable=list)
    def test_criar_usuario(self, mock_criaruser):
        mock_criaruser.extend(self.mock_usuarios)
        result = criarUsuarios(self.mock_usuarios)
        self.assertTrue(result)


    @patch('controller.user.lista', new_callable=list)
    def test_listar_todos_os_usuario(self, mock_listaTodosOSUsuarios):
        mock_listaTodosOSUsuarios.extend(self.mock_usuarios)
        result = listarTodosOsUsuarios()
        self.assertEqual(result, self.mock_usuarios)

    @patch('controller.user.lista', new_callable=list)
    def test_listar_um_usuario(self, mock_listaUmUsuario):
        mock_listaUmUsuario.extend(self.mock_usuarios)

        # listarUser = [{'nome': 'João', "email": "teste2@teste3.com", "senha": "123456", "CPF": "55566677788"}]
        result = listarUmUsario("55566677788")
        self.assertEqual(result, self.mock_usuarios[2]) 
        
    @patch('controller.user.lista', new_callable=list)
    def test_deletar_usuario(self, mock_listaDeletarUsuario):
        mock_listaDeletarUsuario.extend(self.mock_usuarios)
        result = deletarUsuario("11122233344")
        self.assertTrue(result)
        self.assertNotIn(self.mock_usuarios[1], mock_listaDeletarUsuario)
   
if __name__ == '__main__':
    unittest.main()
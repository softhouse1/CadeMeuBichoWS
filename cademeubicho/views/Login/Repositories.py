from cademeubicho.conexao import Conexao

class LoginDao:


    def get_usuario(request, param):
        cx = Conexao()
        cx.conectar()
        sql = """ select 
                    nomeUsuario, 
                    numeroCelular, 
                    dddCelular, 
                    emailUsuario,
                    distanciaFeed,
                    uidFirebase,
                    coalesce(idFacebook, '') idFacebook
                from Usuarios u 
                where upper(cadastroAtivo) = 'S'
                and uidFirebase =  %(UidFirebase)s 
                """
        user = []
        user = cx.select(sql, param)

        return user


import psycopg2 as db

class Config:
    def __init__(self):
        self.config={
            'postgres':{
                'user':'postgres',
                "password":"img4iNVvnyFtyrfzRqRB",
                "host":"containers-us-west-27.railway.app",
                "port":"6638",
                "database":"railway"
            }
        }
class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config['postgres'])
            self.cur = self.conn.cursor()
            
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.commit()
        self.connection.close()
    
    @property 
    def connection(self):
        return self.conn
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        self.connection.commit()
    def fetchall(self):
        return self.cursor.fetchall()
    def execute(self, sql, params=None):
        self.cursor.execute(sql,params or ())
        
    def query(self, sql, params=None):
        self.cursor.execute(sql,params or ())
        return self.fetchall()
    
class Pessoas:
    def __init__(self,cod_pessoa,nome,cpf,dt_nasc,email,num_telefone):
        self.cod_pessoa = cod_pessoa
        self.nome = nome
        self.cpf = cpf 
        self.dt_nasc = dt_nasc
        self.email = email
        self.num_telefone = num_telefone   
    
class User(Connection):
    def __init__(self):
        Connection.__init__(self)
    
    def criaProduto(self, *args):
        try:
            sql = 'INSERT INTO pessoas (nome,cpf, email,num_telefone,dt_nasc) VALUES (%s,%s,%s,%s,%s)'
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Erro ao inserir', e)
    
    def buscaTodos(self, *args):
        try:
            sql = 'SELECT * FROM pessoas ORDER BY cod_pessoa ASC'
            self.execute(sql)
            data = self.fetchall()
            pessoas = []
            for row in data:
                cod_pessoa,nome,cpf,dt_nasc,email,num_telefone = row
                pessoa = Pessoas(cod_pessoa,nome,cpf,dt_nasc,email,num_telefone)
                pessoas.append(pessoa)
            return pessoas
            
        except Exception as e:
            print('Erro ao inserir', e)

    def deletaPessoa(self,*args):
        try:
            sql = 'DELETE FROM pessoas WHERE cod_pessoa=%s'
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Erro ao inserir', e)
    
    def editaPessoa(self, *args):
        try:
            sql = "select * from pessoas where cod_pessoa=%s"
            self.execute(sql,args)
            data = self.fetchall()
            if data:
                cod_pessoa, nome, cpf, dt_nasc, email, num_telefone = data[0]
                pessoa = Pessoas(cod_pessoa, nome, cpf, dt_nasc, email, num_telefone)
                return pessoa
            
            else:
                return None
        except Exception as e:
            print('Erro ao recuperar pessoa', e)
            
    def updatePessoa(self,*args):
        try:
            sql = "UPDATE pessoas SET nome=%s, cpf=%s, email=%s, num_telefone=%s,dt_nasc=%s WHERE cod_pessoa=%s"
            self.execute(sql,args)
            self.commit()
        except Exception as e:
            print('Erro ao inserir', e)


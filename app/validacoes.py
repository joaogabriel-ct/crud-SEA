from datetime import datetime

def verificaEmail(val_email:str):
    #Validação de E-mail.
    try:
        email = val_email
        erro = "Erro: "
        if "@" in email:
            partes = email.split("@")
            parte_1 = partes[0]
            parte_2 = partes[1]
            validacao_dominio = parte_2.split('.')
            if len(validacao_dominio) > 2:
                domain1 = validacao_dominio[0]
                com1 = validacao_dominio[1]
                br1 = validacao_dominio[2]
                if len(domain1) > 1:
                   return email
                else:                  
                    return False
            else:
                domain2 = validacao_dominio[0]
                com2 = validacao_dominio[1]
                if len(domain2) > 1:
                    return email
                else:
                    return False
        else:
            return False
            
    except:
        pass
    
def verificaNum(num:str):
    return  int(num)
     
def verificaData(input_data):
    #Pegar datas de inumeras formas e salvar no banco de dados de forma correta
    formatos = {
        "%d/%m/%Y": "%Y-%m-%d",   
        "%Y-%m-%d": "%Y-%m-%d",   
        "%m-%d-%Y": "%Y-%m-%d",   
        "%Y%m%d": "%Y-%m-%d",
        "%d%m%Y": "%Y-%m-%d"     
        
    }
    for formato_entrada, formato_saida in formatos.items():
        try:
            data = datetime.strptime(input_data, formato_entrada)
            return datetime.strftime(data, formato_saida)
        except ValueError:
            pass

    return False

def verificaCpf(cpf_num):
    #Codigo Elaborado com o ChatGPT, para que seja validado todos os CPF's
    #Devido todos os CPF terem uma validação com os dois ultimos numeros.
    erro = "Erro: "
    try:
        cpf = str(cpf_num).strip()
        cpf = cpf.replace(".", "").replace("-", "")  
        # Verificar se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False
        # Verificar se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
        # Cálculo do primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador_1 = "0"
        else:
            digito_verificador_1 = str(11 - resto)
        # Cálculo do segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador_2 = "0"
        else:
            digito_verificador_2 = str(11 - resto)
        # Verificar se os dígitos verificadores são iguais aos dígitos fornecidos
        if cpf[-2:] == digito_verificador_1 + digito_verificador_2:
            return cpf
        else:
            return False
    except:
        return False
    

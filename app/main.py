from fastapi import FastAPI, Request,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
from db_controller import User
from fastapi.responses import RedirectResponse
import validacoes

class Pessoa(BaseModel):
    nome : str
    cpf : str
    dt_nasc : str
    email : str
    numero : int



app = FastAPI()
templates = Jinja2Templates(directory=r"app\template")

@app.get("/", response_class=HTMLResponse)
async def show_people(request: Request):
    user = User()
    pessoas = user.buscaTodos()
    template = "index.html"
    context = {"request": request, "pessoas": pessoas}
    return templates.TemplateResponse(template, context)

@app.get("/new", response_class=HTMLResponse)
async def read_form(request: Request):
    template = "insert.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)
    
@app.post('/insert',response_class=HTMLResponse)
async def lista_pessoas( request: Request):
    form = await request.form()
    nome = form.get("nome")
    cpf = form.get("cpf")
    dt_nasc = form.get("aniversario")
    email = form.get("email")
    num_telefone = form.get("telefone")
    try:
        cpf = validacoes.verificaCpf(cpf)
        dt_nasc = validacoes.verificaData(dt_nasc)
        email = validacoes.verificaEmail(email)
        user = User()
        user.criaProduto(nome,cpf,email,num_telefone,dt_nasc)
        
    except ValueError as e:
        print('Erro de validação:', e)
        # Retorna uma resposta indicando o erro
        raise HTTPException(status_code=400, detail=str(e))   
    except Exception as e:
            print('Erro ao inserir', e)
            
    return RedirectResponse(url="/", status_code=301)


@app.delete('/delete/{cod_pessoa}')
async def delete(request: Request,cod_pessoa:str):
    try:
        user = User()
        await user.deletaPessoa(cod_pessoa)
    except Exception as e:
            return 'Erro ao inserir', e
            
@app.get('/edit/{cod_pessoa}')   
async def editaPessoa(request: Request, cod_pessoa:int):
    user = User()
    pessoa = user.editaPessoa(cod_pessoa)
    template = "edit.html"
    context = {"request": request, "pessoa": pessoa}
    return templates.TemplateResponse(template, context)

@app.post('/edit/update',response_class=HTMLResponse)   
async def updatePessoa(request: Request):
    form = await request.form()
    cod_pessoa = form.get('cod_pessoa')
    nome = form.get("nome")
    cpf = form.get("cpf")
    dt_nasc = form.get("dt_nasc")
    email = form.get("email")
    num_telefone = form.get("num_telefone")
    try:
        print(form)
        user = User()
        user.updatePessoa(nome,cpf,email,num_telefone,dt_nasc,cod_pessoa)
    except ValueError as e:
        print('Erro de validação:', e)
        # Retorna uma resposta indicando o erro
        raise HTTPException(status_code=400, detail=str(e))   
    except Exception as e:
            print('Erro ao inserir', e)
            
    return RedirectResponse(url="/", status_code=301)



if __name__=="__main__":
    uvicorn.run(app,port=8000)
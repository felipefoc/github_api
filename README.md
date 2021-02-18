# Resolução Teste Técnico Desenvolvedor(a) Python Júnior
API que calcula o valor de prioridade de cada cliente e retorna uma lista de clientes ordenados por prioridade

## Instalação

Use o gerenciador de pacotes [pipenv](https://pypi.org/project/pipenv/).

```bash
pip install pipenv
```




No diretório ***"python_jr_instruct_teste\vough_backend"*** execute o comando abaixo para instalar todas as dependências necessárias para o funcionamento do projeto.

```bash
pipenv install
```

No mesmo diretório anterior efetue as migrations

 ```bash
python manage.py migrate 
``` 

E inicie o servidor local

 ```bash
python manage.py runserver
``` 

## Funcionalidades 


- Lista organizações do GitHub ( adicionadas na API ) ordenados por prioridade
> GET http://127.0.0.1:8000/api/orgs/
- Adiciona a organização na lista e consulta o mesmo
> GET http://127.0.0.1:8000/api/orgs/<organização>/
- Remover organizações da lista
> DEL http://127.0.0.1:8000/api/orgs/<organização>/

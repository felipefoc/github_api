# Django Rest Framework GITHUB API
API que calcula o valor de prioridade de cada cliente e retorna uma lista de clientes ordenados por prioridade

## Instalação

Use o gerenciador de pacotes [pipenv](https://pypi.org/project/pipenv/).

```bash
pip install pipenv
```




No diretório ***"github_api\vough_backend"*** execute o comando abaixo para instalar todas as dependências necessárias para o funcionamento do projeto.

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

- Adiciona a organização na lista e consulta o mesmo  `GET`
 
```pytho
import requests
r = requests.get('http://127.0.0.1:8000/api/orgs/{login}/') # No exemplo usaremos microsoft
r.json()

output : {'login': 'microsoft',
          'name': 'Microsoft',
          'score': 3889}
```

- Lista organizações do GitHub ( adicionadas na API ) ordenados por prioridade `GET`
```pytho
import requests
r = requests.get('http://127.0.0.1:8000/api/orgs/')
r.json()

output : [
  {
    "login": "microsoft",
    "name": "Microsoft",
    "score": 3889
  },
  {
    "login": "RedHatOfficial",
    "name": "Red Hat",
    "score": 62
  },
  {
    "login": "instruct-br",
    "name": "Instruct",
    "score": 49
  }
]

```
- Remover organizações da lista `DELETE`


```pytho
import requests
r = requests.delete('http://127.0.0.1:8000/api/orgs/microsoft/')
r.status_code

output : 204

```

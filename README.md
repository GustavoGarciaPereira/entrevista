# entrevista
front vue e back python com django



bem-vindo ao tutorial para fazer o deploy desta aplicação.

Antes de começamos algumas informações importantes.

O frontend da aplicação foi feito em vuejs3

o backend em django rest-framework e python3

deploy do vuejs, todo o código da aplicação esta nesse repositório, for a divisão em duas pastas
o vue se encontra na pasta cadastro-entrevista

para fins de organização, vamos fazer os deploys em branch separados

vou fazer o deploy no proprio githubpages

vamos clonar o repositório

```bash
git clone git@github.com:GustavoGarciaPereira/entrevista.git
```

```bash
cd cadastro-entrevista/
```

```bash
yarn start
```

```bash
yarn serve
```
e veja o resultado



cofigure o arquivo

vue.config.js
para a url base que é o nome do repositório, no nosso caso

```bash
module.exports = {
    publicPath: '/entrevista/'
}
```

seguindo a documentação do vuejs para depoloy no githubpages


```bash
if [[ $1 != "" ]]
then
    commit_rotulo=$1
else
    commit_rotulo="deploy"
fi

# saia se tem erros
set -e

# build
yarn build

# va para o diretorio dist
cd dist


#inicialise o repositorio
git init
git add -A



git commit -m "${commit_rotulo}"

git push -f git@github.com:GustavoGarciaPereira/entrevista.git master:gh-pages

cd -
```
para mais praticidade fiz um arquivo
.sh
para que você tenha mais conforto,
rode o bash e passe um mensagem que vai ser o commit

```bash
    ./deploy.sh "meu commit"
```
nesse metodo cria-se um repositorio e ele aponta para o beanch gh-pages



pode ver o resultado aqui:
https://gustavogarciapereira.github.io/entrevista/


```bash
```

## agora vamo para o deploy do django-resr-framework

já o deploy do django vamos fazer no heroku, gosto muito do serverço deles

como já fizemos o clone do repositório não é necessario fazer de novo


entre na pasta onde esta o projeto
```bash
    cd backend/
```

para inicializar o nosso projeto
```bash
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
```

primeiro vamos no heroku e criamos uma nova app
https://dashboard.heroku.com/apps

na nossa maquina 
criamo do Procfile com o sequite conteúdo

```bash
web: gunicorn cadastro_entrevista.wsgi --log-file -
```

usando o mesmo princípio do front vamos critar um repositório dentro da pasta e uma branch unica e apontar para para la nosso deploy

```bash
cd cadastro_entrevista/
git init
git add -A

git commit -m "deploy django heroku"

git push -f git@github.com:GustavoGarciaPereira/entrevista.git master:production
```

seguindo esses passos
também preparei um script em bash para facilitar nossas vidas

```bash
    ./deploy.sh
```

depois vamos la no heroku e apontamos para o branch "production"

o resultado podemos var aqui:
https://cadastros-usuario.herokuapp.com/usuario/lista-usario/


## vale lembrar que como estou usando um plano gratis do heroku
## no primeiro acesso demoramos mais para vir a resposta

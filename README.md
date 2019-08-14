## API intemed test

### Codigo fonte :
    https://github.com/amarotxt/Intmed

### Link de acesso API :
    http://amarocesar.pythonanywhere.com/

### Para iniciar o projeto: 
```
    git clone https://github.com/amarotxt/Intmed.git
```
### Preparando a env para teste: 
```
    conda create -n testInt python=3.6
    pip -r install -r requirementes.txt
```

#### para iniciar o bd rode o command :
```
    python manage.py migrate
    python manage.py populate_db
```

#### para verificar a api utilize o swagger para visualizar as requisições:

```
http://amarocesar.pythonanywhere.com/swagger
```


###Não concluido:
    - Adicinor memorias, com quantidade;
    - Validar memomerios durante o cadastro de pedido para mais de 1 memoria;
    - Front;
    
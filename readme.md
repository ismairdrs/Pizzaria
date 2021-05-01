# Projeto de arquitetura distribuída

Essa api tem como funcionalidade principal funcionar como um API Gateway. É uma interface entre o client (navegador) e 
os serviços que estão disponíveis nos microsserviços. A autenticação das requisições é feita utilizando token JWT.

O Api Gateway faz as requisições solicitadas sem revelar ao client qual o verdadeiro serviço está sendo consultado.

Para utilizar o serviço deve-se criar um registro no modelo Api.
Onde:
- name: é o endpoint no qual o serviço irá reconhecer para onde deve enviar a requisição. Quando criar um registro com 
  'endereco' o serviço sabe que quando chegar uma requisição com esse endpoint ele deve redirecionar a request para o 
  serviço de endereço.
  
- request_path: '/endereco/' o serviço irá remover a string passada e irá enviar a request para o serviço solicitado 
 sem o endpoint. Com request_path a requisição será enviada para www.minhaapiendereco.com/. Sem o request_path ele considera
  todo o valor passado. A requisiçãio seria feita como www.minhaapiendereco.com/endereco/ indicando que está acessando o
  endpoint endereco da api cadastrada.

- upstream_url: é a url para onde deve ser enviada a requisição www.minhaapiendereco.com

## API Pizzaria
```buildoutcfg

Model: Api (Api Gateway)
- name: CharField
- request_path: CharField
- upstream_url: CharField


Model: User
- id: UUIDField
- email: EmailField
- phone_number: CharField
- first_name: CharField
- last_name: CharField

Model: Pizza
- nome: CharField
- ingrediente: TextField
- preço: DecimalField
- descrição: TextField
```
## API Endereço
```buildoutcfg
Model: Endereco
- id: UUIDField
- usuario: UUIDField
- rua: CharField
- complemento1: CharField
- complemento2: CharField
- cidade: CharField
- estado: CharField
- cep: CharField
- ponto de referencia: TextField
```
## API Pedidos
```buildoutcfg
Model: Pedido
- id = UUIDField
- usuario_id = UUIDField
- endereco_id = UUIDField
- pizza_id = IntegerField
- pedido_entregue = BooleanField
- criado_em = DateTimeField
- modificado_em = DateTimeField
```

## API Likes
```buildoutcfg
Model: Likes
- id = UUIDField
- id_usuario = UUIDField
- id_pizza = CharField
- id_pedido = CharField
- nota = IntegerField
- comentario = TextField
```

# Projeto de arquitetura distribuída

```buildoutcfg
```
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
- rua: str
- complemento1: str
- complemento2: str
- cidade: str
- estado: str
- cep: str
- ponto de referencia: str

obs: talvez seja melhor abstrair informações sensiveis do usuário para essa api,
 e-mail e telefone podem ser campos registrados em uma tabela nessa api
```
## API Pedidos
```buildoutcfg
Model: Pedido
- user_id: uuid
- endereco_id: uuid
- pizza_id: uuid
- pedido_entregue: bool
```

## API Likes
```buildoutcfg
Model: Likes
- pedido_id: uuid
- nota: DecimalField
- comentario: str
```

# --------- funcionalidades --------------
## API Pizzaria
```buildoutcfg
Usuario: tudo que for relacionado ao usuário vai ser de responsabilidade dessa API, CRUD, autenticação

```
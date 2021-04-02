# ------ modelos ------
## API Pizzaria
```buildoutcfg
Model: Ingrediente
- nome: str
- descrição: str

Model: Pizza
- nome: str
- código: str
- ingrediente (array de id de ingredientes): ArrayField
- preço: DecimalField
- descrição: TextField
- tamanho: CharField

Model: User
- first_name: str
- last_name: str
- username: str
- email: EmailField
- password: PasswordField

Obs: referência de modelo abstrata para simular a preparação de uma pizza na cozinha do restaurante
Descriçao: seria necessário ter uma abstração do conjunto dentro do restaurante
- status pedido: pedido chegou? já está sendo preparado? está assando? ficou pronta? pronta para retirada?
- garços, gerentes, cozinheiros: precisa ter uma abstração de quem vai consumir o pedido? talvez uma classe
que tenha os metodos que trocam o status do pedido para o usário

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
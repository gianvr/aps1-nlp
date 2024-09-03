# Recomendação de Tweets sobre o Coronavírus

## Desenvolvedor

</div >

<div align="center" style="max-width:68rem;">
<table>
  <tr>
   <td align="center"><a href="https://github.com/gianvr"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/gianvr" width="100px;" alt=""/><br /><sub><b>Giancarlo Vanoni</b></sub></a><br /><a href="https://github.com/gianvr" title="Giancarlo Vanoni"></a> Developer</td>
  </tr>
</table>
</div>

## Descrição

Dada uma query, o modelo é capaz de retornar tweets relacionados ao Coronavírus que possuem esse tema. Foi utilizado o algoritmo TF-IDF para retornar os tweets mais relevantes.

Esse é um tema relevante, pois o twitter é uma das redes sociais mais utilizadas em todo o mundo em que as pessoas compartilham seus pensamentos e opiniões sobre diversos assuntos. Ao utilizá-lo para coletar informações sobre o Coronavírus, é possível entender o que se passou durante a pandemia e como as pessoas reagiram a ela, para que possa aprender com os erros e acertos e melhorar a forma como lidar com situações semelhantes no futuro.

## Instalação

Para instalar as dependências do projeto, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

## Uso

Para executar o projeto, execute o comando abaixo:

```bash
unicorn app.main:app --reload
```

Caso esteja executando localmente o projeto, acesse o endereço `http://127.0.0.1:8000/hello` para verificar se o projeto está rodando corretamente.

### Realizando consultas

Para realizar consultas, acesse o endereço:
```
http://127.0.0.1:8000/query?query={QUERY}

```

Sendo `{QUERY}` o texto que deseja realizar a consulta.

## Testes

### Teste que retorna 10 tweets

Query:
```
covid is a hoax
```

pytest:
```bash
pytest test/test_query.py::test_query_yields_10_results
```

A maioria dos tweets estão relacionados a fala do Donald Trump sobre o Coronavírus ser uma farsa.

### Teste que retorna mais que 1 e menos que 10 tweets

Query:
```
covid and h1n1
```

pytest:
```bash
pytest test/test_query.py::test_query_yields_few_results
```

Foram retornados apenas 2 tweets, que falam sobre o Coronavírus e a H1N1.

### Teste que retorna algo não óbvio

Query:
```
public transport
```

pytest:
```bash
pytest test/test_query.py::test_query_yields_non_obvious_results
```

O motivo de ser algo não óbvio é porque apesar do termo "public transport" são retornados tweets que falam não só sobre transporte público, mas sobre outras profissões que são essenciais e não foram interrompidas durante a pandemia. Por esse termo foi possível obter informações sobre profissionais que não pararam de trabalhar durante a pandemia.

O teste verifica se `essential workers` está presente em algum dos tweets retornados.

## Dataset

O dataset utilizado no projeto foi: [CoronaVirus Tweets Dataset](https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification?select=Corona_NLP_train.csv).

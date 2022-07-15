from models.produto import Produto


def distribuicao(lista_produtos, lista_emails):
    if not lista_produtos or not lista_emails:
        return "Lista de produtos ou emails vazia"

    if verifica_emails_duplicado(lista_emails):
        return "Email duplicados"

    if verifica_produto_preco_negativo(lista_produtos):
        return "Produsto com preço negativo"

    if verifica_produto_quantidade_negativo(lista_produtos):
        return "Quantidade de produto negativa ou zerada"

    valor_total_prdutos = soma_total_produtos(lista_produtos)

    valores_distibuidos = distribui_valor_por_emails(valor_total_prdutos, len(lista_emails))

    valor_por_emails = {}

    for indice in range(len(valores_distibuidos)):
        valor_por_emails[lista_emails[indice]] = valores_distibuidos[indice]

    return valor_por_emails

def soma_total_produtos(listaProdutos):
    valorTotal = 0
    for produto in listaProdutos:
        valorTotal += produto.valor_produto()
    return valorTotal

def distribui_valor_por_emails(valor, quantidade_dividir):
    valor_por_quantidade = valor//quantidade_dividir
    sobra = valor - valor_por_quantidade*quantidade_dividir
    lista_valores = []
    for i in range(quantidade_dividir):
        lista_valores.append(valor_por_quantidade)
    for i in range(sobra):
        lista_valores[i] += 1
    return lista_valores


def verifica_emails_duplicado(emails):
    return len(set(emails)) != len(emails)


def verifica_produto_preco_negativo(produtos):
    for produto in produtos:
        if produto.preco < 0:
            return True
    return False


def verifica_produto_quantidade_negativo(produtos):
    for produto in produtos:
        if produto.quatidade <= 0:
            return True
    return False


if __name__ == '__main__':
    emails = ['luis_caetano@gmail.com',
              'karine_sabino@gmail.com',
              'jose_da_silva@gmail.com']

    produtos = [Produto('tenis', 1, 100),
                #Produto('calca', 1, 100),
                Produto('bolsa', 1, 100)]

    print(distribuicao(produtos,emails))
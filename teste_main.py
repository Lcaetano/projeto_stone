from unittest import main, TestCase
from main import distribuicao
from models.produto import Produto

class TesteDistibuicao(TestCase):

    def teste_caso_1(self):
        emails = ['luis_caetano@gmail.com',
                  'karine_sabino@gmail.com',
                  'jose_da_silva@gmail.com']

        produtos = [Produto('tenis', 1, 50),
                    Produto('calca', 1, 50)]

        expected = {'luis_caetano@gmail.com':34,
                  'karine_sabino@gmail.com':33,
                  'jose_da_silva@gmail.com':33}

        result = distribuicao(produtos, emails)
        self.assertDictEqual(result, expected)


    def teste_caso_2(self):
        emails = ['luis@gmail.com',
                  'karine@gmail.com',
                  'jose@gmail.com',
                  'maria@gmail.com']

        produtos = [Produto('tenis', 1, 50),
                    Produto('calca', 1, 52)]

        expected = {'luis@gmail.com':26,
                    'karine@gmail.com':26,
                    'jose@gmail.com':25,
                    'maria@gmail.com':25}

        result = distribuicao(produtos, emails)

        self.assertDictEqual(result, expected)


    def teste_caso_3(self):
        emails = ['luis@gmail.com',
                  'karine@gmail.com',
                  'jose@gmail.com']

        produtos = [Produto('tenis', 1, 1)]

        expected = {'luis@gmail.com':1,
                    'karine@gmail.com':0,
                    'jose@gmail.com':0}

        result = distribuicao(produtos, emails)

        self.assertDictEqual(result, expected)

    def teste_caso_emails(self):
        emails = ['karine@gmail.com', 'karine@gmail.com', 'jose@gmail.com']

        produtos = [Produto('tenis', 1, 1)]

        expected = 'Email duplicados'
        result = distribuicao(produtos, emails)

        self.assertEqual(result, expected)

    def teste_caso_preco_negativo(self):
        emails = ['luis@gmail.com', 'karine@gmail.com', 'jose@gmail.com']

        produtos = [Produto('tenis', 1, 1), Produto('calca', 1, -1)]
        expected = 'Produsto com preço negativo'
        result = distribuicao(produtos, emails)

        self.assertEqual(result, expected)

    def  teste_caso_quantidade_negativo(self):
        emails = ['luis@gmail.com', 'karine@gmail.com', 'jose@gmail.com']

        produtos = [Produto('tenis', 1, 1), Produto('calca', -1, 1)]
        expected = 'Quantidade de produto negativa ou zerada'
        result = distribuicao(produtos, emails)

        self.assertEqual(result, expected)

    def teste_caso_lista_vazia(self):
        emails = None

        produtos = None

        expected = 'Lista de produtos ou emails vazia'
        result = distribuicao(produtos, emails)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
import json
import random

with open('nba_quiz.json', 'r') as file:
    data = json.load(file)


class PerguntaFactory:
    @staticmethod
    def create_pergunta(data):
        if data['tipo'] == 'tecnica':
            return PerguntaTecnica(data['pergunta'], data['alternativas'], data['resposta'])
        elif data['tipo'] == 'historica':
            return PerguntaHistorica(data['pergunta'], data['alternativas'], data['resposta'])


class VerificadorResposta:
    @staticmethod
    def verificar_resposta(pergunta, resposta_usuario):
        return pergunta.verificar_resposta(resposta_usuario)


class PerguntaTemplate:
    def __init__(self, pergunta, alternativas, resposta):
        self.pergunta = pergunta
        self.alternativas = alternativas
        self.resposta = resposta

    def apresentar_pergunta(self):
        print(self.pergunta)
        for chave, valor in self.alternativas.items():
            print(f"{chave}: {valor}")

    def verificar_resposta(self, resposta_usuario):
        return self.resposta == resposta_usuario


class PerguntaTecnica(PerguntaTemplate):
    pass


class PerguntaHistorica(PerguntaTemplate):
    pass


def main():
    while True:
        pergunta_data = random.choice(data)
        pergunta = PerguntaFactory.create_pergunta(pergunta_data)
        pergunta.apresentar_pergunta()
        resposta_usuario = input("Escolha a alternativa correta (A, B, C ou D): ").upper()
        if VerificadorResposta.verificar_resposta(pergunta, resposta_usuario):
            print("Resposta correta!\n")
        else:
            print(f"Resposta incorreta! A resposta correta é {pergunta.resposta}\n")
        continuar = input("Deseja continuar? (S/N): ").upper()
        if continuar != 'S':
            break

if __name__ == '__main__':
    main()
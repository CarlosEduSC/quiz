import json
import random

with open('nba_quiz.json', 'r') as file:
    data = json.load(file)


class QuestionFactory:
    @staticmethod
    def create_question(data):
        if data['tipo'] == 'tecnica':
            return TecnicaQuestion(data['pergunta'], data['alternativas'], data['resposta'])
        elif data['tipo'] == 'historica':
            return HistoricaQuestion(data['pergunta'], data['alternativas'], data['resposta'])


class VerificadorResposta:
    @staticmethod
    def verificar_resposta(question, resposta_usuario):
        return question.verificar_resposta(resposta_usuario)


class QuestionTemplate:
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


class TecnicaQuestion(QuestionTemplate):
    pass


class HistoricaQuestion(QuestionTemplate):
    pass


def main():
    while True:
        question_data = random.choice(data)
        question = QuestionFactory.create_question(question_data)
        question.apresentar_pergunta()
        resposta_usuario = input("Escolha a alternativa correta (A, B, C ou D): ").upper()
        if VerificadorResposta.verificar_resposta(question, resposta_usuario):
            print("Resposta correta!\n")
        else:
            print(f"Resposta incorreta! A resposta correta é {question.resposta}\n")
        continuar = input("Deseja continuar? (S/N): ").upper()
        if continuar != 'S':
            break

if __name__ == '__main__':
    main()
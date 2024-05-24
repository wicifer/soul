from flask import Flask, render_template, request, redirect, url_for, flash

def arquivo_rank():
    rank = []
    file = open('arquivos/ranking.txt')
    rank = []
    lines = file.readlines()
    for line in lines:
        rank.append(eval(line.strip()))
    file.close()

    return rank

def gerar_brinde(posicao, nome):
    if posicao == 1:
        return f"🏆 Parabéns {nome}! Você é o grande campeão da leitura! Além do Troféu de Ouro, você ganhou 50% de desconto em uma assinatura anual da livraria online Amazon!"
    elif posicao == 2:
        return f"🥈 Parabéns {nome}! Você conquistou o segundo lugar no pódio da leitura! Além da Medalha de Prata, você ganhou um vale-presente de R$ 100,00 para gastar em livros!"
    elif posicao == 3:
        return f"🥉 Parabéns {nome}! Você alcançou o terceiro lugar no pódio da leitura! Além do Certificado de Bronze, você desbloqueou um prêmio especial por sua dedicação à leitura: Cupom de desconto de 50% na Amazon: (#SOUL)"

def main():
    ranking = []
    rank = arquivo_rank()

    rank_sorted = sorted(rank, key=lambda x: (-x[1], x[0])) # Classifica os números em ordem decrescente de pontuação e, em caso de empate, em ordem alfabética do nome
    top3 = rank_sorted[:3] # Pega os três primeiros elementos da lista classificada

    for i, (nome, _) in enumerate(top3, start=1): # Itera sobre os elementos da lista top3 juntamente com um contador i
        brinde = gerar_brinde(i, nome)
        ranking.append(f"{i}º lugar: {brinde}")

    return render_template('ranking.html', ranking=ranking)
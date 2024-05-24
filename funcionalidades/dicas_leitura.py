from flask import Flask, render_template, request, redirect, url_for, flash

def main():
    dicas = []
    file = open('arquivos/dicas_leitura.txt')
    for dica in file:
        dicas.append(dica)
    file.close()

    return render_template('dicas_leitura.html', dicas=dicas)
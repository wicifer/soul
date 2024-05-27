from flask import Flask, render_template, request, redirect, url_for, flash

def main():
    ofertas = []
    file = open("arquivos/ofertas.txt", encoding='utf-8')
    for line in file:
        ofertas.append(line)
    file.close()
    
    return render_template('ofertas.html', ofertas=ofertas)
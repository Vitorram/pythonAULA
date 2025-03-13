from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

def gerar_cpf():
 
    
    def calcular_digito(cpf):
        soma = sum(int(cpf[i]) * (10 - i) for i in range(len(cpf)))
        digito = 11 - (soma % 11)
        return str(digito if digito < 10 else 0)

    nove_digitos = ''.join(str(random.randint(0, 9)) for _ in range(9))
    primeiro_digito = calcular_digito(nove_digitos)
    segundo_digito = calcular_digito(nove_digitos + primeiro_digito)

    cpf_completo = f"{nove_digitos}{primeiro_digito}{segundo_digito}"
    cpf_formatado = f"{cpf_completo[:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:]}"
    
    return cpf_formatado

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar_cpf")
def gerar():
    return jsonify({"cpf": gerar_cpf()})

if __name__ == "__main__":
    app.run(debug=True)

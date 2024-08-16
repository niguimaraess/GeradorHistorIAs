from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)
gemini.configure(api_key="coloque aqui a sua chave")
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historia', methods=['POST'])
def make_historia():
    try:    
        dados = request.json
        titulo = dados.get('titulos')

        prompt = f"""
        Crie uma história infantil utilizando exclusivamente elementos presentes no título: {titulo}.
        A história deve ser apresentada em formato HTML com codificação UTF-8, sem a palavra "```html", sem head, sem body, não colocar aspas simples entre as tags, não separar as tags por vírgula
        Exiba o título em uma tag <h1> centralizado e a história em parágrafos (<p>).
        O título deve ser {titulo}.
        Exibir um texto com os dizeres "Tema inapropriado. Procure informar títulos de histórias infantis" caso: o título contenha palavras de baixo calão, alusão a violência, palavras ofensivas, preconceituosas, ou qualquer outro tema que não se enquadre no perfil de Histórias Infantis.
        Desconsidere erros ortográficos, e crie o texto com as palavras com a grafia correta.
        A história deve conter um desfecho com um ditado popular.
        """        
        resposta = model.generate_content(prompt, generation_config = gemini.GenerationConfig(temperature=2))
        print(resposta)
        # Extrai a historia do texto da resposta
        historia = resposta.text.strip('').split('\n')
        print(historia)
        return jsonify(historia), 200
        
    except Exception as e:
        return jsonify({"Erro": str(e)}), 300
if __name__ == '__main__':
    app.run(debug=True)

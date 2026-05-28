from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='static')
CORS(app)

ARQUIVO = 'prontuarios.json'

# =========================
# CRIAR JSON SE NÃO EXISTIR
# =========================

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'w') as f:
        json.dump([], f)


# =========================
# FUNÇÕES AUXILIARES
# =========================

def ler_dados():
    with open(ARQUIVO, 'r') as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def achar_paciente(lista, cpf_limpo):
    for i, p in enumerate(lista):
        if p['cpf'] == cpf_limpo:
            return i, p
    return None, None


def limpar_cpf(cpf):
    return ''.join(filter(str.isdigit, cpf))


# =========================
# FRONTEND
# =========================

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')


# =========================
# POST /prontuario
# Cria paciente com dados base
# =========================

@app.route('/prontuario', methods=['POST'])
def criar_prontuario():
    dados = request.json

    campos_obrigatorios = ['nome', 'cpf', 'nascimento', 'queixa', 'pressao', 'temperatura', 'fc']
    for campo in campos_obrigatorios:
        if campo not in dados or str(dados[campo]).strip() == '':
            return jsonify({'erro': f'Campo obrigatório: {campo}'}), 400

    cpf = limpar_cpf(dados['cpf'])
    if len(cpf) != 11:
        return jsonify({'erro': 'CPF inválido'}), 400

    try:
        temperatura = float(dados['temperatura'])
        if temperatura < 30 or temperatura > 45:
            return jsonify({'erro': 'Temperatura inválida'}), 400
    except:
        return jsonify({'erro': 'Temperatura inválida'}), 400

    try:
        fc = int(dados['fc'])
        if fc < 20 or fc > 250:
            return jsonify({'erro': 'Frequência cardíaca inválida'}), 400
    except:
        return jsonify({'erro': 'Frequência cardíaca inválida'}), 400

    lista = ler_dados()
    for paciente in lista:
        if paciente['cpf'] == cpf:
            return jsonify({'erro': 'Paciente já cadastrado'}), 409

    novo = {
        'nome': dados['nome'].strip(),
        'cpf': cpf,
        'nascimento': dados['nascimento'],
        'queixa': dados['queixa'].strip(),
        'observacoes': dados.get('observacoes', '').strip(),
        'pressao': dados['pressao'].strip(),
        'temperatura': temperatura,
        'fc': fc,
        'protocolo': dados.get('protocolo', 'A definir').strip(),
        'horario': datetime.now().strftime('%d/%m/%Y %H:%M'),
        # Histórico de sessões: lista de objetos { data, exercicios, dor }
        'sessoes': [],
        # Anotações clínicas: lista de objetos { texto, horario }
        'anotacoes': []
    }

    lista.append(novo)
    salvar_dados(lista)
    return jsonify({'mensagem': 'Prontuário salvo'}), 201


# =========================
# GET /prontuarios
# Retorna lista com campos resumidos
# =========================

@app.route('/prontuarios', methods=['GET'])
def listar_prontuarios():
    lista = ler_dados()
    resumo = []
    for p in lista:
        sessoes = p.get('sessoes', [])
        ultima_sessao = sessoes[-1] if sessoes else None
        dor_recente = ultima_sessao['dor'] if ultima_sessao else None
        resumo.append({
            'nome': p['nome'],
            'cpf': p['cpf'],
            'protocolo': p.get('protocolo', 'A definir'),
            'ultima_sessao': ultima_sessao['data'] if ultima_sessao else None,
            'dor_recente': dor_recente,
            'queixa': p['queixa'],
            'horario': p['horario']
        })
    return jsonify(resumo), 200


# =========================
# GET /prontuarios/<cpf>
# Retorna detalhe completo do paciente
# =========================

@app.route('/prontuarios/<cpf>', methods=['GET'])
def buscar_paciente(cpf):
    cpf_limpo = limpar_cpf(cpf)
    lista = ler_dados()
    idx, paciente = achar_paciente(lista, cpf_limpo)
    if paciente is None:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    # Retorna as últimas 7 sessões (mais recente primeiro)
    sessoes_7 = list(reversed(paciente.get('sessoes', [])))[:7]
    anotacoes = list(reversed(paciente.get('anotacoes', [])))

    return jsonify({
        **paciente,
        'sessoes_recentes': sessoes_7,
        'anotacoes': anotacoes
    }), 200


# =========================
# POST /sessao/<cpf>
# Registra uma sessão de reabilitação
# Payload: { exercicios: "...", dor: 0-10 }
# =========================

@app.route('/sessao/<cpf>', methods=['POST'])
def registrar_sessao(cpf):
    cpf_limpo = limpar_cpf(cpf)
    dados = request.json

    try:
        dor = int(dados.get('dor', -1))
        if dor < 0 or dor > 10:
            return jsonify({'erro': 'Nível de dor deve ser entre 0 e 10'}), 400
    except:
        return jsonify({'erro': 'Nível de dor inválido'}), 400

    exercicios = str(dados.get('exercicios', '')).strip()
    if not exercicios:
        return jsonify({'erro': 'Informe os exercícios concluídos'}), 400

    lista = ler_dados()
    idx, paciente = achar_paciente(lista, cpf_limpo)
    if paciente is None:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    nova_sessao = {
        'data': datetime.now().strftime('%d/%m/%Y %H:%M'),
        'exercicios': exercicios,
        'dor': dor
    }

    lista[idx]['sessoes'].append(nova_sessao)
    salvar_dados(lista)
    return jsonify({'mensagem': 'Sessão registrada', 'sessao': nova_sessao}), 201


# =========================
# POST /anotacao/<cpf>
# Salva anotação clínica sem recarregar
# Payload: { texto: "..." }
#
# O frontend chama este endpoint via fetch():
#
#   const resp = await fetch(`/anotacao/${cpf}`, {
#       method: 'POST',
#       headers: { 'Content-Type': 'application/json' },
#       body: JSON.stringify({ texto: textoAnotacao })
#   });
#   const resultado = await resp.json();
#   // Atualiza UI sem reload com resultado.anotacao
#
# =========================

@app.route('/anotacao/<cpf>', methods=['POST'])
def salvar_anotacao(cpf):
    cpf_limpo = limpar_cpf(cpf)
    dados = request.json

    texto = str(dados.get('texto', '')).strip()
    if not texto:
        return jsonify({'erro': 'A anotação não pode estar vazia'}), 400

    lista = ler_dados()
    idx, paciente = achar_paciente(lista, cpf_limpo)
    if paciente is None:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    nova_anotacao = {
        'texto': texto,
        'horario': datetime.now().strftime('%d/%m/%Y %H:%M')
    }

    lista[idx]['anotacoes'].append(nova_anotacao)
    salvar_dados(lista)
    return jsonify({'mensagem': 'Anotação salva', 'anotacao': nova_anotacao}), 201


# =========================
# DELETE /deletar/<cpf>
# =========================

@app.route('/deletar/<cpf>', methods=['DELETE'])
def deletar(cpf):
    cpf_limpo = limpar_cpf(cpf)
    lista = ler_dados()
    nova_lista = [p for p in lista if p['cpf'] != cpf_limpo]
    salvar_dados(nova_lista)
    return jsonify({'mensagem': 'Paciente deletado'}), 200


# =========================

if __name__ == '__main__':
    print('🚀 Servidor rodando em http://127.0.0.1:5000')
    app.run(debug=True)
    
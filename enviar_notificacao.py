#   QUESTÃO 4 DA ATIVIDADE

import requests

MS_URL = 'http://127.0.0.1:8001'
API_KEY = 'cole_aqui_o_hash_da_empresa'

headers = {
    'X-Api-Key': API_KEY,
    'Content-Type': 'application/json',
}

def enviar_notificacao(user_id, mensagem, titulo=''):
    payload = {
        'user_id': user_id,
        'mensagem': mensagem,
        'titulo': titulo,
    }

    response = requests.post(
        MS_URL + '/api/notificacoes/criar/',
        json=payload,
        headers=headers,
    )

    if response.status_code == 201:
        print(f'✓ Notificacao enviada: {titulo or mensagem[:30]}')
    else:
        print(f'✗ Erro {response.status_code}: {response.text}')

if __name__ == '__main__':
    enviar_notificacao(1, 'Sua matricula foi confirmada.', titulo='Matricula')
    enviar_notificacao(1, 'Nova nota lancada em Banco de Dados.', titulo='Notas')
    enviar_notificacao(1, 'Reuniao de orientacao amanha as 14h.', titulo='Agenda')
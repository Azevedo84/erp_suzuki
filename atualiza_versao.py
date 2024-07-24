from banco_dados.conexao import conecta_robo
import socket
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


msg_erro = 'Houve um problema com a função '
msg_erro1 = '\nComunique o desenvolvedor sobre o erro abaixo:\n\n'


def mensagem_email():
    try:
        current_time = (datetime.now())
        horario = current_time.strftime('%H')
        hora_int = int(horario)
        saudacao = "teste"
        if 4 < hora_int < 13:
            saudacao = "Bom Dia!"
        elif 12 < hora_int < 19:
            saudacao = "Boa Tarde!"
        elif hora_int > 18:
            saudacao = "Boa Noite!"
        elif hora_int < 5:
            saudacao = "Boa Noite!"

        msg_final = f"Att,\n" \
                    f"Suzuki Máquinas Ltda\n" \
                    f"Fone (51) 3561.2583/(51) 3170.0965\n\n" \
                    f"Mensagem enviada automaticamente, por favor não responda.\n\n" \
                    f"Se houver algum problema com o recebimento de emails, " \
                    f"favor entrar em contato pelo email maquinas@unisold.com.br.\n\n"

        email_user = 'ti.ahcmaq@gmail.com'
        to = ['<fat_maq@unisold.com.br>', '<maquinas@unisold.com.br>', '<ahcmaquinas@gmail.com>']

        password = 'poswxhqkeaacblku'

        return saudacao, msg_final, email_user, to, password

    except Exception as e:
        print(f'{msg_erro}"mensagem_email"{msg_erro1}{e}')


def envia_email(alteracoes, versao_final):
    try:
        saudacao, msg_final, email_user, to, password = mensagem_email()

        subject = f'Atualização ERP Suzuki - Versão: {versao_final}'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['Subject'] = subject

        body = f"{saudacao}\n\nAbaixo a lista de modificações feitas na atualizção {versao_final}:\n\n"

        for i in alteracoes:
            body += f"- {i}\n"

        body += f"\n{msg_final}"

        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, password)

        server.sendmail(email_user, to, text)
        server.quit()

        print("email enviado")

    except Exception as e:
        print(f'{msg_erro}"envia_email_sem_anexo"{msg_erro1}{e}')


lista_modifica = ['(27/06) OP CONSUMIR: CORRIGIDO ERRO QUANDO CLICAR DUAS NA PARTE BRANCA DA TABELA',
                  '(02/07) SOL INCLUIR: INCLUIDO ITEM AO CADASTRO DA SOLICITACAO',
                  '(03/07) OP CONSUMIR: PERMITIDO SOMENTE NUMEROS NO CAMPO OP E CODIGO PRODUTO',
                  '(11/07) OC ALTERAR: CORRIGIDO FORMA DE ALTERAR AS ORDENS DE COMPRA',
                  '(17/07) ESTRUTURA INCLUIR: CORRIGIDO FORMA DE ALTERAR AS ESTRUTURAS',
                  '(22/07) ERP: REVISADO FORMA DE TRATAR OS ERROS GRAVADOS NO BANCO']

programa = "ERP SUZUKI"
versao = "2.01.006"
nome_computador = socket.gethostname()

cursor = conecta_robo.cursor()
cursor.execute("select GEN_ID(GEN_CONTROLE_VERSOES_ID,0) from rdb$database;")
ultimo_id0 = cursor.fetchall()
ultimo_id1 = ultimo_id0[0]
ultimo_id = int(ultimo_id1[0]) + 1
print(ultimo_id)

cursor = conecta_robo.cursor()
cursor.execute(f"Insert into CONTROLE_VERSOES "
               f"(ID, PROGRAMA, VERSAO, NOME_PC) "
               f"values (GEN_ID(GEN_CONTROLE_VERSOES_ID,1), '{programa}', '{versao}', '{nome_computador}');")

if lista_modifica:
    for i in lista_modifica:
        print(i)

        cursor = conecta_robo.cursor()
        cursor.execute(f"Insert into MODIFICACOES_VERSOES "
                       f"(ID, MODIFICACAO, ID_VERSAO, NOME_PC) "
                       f"values (GEN_ID(GEN_MODIFICACOES_VERSOES_ID,1), '{i}', {ultimo_id}, '{nome_computador}');")

conecta_robo.commit()

envia_email(lista_modifica, versao)

print("VERSÃO SALVA COM SUCESSO!")

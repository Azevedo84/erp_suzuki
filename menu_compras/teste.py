from nfe import ConsultaNotaFiscal

# Substitua com sua chave válida
chave = '35250613743249000139550010001562461121645934'

# Consulta usando certificado instalado no Windows
resposta = ConsultaNotaFiscal(chave).send()

print("✅ XML de resposta:")
print(resposta.text)

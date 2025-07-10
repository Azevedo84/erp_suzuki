from zeep import Client
from zeep.transports import Transport
from zeep.xsd import AnyObject
from requests_pkcs12 import Pkcs12Adapter
import requests

cert_path = r"C:\Users\Anderson\Downloads\Maquinas_1006652074.pfx"
cert_password = "unisold11"
chave_nfe = "4325 0693 1838 5300 0197 5500 1000 0085 8418 6156 5782"
ambiente = "1"
wsdl_url = "https://nfe.sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx?wsdl"

session = requests.Session()
session.mount("https://", Pkcs12Adapter(pkcs12_filename=cert_path, pkcs12_password=cert_password))
transport = Transport(session=session)
client = Client(wsdl=wsdl_url, transport=transport)

# Obtém o tipo esperado do parâmetro
nfeDadosMsg_type = client.get_element('ns0:nfeDadosMsg')

# Cria o dicionário no formato esperado, com o namespace correto
param = AnyObject(nfeDadosMsg_type.type, {
    'consSitNFe': {
        'tpAmb': ambiente,
        'xServ': 'CONSULTAR',
        'chNFe': chave_nfe
    }
})

try:
    resposta = client.service.nfeConsultaNF(param)
    print("✅ Resposta da SEFAZ:")
    print(resposta)
except Exception as e:
    print("❌ Erro ao consultar nota:", e)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=completa")

try:
    # Espera até 15 segundos até o campo aparecer
    wait = WebDriverWait(driver, 15)
    input_chave = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtChaveAcessoCompleta")))
    input_chave.send_keys("3525 0613 7432 4900 0139 5500 1000 1562 4611 2164 5934")

    # Clica no botão
    botao = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnConsultar")
    botao.click()
except Exception as e:
    print("Erro:", e)

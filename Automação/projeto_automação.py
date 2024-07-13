# Importando a bibliotecas necessárias
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



def tempo(duration = 1):
        time.sleep(duration)      

def teste(duration = 1.5):
    time.sleep(duration)
    

# Localizando a versão do chrome e comparando com o drive
# Caso o drive seja inferior, ele irá instalar automaticamente
servico = Service(ChromeDriverManager().install())
# Iniciando o navegador
driver = webdriver.Chrome(service=servico)
wait = WebDriverWait(driver, 10)
driver.get("http://127.0.0.1:5500/Automa%C3%A7%C3%A3o/index1.html")
tempo()


'''FORMULÁRIO 1'''
# o find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento

driver.find_element('xpath', '//*[@id="order-number"]').send_keys('Thiago Messias Ventricci Dias dos Santos') 
tempo()
driver.find_element('xpath', '//*[@id="name"]').send_keys('thiagoventricci487@gmail.com') 
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 99412-5518') 
tempo()
driver.find_element('xpath', '//*[@id="pais"]').send_keys('Brasil') 
tempo()
driver.find_element('xpath', '//*[@id="product-name"]').send_keys('Suporte técnico') 
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[6]/select')
select = Select(select_element)
select.select_by_visible_text("WhatsApp")
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/select')
select = Select(select_element) 
select.select_by_visible_text('Tarde')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[8]/button').click()
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[9]/a/button').click()
tempo()

'''FORMULÁRIO 2'''
# O find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento

driver.find_element('xpath', '//*[@id="order-number"]').send_keys('Beatriz Dias Santos')
tempo()
driver.find_element('xpath', '//*[@id="email"]').send_keys('beatrizdiad124@gmail.com')
tempo()
date_field = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[3]/input')  
date_field.send_keys('22-10-2002') # Inserir a data desejada (por exemplo, '2023-07-08')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[4]/select')
select = Select(select_element)
select.select_by_visible_text('Feminino') 
tempo()
driver.find_element('xpath', '//*[@id="endereco"]').send_keys('Rua laranjeira. 180')
tempo()
driver.find_element('xpath', '//*[@id="cep"]').send_keys('08578-410')
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 99451-4623')
tempo()
driver.find_element('xpath', '//*[@id="nome_usuario"]').send_keys('bia1234')
tempo()
driver.find_element('xpath', '//*[@id="senha"]').send_keys('12345678')
tempo()
driver.find_element('xpath', '//*[@id="confirme_senha"]').send_keys('12345678')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[12]/button').click()
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[13]/a/button').click()
tempo()

'''FORMULÁRIO 3'''
# O find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento

driver.find_element('xpath', '//*[@id="nome_cliente"]').send_keys('Batista Silva')
tempo()
driver.find_element('xpath', '//*[@id="email"]').send_keys('batistasilva@gmail.com')
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 95485-8758')
tempo()
driver.find_element('xpath', '//*[@id="endereco"]').send_keys('Rua sebastião,194')
tempo()
driver.find_element('xpath', '//*[@id="cep"]').send_keys('08858-010')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[6]/select')
select = Select(select_element)
select.select_by_visible_text('Iphone 15 Pro Max')
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/select')
select = Select(select_element)
select.select_by_visible_text('2')
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[8]/select')
select = Select(select_element)
select.select_by_visible_text('Cartão de Crédito')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[10]/button').click()
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[11]/a/button').click()
tempo()

'''FORMULÁRIO 4'''
# O find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento


driver.find_element('xpath', '//*[@id="nome_cliente"]').send_keys('João Batista')
tempo()
driver.find_element('xpath', '//*[@id="email"]').send_keys('joaobatista@gmail.com')
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 99458-8457')
tempo()
driver.find_element('xpath', '//*[@id="cargo"]').send_keys('Desenvolvedor python')
tempo()
# o CSS_SELECTOR especifica que estamos procurando por um elemento <input> do tipo 'file'
upload_curriculo = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
# Aqui estou selecionando o caminho do arquivo que eu quero 
upload_curriculo.send_keys("C:/Users/totth/Downloads/Curriculo_Thiago.pdf")
tempo()
driver.find_element('xpath', '//*[@id="linkedin"]').send_keys('https://www.linkedin.com/in/thiago-messias-5b9621262/')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/select')
select = Select(select_element)
select.select_by_visible_text('Sim')
tempo()
driver.find_element('xpath', '//*[@id="salario"]').send_keys('2000')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[9]/select')
select = Select(select_element)
select.select_by_visible_text('Manhã')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[11]/button').click()
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[12]/a/button').click()
tempo()

'''FORMULÁRIO 5'''
# O find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento

driver.find_element('xpath', '//*[@id="nome_cliente"]').send_keys('Maria Valentina da Silva')

driver.find_element('xpath', '//*[@id="email"]').send_keys('mariadasilva@gmail.com')
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 96325-7957')
tempo()
date_field = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[4]/input')
date_field.send_keys('10-08-1965')
tempo()
driver.find_element('xpath', '//*[@id="documento"]').send_keys('445-897-654-2')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[6]/select')
select = Select(select_element)
select.select_by_visible_text('Ortopedista')
tempo()
date_field = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/input')
date_field.send_keys('05-10-2024')
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/select')
select = Select(select_element)
select.select_by_visible_text('14:00')
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[8]/select')
select = Select(select_element)
select.select_by_visible_text('Sim')
tempo()
driver.find_element('xpath', '//*[@id="text_area"]').send_keys('Dores na costas toda vez que ando')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[11]/button').click()
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[12]/a/button').click()
tempo()

'''FORMULÁRIO 6'''
# O find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento

driver.find_element('xpath', '//*[@id="nome"]').send_keys('João Batista')
tempo()
driver.find_element('xpath', '//*[@id="email"]').send_keys('joaobatista087@gmail.com')
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 94758-4512')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH,'//*[@id="return-form"]/div[4]/select')
select = Select(select_element)
select.select_by_visible_text('Automatização de Tarefas')
tempo()
driver.find_element('xpath', '//*[@id="text_area"]').send_keys('Quero que automatize 8 formulários que são bem cotidianos para mim, coisa simples, mas que vai fazer bastante diferencia' +
 ' e detalhe, quero que use a biblioteca selenium.')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[6]/select')
select = Select(select_element)
select.select_by_visible_text('O mais rápido possivel')
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/select')
select = Select(select_element)
select.select_by_visible_text('Não sei, espero seu orçamento')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[9]/button').click()
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[10]/a/button').click()
tempo()

'''FORMULÁRIO 7'''
# O find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento

driver.find_element('xpath', '//*[@id="nome"]').send_keys('Gabriela Santos')
tempo()
driver.find_element('xpath', '//*[@id="email"]').send_keys('gabrielasantos124@gmail.com')
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 95478-4587')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH,'//*[@id="return-form"]/div[4]/select')
select = Select(select_element)
select.select_by_visible_text('Sapatos e Botas')
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[5]/select')
select = Select(select_element)
select.select_by_visible_text('Sim')
tempo()
driver.find_element('xpath', '//*[@id="valor_doação"]').send_keys('100,00')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/select')
select = Select(select_element)
select.select_by_visible_text('Dinheiro')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[9]/button').click()
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[10]/a/button').click()
tempo()

'''FORMULÁRIO 8'''
# O find_element permite você localizar um elemento na página web, assim você pode interagir com ele
# O send_keys, serve para você digitar algo no elemento

driver.find_element('xpath', '//*[@id="nome"]').send_keys('Angelina Dias')
tempo()
driver.find_element('xpath', '//*[@id="email"]').send_keys('angelinadias876@gmail.com')
tempo()
driver.find_element('xpath', '//*[@id="telefone"]').send_keys('11 94523-1414')
tempo()
date_field = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[4]/input')
date_field.send_keys('22-10-2024')
tempo()
date_field = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[5]/input')
date_field.send_keys('28-10-2024')
tempo()
# Select é uma classe do selenium , usada para interagir com menus suspensos <select> e <option>
# O select_by_visible_text está selecionando a opção pelo valor
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[6]/select')
select = Select(select_element)
select.select_by_visible_text('Quarto Executivo')
tempo()
select_element = driver.find_element(By.XPATH, '//*[@id="return-form"]/div[7]/select')
select = Select(select_element)
select.select_by_visible_text('2')
tempo()
driver.find_element('xpath', '//*[@id="return-form"]/div[9]/button').click()
tempo()

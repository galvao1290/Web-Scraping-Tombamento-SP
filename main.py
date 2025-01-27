from imports import *
import json

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://condephaat.sp.gov.br/page/7/?unonce=9c37a1900b&uformid=176&s=uwpsfsearchtrg&taxo%5B0%5D%5Bname%5D=cidades&taxo%5B0%5D%5Bopt%5D&taxo%5B0%5D%5Bterm%5D=uwpqsftaxoall&taxo%5B1%5D%5Bname%5D=classificacao&taxo%5B1%5D%5Bopt%5D&taxo%5B1%5D%5Bterm%5D=uwpqsftaxoall&taxo%5B2%5D%5Bname%5D=livrostombo&taxo%5B2%5D%5Bopt%5D&taxo%5B2%5D%5Bterm%5D=uwpqsftaxoall&skeyword")

counter = 1
dados = []

for i in range(31):
    registro = {}
    try:
        link = WebDriverWait(driver, 20).until(           
            EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div/div[2]/main/div/article[{counter}]/div/div/header/h2/a'))
        )
    except:
        break

    print(link.text)
    link.click()

    title = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
    )
    registro['Patrimônio'] = title.text

    lista_p = driver.find_elements(By.TAG_NAME, 'p')
    for p in lista_p:
        try:

            b = p.find_element(By.TAG_NAME, 'b')
        except:
            continue

        if b:
            
            texto = p.text
            if ":" in texto:
                chave, valor = texto.split(":", 1)
                registro[chave.strip()] = valor.strip()

    dados.append(registro)
    counter += 1
    driver.back()

driver.quit()


with open('dados_tombamento7.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)
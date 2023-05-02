from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from conexao_banco import conexao


cursor = conexao.cursor()
lista = []

class Web:
    def __init__(self):
        self.site = 'https://asloterias.com.br/resultados-da-mega-sena-%contador%'
        self.map = {
            'sorteio':{
                'xpath': f'/html/body/main/div[2]/div/div/div[1]/strong[%contador%]'
            },
            'numero':{
                'xpath': f'/html/body/main/div[2]/div/div/div[1]/span[%contador2%]'
            },
        }
        self.driver = webdriver.Chrome()
        self.abrir_site()

    def abrir_site(self):
        for ano in range(2022, 1995, -1):
            print(self.site)
            print(self.site.replace('%contador%', f'{ano}'))
            self.driver.get(self.site.replace('%contador%', f'{ano}'))
            sleep(3)
            k = 1
            for i in range(1, 111):
                try:
                    lista.clear()
                    num = self.driver.find_element(By.XPATH, self.map["sorteio"]["xpath"].replace('%contador%', f'{i+3}')).text
                    for j in range(6):
                        lista.append(self.driver.find_element(By.XPATH, self.map["numero"]["xpath"].replace('%contador2%', f'{k}')).text)
                        k+=1
                    inserir_num = f"""
                        INSERT INTO resultados(ano_sorteio, num_sorteio, num1, num2, num3, num4, num5, num6)
                        VALUES ({ano}, {num}, {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}, {lista[5]})
                     """
                    cursor.execute(inserir_num)
                    conexao.commit()
                except:
                    print("Acabaram os sorteios antes do esperado")

j = Web()
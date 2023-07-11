# Script para verificação de IDs (Resource ID ou Accessibility ID) usado para automação 
# Autor: Alexsander Loula (15/08/2022)

import json, sys, argparse
from progress.bar import Bar
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Para Ações W3C
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Conecta ao device através do Appium
def connect_device(config_file):
    # Carrega arquivo de configuração
     with open(config_file) as file:
        data = json.load(file)
        caps = {}
        caps["platformName"] = data['platformName']
        caps["appium:platformVersion"] = data['platformVersion']
        caps["appium:deviceName"] = data['deviceName']
        caps["appium:appPackage"] = data['appPackage']
        caps["appium:appActivity"] = data['appActivity'] 
        caps["appium:automationName"] = data['automationName'] 
        caps["appium:ensureWebviewsHavePages"] = data['ensureWebviewsHavePages'] 
        caps["appium:nativeWebScreenshot"] = data['nativeWebScreenshot'] 
        caps["appium:newCommandTimeout"] = data['newCommandTimeout']
        caps["appium:autoGrantPermissions"] = data['autoGrantPermissions']
        caps["appium:noReset"] = data['noReset']
        # Criar o driver
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        return driver

# Main
def main():
    count = 1
    response = ""
    # Cria argumentos que serão passados via linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("-cfg", "--Config_File", help = "Config File")
    parser.add_argument("-id", "--Resource_ID", help = "Resource ID")
    parser.add_argument("-t", "--Timeout", help = "Search Timeout")
    args = parser.parse_args()
    # Verifica que os argumentos foram informados 
    if args.Config_File and args.Resource_ID and args.Timeout:
        config_file = args.Config_File
        resource_id = args.Resource_ID
        timeout = int(args.Timeout)
        print("Verificando Resource ID:", resource_id)
        try:
            print("Conectando-se ao dipositivo...")
            sleep(1)
            driver = connect_device(config_file)
        except:
            print("Não foi possível se conectar ao dispositivo, favor verificar se o Appium está rodando e se as configurações no '" +  config_file + "' estão corretas.")
            sys.exit(1)
        sleep(1)
        with Bar('Procurando elemento (sec/timeout)', max=timeout) as bar:
            while count <= timeout:
                response = driver.find_elements(by=AppiumBy.ID, value=resource_id)
                if response:
                    print("\nElemento encontrado com estratégia de RESOURCE ID")
                    driver.quit()
                    sys.exit(0)
                response = driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value=resource_id)
                if response:
                    print("\nElemento encontrado com estratégia de ACCESSIBILITY ID")
                    driver.quit()
                    sys.exit(0)           
                else:
                    count = count + 1
                    bar.next()
                    sleep(1)    
        print("\nElemento: '" + resource_id + "' NÃO encontrado!")                               
    else:
        print("Uso: python verifica_id.py -cfg <config_file> -id <resource_id> -t <timeout>")
        print("Exemplo: python verificada_id.py -cfg 'cfg/appium.json' -id 'key pad' -t 20")


if __name__ == "__main__":
    main()
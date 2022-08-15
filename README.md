## Verifica IDs

Script para verificação de IDs (Resource ou Accessibility) utilizados para automação de testes de APPs (Android ou iOS) com Appium 

### Pré-requisitos:

- Android Studio 2021+: https://developer.android.com/studio
- Python 3.8+: https://www.python.org/downloads/
- Appium 1.22+: https://appium.io/
- Opcional - Appium-Inspector 2022.+: https://github.com/appium/appium-inspector/releases


### Instalação:

1 - Criar e ativar um ambiente virtual do Python:
```
$ python -m venv .venv
$ source .venv/bin/activate
```

2 - Instalar a lib do appium:
```
$ python -m pip install --upgrade pip
$ pip install progress
$ pip install Appium-Python-Client
```


### Configuração do Emulador Android:

1 - Instale e configure o Android Studio  
2 - Abra o Android Studio e crie um Dispositivo Virtual com Play Store, ex: "Pixel 4 API 33"  
3 - Rode o emulador do dispositivo criado  
4 - Instale o App que será testando arrastando-o para o emulador

### Verificação do 'appPackage' e 'appActivity':

1 - Abra o App no Emulador

2 - Entre no shell do adb faça o dumpsys:
```
$ adb shell
generic_x86_arm:/ $ dumpsys window | grep -E 'mCurrentFocus'
  mCurrentFocus=Window{1204c85 u0 com.example.foo/com.example.foo.MainActivity}
```

### Executando o script:

1 - Execute o Appium Server:
```
$ ./run-appium.sh
```

2 - Abra outro terminal para executar o Emulador:
```
$ ./start-emulator.sh
```

3 - Ative o ambiente virtual
```
$ source .venv/bin/activate
```

4 - Caso necessário, altere as configurações 'cfg/appium.json'

5 - Execute o script: verifica_id.py -cfg <config_file> -id <resource_id> -t <timeout>

Exemplo 1:
```
$ python verifica_id.py -cfg 'cfg/appium.json' -id 'key pad' -t 10
Verificando Resource ID: key pad
Conectando ao dipositivo...
Procurando elemento (sec/timeout) |                                | 0/10
Elemento encontrado com estratégia de ACCESSIBILITY ID
```

Exemplo 2:
```
$ python verifica_id.py -cfg "cfg/chrome.json" -id "terms_accept" -t 20
Verificando Resource ID: terms_accept
Conectando ao dipositivo...
Procurando elemento (sec/timeout) |                                | 0/20
Elemento encontrado com estratégia de RESOURCE ID
```
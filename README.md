# runner de escritório do Mestre Ruan

1. Crie um ambiente virtual:
```bash
python3 -m venv venv
```
2. Ative o ambiente virtual:
```bash
venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Inicie o *SAP runner*:
```bash
python3 main.py
```
5. Para finalizar, execute:
```bash
deactivate
```

Obs.0: Esse script contém dependências específicas para o sistema operacional `Windowns`.

Obs.1: É necessário ter o `SAP FrontEnd` instalado e estar autenticado para usar o _runner_.

Obs.2: Esse _runner_ foi construído para o uso exclusivo do `CORE BAIXADA` e não se aplica para outros usos.

Obs.3: Estarei em breve escrevendo uma documentação completa do processo de automação do SAP para que ele possa ser usado como modelo de automação.
# Gerador de Dados Fictícios para o projeto de gerenciamento de clínicas Vollmed

Este projeto é uma coleção de scripts Python para gerar dados fictícios de médicos, pacientes e agendamentos de consultas. Os dados são salvos em arquivos JSON e podem ser utilizados para testes e preenchimento de bases de dados.

## Scripts Disponíveis

1. **Gerar Médicos (`generate_fake_doctors.py`)**  
   Gera dados fictícios de médicos, incluindo nome, CRM, especialidade e endereço.

2. **Gerar Pacientes (`generate_fake_patients.py`)**  
   Gera dados fictícios de pacientes, incluindo nome, CPF, telefone e endereço.

3. **Gerar Agendamentos (`generate_fake_appointments.py`)**  
   Lê os dados de médicos e pacientes gerados anteriormente e cria agendamentos de consultas com horários aleatórios no formato ISO.

## Como Usar

1. Clone o repositório para o seu computador:
   ```bash
   git clone https://github.com/raul-franca/py-fakeData.git
   ```
2. Instale as dependências:
   ```bash
    pip install -r requirements.txt
    ```
3. Execute os scripts na ordem desejada:
   ```bash
   python generate_fake_medicos.py
   python generate_fake_pacientes.py
   python generate_fake_agendamentoss.py
   ```
4. Os dados gerados serão salvos em arquivos JSON na pasta `data/`.

### Exemplo de Dados Gerados
* Lembrando que essa estrutura json é para importar no banco de dados, a estrutura das requisições é diferente.
<br>
   ***Médico:***
   ```json
   
       {"id": 1,
       "nome": "Dr. João Silva",
       "crm": "123456",
       "especialidade": "CARDIOLOGIA",
       "telefone": "(81) 99999-1234",
       "logradouro": "Rua Exemplo",
       "bairro": "Centro",
       "cep": "50000000",
       "numero": "10",
       "complemento": "Sala 101",
       "cidade": "Recife",
       "uf": "PE",
       "ativo": 1 }
    ```
    ***Paciente:***

 ```json
    {"id": 1,
    "nome": "Maria da Silva",
    "cpf": "12345678901",
    "telefone": "(81) 98888-1234",
    "logradouro": "Rua Exemplo",
    "bairro": "Centro",
    "cep": "50000000",
    "numero": "10",
    "complemento": "Sala 101",
    "cidade": "Recife",
    "uf": "PE",
    "ativo": 1 }
 ```
    ***Agendamento:***
 
 ```json
    {"id": 1,
    "id_medico": 1,
    "id_paciente": 1,
    "data_hora": "2021-10-01T08:00:00",
    "status": "AGENDADO" }
 ```
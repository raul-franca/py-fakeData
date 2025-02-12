import json
from faker import Faker

# Inicializa o Faker com suporte para português do Brasil
faker = Faker(['pt_BR'])

# Conjuntos para evitar duplicatas
unique_id = set()
unique_emails = set()
unique_cpfs = set()
unique_addresses = set()

def sanitize_name(name):
    """Remove títulos como 'Dr.' ou 'Dra.' dos nomes."""
    for title in ["Dr. ", "Dra. ", "Dr ", "Dra ", "Sr. ", "Sra. ", "Sr ", "Sra ", "Srta. ", "Srta "]:
        name = name.replace(title, "")
    return name.strip()

def generate_unique_id():
    while True:
        id = faker.random_number(digits=4, fix_len=True)
        if id not in unique_id:
            unique_id.add(id)
            return id

def generate_unique_email():
    while True:
        email = faker.email()
        if email not in unique_emails:
            unique_emails.add(email)
            return email

def generate_unique_cpf():
    while True:
        cpf = faker.cpf().replace(".", "").replace("-", "")
        if cpf not in unique_cpfs:
            unique_cpfs.add(cpf)
            return cpf

def generate_unique_address():
    while True:
        address = {
            "logradouro": faker.street_name(),
            "bairro": faker.city(),
             "cep": faker.postcode().replace("-", ""),
            "numero": faker.building_number(),
            "complemento": faker.random_element(["casa", "apartamento"]),
            "cidade": faker.city(),
            "uf": faker.state_abbr()
        }
        address_key = json.dumps(address)
        if address_key not in unique_addresses:
            unique_addresses.add(address_key)
            return address

def generate_brazilian_phone_number():
    """Gera um número de celular brasileiro amigável no formato (XX) 99999-9999."""
    ddd = faker.random_number(digits=2, fix_len=True)  # Gera um DDD de 2 dígitos
    number = f"99{faker.random_number(digits=7, fix_len=True)}"  # Gera o número com prefixo 99 e mais 7 dígitos
    # return f"({ddd}) {number[:5]}-{number[5:]}"  # Formata o número no padrão brasileiro
    return f"{ddd}{number}"  # Formata sem máscara o número no padrão brasileiro


def generate_fake_patient_data(n):
    data = []
    for _ in range(n):
        name_with_titles = faker.name()
        sanitized_name = sanitize_name(name_with_titles)  # Remove títulos do nome
        address = generate_unique_address()  # Gera endereço único
        data.append({
            "id": generate_unique_id(),
            "nome": sanitized_name,
            "cpf": generate_unique_cpf(),
            "telefone": generate_brazilian_phone_number(),
            "email": generate_unique_email(),
            "logradouro": address["logradouro"],
            "bairro": address["bairro"],
            "cep": address["cep"],
            "numero": address["numero"],
            "complemento": address["complemento"],
            "cidade": address["cidade"],
            "uf": address["uf"],
            "ativo": 1
        })
    return data

def save_to_json_file(data, filename="data/fake_data_pacientes.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Arquivo {filename} gerado com sucesso!")

if __name__ == "__main__":
    # Número de registros que deseja gerar
    num_records = int(input("Quantos registros você deseja gerar? "))
    fake_data_pacientes = generate_fake_patient_data(num_records)
    save_to_json_file(fake_data_pacientes)
import json
import random
from datetime import datetime, timedelta
from faker import Faker

# Inicializa o Faker
faker = Faker(['pt_BR'])

unique_id = set()

def load_json_file(filename):
    """Carrega dados de um arquivo JSON."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save_to_json_file(data, filename):
    """Salva dados em um arquivo JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Arquivo {filename} gerado com sucesso!")

def generate_unique_id():
    """Gera um ID único."""
    while True:
        id = faker.random_number(digits=4, fix_len=True)  # Gera um número com 4 dígitos
        if id not in unique_id:
            unique_id.add(id)
            return id

def generate_random_datetime():
    """Gera uma data e hora aleatória no formato ISO (YYYY-MM-DD HH:MM:SS)."""
    base_date = datetime.now()
    random_days = random.randint(1, 30)  # Gera uma data dentro dos próximos 30 dias
    random_hour = random.randint(7, 17)  # Horário entre 7:00 e 17:00
    random_minute = random.choice([0])  # Minutos fixos: 0
    appointment_time = base_date + timedelta(days=random_days)
    appointment_time = appointment_time.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)
    return appointment_time.strftime("%Y-%m-%d %H:%M:%S")  # Formato ISO

def generate_appointments(medicos, pacientes, num_appointments):
    """Gera agendamentos de consultas."""
    appointments = []
    for _ in range(num_appointments):
        medico = random.choice(medicos)
        paciente = random.choice(pacientes)
        appointments.append({
            "id": generate_unique_id(),
            "medico_id": medico["id"],
            "paciente_id": paciente["id"],
            "data": generate_random_datetime()
        })
    return appointments

if __name__ == "__main__":
    medicos_file = "data/fake_data_medicos.json"
    pacientes_file = "data/fake_data_pacientes.json"
    # Carrega os dados dos arquivos
    medicos = load_json_file(medicos_file)
    pacientes = load_json_file(pacientes_file)

    # Solicita o número de agendamentos
    num_appointments = int(input("Quantos agendamentos você deseja gerar? "))

    # Gera os agendamentos
    appointments = generate_appointments(medicos, pacientes, num_appointments)

    # Salva os agendamentos em um novo arquivo JSON
    save_to_json_file(appointments, "data/fake_data_agendamentos.json")
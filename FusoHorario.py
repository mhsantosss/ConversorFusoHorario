import datetime
import pytz
import os

def set_system_time_to_brasilia():
    # Obter o horário atual em Brasília
    brasilia_tz = pytz.timezone('America/Sao_Paulo')
    brasilia_time = datetime.datetime.now(brasilia_tz)

    # Formatar a data e hora para o comando do sistema
    formatted_time = brasilia_time.strftime('%Y-%m-%d %H:%M:%S')

    # Ajustar a data e hora do sistema (funciona para sistemas Unix/Linux)
    try:
        os.system(f'sudo date -s "{formatted_time}"')
        print(f"Data e hora ajustadas para: {formatted_time} (Brasília)")
    except Exception as e:
        print(f"Erro ao ajustar a data e hora: {e}")

if __name__ == "__main__":
    set_system_time_to_brasilia()

import subprocess
import os
import socket
import time
import xml.etree.ElementTree as ET

def run_powershell_command(command):
""" Executa um comando no PowerShell """
completed = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
if completed.returncode != 0:
print(f"Erro ao executar comando: {command}")
print(completed.stderr)
return completed


def install_new_agent():
""" Faz o download e instala o novo agente Wazuh """
wazuh_manager_ip = 'IP_WAZUH_MANAGER'
wazuh_agent_group = 'WAZUH_GROUP'
wazuh_agent_name = socket.gethostname()
wazuh_installer_url = "https://packages.wazuh.com/4.x/windows/wazuh-agent-4.12.0-1.msi"
temp_file_path = os.path.join(os.getenv('TEMP'), 'wazuh-agent.msi')
ossec_conf_path = r'C:\Program Files (x86)\ossec-agent\ossec.conf'

# Download do instalador
download_command = f"Invoke-WebRequest -Uri {wazuh_installer_url} -OutFile {temp_file_path}"
run_powershell_command(download_command)

# Instalação do agente
install_command = (
    f"msiexec.exe /i {temp_file_path} /q "
    f"WAZUH_MANAGER='{wazuh_manager_ip}' "
    f"WAZUH_AGENT_GROUP='{wazuh_agent_group}' "
    f"WAZUH_AGENT_NAME='{wazuh_agent_name}'"
)
run_powershell_command(install_command)

# Iniciar o serviço do Wazuh
run_powershell_command("NET START WazuhSvc")


print("Agente Wazuh instalado e configurado com sucesso.")


def main():
install_new_agent()

print("Processo concluído com sucesso.")

# Pausa de 5 segundos antes de fechar o script
print("O script será encerrado em 5 segundos...")
time.sleep(5)

# Aguardar uma interação para manter a janela aberta
input("Pressione qualquer tecla para sair...")

if **name** == "**main**":
main()

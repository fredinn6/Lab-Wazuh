import os
import requests
import zipfile
import shutil
import subprocess
from pathlib import Path

# Caminho Downloads

downloads_path = Path.home() / "Downloads"
sysmon_dir = downloads_path / "Sysmon"
sysmon_dir.mkdir(exist_ok=True)

# -----------------------------------------

# Etapa 1: Baixar Sysmon.zip

# -----------------------------------------

sysmon_url = "https://download.sysinternals.com/files/Sysmon.zip"
sysmon_zip_path = downloads_path / "Sysmon.zip"

print("[+] Baixando Sysmon...")
with requests.get(sysmon_url, stream=True) as r:
r.raise_for_status()
with open(sysmon_zip_path, 'wb') as f:
for chunk in r.iter_content(chunk_size=8192):
f.write(chunk)

# Extrair Sysmon.zip para Downloads\Sysmon

print(f"[+] Extraindo Sysmon.zip para {sysmon_dir}")
with zipfile.ZipFile(sysmon_zip_path, 'r') as zip_ref:
zip_ref.extractall(sysmon_dir)

# -----------------------------------------

# Etapa 2: Baixar sysmonconfig-export.zip

# -----------------------------------------

config_zip_url = "https://github.com/SwiftOnSecurity/sysmon-config/archive/refs/heads/master.zip"
config_zip_path = downloads_path / "sysmonconfig-export.zip"

print("[+] Baixando sysmonconfig-export.zip...")
with requests.get(config_zip_url, stream=True) as r:
r.raise_for_status()
with open(config_zip_path, 'wb') as f:
for chunk in r.iter_content(chunk_size=8192):
f.write(chunk)

# Extrair sysmonconfig-export.zip

print("[+] Extraindo sysmonconfig-export.zip...")
temp_extract_path = downloads_path / "sysmon-config-master"
with zipfile.ZipFile(config_zip_path, 'r') as zip_ref:
zip_ref.extractall(downloads_path)

# Procurar o sysmonconfig-export.xml

print("[+] Procurando sysmonconfig-export.xml...")
xml_found = False
for root, dirs, files in os.walk(temp_extract_path):
for file in files:
if file == "sysmonconfig-export.xml":
src_xml = Path(root) / file
dest_xml = sysmon_dir / "sysmonconfig-export.xml"
shutil.copy(src_xml, dest_xml)
xml_found = True
print(f"[+] Arquivo XML copiado para: {dest_xml}")
break
if xml_found:
break

if not xml_found:
print("[-] ERRO: sysmonconfig-export.xml não encontrado.")
exit(1)

# -----------------------------------------

# Etapa 3: Executar Sysmon diretamente

# -----------------------------------------

print("[+] Executando Sysmon diretamente com subprocess...")

sysmon_exe = sysmon_dir / "Sysmon64.exe"
sysmon_xml = sysmon_dir / "sysmonconfig-export.xml"

# Com "-m" para evitar erro de event manifest

result = subprocess.run(
[str(sysmon_exe), "-accepteula", "-i", str(sysmon_xml)],
cwd=sysmon_dir,
capture_output=True,
text=True
)

# Mostrar a saída

print("----- SAÍDA DO COMANDO -----")
print(result.stdout)

print("----- ERRO (se houver) -----")
print(result.stderr)

if result.returncode == 0:
print("[✓] Sysmon instalado com sucesso.")
else:
print(f"[!] Sysmon retornou código de erro: {result.returncode}")

# -----------------------------------------

# Etapa 4: Reiniciar o serviço Wazuh

# Cortar o código a partir daqui caso não tenha Wazuh na máquina

# -----------------------------------------

print("[+] Reiniciando o serviço do Wazuh...")

restart_wazuh = subprocess.run(
["cmd", "/c", "net stop wazuhsvc && net start wazuhsvc"],
capture_output=True,
text=True
)

print("----- SAÍDA WAZUH -----")
print(restart_wazuh.stdout)

print("----- ERRO WAZUH (se houver) -----")
print(restart_wazuh.stderr)

if restart_wazuh.returncode == 0:
print("[✓] Serviço do Wazuh reiniciado com sucesso.")
else:
print(f"[!] Falha ao reiniciar o serviço do Wazuh (código: {restart_wazuh.returncode})")

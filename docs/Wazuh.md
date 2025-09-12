# 🛡️ Wazuh - Documentação do Laboratório

## 📌 Visão Geral
Este documento reúne **prints, anotações e configurações** relacionadas ao Wazuh dentro do laboratório de cibersegurança.

O objetivo é registrar todo o processo, desde a instalação inicial até as regras customizadas e integrações realizadas.

A instalação foi realizada utilizando o passo a passo descrito na documentação oficial em: https://documentation.wazuh.com/current/installation-guide/index.html 
---

## ⚙️ Instalação Inicial

- Sistema operacional utilizado: Ubuntu Server 20.04
- Versão do Wazuh: 4.12

**Wazuh Indexer**
- Arquivo `config.yml`:
<img width="1009" height="493" alt="image" src="https://github.com/user-attachments/assets/b1f91368-a899-47ba-8aa3-ef57433d3e89" />

- Arquivo `/etc/wazuh-indexer/opensearch.yml`:
<img width="1015" height="648" alt="image" src="https://github.com/user-attachments/assets/77f62120-2020-4fde-86c1-1b993bbb3ab6" />

- Se o passo a passo for feito corretamente, a saída tem que ser essa na inicialização do cluster:
<img width="1012" height="795" alt="image" src="https://github.com/user-attachments/assets/71d3bd1a-1e08-4b71-b2d9-1f134d64cd60" />

**Wazuh Manager**
- Arquivo `/etc/filebeat/filebeat.yml`:
<img width="1012" height="795" alt="image" src="https://github.com/user-attachments/assets/abe49d33-f9c5-4145-8be1-c0780faae975" />

- Arquivo `/var/ossec/etc/ossec.conf`:
<img width="535" height="204" alt="image" src="https://github.com/user-attachments/assets/5d2ca7e6-0213-4ade-9cbc-fcbe1343671f" />

- Se o passo a passo for feito corretamente, a saída tem que ser essa no teste de saída do filebeat:
<img width="536" height="224" alt="image" src="https://github.com/user-attachments/assets/abc89547-cdaf-46f7-bdf3-947861fdd50b" />

**Wazuh Dashboard**
  - Arquivo `/etc/wazuh-dashboard/opensearch_dashboards.yml`:
<img width="1013" height="272" alt="image" src="https://github.com/user-attachments/assets/d4a11fde-1bad-4166-9897-1f706e770038" />

- Arquivo `/usr/share/wazuh-dashboard/data/wazuh/config/wazuh.yml`:
<img width="379" height="132" alt="image" src="https://github.com/user-attachments/assets/0ed9ada6-b031-4d2b-86d0-f02b3a6d1c2f" />

- Wazuh Dashboard configurado com sucesso:
<img width="1274" height="1237" alt="image" src="https://github.com/user-attachments/assets/a847d8d2-655f-47a2-840b-d5cd341d149d" />

  
---

## 🔑 Configurações Iniciais

- Ajustes realizados:

**Troca de senha de todos os usuários:**
```powershell
/usr/share/wazuh-indexer/plugins/opensearch-security/tools/wazuh-passwords-tool.sh --api --change-all --admin-user wazuh --admin-password wazuh
```
Exemplo:
<img width="1013" height="234" alt="image" src="https://github.com/user-attachments/assets/e3888757-eb5a-4e58-9edb-ed70cfadb2b3" />

**Troca de senha de usuário específico:**
```powershell
/usr/share/wazuh-indexer/plugins/opensearch-security/tools/wazuh-passwords-tool.sh --user "seu_user" -password "senha_desejada"
```
 *Altere os campos "seu_user" e "senha_desejada" para realizar a troca*

- Agentes cadastrados:  

---

## 📂 Regras Customizadas 

- Outras regras customizadas:  

---

## 🔗 Integrações

- **Suricata → Wazuh**  
- **Sysmon → Wazuh**  
- **pfSense (Syslog) → Wazuh**  
- **VirusTotal → Wazuh**  
- Outras integrações:  

---

## 📝 Observações
Anotações importantes que podem ajudar na reprodução do ambiente ou troubleshooting:  

-  **Instalação utilizada: Step-by-step**
-  **Todas as instâncias do Wazuh foram instaladas em apenas uma VM**
-  

---


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

---

## 🔑 Configurações Iniciais

- Ajustes realizados:  
- Agentes cadastrados:  
- Conexões testadas:  

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


# 🔐 Laboratório de Cibersegurança

## 📑 Sumário
- [📂 docs/](./docs) — diagramas e prints  
- [⚙️ configs/](./configs) — templates e exemplos de configurações (Wazuh, Sysmon, Suricata, etc.)  
- [📜 scripts/](./scripts) — scripts de automação (instalação / deploy de agentes)  
- [📊 dashboards/](./dashboards) — exports/imports de dashboards (Grafana / Kibana)  

---

## 📌 Objetivo
Este projeto tem como objetivo **simular uma infraestrutura corporativa** para estudo e prática de segurança **defensiva (Blue Team)**.

O laboratório foi construído com:
- **pfSense**  
- **Active Directory (Windows Server)**  
- **Wazuh (SIEM)**
- **Sysmon**
- **Suricata**     
- **Grafana**

A ideia é **documentar todo o processo** passo a passo para que qualquer pessoa consiga recriar o ambiente e aprender com ele.

---

## 🏗️ Arquitetura do Laboratório
- **pfSense** → Firewall e roteamento  
- **Windows Server** → Controlador de domínio  
- **Windows Client** → Workstation ingressada no domínio  
- **2 Ubuntu Server** → Servidores para hospedar aplicações
- **Wazuh + Suricata + Grafana** → Stack de monitoramento e SIEM

> O ambiente foi criado utilizando **VirtualBox** e **Vagrant**.

---

## ⚙️ Principais Configurações

### pfSense
- **LAN:** `192.168.1.1/24`  
- **DHCP range:** `192.168.1.100` — `192.168.1.150`  
- **NAT:** configurado para permitir acesso à Internet (pfSense WAN → VirtualBox NAT/host)

### Active Directory (Windows Server)
- **Domínio:** `corp.local`  
- **Controlador de Domínio (DC) IP:** `192.168.1.10`  
- **DNS:** integrado ao AD (servidor DNS rodando no DC)

### Windows Client
- **IP (exemplo):** `192.168.1.101`  
- **Status:** ingressado no domínio `corp.local`

### Ubuntu Server
- **IP (exemplo):** `192.168.1.106`  
- **Uso:** servidor alvo / serviços para testes

### Ubuntu Server - SIEM
- **IP (exemplo):** `192.168.1.105`  
- **Uso:** servidor alvo / serviços para testes

---

## 🔎 Segurança Defensiva (Blue Team)
Neste laboratório foram implementadas as seguintes proteções e integrações:

- **Sysmon** instalado nos clientes Windows (para telemetria de processos, comandos, rede e persistência)  
- **Wazuh Agents** nas máquinas para envio de logs ao Wazuh Manager  
- **Regras customizadas** (Wazuh / Sysmon / Suricata)
- **Suricata** integrado para análise de tráfego de rede (IDS/IPS)
- **Dashboards no Grafana** para visualização e investigação em tempo real

---

## 📢 Licença
Este projeto está disponível sob a **MIT License** — use, modifique e compartilhe com atribuição. *(opcional: ajuste conforme sua preferência)*

---

## 📸 Evidências e documentação
Veja a pasta `/docs` para diagramas, capturas de tela (pfSense, AD, Wazuh, Suricata, Grafana) e tutoriais detalhados para reprodução do lab.

---

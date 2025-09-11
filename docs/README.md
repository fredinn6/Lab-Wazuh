
# 📂 Documentação do Projeto

Este diretório contém a documentação detalhada de todas as etapas de construção, configuração e utilização do laboratório de segurança **corp.local**.  

---

## 📑 Arquivos e Descrições

Aqui você encontrará os arquivos/documentos desta pasta e uma breve explicação do que cada um contém:

| Arquivo | Descrição |
|---------|-----------|
| [`configs VMs.md`](/Configs VMs.md) | Prints e informações sobre a configuração das VMs no VirtualBox, incluindo redes e adaptadores. |
| *(adicione aqui os próximos arquivos)* | *(descreva o conteúdo do arquivo)* |

---
## 🖼️ Arquitetura do Ambiente  

<img width="1000" height="560" alt="Arquitetura" src="https://github.com/user-attachments/assets/dbcfd98c-bbc2-4820-959c-5f997a82ad7b" />
 
---

## 📌 Estrutura da Documentação  

- **pfSense/** → Configuração do firewall, NAT, regras de rede e integração com Suricata e Wazuh.  
- **Active Directory/** → Instalação e configuração do Windows Server como controlador de domínio, DNS, DHCP e políticas de grupo (GPO).  
- **Windows Client/** → Ingresso no domínio, aplicação de GPOs e configuração do Sysmon para envio de logs ao Wazuh.  
- **Linux Server/** → Configuração de serviços no Ubuntu e integração com o Suricata e o Wazuh.  
- **Wazuh/** → Instalação, configuração de agentes e integração com VirusTotal e Suricata.
- **Grafana/** → Configuração de dashboards personalizados para monitoramento e correlação de eventos de segurança.  
 


---

## 🎯 Objetivo  

A documentação serve para:  
1. **Reprodução** → Permitir que qualquer pessoa recrie o ambiente do zero.  
2. **Estudo** → Facilitar o aprendizado prático em **cibersegurança defensiva**.  
3. **Referência** → Servir como guia de boas práticas para laboratórios locais.  

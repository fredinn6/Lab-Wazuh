
# 📂 Documentação do Projeto

Este diretório contém a documentação detalhada de todas as etapas de construção, configuração e utilização do laboratório de segurança **corp.local**.  

---

## 🖼️ Arquitetura do Laboratório  

![Arquitetura do Ambiente](../assets/arquitetura.png)  
*(adicione aqui a imagem gerada do diagrama da arquitetura)*  

---

## 📌 Estrutura da Documentação  

- **pfSense/** → Configuração do firewall, NAT, regras de rede e integração com Suricata e Wazuh.  
- **Active Directory/** → Instalação e configuração do Windows Server como controlador de domínio, DNS, DHCP e políticas de grupo (GPO).  
- **Windows Client/** → Ingresso no domínio, aplicação de GPOs e configuração do Sysmon para envio de logs ao Wazuh.  
- **Linux Server/** → Configuração de serviços no Ubuntu e integração com o Suricata e o Wazuh.  
- **Wazuh/** → Instalação, configuração de agentes, criação de regras customizadas e integração com VirusTotal e Suricata.  
- **Grafana/** → Configuração de dashboards personalizados para monitoramento e correlação de eventos de segurança.  
- **Red Team/** → Registro das simulações de ataque (Kali Linux) contra o ambiente corporativo.  

---

## 🎯 Objetivo  

A documentação serve para:  
1. **Reprodução** → Permitir que qualquer pessoa recrie o ambiente do zero.  
2. **Estudo** → Facilitar o aprendizado prático em **cibersegurança ofensiva e defensiva**.  
3. **Referência** → Servir como guia de boas práticas para laboratórios locais.  

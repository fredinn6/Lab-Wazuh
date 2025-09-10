# ⚙️ Configurações do Ambiente

Este diretório contém os arquivos de configuração utilizados no laboratório **corp.local**.  
Eles servem como base para padronizar a coleta de logs e a criação de regras de detecção no **Wazuh**.

---

## 📂 Estrutura

- **sysmon-config.xml** → Arquivo de configuração do **Sysmon** (Windows).  
  - Define quais eventos do Windows serão monitorados.  
  - Inclui monitoramento de criação de processos, alterações em registro, conexões de rede e muito mais.  
  - Baseado em boas práticas da comunidade (SwiftOnSecurity + customizações para este lab).  

- **wazuh-rules.xml** → Arquivo de regras customizadas do **Wazuh**.    

---

## 🎯 Objetivo

Centralizar e versionar os principais arquivos de configuração para:  
1. **Facilitar a reprodução** → qualquer pessoa pode reutilizar esses arquivos em seu próprio lab.  
2. **Garantir padronização** → todos os clientes e servidores seguem as mesmas regras.  
3. **Melhorar a detecção** → com regras customizadas adaptadas ao ambiente.  

---

## 📌 Como Usar

1. Copie o arquivo `sysmon-config.xml` para a estação Windows e instale o Sysmon com:  
   ```powershell
   sysmon -accepteula -i sysmon-config.xml


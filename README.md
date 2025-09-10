# Lab-Wazuh
Laboratório Empresarial  — pfSense, AD, Wazuh, Suricata, scripts e dashboards

# Red Team vs Blue Team — Lab

Resumo: repositório para documentação, configs e scripts do laboratório com pfSense, AD, Wazuh, Suricata e dashboards.

## Objetivo
Montar um ambiente de laboratório realista para testes Red Team vs Blue Team e geração de detections no Wazuh.

## Estrutura do repositório
- `docs/` — diagramas, screenshots e tutoriais.
- `configs/` — regras e templates (Wazuh, Suricata, Sysmon). **NÃO** commitar segredos.
- `scripts/` — scripts de instalação e automação.
- `dashboards/` — JSON/exports de dashboards (Kibana/Grafana).
- `examples/` — exemplos de testes e playbooks.

## Boas práticas
- Nunca commitar credentials ou chaves privadas.
- Use `.gitignore` e GitHub Secrets para CI.
- Mantenha `configs/*/*.example` com placeholders.

## Como contribuir
Adicionar PR com: descrição, passos para reproduzir e arquivos de configuração em `configs/` com sufixo `.example`.


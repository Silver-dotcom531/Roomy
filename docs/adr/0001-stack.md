# ADR-0001 — Stack tecnológica e convenções

**Status: PROPOSTA** — precisa ser aceita pela equipe (T-001). Até lá o laço não instala nada. Confiança da recomendação: ~65%; o principal fator desconhecido é o que a equipe domina e o que o curso exige no 3º período.

## Contexto
Requisitos que pesam na escolha: duas camadas independentes (RNF-011); Chrome/Firefox/Safari e 360–1440 px (RNF-006); desempenho medido por Lighthouse em 4G simulado (RNF-005); senha com hash (RNF-004); dados fortemente relacionais (usuário, anúncio, conversa, interesse mútuo, avaliação) e regras de integridade (RNE-005, RNE-008).

## Proposta
| Camada | Escolha | Por quê |
|---|---|---|
| Frontend | React + TypeScript + Vite, CSS com variáveis dos tokens do Figma (Light/Dark), React Router | build leve, 1 linguagem nas duas camadas, tokens mapeiam direto para CSS variables |
| Backend | Node.js + Fastify + TypeScript | rápido, esquema de validação por rota, gera OpenAPI |
| Banco | PostgreSQL + Prisma (migrações versionadas) | modelo relacional do diagrama de classes; integridade e consultas de média por bairro/tipo (RNE-009) |
| Senhas | argon2id | RNF-004 |
| Testes | Vitest (unidade/integração), Playwright (e2e em chromium, firefox, webkit), axe (RNF-009), Lighthouse CI (RNF-005) | cobre os RNF mensuráveis |
| CI | GitHub Actions | já usam GitHub Projects |
| Contrato | OpenAPI em `docs/api/openapi.yaml` | desacopla as camadas |
| Verificador RNF-010 | `typescript@5` fixado na raiz | a API de compilador usada por `scripts/check-rnf010.mjs` não existe no pacote `typescript` 7 |

Idioma: identificadores em inglês, interface/docs/commits em português (glossário em `docs/glossario.md`).

## Alternativas
- Java + Spring Boot ou Python + Django: válidas se o curso/equipe exigir; trocar custa reescrever agentes `backend-dev`/`test-engineer` e gates.
- Next.js full-stack: menos arquivos, mas mistura as camadas e enfraquece o RNF-011.

## Decisão
(preencher após reunião: aceito / aceito com mudanças / rejeitado, data e responsáveis)

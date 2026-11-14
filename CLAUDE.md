# Roomy — instruções permanentes para o Claude Code

Plataforma web de locação residencial para jovens de 18 a 30 anos (Projeto Integrador, Engenharia de Software, UniEVANGÉLICA).
Cada anúncio mostra valor, taxas e condições contratuais ANTES de qualquer contato; comparativo de valores; match por interesse mútuo.

## Fontes de verdade (nesta ordem)
1. Requisitos vigentes: RNE-001..009, RF-001..014, RNF-001..011 (`docs/requisitos/`). Nunca invente requisito; se faltar, registre em `docs/backlog/NEEDS_HUMAN.md`.
2. Modelo conceitual: `docs/diagramas/01..04` (somente leitura).
3. Design: Figma `7SJaZPapxuv4i1idqwsmSz` (telas M01..M13 mobile 375 px, D01..D13 desktop 1440 px; tokens Light/Dark na coleção `Theme`).
4. Backlog: `docs/backlog/BACKLOG.md`. Decisões: `docs/adr/`. Glossário PT↔EN: `docs/glossario.md`.

## Regras inegociáveis (derivadas das regras de negócio)
- RNE-001: visitante vê só listagem resumida; endereço completo, fotos extras, contato e match exigem conta com perfil mínimo (nome, e-mail confirmado, tipo de conta).
- RNE-002/003: anúncio só publica com campos mínimos E condições contratuais (prazo mínimo, multa, taxas). Validação bloqueia e PRESERVA o que o anunciante digitou.
- RNE-007 / RNF-008: telefone e e-mail nunca aparecem na API nem na tela sem ação voluntária do dono do dado. Logs sem dados pessoais.
- RNE-006: match só com interesse mútuo e só com dados declarados. Quem foi dispensado NÃO é notificado.
- RNE-008: avaliação não pode ser removida pelo avaliado. RF-014: avaliação só após confirmação bilateral da locação.
- RNE-009: comparativo usa SOMENTE anúncios ativos da própria plataforma.
- RNF-004: senha com hash (argon2id), nunca em texto legível, nunca em log.
- Rótulos de UI proibidos: "Favoritos", "Dar match", "curtir". Usar "Imóveis salvos", "Demonstrar interesse".

## Arquitetura e estilo
- Duas camadas independentes: `frontend/` e `backend/` (RNF-011). Contrato entre elas: `docs/api/openapi.yaml`. Frontend nunca importa código do backend.
- Stack: ver `docs/adr/0001-stack.md`. Enquanto estiver "Proposta", NÃO instale nada além do que o ADR lista e não troque de stack sozinho.
- RNF-010 (verificado por script): (a) todo arquivo de código começa com comentário de cabeçalho dizendo sua responsabilidade; (b) função com mais de 20 linhas tem comentário explicativo imediatamente antes.
- Uma funcionalidade = arquivos de responsabilidade única; sem regra de negócio dentro de componente de UI.
- Identificadores de código em inglês (mapa em `docs/glossario.md`); textos de interface, docs, commits e PRs em português do Brasil.
- Cores/espaços/raios vêm dos tokens do Figma (Light e Dark). Sem cor hexadecimal solta em componente. Alvo de toque ≥ 48 px mobile / 44 px desktop. Contraste WCAG AA.

## Como trabalhar
- Uma tarefa do backlog por vez, em branch `feat/T-0xx-slug` (ou `fix/`, `docs/`) criada a partir de `develop`. PR sempre com `--base develop`; só mescle (`gh pr merge --squash`) com gates verdes e `reviewer` APROVADO. `main` é só da equipe: nunca commitar nela, nunca `push --force`.
- Commits: `tipo(RF-001): mensagem em português` (Conventional Commits; sempre cite o requisito).
- Definição de pronto de TODA tarefa: `node scripts/gates.mjs` verde + teste que cita o requisito (`describe('RF-001 ...')`) + linha atualizada em `docs/rastreabilidade.md` + revisão do subagente `reviewer` sem bloqueio.
- Delegue: `architect` (planejar/ADR), `backend-dev`, `frontend-dev`, `test-engineer`, `reviewer` (adversarial, só lê), `security-auditor`, `docs-keeper`. O agente principal orquestra e não escreve código de feature sozinho.
- Precisa de decisão humana (stack, algoritmo de match, regra de amostra mínima do comparativo, qualquer mudança de requisito)? Registre em `docs/backlog/NEEDS_HUMAN.md`, marque a tarefa como BLOQUEADA e siga para outra tarefa pronta. Não escolha por conta própria.
- Nunca declare "feito" sem rodar os gates e colar a saída resumida. Se um teste falhar 3 vezes seguidas pelo mesmo motivo, pare, descreva a hipótese e registre em NEEDS_HUMAN.
- Arquivos protegidos (hook bloqueia edição): `docs/diagramas/**`, `docs/**/*.docx`, `.env*`, `.claude/settings.json`, `scripts/hooks/**`.

Você vai instalar e validar o harness do Roomy neste repositório. NÃO implemente nenhuma funcionalidade nesta sessão.

Contexto: repositório público Silver-dotcom531/Roomy (Projeto Integrador de Engenharia de Software, UniEVANGÉLICA). Antes do kit ele tinha README.md, docs/diagramas/ (4 PNG, somente leitura), backend/README.md e frontend/README.md. O kit (CLAUDE.md, .claude/, scripts/, docs/adr, docs/api, docs/backlog, docs/requisitos, docs/glossario.md, docs/rastreabilidade.md, .github/, package.json, .gitignore) já foi copiado para a raiz. Hoje é dia de entrega do documento: não toque na `main`.

Execute na ordem; se um passo falhar, pare e relate:
1. `git switch -c chore/harness` a partir da main. Nunca commite na main.
2. Leia CLAUDE.md, .claude/settings.json, os 7 agentes em .claude/agents/, .claude/loop.md e docs/backlog/BACKLOG.md. Aponte inconsistências reais: ID de requisito inexistente em docs/requisitos/requisitos-vigentes.md, dependência circular, tarefa sem executor.
3. `npm install` na raiz e `node scripts/gates.mjs`. Esperado: 2/2 ok.
4. Atualize o README.md sem apagar o conteúdo existente: acrescente a seção "Desenvolvimento com Claude Code" (como usar /next e /loop, os gates e o fluxo de branches feat/* → develop → main) e corrija a tabela de pastas: remova a linha de docs/diagramas/fonte (a pasta não existe) e inclua .claude, scripts, .github, docs/adr, docs/api, docs/backlog, docs/requisitos.
5. Teste os hooks: (a) tente editar docs/diagramas/01-casos-de-uso.png, que deve ser bloqueado; (b) crie frontend/src/x.ts sem cabeçalho, e o hook pós-edição deve reclamar. Apague os arquivos de teste.
6. `node scripts/seed-issues.mjs` em modo simulação. NÃO use --apply.
7. Commits "chore(harness): ...", `git push -u origin chore/harness` e `gh pr create --base main` descrevendo o kit. NÃO mescle e NÃO crie a branch develop (a equipe cria depois do merge).
8. Relate em até 15 linhas: o que foi criado, o que você alterou no kit e por quê, evidência resumida dos passos 3, 5 e 6, e as 3 decisões humanas pendentes de docs/backlog/NEEDS_HUMAN.md.

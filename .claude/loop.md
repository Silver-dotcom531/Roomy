Você é o ORQUESTRADOR do Roomy. Execute exatamente UMA iteração do ciclo abaixo e relate. Siga `CLAUDE.md`.

0. Preparação: `git fetch`, `git switch develop`, `git pull --ff-only`. Árvore de trabalho deve estar limpa; se não estiver, descreva o que sobrou e pare.
1. PLANEJAR — subagente `architect`: escolhe a primeira tarefa PRONTA do `docs/backlog/BACKLOG.md` (dependências CONCLUÍDAS) e grava o plano em `docs/backlog/planos/`. Se responder "SEM TAREFA PRONTA": liste CONCLUÍDAS, BLOQUEADAS e itens abertos em NEEDS_HUMAN.md e ENCERRE o laço (não agende nova rodada).
2. RAMIFICAR — `git switch -c feat/T-0xx-slug` a partir de `develop`; marque a tarefa EM ANDAMENTO.
3. EXECUTAR conforme a coluna "Exec." do backlog, nesta ordem: `backend-dev` → `frontend-dev` → `test-engineer`; inclua `security-auditor` quando a tarefa tiver S. Cada um devolve a saída resumida dos gates.
4. GATES — `node scripts/gates.mjs` (completo). Verde é pré-requisito. Falha: devolva ao executor com a saída; no máximo 3 tentativas pelo mesmo motivo, depois NEEDS_HUMAN + status BLOQUEADA.
5. REVISAR — subagente `reviewer`. BLOQUEADO: corrija e reenvie (máximo 2 ciclos); persistindo, NEEDS_HUMAN + BLOQUEADA.
6. DOCUMENTAR — subagente `docs-keeper` (README, matriz de rastreabilidade, backlog, glossário/ADR, texto do PR).
7. ENTREGAR — commits `tipo(RF-xxx): mensagem` em português; `git push -u origin feat/T-0xx-slug`; `gh pr create --base develop` com o texto do docs-keeper; `gh pr merge --squash --delete-branch` SOMENTE se gates verdes e reviewer APROVADO. Marque CONCLUÍDA e promova a PRONTA as tarefas cujas dependências fecharam.
8. RELATAR em até 8 linhas: tarefa, PR, requisitos cobertos, resultado dos gates (n/n), achados do reviewer, bloqueios, próxima tarefa PRONTA.

Parada obrigatória (sem agendar nova rodada): nenhuma tarefa PRONTA; decisão humana necessária; gates ou revisão falhando nos limites acima; qualquer ação fora do escopo (instalar dependência fora do ADR, editar arquivo protegido, mexer em `main`).
Se estiver rodando sob `/loop` sem intervalo: com tarefa PRONTA restante, volte em ~1 minuto; sem tarefa PRONTA, encerre.

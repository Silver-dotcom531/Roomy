# Como rodar o laço (depois que a equipe aceitar o ADR-0001)

Pré-condição: branch `develop` criada a partir da main; `docs/adr/0001-stack.md` com status "Aceito"; em `docs/backlog/BACKLOG.md`, T-001 = CONCLUÍDA e T-002 = PRONTA.

## Opção A — uma iteração supervisionada (comece sempre por esta)
No Claude Code, dentro do repositório:

    /next

Leia o PR gerado e o relatório de 8 linhas antes de liberar mais.

## Opção B — laço dentro da sessão
    /loop

`/loop` sem argumentos usa `.claude/loop.md` (iteração única descrita lá) e o Claude escolhe o intervalo entre rodadas, de 1 min a 1 h. Esc interrompe o laço em espera. A sessão precisa ficar aberta e ociosa; tarefas recorrentes expiram em 7 dias.

## Opção C — laço externo, uma tarefa por processo (contexto novo a cada volta)
    node scripts/run-loop.mjs --max 3 --turns 60 --budget 5

Cada volta chama `claude -p` com o conteúdo de `.claude/loop.md`, limite de turnos e de gasto por volta. Para sozinho quando não há tarefa PRONTA ou quando o `claude` sai com erro.

## O que o laço NUNCA faz sozinho
Aceitar ADR, decidir regra de comparativo ou de match, editar diagramas/.docx/.env, mexer na `main`, instalar dependência fora do ADR.

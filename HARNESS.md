# Harness do Roomy — visão geral

Harness = tudo que cerca o modelo para ele errar menos: instruções permanentes, agentes com papéis estreitos, travas e verificação automática. O laço (loop) é só o repetidor.

```
          ┌────────────── .claude/loop.md (1 iteração) ──────────────┐
BACKLOG → architect → backend-dev → frontend-dev → test-engineer → (security-auditor)
   ▲          │ plano       código        telas          testes + mutação     │
   │          ▼                                                               ▼
docs-keeper ◄── reviewer (adversarial) ◄── node scripts/gates.mjs ◄───────────┘
   │ PR feat/T-0xx → develop (squash) → matriz de rastreabilidade atualizada
   └─ decisão humana? → NEEDS_HUMAN.md + tarefa BLOQUEADA → próxima PRONTA
```

| Camada | Arquivo | Função |
|---|---|---|
| Instruções | `CLAUDE.md` | regras de negócio inegociáveis, arquitetura, definição de pronto |
| Agentes | `.claude/agents/*.md` | 7 papéis; reviewer e security-auditor sem permissão de editar |
| Permissões | `.claude/settings.json` | allow/deny de comandos (sem push na main, sem `--force`, sem `rm -rf`) |
| Hooks | `scripts/hooks/*.mjs` | PreToolUse bloqueia arquivos protegidos; PostToolUse aplica RNF-010; Stop impede encerrar com gate vermelho (máx. 3 bloqueios, depois registra em NEEDS_HUMAN) |
| Gates | `scripts/gates.mjs` | lint, typecheck, testes por camada, RNF-010 e rastreabilidade |
| Backlog | `docs/backlog/` | 34 tarefas ligadas a RF/RNE/RNF, dependências, "pronto quando" |
| Rastreio | `docs/rastreabilidade.md` | requisito → tarefa → arquivo de teste (verificado por script) |
| Laço | `.claude/loop.md`, `/next`, `scripts/run-loop.mjs` | uma tarefa por iteração |

Todos os scripts são Node (.mjs): funcionam igual em Windows, Linux e macOS, sem depender de bash ou jq.

## Limites conhecidos
- O verificador de função longa (RNF-010 b) é por AST do TypeScript 5: avalia o comentário no início do comando que contém a função; não julga a qualidade do comentário (o `reviewer` faz isso).
- Os gates só rodam o que existe: antes de T-002 só valem RNF-010 e rastreabilidade.
- O stack do ADR-0001 é proposta. Se a equipe escolher outra, ajustar `backend-dev`, `test-engineer`, `scripts/gates.mjs` e o CI.

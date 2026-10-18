# Backlog do Roomy (fonte única para o laço do Claude Code)

Status: `HUMANO` (decisão da equipe), `PRONTA`, `AGUARDA` (dependência aberta), `EM ANDAMENTO`, `BLOQUEADA` (ver NEEDS_HUMAN.md), `CONCLUÍDA`.
Regra de transição: o `docs-keeper` promove `AGUARDA` → `PRONTA` quando todas as dependências estão `CONCLUÍDA`. Telas citadas (M/D) são as do Figma `7SJaZPapxuv4i1idqwsmSz`.
Executor: B = backend-dev, F = frontend-dev, T = test-engineer, S = security-auditor, D = docs-keeper (o `reviewer` revisa todas).

## E0 — Fundação (RNF-010, RNF-011)
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-001 | Equipe aprova `docs/adr/0001-stack.md` (stack e idioma do código) | RNF-011 | humano | — | HUMANO | ADR com status "Aceito", assinado por Pedro e João Gabriel |
| T-002 | Monorepo: estrutura, lint, formatação, tsconfig, `scripts/gates.mjs` rodando, CI | RNF-010, RNF-011 | B+F | T-001 | AGUARDA | CI verde em PR vazio; README com tabela de pastas |
| T-003 | Backend esqueleto: servidor, `/health`, config por ambiente, erro padrão, log sem dado pessoal | RNF-003, RNF-007, RNF-008 | B | T-002 | AGUARDA | teste do `/health`; erro em português; log sem e-mail/telefone |
| T-004 | Frontend esqueleto: rotas, layout responsivo 360–1440, tokens do Figma Light/Dark | RNF-006, RNF-009, RNF-001 | F | T-002 | AGUARDA | tema alterna; página de exemplo sem cor fora dos tokens |
| T-005 | Banco: Postgres via Docker, esquema inicial derivado de `docs/diagramas/04`, migração, seed com os imóveis P1–P8 | RNE-002, RNE-003, RNE-004 | B | T-003 | AGUARDA | `docker compose up` + migração + seed reproduzíveis do zero |
| T-006 | Contrato `docs/api/openapi.yaml` v0 + validação do contrato no CI | RNF-011 | B | T-003 | AGUARDA | CI falha se API diverge do contrato |

## E1 — Conta e acesso (telas M01–M03 / D01–D03)
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-010 | Cadastro com tipo de conta (locatário, anunciante ou ambos) e e-mail a confirmar | RF-001, RNE-001, RNE-004, RNF-004 | B,T,S | T-005, T-006 | AGUARDA | senha com hash; um usuário pode ter os dois tipos |
| T-011 | Login e encerramento de sessão | RF-002, RNF-004, RNF-008 | B,T,S | T-010 | AGUARDA | limite de tentativas; cookie seguro |
| T-012 | Recuperação de senha | RF-003, RNF-004 | B,T,S | T-011 | AGUARDA | mensagem neutra (não revela se o e-mail existe); token expira |
| T-013 | Guarda de acesso: visitante vê só listagem resumida; perfil mínimo para o resto | RNE-001 | B,T | T-011 | AGUARDA | testes negativos por rota (visitante, perfil incompleto) |
| T-014 | Telas Tela Inicial, Autenticação e Menu Principal ligadas à API | RF-001, RF-002, RF-003, RNF-001 | F,T | T-011, T-004 | AGUARDA | M01–M03/D01–D03 fiéis ao Figma; validação inline |

## E2 — Anúncios (M09, M11 / D09, D11)
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-020 | Publicar anúncio com campos mínimos e condições contratuais; validação bloqueia e preserva dados | RF-004, RNE-002, RNE-003 | B,T | T-013 | AGUARDA | anúncio sem prazo mínimo/multa/taxas não publica; dados digitados voltam na resposta |
| T-021 | Editar, desativar e reativar sem perder histórico | RF-005, RNE-005 | B,T | T-020 | AGUARDA | reativar restaura o mesmo anúncio; só o dono edita |
| T-022 | Upload de fotos com compressão (≤ 500 KB) | RF-004, RNF-005 | B,S | T-020 | AGUARDA | tipo/tamanho validados |
| T-023 | Telas Publicar Anúncio e Painel de Anúncios | RF-004, RF-005, RNE-002, RNE-003 | F,T | T-020, T-021, T-004 | AGUARDA | M09/M11/D09/D11 fiéis; erro inline sem perder dados |

## E3 — Busca, detalhe e comparativo (M04, M05 / D04, D05)
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-030 | Busca e filtros (valor, prazo mínimo, quartos, bairro) com paginação | RF-006, RNE-001, RNF-005 | B,T | T-020 | AGUARDA | resultado ≤ 2 s com o seed; visitante só recebe campos resumidos |
| T-031 | Detalhe do imóvel: endereço completo só para logado, nunca contato | RF-007, RNE-001, RNE-003, RNE-007 | B,T,S | T-030 | AGUARDA | teste de vazamento de contato |
| T-032 | Comparativo de valores (abaixo/dentro/acima da média) só com anúncios ativos da plataforma | RF-011, RNE-009 | B,T | T-031 | BLOQUEADA | **depende de decisão humana**: amostra mínima e critério de "semelhante" (ver NEEDS_HUMAN) |
| T-033 | Telas Busca e Detalhe (valor, prazo, multa e taxas acima da dobra no mobile) | RF-006, RF-007, RF-011, RNF-002 | F,T | T-030, T-031 | AGUARDA | M04/M05/D04/D05 fiéis |

## E4 — Contato, locação e avaliação (M06, M13 / D06, D13)
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-040 | Canal de contato interno sobre um imóvel | RF-010, RNE-007 | B,T,S | T-031 | AGUARDA | telefone/e-mail nunca trafegam |
| T-041 | Confirmação bilateral da locação (cada parte confirma; "aguardando a outra parte") | RF-014 | B,T | T-040 | AGUARDA | avaliação só liberada com as duas confirmações |
| T-042 | Avaliação mútua pública, sem remoção pelo avaliado | RF-012, RNE-008 | B,T | T-041 | AGUARDA | no máximo uma avaliação por parte; sem endpoint de remoção pelo avaliado |
| T-043 | Telas Conversa/Confirmação e Avaliação | RF-010, RF-012, RF-014 | F,T | T-040, T-041, T-042 | AGUARDA | M06/M13/D06/D13 fiéis; banner de status |

## E5 — Match (M07, M12 / D07, D12)
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-050 | Perfil de convivência (voluntário) | RF-008, RNE-006 | B,T | T-013 | AGUARDA | sem perfil, sem sugestões e sem bloqueio de uso |
| T-051 | Sugestões, interesse e interesse mútuo liberando o canal | RF-009, RNE-006, RNE-007 | B,T,S | T-050 | BLOQUEADA | **depende de decisão humana**: critérios de compatibilidade (ver NEEDS_HUMAN) |
| T-052 | Telas Match e Perfil de Convivência ("Demonstrar interesse", "Dispensar") | RF-008, RF-009 | F,T | T-050, T-051 | AGUARDA | M07/M12/D07/D12 fiéis |

## E6 — Perfil e ajuda (M08, M10 / D08, D10)
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-060 | Gerenciamento do perfil (editar dados, tipo de conta, Imóveis salvos) | RF-013, RNE-004 | B,F,T | T-013 | AGUARDA | M08/D08 fiéis |
| T-061 | Central de ajuda (FAQ) | RNF-001 | F | T-004 | AGUARDA | M10/D10 fiéis |

## E7 — Qualidade transversal
| ID | Tarefa | Requisitos | Exec. | Depende | Status | Pronto quando |
|---|---|---|---|---|---|---|
| T-070 | Acessibilidade: axe em todas as telas, teclado, foco, contraste | RNF-009 | F,T | T-033 | AGUARDA | zero violações sérias/críticas |
| T-071 | Desempenho: Lighthouse CI em 4G simulado (≤ 3 s), imagens ≤ 500 KB | RNF-005 | F,T | T-033 | AGUARDA | orçamento de desempenho no CI |
| T-072 | Compatibilidade: Playwright em Chrome, Firefox e Safari (WebKit), 360 a 1440 px | RNF-006 | T | T-033 | AGUARDA | matriz verde no CI |
| T-073 | Auditoria de segurança e privacidade completa | RNF-004, RNF-008, RNE-007 | S | T-051, T-042 | AGUARDA | relatório sem achado Alto aberto |
| T-074 | Disponibilidade e operação: health, README de execução, guia de deploy | RNF-007 | B,D | T-003 | AGUARDA | uma pessoa nova sobe o sistema só com o README |
| T-075 | Fechamento: matriz de rastreabilidade 100%, README, glossário, ADRs | RNF-010 | D | todas | AGUARDA | `trace-check` verde; nenhum RF/RNE sem teste |

## Progresso (o `docs-keeper` acrescenta uma linha por tarefa concluída)
| Data | Tarefa | PR | Evidência |
|---|---|---|---|

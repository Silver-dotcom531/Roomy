# Roomy

Plataforma web de locação residencial para estudantes universitários, jovens profissionais e recém-formados de 18 a 30 anos.

O Roomy ataca dois problemas do aluguel tradicional: a falta de informação do locatário sobre valores e cláusulas, e a rigidez dos contratos. Cada anúncio exibe de forma padronizada o valor, as taxas e as condições do contrato, como prazo mínimo e multa por rescisão, antes de qualquer contato com o anunciante. A plataforma também compara os valores de aluguel com base nos anúncios cadastrados e oferece um sistema de compatibilidade (match) para quem quer dividir moradia, em que o contato só é liberado quando há interesse mútuo.

> Projeto Integrador do curso de Engenharia de Software da Universidade Evangélica de Goiás (UniEVANGÉLICA). O sistema ainda não foi implementado. Por enquanto, este repositório guarda a documentação, os diagramas de modelagem e a estrutura inicial para o código, que será desenvolvido nos próximos períodos.

## Protótipo

[Protótipo no Figma](https://www.figma.com/design/7SJaZPapxuv4i1idqwsmSz/Roomy-%E2%80%93-Prot%C3%B3tipo-Alta-Fidelidade--2%C2%BA-per%C3%ADodo--Fase-02-?node-id=0-1&t=bLvcrUeLDhDdassG-1)

## Estrutura do repositório

| Pasta              | Conteúdo                                                                 |
|--------------------|--------------------------------------------------------------------------|
| `docs`             | Documento de especificação do Projeto Integrador                         |
| `docs/diagramas`   | Diagramas de casos de uso, fluxo de locação, fluxo de match e classes conceituais |
| `frontend`         | Interface web, camada de apresentação (em breve)                         |
| `backend`          | Regras de negócio, API e acesso a dados (em breve)                       |
| `.claude`          | Configuração do Claude Code: agentes (`agents`), comandos (`commands`), permissões e hooks (`settings.json`) e o laço (`loop.md`) |
| `scripts`          | Scripts Node: portões de qualidade (`gates.mjs`), verificação do RNF-010 e da rastreabilidade, laço externo e criação de issues; `hooks` são os travamentos automáticos |
| `.github`          | CI (`workflows`), modelo de PR e modelo de issue de tarefa             |
| `docs/adr`         | Decisões de arquitetura (ADR), a começar por `0001-stack.md`           |
| `docs/api`         | Contrato OpenAPI entre frontend e backend (criado na tarefa T-006)       |
| `docs/backlog`     | Backlog de tarefas (`BACKLOG.md`) e decisões pendentes da equipe (`NEEDS_HUMAN.md`) |
| `docs/requisitos`  | Requisitos vigentes (RNE, RF, RNF), fonte de verdade do projeto          |

O frontend e o backend ficam em pastas separadas desde o início, para manter as camadas independentes (RNF-011). Esta tabela é a documentação oficial da estrutura de pastas (RNF-010) e deve ser atualizada sempre que uma pasta for criada ou mudar de função.

## Desenvolvimento com Claude Code

O desenvolvimento é conduzido por um *harness* (instruções, agentes, hooks e gates) descrito em `CLAUDE.md` e `HARNESS.md`. O backlog fica em `docs/backlog/BACKLOG.md`.

- **`/next`**: executa UMA iteração supervisionada (planejar, implementar, testar, revisar, documentar e abrir PR). Comece sempre por ela e leia o PR e o relatório antes de liberar mais.
- **`/loop`**: repete a iteração dentro da sessão aberta, com intervalo escolhido pelo Claude. Esc interrompe. Variante externa, uma tarefa por processo: `node scripts/run-loop.mjs --max 3 --turns 60 --budget 5`.
- **Gates**: `node scripts/gates.mjs` (`--fast` pula e2e). Roda lint, typecheck e testes de cada camada, RNF-010 e rastreabilidade. Nada é "pronto" com gate vermelho.
- **Fluxo de branches**: `feat/T-0xx-slug` (ou `fix/`, `docs/`) a partir de `develop` → PR para `develop` (squash, com gates verdes e revisão aprovada) → a equipe promove `develop` para `main`. Ninguém commita direto na `main` nem usa `push --force`.
- **Decisão humana**: o laço registra em `docs/backlog/NEEDS_HUMAN.md`, marca a tarefa como BLOQUEADA e segue para outra.

## Equipe

| Matrícula | Nome                           | Função                     |
|-----------|--------------------------------|----------------------------|
| 2611903   | Arthur Chagas Coutinho         | Documentação e Requisitos  |
| 2611640   | João Gabriel Moura Souza       | Full-Stack                 |
| 2611201   | João Paulo Silva Abrenhosa     | Front-End                  |
| 2621190   | Pedro Augusto Ferreira Coelho  | Back-End                   |

## Orientadores

- Igor Dalarmelino Borges (orientador principal)
- Jeferson Silva Araújo (orientador secundário)

# Roomy

Plataforma web de locação residencial para estudantes universitários, jovens profissionais e recém-formados de 18 a 30 anos.

O Roomy ataca dois problemas do aluguel tradicional: a falta de informação do locatário sobre valores e cláusulas, e a rigidez dos contratos. Cada anúncio exibe de forma padronizada o valor, as taxas e as condições do contrato, como prazo mínimo e multa por rescisão, antes de qualquer contato com o anunciante. A plataforma também compara os valores de aluguel com base nos anúncios cadastrados e oferece um sistema de compatibilidade (match) para quem quer dividir moradia, em que o contato só é liberado quando há interesse mútuo.

> Projeto Integrador do curso de Engenharia de Software da Universidade Evangélica de Goiás (UniEVANGÉLICA). O sistema ainda não foi implementado. Por enquanto, este repositório guarda a documentação, os diagramas de modelagem e a estrutura inicial para o código, que será desenvolvido nos próximos períodos.

## Protótipo

[Protótipo no Figma] [(https://www.figma.com/design/7SJaZPapxuv4i1idqwsmSz.)] 

## Estrutura do repositório

| Pasta              | Conteúdo                                                                 |
|--------------------|--------------------------------------------------------------------------|
| `docs`             | Documento de especificação do Projeto Integrador                         |
| `docs/diagramas`   | Diagramas de casos de uso, fluxo de locação, fluxo de match e classes conceituais |
| `docs/diagramas/fonte` | Arquivos-fonte dos diagramas, para edição                            |
| `frontend`         | Interface web, camada de apresentação (em breve)                         |
| `backend`          | Regras de negócio, API e acesso a dados (em breve)                       |

O frontend e o backend ficam em pastas separadas desde o início, para manter as camadas independentes (RNF-011). Esta tabela é a documentação oficial da estrutura de pastas (RNF-010) e deve ser atualizada sempre que uma pasta for criada ou mudar de função.

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

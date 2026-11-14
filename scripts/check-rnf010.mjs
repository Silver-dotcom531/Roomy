// Verifica o RNF-010: (1) todo arquivo de código tem cabeçalho de responsabilidade; (2) função com mais de 20 linhas tem comentário antes.
// Uso: node scripts/check-rnf010.mjs [arquivos...]   (sem argumentos varre frontend/src e backend/src)
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join } from 'node:path';

let ts;
try { ts = (await import('typescript')).default; } catch { console.log('RNF-010: typescript ausente (npm install) — checagem pulada'); process.exit(0); }

const LIMITE_LINHAS = 20;
const EXT = /\.(ts|tsx|js|jsx|mjs)$/;
const IGNORAR = /(node_modules|dist|build|coverage|\.d\.ts$|\.test\.|\.spec\.|vite-env)/;

function listar(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir).flatMap((nome) => {
    const caminho = join(dir, nome);
    return statSync(caminho).isDirectory() ? listar(caminho) : [caminho];
  });
}

const args = process.argv.slice(2);
const arquivos = (args.length ? args : [...listar('frontend/src'), ...listar('backend/src')])
  .map((a) => a.replaceAll('\\', '/')).filter((a) => EXT.test(a) && !IGNORAR.test(a));

const falhas = [];
for (const arq of arquivos) {
  const texto = readFileSync(arq, 'utf8');
  const sf = ts.createSourceFile(arq, texto, ts.ScriptTarget.Latest, true);

  // (1) cabeçalho: o primeiro comentário do arquivo (após shebang/'use client') precisa ter texto.
  const corpo = texto.replace(/^#!.*\n/, '').replace(/^\s*['"]use (client|strict)['"];?\s*/, '');
  if (!/^\s*(\/\*[\s\S]*?\*\/|\/\/[^\n]*)/.test(corpo)) falhas.push(`${arq}:1 sem cabeçalho de responsabilidade (RNF-010 a)`);

  // (2) funções longas precisam de comentário no início do comando que as contém.
  const visita = (no) => {
    const ehFuncao = ts.isFunctionDeclaration(no) || ts.isFunctionExpression(no) || ts.isArrowFunction(no) || ts.isMethodDeclaration(no);
    if (ehFuncao) {
      const ini = sf.getLineAndCharacterOfPosition(no.getStart(sf)).line;
      const fim = sf.getLineAndCharacterOfPosition(no.getEnd()).line;
      if (fim - ini + 1 > LIMITE_LINHAS && !temComentario(no, sf)) {
        falhas.push(`${arq}:${ini + 1} função com ${fim - ini + 1} linhas sem comentário explicativo (RNF-010 b)`);
      }
    }
    ts.forEachChild(no, visita);
  };
  visita(sf);
}

/** Sobe até o comando/membro que contém a função e verifica se há comentário logo antes dele. */
function temComentario(no, sf) {
  let n = no;
  while (n.parent && !ts.isSourceFile(n.parent) && !ts.isBlock(n.parent) && !ts.isClassDeclaration(n.parent)
         && !ts.isModuleBlock(n.parent) && !ts.isObjectLiteralExpression(n.parent)) n = n.parent;
  const topo = n.getFullStart();
  // O comentário de cabeçalho (posição 0) não conta como comentário da função.
  return (ts.getLeadingCommentRanges(sf.text, topo) ?? []).filter((c) => c.pos > 0).length > 0;
}

if (falhas.length) { console.log(falhas.join('\n')); console.log(`\nRNF-010: ${falhas.length} problema(s).`); process.exit(1); }
console.log(`RNF-010: ${arquivos.length} arquivo(s) conferidos, ok.`);

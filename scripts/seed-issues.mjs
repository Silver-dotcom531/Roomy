// Cria uma issue do GitHub por tarefa do BACKLOG.md (idempotente pelo prefixo "[T-0xx]"). Padrão: simulação.
// Uso: node scripts/seed-issues.mjs            (mostra o que faria)
//      node scripts/seed-issues.mjs --apply    (cria issues e rótulos; exige `gh auth login`)
import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const aplicar = process.argv.includes('--apply');
const gh = (args) => spawnSync('gh', args, { encoding: 'utf8', shell: process.platform === 'win32' });

const tarefas = [];
let epico = '';
for (const l of readFileSync('docs/backlog/BACKLOG.md', 'utf8').split('\n')) {
  const e = l.match(/^## (E\d+) — (.*)/); if (e) epico = e[1];
  const c = l.split('|').map((x) => x.trim());
  if (/^T-\d{3}$/.test(c[1] ?? '')) tarefas.push({ id: c[1], titulo: c[2], req: c[3], dep: c[5], pronto: c[7] ?? '', epico });
}

const existentes = aplicar ? JSON.parse(gh(['issue', 'list', '--state', 'all', '--limit', '300', '--json', 'title']).stdout || '[]').map((i) => i.title) : [];
for (const t of tarefas) {
  const titulo = `[${t.id}] ${t.titulo}`;
  if (existentes.some((x) => x.startsWith(`[${t.id}]`))) { console.log(`= já existe: ${titulo}`); continue; }
  const corpo = `**Requisitos:** ${t.req}\n**Depende de:** ${t.dep}\n**Pronto quando:** ${t.pronto}\n\nFonte: docs/backlog/BACKLOG.md`;
  if (!aplicar) { console.log(`+ (simulação) ${titulo}  [epic:${t.epico}]`); continue; }
  gh(['label', 'create', `epic:${t.epico}`, '--force']);
  const r = gh(['issue', 'create', '--title', titulo, '--body', corpo, '--label', `epic:${t.epico}`]);
  console.log(r.status === 0 ? `+ ${titulo}` : `! falhou: ${titulo}\n${r.stderr}`);
}
console.log(`${tarefas.length} tarefas lidas${aplicar ? '' : ' (nada foi criado; use --apply)'}.`);

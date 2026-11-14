// Laço externo ("ralph loop"): chama o Claude Code em modo não interativo, uma tarefa por iteração, com contexto novo a cada volta.
// Para quando: não há tarefa PRONTA, o orçamento de iterações acaba ou o Claude sai com erro. Pendências humanas só bloqueiam a tarefa afetada (status BLOQUEADA).
// Uso: node scripts/run-loop.mjs [--max 5] [--turns 60] [--budget 5]
import { readFileSync, existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const arg = (n, d) => { const i = process.argv.indexOf(`--${n}`); return i > -1 ? process.argv[i + 1] : d; };
const MAX = Number(arg('max', 5)), TURNOS = arg('turns', '60'), ORCAMENTO = arg('budget', '5');
const prompt = readFileSync('.claude/loop.md', 'utf8');
const prontas = () => (readFileSync('docs/backlog/BACKLOG.md', 'utf8').match(/\|\s*PRONTA\s*\|/g) ?? []).length;
const pendencias = () => existsSync('docs/backlog/NEEDS_HUMAN.md')
  ? (readFileSync('docs/backlog/NEEDS_HUMAN.md', 'utf8').match(/^- \[ \]/gm) ?? []).length : 0;

for (let i = 1; i <= MAX; i++) {
  if (!prontas()) { console.log('Nenhuma tarefa PRONTA. Fim.'); break; }
  console.log(`\n=== Iteração ${i}/${MAX} (pendências humanas abertas: ${pendencias()}) ===`);
  const r = spawnSync('claude', ['-p', prompt, '--max-turns', TURNOS, '--max-budget-usd', ORCAMENTO,
    '--permission-mode', 'acceptEdits', '--output-format', 'text'], { stdio: 'inherit', shell: process.platform === 'win32' });
  if (r.status !== 0) { console.log(`claude saiu com código ${r.status}. Parando para revisão.`); break; }
}

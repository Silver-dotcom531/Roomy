// Hook Stop: impede o Claude de encerrar o turno com os gates quebrados.
// Para não travar em laço infinito, desiste após 3 bloqueios seguidos e registra em NEEDS_HUMAN.md.
import { existsSync, readFileSync, writeFileSync, appendFileSync, mkdirSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const CONTADOR = '.claude/.stop-gate-count';
const LIMITE = 3;
const ler = () => (existsSync(CONTADOR) ? Number(readFileSync(CONTADOR, 'utf8')) || 0 : 0);

const r = spawnSync(process.execPath, ['scripts/gates.mjs', '--fast'], { encoding: 'utf8' });
if (r.status === 0) { writeFileSync(CONTADOR, '0'); process.exit(0); }

const n = ler() + 1;
writeFileSync(CONTADOR, String(n));
if (n >= LIMITE) {
  mkdirSync('docs/backlog', { recursive: true });
  appendFileSync('docs/backlog/NEEDS_HUMAN.md',
    `\n- ${new Date().toISOString()} — gates falharam ${n}x seguidas ao encerrar; revisão humana necessária.\n\`\`\`\n${(r.stdout + r.stderr).slice(-1500)}\n\`\`\`\n`);
  writeFileSync(CONTADOR, '0');
  process.exit(0);
}
console.error(`Gates falharam (tentativa ${n}/${LIMITE}). Corrija antes de encerrar:\n` + (r.stdout + r.stderr).slice(-2500));
process.exit(2);

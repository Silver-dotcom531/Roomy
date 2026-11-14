// Portões de qualidade. Roda o que existir: lint, typecheck e testes de cada camada, RNF-010 e rastreabilidade.
// Uso: node scripts/gates.mjs [--fast]   (--fast pula testes e2e / Lighthouse)
import { existsSync, readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const rapido = process.argv.includes('--fast');
const npm = process.platform === 'win32' ? 'npm.cmd' : 'npm';
const resultados = [];

function roda(nome, cmd, args, opts = {}) {
  const r = spawnSync(cmd, args, { encoding: 'utf8', shell: process.platform === 'win32', ...opts });
  const ok = r.status === 0;
  resultados.push({ nome, ok });
  if (!ok) console.log(`\n--- FALHOU: ${nome}\n${(r.stdout + r.stderr).slice(-1800)}`);
}

for (const camada of ['backend', 'frontend']) {
  const pkgPath = `${camada}/package.json`;
  if (!existsSync(pkgPath)) { console.log(`(${camada}: sem package.json, pulado)`); continue; }
  const scripts = JSON.parse(readFileSync(pkgPath, 'utf8')).scripts ?? {};
  for (const s of ['lint', 'typecheck', 'test']) {
    if (scripts[s]) roda(`${camada}:${s}`, npm, ['run', s, '--silent'], { cwd: camada });
  }
  if (!rapido && scripts['test:e2e']) roda(`${camada}:test:e2e`, npm, ['run', 'test:e2e', '--silent'], { cwd: camada });
}
// shell:true no Windows quebra caminhos com espaço (C:\Program Files): o node roda sem shell
roda('rnf010', process.execPath, ['scripts/check-rnf010.mjs'], { shell: false });
roda('rastreabilidade', process.execPath, ['scripts/trace-check.mjs'], { shell: false });

const falhas = resultados.filter((r) => !r.ok);
console.log(`\nGATES: ${resultados.length - falhas.length}/${resultados.length} ok${falhas.length ? ' — falharam: ' + falhas.map((f) => f.nome).join(', ') : ''}`);
process.exit(falhas.length ? 1 : 0);

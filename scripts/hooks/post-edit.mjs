// Hook PostToolUse: após editar um arquivo de código, aplica a checagem RNF-010 (cabeçalho e funções longas) só nele.
// exit 2 devolve a mensagem ao Claude para corrigir na hora.
import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

let entrada = {};
try { entrada = JSON.parse(readFileSync(0, 'utf8') || '{}'); } catch { process.exit(0); }
const arquivo = String(entrada?.tool_input?.file_path ?? '').replaceAll('\\', '/');

if (!/(^|\/)(frontend|backend)\/src\/.*\.(ts|tsx|js|jsx|mjs)$/.test(arquivo)) process.exit(0);

const r = spawnSync(process.execPath, ['scripts/check-rnf010.mjs', arquivo], { encoding: 'utf8' });
if (r.status !== 0) {
  console.error(r.stdout + r.stderr);
  process.exit(2);
}
process.exit(0);

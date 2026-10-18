// Hook PreToolUse: bloqueia edição de arquivos protegidos (diagramas, .docx, .env, configuração do harness).
// Entrada: JSON no stdin com tool_input.file_path. Saída: exit 2 + mensagem em stderr bloqueia a chamada.
import { readFileSync } from 'node:fs';

const PROTEGIDOS = [
  /(^|\/)docs\/diagramas\//, /\.docx$/i, /(^|\/)\.env(\..*)?$/,
  /(^|\/)\.claude\/settings\.json$/, /(^|\/)scripts\/hooks\//,
];

let entrada = {};
try { entrada = JSON.parse(readFileSync(0, 'utf8') || '{}'); } catch { process.exit(0); }
const alvo = String(entrada?.tool_input?.file_path ?? '').replaceAll('\\', '/');

if (alvo && PROTEGIDOS.some((re) => re.test(alvo))) {
  console.error(`BLOQUEADO: "${alvo}" é protegido (diagramas, .docx, .env ou harness). Se a mudança é realmente necessária, registre em docs/backlog/NEEDS_HUMAN.md.`);
  process.exit(2);
}
process.exit(0);

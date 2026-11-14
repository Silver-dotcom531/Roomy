// Confere docs/rastreabilidade.md: todos os RF/RNE do documento têm linha; linha "feito" cita testes que existem.
import { readFileSync, existsSync } from 'node:fs';

const ESPERADOS = [
  ...Array.from({ length: 14 }, (_, i) => `RF-${String(i + 1).padStart(3, '0')}`),
  ...Array.from({ length: 9 }, (_, i) => `RNE-${String(i + 1).padStart(3, '0')}`),
  ...Array.from({ length: 11 }, (_, i) => `RNF-${String(i + 1).padStart(3, '0')}`),
];
const ARQ = 'docs/rastreabilidade.md';
if (!existsSync(ARQ)) { console.log(`trace: ${ARQ} não existe`); process.exit(1); }

const linhas = readFileSync(ARQ, 'utf8').split('\n').filter((l) => l.startsWith('|'));
const mapa = new Map();
for (const l of linhas) {
  const c = l.split('|').map((x) => x.trim());
  if (/^(RF|RNE|RNF)-\d{3}$/.test(c[1] ?? '')) mapa.set(c[1], { status: (c[3] ?? '').toLowerCase(), testes: c[4] ?? '' });
}

const erros = [];
for (const id of ESPERADOS) if (!mapa.has(id)) erros.push(`${id} sem linha na matriz`);
for (const [id, { status, testes }] of mapa) {
  if (status.includes('feito')) {
    const arquivos = testes.split(/[,;\s]+/).filter((t) => /\.(test|spec)\./.test(t));
    if (!arquivos.length) erros.push(`${id} marcado feito sem arquivo de teste`);
    for (const a of arquivos) if (!existsSync(a)) erros.push(`${id}: teste citado não existe (${a})`);
  }
}
if (erros.length) { console.log(erros.join('\n')); process.exit(1); }
console.log(`trace: ${mapa.size} linhas, ok.`);

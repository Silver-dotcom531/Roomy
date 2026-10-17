#!/usr/bin/env python3
"""Diagrama 4 - Classes conceituais do Roomy (2o periodo).

Conceitual: sem tipos de dados, chaves ou operacoes (modelo formal = Secao 18).
Fonte: RF-001..RF-014, RNE-001..RNE-009 (PI 2_periodo_fase_1.docx).
Layout manual; pontos de conexao calculados a partir das caixas (sem folgas).
"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

OUT = sys.argv[1] if len(sys.argv) > 1 else "d4_classes.png"

INK = "#0F1C2E"
TEAL_DK = "#138A7A"
BODY = "#E3F6F2"
GRAY = "#4A5568"

plt.rcParams["font.family"] = "DejaVu Sans"

W, H = 7.2, 7.05
fig, ax = plt.subplots(figsize=(W, H), dpi=300)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")
ax.axis("off")

HDR_H, LINE_H, TOP_PAD, BOT_PAD = 0.26, 0.135, 0.065, 0.05
BOX = {}


def klass(key, name, attrs, x0, ytop, w):
    h = HDR_H + TOP_PAD + len(attrs) * LINE_H + BOT_PAD
    y0 = ytop - h
    ax.add_patch(Rectangle((x0, y0), w, h, fc=BODY, ec=TEAL_DK, lw=1.1, zorder=2))
    ax.add_patch(Rectangle((x0, ytop - HDR_H), w, HDR_H, fc=TEAL_DK, ec=TEAL_DK,
                           lw=1.1, zorder=3))
    ax.text(x0 + w / 2, ytop - HDR_H / 2, name, ha="center", va="center",
            fontsize=7.2, fontweight="bold", color="white", zorder=4)
    for i, a in enumerate(attrs):
        ax.text(x0 + 0.08, ytop - HDR_H - TOP_PAD - (i + 0.5) * LINE_H, a,
                ha="left", va="center", fontsize=6.7, color=INK, zorder=4)
    BOX[key] = (x0, y0, x0 + w, ytop)


def L(k): return BOX[k][0]
def B(k): return BOX[k][1]
def R(k): return BOX[k][2]
def T(k): return BOX[k][3]


klass("perfil", "PerfilDeConvivência",
      ["horário de sono", "nível de organização", "tolerância a barulho",
       "animais de estimação", "frequência de visitas"], 0.12, 6.90, 1.72)
klass("usuario", "Usuário",
      ["nome completo", "e-mail (único)", "senha", "e-mail confirmado",
       "tipo(s) de conta: locatário", "   e/ou anunciante",
       "foto e nome de exibição", "descrição pessoal", "dados de contato (opcionais)"], 2.62, 6.90, 2.00)
klass("interesse", "InteresseDeMatch", ["data", "/mútuo"], 5.60, 6.70, 1.52)
klass("anuncio", "Anúncio",
      ["valor mensal do aluguel", "localização (bairro e cidade)", "tipo de imóvel",
       "nº de quartos disponíveis", "prazo mínimo de contrato",
       "condições de cancelamento", "fotos (mínimo de 1)", "descrição",
       "status (ativo ou inativo)"], 0.45, 4.70, 2.45)
klass("conversa", "Conversa",
      ["mensagens (canal interno)", "/locação concretizada"], 3.10, 2.70, 1.95)
klass("avaliacao", "Avaliação",
      ["nota (de 1 a 5)", "comentário descritivo", "data"], 5.60, 2.70, 1.52)
klass("confirm", "ConfirmaçãoDeLocação",
      ["parte (locatário ou anunciante)", "data e hora"], 3.20, 1.35, 2.20)


def line(pts, lw=0.95):
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=INK, lw=lw, zorder=1,
            solid_capstyle="butt", solid_joinstyle="miter")


def t(x, y, s, ha="left", va="center", size=6.4, italic=False, color=INK):
    ax.text(x, y, s, ha=ha, va=va, fontsize=size, color=color,
            style="italic" if italic else "normal", zorder=5)


def mult(x, y, s, ha="left"):
    t(x, y, s, ha=ha, size=6.4)


def role(x, y, s, ha="left", va="center"):
    t(x, y, s, ha=ha, va=va, size=5.9, italic=True, color=GRAY)


def assoc_name(x, y, s, ha="left", va="center"):
    t(x, y, s, ha=ha, va=va, size=6.3, italic=True)


# 1) Usuario - PerfilDeConvivencia (preenche)  [RF-008]
y = 6.40
line([(R("perfil"), y), (L("usuario"), y)])
mult(L("usuario") - 0.05, y + 0.08, "1", ha="right")
mult(R("perfil") + 0.06, y + 0.08, "0..1")
assoc_name((R("perfil") + L("usuario")) / 2, y - 0.06, "preenche", ha="center", va="top")

# 2) Usuario - InteresseDeMatch (destino acima / origem abaixo)  [RF-009, RNE-006]
yd, yo = 6.55, 6.22
xm = (R("usuario") + L("interesse")) / 2
line([(R("usuario"), yd), (L("interesse"), yd)])
line([(R("usuario"), yo), (L("interesse"), yo)])
mult(R("usuario") + 0.07, yd + 0.08, "1")
mult(L("interesse") - 0.05, yd + 0.08, "0..*", ha="right")
mult(R("usuario") + 0.07, yo - 0.08, "1")
mult(L("interesse") - 0.05, yo - 0.08, "0..*", ha="right")
role(xm, yd - 0.075, "destino", ha="center")
role(xm, yo + 0.075, "origem", ha="center")

# 3) Usuario - Anuncio (publica)  [RF-004]
x = 2.72
line([(x, B("usuario")), (x, T("anuncio"))])
mult(x - 0.05, B("usuario") - 0.09, "1", ha="right")
role(x + 0.06, B("usuario") - 0.10, "anunciante")
assoc_name(x + 0.06, (B("usuario") + T("anuncio")) / 2, "publica")
mult(x - 0.05, T("anuncio") + 0.09, "0..*", ha="right")

# 4) Usuario - Conversa (inicia)  [RF-010]
x = 3.67
line([(x, B("usuario")), (x, T("conversa"))])
mult(x - 0.05, B("usuario") - 0.09, "1", ha="right")
role(x + 0.06, B("usuario") - 0.10, "locatário")
assoc_name(x + 0.06, 4.20, "inicia")
mult(x - 0.05, T("conversa") + 0.09, "0..*", ha="right")

# 5) Usuario - Avaliacao (autor = externa / avaliado = interna)  [RF-012, RNE-008]
ya, yv = 5.90, 5.70
xa, xv = 6.25, 5.95
line([(R("usuario"), ya), (xa, ya), (xa, T("avaliacao"))])
line([(R("usuario"), yv), (xv, yv), (xv, T("avaliacao"))])
mult(R("usuario") + 0.07, ya + 0.075, "1")
mult(R("usuario") + 0.07, yv + 0.075, "1")
role(xa + 0.06, 4.40, "autor")
role(xv - 0.06, 4.40, "avaliado", ha="right")
mult(xa + 0.06, T("avaliacao") + 0.09, "0..*")
mult(xv - 0.06, T("avaliacao") + 0.09, "0..*", ha="right")

# 6) Anuncio - Conversa (origina)  [RF-010, RF-014: conversa referente ao imovel]
x, y = 2.40, 2.40
line([(x, B("anuncio")), (x, y), (L("conversa"), y)])
mult(x + 0.06, B("anuncio") - 0.09, "1")
assoc_name(x + 0.07, 2.80, "origina")
mult(L("conversa") - 0.06, y + 0.08, "0..*", ha="right")

# 7) Conversa - Avaliacao (gera)  [RF-012 liberada por RF-014]
y = 2.40
line([(R("conversa"), y), (L("avaliacao"), y)])
mult(R("conversa") + 0.04, y + 0.08, "1")
mult(L("avaliacao") - 0.04, y + 0.08, "0..2", ha="right")
assoc_name((R("conversa") + L("avaliacao")) / 2, y - 0.06, "gera", ha="center", va="top")

# 8) Conversa - ConfirmacaoDeLocacao (registra)  [RF-014]
x = 4.00
line([(x, B("conversa")), (x, T("confirm"))])
mult(x - 0.05, B("conversa") - 0.09, "1", ha="right")
assoc_name(x + 0.06, (B("conversa") + T("confirm")) / 2, "registra")
mult(x - 0.05, T("confirm") + 0.09, "0..2", ha="right")

# --- nota de notacao ---
ax.add_patch(FancyBboxPatch((0.12, 0.15), 2.62, 0.97,
                            boxstyle="round,pad=0,rounding_size=0.05",
                            fc="white", ec=GRAY, lw=0.7, zorder=2))
notes = [
    ("Notação", True),
    ("/atributo = atributo derivado (calculado)", False),
    ("Multiplicidades: 1 · 0..1 · 0..* · 0..2", False),
    ("Conceitual: sem tipos de dados, chaves", False),
    ("ou operações. Modelo formal: Seção 18.", False),
]
for i, (s, bold) in enumerate(notes):
    ax.text(0.21, 0.99 - i * 0.175, s, ha="left", va="center",
            fontsize=6.4 if bold else 5.8, fontweight="bold" if bold else "normal",
            color=INK if bold else GRAY, zorder=4)

fig.savefig(OUT, dpi=300, facecolor="white", bbox_inches="tight", pad_inches=0.06)
print("salvo:", OUT)

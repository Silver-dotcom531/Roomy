#!/usr/bin/env python3
"""Diagrama 1 - Casos de uso do Roomy (conceitual, 2o periodo).

Fonte de verdade: PI 2_periodo_fase_1.docx (RF-001..RF-014, RNE-001..RNE-009).
Layout: coluna unica de casos de uso; atores a esquerda (Visitante, Locatario)
e a direita (Anunciante). As linhas terminam nas pontas das elipses e nunca
atravessam outra elipse.
"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch, Circle, FancyArrowPatch

OUT = sys.argv[1] if len(sys.argv) > 1 else "d1_casos_de_uso.png"

INK = "#0F1C2E"
TEAL = "#1DB5A0"
TEAL_DK = "#138A7A"
TEAL_BG = "#F2FBF9"
UC_FILL = "#E3F6F2"
AMBER_DK = "#B86E00"
GRAY = "#4A5568"

plt.rcParams["font.family"] = "DejaVu Sans"

W, H = 7.2, 10.5
fig, ax = plt.subplots(figsize=(W, H), dpi=300)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")
ax.axis("off")

CX = 3.6
EW, EH = 2.78, 0.42

# (id, titulo, referencias, y)
ROWS = [
    ("uc01", "Cadastrar-se", "RF-001", 9.65),
    ("uc02", "Ver listagem resumida de imóveis", "RNE-001", 9.13),
    ("uc03", "Buscar e filtrar imóveis", "RF-006", 8.61),
    ("uc04", "Visualizar detalhes do imóvel", "RF-007", 8.09),
    ("uc05", "Ver comparativo de valores", "RF-011 · RNE-009", 7.43),
    ("uc06", "Preencher perfil de convivência", "RF-008", 6.91),
    ("uc07", "Encontrar colegas de quarto (match)", "RF-009 · RNE-006", 6.25),
    ("uc08", "Fazer login e logout", "RF-002", 5.73),
    ("uc09", "Recuperar ou alterar senha", "RF-003", 5.21),
    ("uc10", "Gerenciar perfil", "RF-013", 4.69),
    ("uc11", "Conversar pelo canal interno", "RF-010 · RNE-007", 4.17),
    ("uc12", "Confirmar locação concretizada", "RF-014", 3.65),
    ("uc13", "Avaliar a outra parte", "RF-012 · RNE-008", 2.99),
    ("uc14", "Publicar anúncio", "RF-004", 2.47),
    ("uc15", "Validar campos obrigatórios", "RNE-002 · RNE-003", 1.81),
    ("uc16", "Editar, desativar ou reativar anúncio", "RF-005 · RNE-005", 1.29),
]
YPOS = {r[0]: r[3] for r in ROWS}

# --- fronteira do sistema ---
bx0, bx1, by0, by1 = 2.0, 5.2, 0.82, 10.3
ax.add_patch(FancyBboxPatch((bx0, by0), bx1 - bx0, by1 - by0,
                            boxstyle="round,pad=0,rounding_size=0.12",
                            fc=TEAL_BG, ec=TEAL, lw=1.6, zorder=0))
ax.text((bx0 + bx1) / 2, by1 - 0.19, "Sistema Roomy (plataforma web)",
        ha="center", va="center", fontsize=8.6, fontweight="bold",
        color=TEAL_DK, zorder=5)

# --- elipses ---
for uid, title, ref, y in ROWS:
    ax.add_patch(Ellipse((CX, y), EW, EH, fc=UC_FILL, ec=TEAL_DK, lw=1.0, zorder=2))
    fs = 6.9 if len(title) <= 31 else 6.1
    ax.text(CX, y + 0.06, title, ha="center", va="center", fontsize=fs,
            fontweight="bold", color=INK, zorder=4)
    ax.text(CX, y - 0.105, ref, ha="center", va="center", fontsize=5.7,
            color=GRAY, zorder=4)


def actor(x, y, label):
    """Boneco palito; (x, y) = centro da cabeca. Retorna o ponto do braco."""
    r = 0.11
    ax.add_patch(Circle((x, y), r, fc="white", ec=INK, lw=1.3, zorder=3))
    ax.plot([x, x], [y - r, y - 0.52], color=INK, lw=1.3, zorder=3)
    ax.plot([x - 0.22, x + 0.22], [y - 0.26, y - 0.26], color=INK, lw=1.3, zorder=3)
    ax.plot([x, x - 0.18], [y - 0.52, y - 0.82], color=INK, lw=1.3, zorder=3)
    ax.plot([x, x + 0.18], [y - 0.52, y - 0.82], color=INK, lw=1.3, zorder=3)
    ax.text(x, y - 1.0, label, ha="center", va="top", fontsize=7.2,
            fontweight="bold", color=INK, linespacing=1.1, zorder=3)
    return (x, y - 0.26)


vis = actor(0.95, 9.40, "Visitante\n(não autenticado)")
loc = actor(0.95, 6.20, "Locatário")
anu = actor(6.25, 3.60, "Anunciante")


def assoc(actor_pt, uid, side):
    y = YPOS[uid]
    x_tip = CX - EW / 2 if side == "L" else CX + EW / 2
    ax_, ay_ = actor_pt
    start = (ax_ + 0.22, ay_) if side == "L" else (ax_ - 0.22, ay_)
    ax.plot([start[0], x_tip], [start[1], y], color=INK, lw=0.85, zorder=1)


ASSOC_VIS = ["uc01", "uc02"]
ASSOC_LOC = ["uc03", "uc04", "uc06", "uc07", "uc08", "uc09", "uc10", "uc11", "uc12", "uc13"]
ASSOC_ANU = ["uc08", "uc09", "uc10", "uc11", "uc12", "uc13", "uc14", "uc16"]
for u in ASSOC_VIS:
    assoc(vis, u, "L")
for u in ASSOC_LOC:
    assoc(loc, u, "L")
for u in ASSOC_ANU:
    assoc(anu, u, "R")


def vgap_arrow(uid_from, uid_to, label, color):
    y1, y2 = YPOS[uid_from], YPOS[uid_to]
    start_y = y1 - EH / 2 if y2 < y1 else y1 + EH / 2
    end_y = y2 + EH / 2 if y2 < y1 else y2 - EH / 2
    ax.add_patch(FancyArrowPatch((CX, start_y), (CX, end_y), arrowstyle="-|>",
                                 mutation_scale=7, lw=1.0, color=color,
                                 linestyle=(0, (3, 2)), zorder=1))
    ax.text(CX + 0.07, (start_y + end_y) / 2, label, ha="left", va="center",
            fontsize=5.8, style="italic", color=color, zorder=4)


INCLUDES = [("uc04", "uc05"), ("uc14", "uc15")]
PRECOND = [("uc07", "uc06"), ("uc13", "uc12")]
for a, b in INCLUDES:
    vgap_arrow(a, b, "«include»", INK)
for a, b in PRECOND:
    vgap_arrow(a, b, "pré-condição", AMBER_DK)

# --- legenda ---
lx, ly = 0.12, 1.5
ax.add_patch(FancyBboxPatch((lx, ly - 1.0), 1.78, 1.12,
                            boxstyle="round,pad=0,rounding_size=0.06",
                            fc="white", ec=GRAY, lw=0.7, zorder=2))
ax.text(lx + 0.08, ly + 0.02, "Legenda", fontsize=6.6, fontweight="bold",
        color=INK, va="center", zorder=4)
ax.plot([lx + 0.08, lx + 0.42], [ly - 0.22, ly - 0.22], color=INK, lw=0.85, zorder=4)
ax.text(lx + 0.5, ly - 0.22, "associação", fontsize=6.0, va="center", color=INK, zorder=4)
for dy, col, txt in ((0.45, INK, "«include»"), (0.68, AMBER_DK, "pré-condição")):
    ax.add_patch(FancyArrowPatch((lx + 0.08, ly - dy), (lx + 0.42, ly - dy),
                                 arrowstyle="-|>", mutation_scale=6, lw=1.0,
                                 color=col, linestyle=(0, (3, 2)), zorder=4))
    ax.text(lx + 0.5, ly - dy, txt, fontsize=6.0, va="center", color=col, zorder=4)
ax.text(lx + 0.08, ly - 0.90, "RF/RNE = requisito de origem", fontsize=5.4,
        va="center", color=GRAY, zorder=4)

fig.savefig(OUT, dpi=300, facecolor="white", bbox_inches="tight", pad_inches=0.06)
print("salvo:", OUT)

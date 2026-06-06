"""
Generates assets/coverage.png — the "Where saas-builder fits in your stack" hero chart.
Reproducible: `python assets/coverage_chart.py` (needs matplotlib).

Honest framing: bars show what saas-builder COVERS (cream) vs what it leaves to
Superpowers (process) and optional audit plugins (review) — not a personal setup score.
"""
import matplotlib.pyplot as plt
from matplotlib import font_manager

BG     = "#1C1B19"   # warm near-black
CREAM  = "#ECE7DF"   # filled bar / saas-builder
SUB    = "#A8A29A"   # subtitle
DIM    = "#6E6A63"   # non-saas labels
TRACK  = "#4A463F"   # dotted empty texture

plt.rcParams["font.family"] = "serif"

# (area, coverage 0-100, covered-by, is_saas)
rows = [
    ("Dev process — brainstorm, TDD, git",          0,   "Superpowers",            False),
    ("Product discovery & MVP scoping",             100, "saas-builder",           True),
    ("Architecture & system design",                100, "saas-builder",           True),
    ("UI / UX & design system",                     100, "saas-builder",           True),
    ("Backend — API, data modeling, auth",          100, "saas-builder",           True),
    ("Applied security (prevention)",               100, "saas-builder",           True),
    ("Payments & monetization",                     100, "saas-builder",           True),
    ("Performance · a11y · SEO · PWA",              100, "saas-builder",           True),
    ("Pre-ship security review",                    100, "saas-builder",           True),
    ("Deploy · CI/CD · monitoring · rollback",      100, "saas-builder",           True),
    ("Deep security audit & fuzzing",               0,   "optional audit plugins", False),
    ("Codebase & docs audit",                       0,   "optional audit plugins", False),
]

n = len(rows)
fig, ax = plt.subplots(figsize=(13, 8.6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

H = 0.62
for i, (area, cov, who, is_saas) in enumerate(rows):
    y = n - 1 - i
    # dotted "empty" track across the full width
    ax.barh(y, 100, height=H, facecolor="none", edgecolor=TRACK, hatch="....", linewidth=0)
    # solid cream fill up to coverage
    if cov > 0:
        ax.barh(y, cov, height=H, color=CREAM, edgecolor="none", zorder=3)
    # thin separator under the row
    ax.axhline(y - 0.5, color="#2E2C28", linewidth=0.8, zorder=0)
    # left label (area)
    ax.text(-3, y, area, ha="right", va="center", color=CREAM if is_saas else SUB,
            fontsize=12, zorder=4)
    # right label (covered by)
    ax.text(104, y, who, ha="left", va="center",
            color=CREAM if is_saas else DIM, fontsize=11.5,
            fontweight="bold" if is_saas else "normal", zorder=4)

ax.set_xlim(0, 100)
ax.set_ylim(-0.6, n - 0.3)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_xticks([]); ax.set_yticks([])

# column headers
ax.text(-3, n - 0.15, "AREA", ha="right", va="bottom", color=DIM, fontsize=10, fontfamily="sans-serif")
ax.text(0,  n - 0.15, "WHAT saas-builder COVERS", ha="left", va="bottom", color=DIM, fontsize=10, fontfamily="sans-serif")
ax.text(104, n - 0.15, "COVERED BY", ha="left", va="bottom", color=DIM, fontsize=10, fontfamily="sans-serif")

# title + subtitle
fig.text(0.043, 0.95, "From idea to shipped product", fontsize=25, color=CREAM, fontweight="bold")
fig.text(0.043, 0.905,
         "What saas-builder covers — and what it leaves to Superpowers and optional audit plugins.",
         fontsize=13.5, color=SUB)
fig.text(0.043, 0.038, "Superpowers + saas-builder  =  idea → shipped product.    github.com/MartinOlivero/saas-builder",
         fontsize=11, color=DIM)

plt.subplots_adjust(left=0.37, right=0.82, top=0.855, bottom=0.085)
fig.savefig("assets/coverage.png", dpi=200, facecolor=BG)
print("wrote assets/coverage.png")

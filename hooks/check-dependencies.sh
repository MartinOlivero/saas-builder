#!/usr/bin/env bash
# saas-builder — SessionStart dependency check.
#
# Qué hace: busca si ui-ux-pro-max está instalado como skill.
#   - Si LO encuentra  -> sale en silencio (exit 0, sin salida).
#   - Si NO lo encuentra -> muestra un aviso al usuario y sale con código 2.
#
# Por qué exit 2: en el evento SessionStart, lo que va a stdout se agrega al
# contexto de Claude (el usuario no lo ve). El único canal documentado para
# mostrarle un mensaje AL USUARIO es stderr + exit 2 (la sesión continúa igual).
#
# Compatible con macOS (BSD find) y Linux (GNU find): -iname y -maxdepth
# existen en ambos.

set -u

# Carpetas de skills a inspeccionar: las del usuario y, si existe, las del proyecto.
search_dirs="$HOME/.claude/skills"
if [ -n "${CLAUDE_PROJECT_DIR:-}" ]; then
  search_dirs="$search_dirs $CLAUDE_PROJECT_DIR/.claude/skills"
fi

found=0
for dir in $search_dirs; do
  [ -d "$dir" ] || continue
  # Coincidencia case-insensitive de cualquier carpeta ui-ux-pro* o uipro*
  # (uipro instala bajo nombres ligeramente distintos según versión).
  if find "$dir" -maxdepth 1 -type d \( -iname 'ui-ux-pro*' -o -iname 'uipro*' \) 2>/dev/null | grep -q .; then
    found=1
    break
  fi
done

# Detectado: nada que hacer, salida silenciosa.
[ "$found" -eq 1 ] && exit 0

# No detectado: avisar al usuario (stderr + exit 2 = visible en SessionStart).
printf '%s\n' \
  "⚠️  saas-builder: ui-ux-pro-max not detected." \
  "   For professional-grade design intelligence (161 palettes, 50+ styles):" \
  "   npx uipro@latest init --ai claude" \
  "   Run once — saas-builder will use it automatically." >&2
exit 2

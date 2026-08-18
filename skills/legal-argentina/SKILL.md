---
name: legal-argentina
description: This skill should be used when a product operating in Argentina needs its legal documents — terms of service, privacy policy, security policy, botón de arrepentimiento, botón de baja — either written from scratch or audited against the real codebase. Trigger phrases (Spanish) include "términos y condiciones", "política de privacidad", "política de seguridad", "botón de arrepentimiento", "botón de baja", "legales para mi SaaS", "¿cumplo con la ley de datos?", "auditá mis legales", "revisá mi política de privacidad", "Ley 25.326", "AAIP", "habeas data", "necesito los legales antes de lanzar". Trigger phrases (English) include "terms and conditions for Argentina", "Argentine privacy policy", "audit my legal docs", "data protection compliance Argentina". Use it INSTEAD of generic GDPR/CCPA templates whenever the responsible party, the users, or the servers touch Argentina.
---

# Legales para SaaS argentinos

Genera y audita documentos legales para productos que operan en Argentina, deduciéndolos
del código real en vez de una plantilla.

**Por qué existe:** las skills de legales apuntan a GDPR, CCPA y LGPD. Un SaaS argentino
que las usa termina con un documento que promete "portabilidad" y "DPO" —figuras que la
Ley 25.326 no tiene— y sin las tres cosas que sí le van a reclamar: identificación del
responsable con CUIT, transferencia internacional declarada, y los dos botones de la
Disposición 954/2025.

Analogía: una plantilla internacional es un traje comprado hecho. Le sobra tela de un lado
y le falta del otro, y desde lejos parece que te queda. Esta skill toma las medidas.

## Los cinco no negociables

Si alguno se rompe, la salida no sirve. No son sugerencias.

1. **Verificar vigencia antes de escribir.** El modelo recuerda normativa vieja. En 2025-2026
   cambiaron tres cosas centrales (ver `references/normativa-ar.md` § Verificación obligatoria).
   Nunca escribas un documento sin correr ese paso.
2. **Leer el producto antes de redactar.** Esquema, código, proveedores, píxeles. Ver "El método".
3. **No prometer lo que el producto no hace.** Sin respaldos verificados, el documento no
   dice que hay respaldos. Es la regla que más valor agrega y la que más se rompe.
4. **Frenar sin identificación del responsable.** Razón social o nombre, CUIT y domicilio.
   Si el usuario no los tiene, se entrega el borrador marcado `[FALTA]` y **no se publica**.
5. **Decir el límite en la salida, no solo acá.** Todo documento generado cierra con el
   aviso de revisión profesional. Esto produce un borrador informado, no un documento
   validado por un abogado.

## Elegir el modo

| El usuario quiere | Modo | Sección |
| --- | --- | --- |
| Escribir los legales de un producto (nuevo o sin documentos) | **Generar** | ↓ |
| Revisar documentos que ya existen (URL, archivos del repo, texto pegado) | **Auditar** | ↓ |
| No está claro | Preguntar: "¿Los escribimos de cero o revisamos los que ya tenés?" | |

Si hay documentos publicados, **auditar primero**. Reescribir de cero lo que ya está en el
aire pierde el historial de a qué se comprometió el usuario y desde cuándo.

---

## Modo Generar

### Paso 0 — Verificar vigencia (obligatorio)

Correr el protocolo de `references/normativa-ar.md` § Verificación obligatoria. Son tres
consultas. Si algo cambió, avisar antes de escribir. No saltear este paso por parecer lento:
el material se desactualizó dos veces en 18 meses.

### Paso 1 — Leer el producto

Antes de una línea de texto legal, leer:

1. **Esquema de la base** — qué tablas, qué columnas, cuáles son datos personales, cuáles
   son sensibles (art. 7: salud, origen racial, opiniones políticas, vida sexual).
2. **Código que recibe datos del usuario** — distinguir qué se **guarda** de qué solo **pasa**.
   Esa distinción suele ser el mejor párrafo del documento.
3. **Proveedores reales y su país** — hosting, base, mails, pagos, analítica, colas, IA.
   Buscar en `package.json`, variables de entorno, imports de SDKs, `vercel.json`.
   Alimenta la tabla de transferencia internacional.
4. **Píxeles y cookies en el HTML** — casi siempre hay un píxel de Meta, un GA o un
   Hotjar que nadie declaró.
5. **Flujo de baja** — ¿borra o desactiva? Determina qué puede prometer la política.

### Paso 2 — Preguntar lo que no se deduce

Preguntar todo junto, en una sola pasada. No de a una.

**Bloqueantes** (sin esto no se publica): razón social o nombre del titular · CUIT ·
domicilio · correo de contacto para ejercer derechos.

**Definen el contenido:** ¿el público es consumidor final o profesional? · ¿quién cobra —
el mismo titular u otra entidad? (Stripe no opera con cuentas argentinas: es habitual que
cobre una LLC del exterior, y hay que declararlo) · precio, renovación y cancelación ·
¿hay respaldos, cada cuánto, alguien probó restaurarlos? · ¿cuánto se conservan los datos
tras la baja? · ¿quién del equipo accede a producción?

Ante la duda sobre consumidor vs. profesional, **incluir la protección al consumidor igual**:
cuesta una sección y el riesgo de no tenerla es asimétrico (art. 36 de la Ley 24.240 es de
orden público, no se puede pactar en contra).

### Paso 3 — Escribir

Documentos y esqueletos en `references/plantillas.md`. Normalmente cuatro:

| Documento | Cuándo | Base normativa |
| --- | --- | --- |
| Términos y condiciones | siempre | Ley 24.240, CCyC arts. 1092-1122 |
| Política de privacidad | siempre que se traten datos personales | Ley 25.326 |
| Política de seguridad | recomendada; obligatoria de hecho si hay datos sensibles | Res. AAIP 47/2018 |
| Botón de arrepentimiento | si vende a consumidores a distancia | Disp. 954/2025 |
| Botón de baja de servicio | si hay suscripción o servicio continuo | Disp. 954/2025 |

**Formato:** adaptarse al stack donde corre. HTML suelto si hay landing estática (compartir
los estilos existentes), página en el router si es Next/Astro/Remix, Markdown si no hay web
todavía. No imponer HTML.

Cada documento lleva **fecha de versión** visible y el aviso de revisión profesional.

### Paso 4 — Cerrar

Antes de dar por terminado, correr el checklist de `references/normativa-ar.md` § Checklist
y reportar qué quedó pendiente fuera del texto (típicamente: inscripción en el Registro
Nacional de Bases de Datos, y enlazar los documentos en el pie del sitio **y de la app**).

---

## Modo Auditar

Entrada: URL del sitio, rutas de archivos, o texto pegado. **Más el código del producto** —
sin acceso al código se puede hacer la mitad del trabajo, y hay que decírselo al usuario.

Catálogo completo de hallazgos, cómo detectarlos y cómo redactarlos en `references/auditoria.md`.

### La distinción que ordena todo el informe

Separar siempre estas dos categorías, porque son problemas de naturaleza distinta:

- **🔴 CONTRADICCIÓN** — el documento afirma algo que el código desmiente. "Ciframos en
  reposo" sin cifrado; "no compartimos con terceros" con un píxel de Meta cargando; "eliminamos
  tu cuenta" cuando la baja solo pone `active = false`. Es una **afirmación falsa firmada por
  el usuario**, y es exactamente lo que le van a mostrar si hay un reclamo. Va primero, siempre.
- **🟠 INCUMPLIMIENTO** — falta algo que la norma exige. Sin CUIT, sin AAIP, sin botón de baja,
  plazos inventados.

Al primero le falta algo. El segundo dice algo que no es cierto, y es bastante peor.

### Las cuatro pasadas

1. **Qué falta** — contra el checklist de `references/normativa-ar.md`.
2. **Qué está escrito para otro país** — señal más común de política copiada, y la más
   fácil de detectar (`references/auditoria.md` § Señales de copia).
3. **Qué cita que ya no corresponde** — Disp. 11/2006 y 9/2008 (derogadas), Res. 424/2020
   (derogada en 2025), DNPDP (hoy AAIP), COPREC (disuelto en 2025).
4. **Qué promete que el producto no cumple** — comparar documento contra código. Esta es la
   razón de ser del modo. Ninguna otra herramienta lo hace.

### Salida

Informe ordenado por gravedad. Cada hallazgo con tres campos, siempre:

```
[🔴 CONTRADICCIÓN] Promete cifrado en reposo que no existe
  Dice el documento: "Todos los datos se almacenan cifrados en reposo" (privacidad.html:88)
  Dice el código:    Postgres sin pgcrypto; columnas en texto plano (schema.sql:12-40)
  Qué hacer:         Activar el cifrado, o cambiar la frase por lo que sí es cierto
                     ("el proveedor cifra los volúmenes; la aplicación no cifra por columna")
```

Terminado el informe, **ofrecer aplicar las correcciones** — nunca aplicarlas sin pedir.
Corregir un legal publicado cambia a qué se comprometió el usuario y eso lo decide él.

---

## Alcance y honestidad

- Cubre **Argentina**. El método sirve para cualquier país; lo que cambia es la tabla de
  normas. Para agregar otro, replicar `references/normativa-ar.md` con ese sufijo.
- Si el producto también tiene usuarios en la UE o Brasil, **decirlo y no fingir que se
  cubre**: hace falta sumar RGPD o LGPD, y eso es otro trabajo.
- **Nunca copiar texto de otra política.** Ni de competidores ni de plantillas: además del
  problema de derechos, describen otro producto.
- La skill produce un borrador informado y verificable. **No reemplaza a un abogado**, y
  eso tiene que quedar escrito en la salida al usuario y en el pie de cada documento.

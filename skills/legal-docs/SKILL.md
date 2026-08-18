---
name: legal-docs
description: This skill should be used when a SaaS or digital product needs its legal documents — terms of service, privacy policy, security policy, consumer buttons — written from scratch or audited against the real codebase. Covers Argentina (Ley 25.326, Ley 24.240, Disp. 954/2025), the European Union (GDPR), the United States (state privacy laws, call-recording consent, BIPA, FTC Section 5, TCPA), Brazil (LGPD) and the United Kingdom (UK GDPR + DUAA 2025), with verified normative tables; it names what it does not cover instead of faking it. Trigger phrases (Spanish) include "términos y condiciones", "política de privacidad", "política de seguridad", "botón de arrepentimiento", "botón de baja", "legales para mi SaaS", "auditá mis legales", "¿cumplo con el RGPD?", "Ley 25.326", "AAIP", "necesito los legales antes de lanzar". Trigger phrases (English) include "terms and conditions", "privacy policy", "GDPR compliance", "audit my legal docs", "do I need a DPO", "data processing agreement", "CCPA", "can I record this call", "BIPA", "LGPD", "ANPD", "ICO", "UK GDPR". Use it INSTEAD of generic templates: it deduces the document from the actual schema, providers and pixels, and in audit mode it compares what the published text promises against what the code does.
---

# Legales para productos digitales

Genera y audita documentos legales deduciéndolos del **código real**, no de una plantilla.
Cubre **Argentina, Unión Europea, Estados Unidos, Brasil y Reino Unido**, cada una con su
tabla normativa verificada contra fuente primaria.

**Por qué existe:** los generadores de legales rellenan un formulario y producen un texto
genérico que describe un producto que no es el tuyo. Esta skill hace lo contrario: lee el
esquema, los proveedores y los píxeles, y escribe lo que ese producto efectivamente hace. En
modo auditoría, compara lo que el documento promete contra lo que el código cumple.

Analogía: una plantilla es un traje comprado hecho. Le sobra tela de un lado y le falta del
otro, y desde lejos parece que te queda. Esta skill toma las medidas.

## Los seis no negociables

Si alguno se rompe, la salida no sirve. No son sugerencias.

1. **Determinar la jurisdicción antes que nada.** No se deduce del código: un producto en
   Vercel con la interfaz en español puede vender a treinta países. Preguntar → Paso 0.
   Escribir un documento argentino para un producto global lo deja desprotegido justo donde
   vende, y es el mismo error que una plantilla europea para un producto argentino.
2. **Verificar vigencia antes de escribir.** El modelo recuerda normativa vieja. Cada tabla
   normativa tiene su § Verificación obligatoria. Correrla, siempre.
3. **Leer el producto antes de redactar.** Esquema, código, proveedores, píxeles → Paso 2.
4. **No prometer lo que el producto no hace.** Sin respaldos verificados, el documento no dice
   que hay respaldos. Es la regla que más valor agrega y la que más se rompe.
5. **Frenar sin identificación del responsable.** Razón social o nombre, identificación fiscal
   y domicilio. Si el usuario no los tiene, se entrega el borrador marcado `[FALTA]` y **no se
   publica**.
6. **Decir el límite en la salida, no solo acá.** Todo documento generado cierra con el aviso
   de revisión profesional. Esto produce un borrador informado, no un documento validado por
   un abogado.

## Qué cubre y qué no

| Jurisdicción | Estado | Tabla |
| --- | --- | --- |
| 🇦🇷 **Argentina** | ✅ verificada 2026-08-17 | `references/normativa-ar.md` |
| 🇪🇺 **Unión Europea (RGPD)** | ✅ verificada 2026-08-18 | `references/normativa-eu.md` |
| 🇺🇸 **Estados Unidos** (leyes estatales, grabación de llamadas, BIPA, FTC §5, TCPA) | ✅ verificada 2026-08-18 | `references/normativa-us.md` |
| 🇧🇷 **Brasil (LGPD)** | ✅ verificada 2026-08-18 | `references/normativa-br.md` |
| 🇬🇧 **Reino Unido (UK GDPR)** | ✅ verificada 2026-08-18 | `references/normativa-uk.md` — solo las diferencias; leer junto con la europea |

**Lo no cubierto se nombra, no se improvisa.** El valor de esta skill es que cada norma está
verificada contra fuente primaria con su artículo y su plazo. Un régimen escrito de memoria no
tiene esa garantía y sería exactamente el problema que la skill combate. Si hace falta uno de
esos, decirlo y ofrecer hacer el trabajo de verificación primero.

## Elegir el modo

| El usuario quiere | Modo |
| --- | --- |
| Escribir los legales de un producto (nuevo o sin documentos) | **Generar** ↓ |
| Revisar documentos que ya existen (URL, archivos del repo, texto pegado) | **Auditar** ↓ |
| No está claro | Preguntar: "¿Los escribimos de cero o revisamos los que ya tenés?" |

Si hay documentos publicados, **auditar primero**. Reescribir de cero lo que ya está en el aire
pierde el historial de a qué se comprometió el usuario y desde cuándo.

---

## Modo Generar

### Paso 0 — Jurisdicción y vigencia (obligatorio)

**Una pregunta, y no se saltea:**

> ¿A quién le vendés este producto, y desde dónde operás vos?

Son dos cosas distintas y las dos importan. Quien opera desde Argentina queda alcanzado por la
Ley 25.326 aunque todos sus clientes estén afuera. Quien le vende a personas en la UE queda
alcanzado por el RGPD aunque no tenga un pie en Europa (art. 3.2: **ofrecer servicios alcanza**,
incluso gratis).

| Situación | Tablas a cargar |
| --- | --- |
| Opera y vende en Argentina | `normativa-ar.md` |
| Opera desde Argentina, vende a la UE | **las dos** — y se cumple la más exigente de cada fila |
| Opera desde Argentina, vende a EEUU | `normativa-ar.md` + `normativa-us.md` |
| Vende a Brasil | sumar `normativa-br.md` |
| Vende al Reino Unido | sumar `normativa-eu.md` **y** `normativa-uk.md` (la británica solo lista diferencias) |
| Vende a varios mercados | **todas las tablas que apliquen.** Ver § Cuando aplican varias |
| Sin ningún vínculo con Argentina ni la UE | **Frenar.** Decir qué haría falta y ofrecer verificarlo |

### Cuando aplican varias

Cada tabla cierra con una comparación que resuelve los conflictos fila por fila. La más útil
cuando aplican tres o más es § Diferencias con RGPD y con Argentina de `normativa-br.md`, que
pone los plazos de las cuatro juntos: **10 días corridos** (AR) · **15 días** (BR) · **1 mes**
(UE y UK).

Tres reglas que valen siempre:

1. **Gana la más exigente de cada fila.** Un producto argentino que vende a Europa responde
   accesos en 10 días corridos (plazo argentino) **y** notifica brechas en 72 horas
   (obligación europea).
2. **Los umbrales son por jurisdicción, no globales.** Un SaaS chico puede estar alcanzado de
   lleno por la ley argentina y por el RGPD, y quedar **exento** de casi todas las leyes
   estatales de EEUU. Decirlo es más honesto que fingir cumplimiento total.
3. **Si el producto graba llamadas y tiene un solo usuario en EEUU, se pide consentimiento de
   todos los participantes, siempre.** No hay forma operable de decidir según el estado en
   tiempo real, y en 11 estados grabar sin permiso puede ser delito penal.

**Después, la vigencia.** Correr § Verificación obligatoria de cada tabla cargada. Son pocas
consultas y evitan escribir contra una norma muerta: en 18 meses cambiaron tres cosas centrales
en Argentina, y el marco de transferencias UE-EEUU se cayó dos veces en diez años.

### Paso 1 — Leer el producto

Antes de una línea de texto legal:

1. **Esquema de la base** — qué tablas, qué columnas, cuáles son datos personales y cuáles
   caen en categorías especiales (art. 7 Ley 25.326 / art. 9 RGPD).
2. **Código que recibe datos del usuario** — distinguir qué se **guarda** de qué solo **pasa**.
   Esa distinción suele ser el mejor párrafo del documento.
3. **Proveedores reales y su país** — hosting, base, mails, pagos, analítica, colas, IA.
   Buscar en `package.json`, variables de entorno, imports de SDKs, `vercel.json`, y **también
   en el HTML**: las fuentes y los CDN externos son proveedores que nadie declara.
4. **Píxeles y cookies** — casi siempre hay un píxel de Meta, un GA o un Hotjar sin declarar.
5. **Flujo de baja** — ¿borra o desactiva? Determina qué puede prometer la política.
6. **De quién son los datos** — si el usuario carga datos de terceros (leads, pacientes,
   alumnos), el producto es **encargado** y el cliente es **responsable**. Esa distinción
   reordena el documento entero.

### Paso 2 — Preguntar lo que no se deduce

Todo junto, en una sola pasada. No de a una.

**Bloqueantes** (sin esto no se publica): razón social o nombre del titular · identificación
fiscal (CUIT o equivalente) · domicilio · correo de contacto para ejercer derechos.

**Definen el contenido:** ¿el público es consumidor o profesional? · ¿quién cobra — el mismo
titular u otra entidad? (habitual: una LLC del exterior porque el procesador de pagos no opera
con cuentas locales; hay que declararlo) · precio, renovación y cancelación · ¿hay respaldos,
cada cuánto, alguien probó restaurarlos? · ¿cuánto se conservan los datos tras la baja? ·
¿quién del equipo accede a producción?

Ante la duda sobre consumidor vs. profesional, **incluir la protección al consumidor igual**:
cuesta una sección y el riesgo de no tenerla es asimétrico.

### Paso 3 — Escribir

Esqueletos en `references/plantillas.md`.

| Documento | Cuándo |
| --- | --- |
| Términos y condiciones | siempre |
| Política de privacidad | siempre que se traten datos personales |
| Política de seguridad | recomendada; de hecho obligatoria si hay datos sensibles |
| Botón de arrepentimiento + botón de baja | Argentina, si vende a consumidores (Disp. 954/2025) |
| Política de cookies | si vende a la UE y usa cookies no esenciales |

**Formato:** adaptarse al stack. HTML suelto si hay landing estática (compartiendo sus
estilos), página del router si es Next/Astro/Remix, Markdown si no hay web todavía.

Cada documento lleva **fecha de versión** visible y el aviso de revisión profesional.

### Paso 4 — Cerrar

Correr el checklist de cada tabla cargada y reportar qué quedó pendiente **fuera del texto**:
típicamente el registro de bases de datos, implementar los botones, el DPA con los proveedores,
el circuito de brechas, y enlazar los documentos en el pie del sitio **y de la app**.

---

## Modo Auditar

Entrada: URL del sitio, rutas de archivos, o texto pegado. **Más el código del producto** — sin
acceso al código se puede hacer la mitad del trabajo, y hay que decírselo al usuario.

**Preguntar la jurisdicción primero, igual que al generar.** Auditar contra el checklist
equivocado produce un informe que señala faltantes reales pero omite los que más exponen.

Catálogo completo de hallazgos, cómo detectarlos y cómo redactarlos en `references/auditoria.md`.

### La distinción que ordena todo el informe

- **🔴 CONTRADICCIÓN** — el documento afirma algo que el código desmiente. "Ciframos en reposo"
  sin cifrado; "no compartimos con terceros" con un píxel cargando; "eliminamos tu cuenta"
  cuando la baja solo pone `active = false`. Es una **afirmación falsa firmada por el usuario**,
  y es exactamente lo que le van a mostrar si hay un reclamo. Va primero, siempre.
- **🟠 INCUMPLIMIENTO** — falta algo que la norma exige.

Al primero le falta algo. El segundo dice algo que no es cierto, y es bastante peor.

### Las cuatro pasadas

1. **Qué falta** — contra el checklist de la tabla que corresponda.
2. **Qué está escrito para otra jurisdicción** — la señal más común de documento copiado
   (`auditoria.md` § Señales de copia).
3. **Qué cita que ya no corresponde** — normas derogadas, organismos que cambiaron de nombre,
   y el caso difícil: la norma correcta en su versión anterior.
4. **Qué promete que el producto no cumple** — comparar documento contra código. Es la razón de
   ser del modo y lo que ninguna otra herramienta hace.

### Salida

Informe por gravedad. Cada hallazgo con tres campos, siempre:

```
[🔴 CONTRADICCIÓN] Promete cifrado en reposo que no existe
  Dice el documento: "Todos los datos se almacenan cifrados" (privacidad.html:88)
  Dice el código:    Postgres sin pgcrypto; columnas en texto plano (schema.sql:12-40)
  Qué hacer:         Activar el cifrado, o cambiar la frase por lo que sí es cierto
```

Terminado el informe, **ofrecer aplicar las correcciones** — nunca aplicarlas sin pedir.
Corregir un legal publicado cambia a qué se comprometió el usuario y eso lo decide él.

Y separar siempre lo que se arregla **en el texto** de lo que se arregla **en el producto**.
Si el documento promete un aislamiento que no existe, la solución no es suavizar la frase: la
promesa estaba bien, lo que faltaba era cumplirla.

---

## Honestidad

- **Nunca copiar texto de otra política.** Ni de competidores ni de plantillas: además del
  problema de derechos, describen otro producto.
- **Nunca escribir contra un régimen no verificado.** Si el producto necesita una jurisdicción
  que la skill no cubre, decirlo y ofrecer hacer el trabajo de verificación primero.
- La skill produce un borrador informado y verificable. **No reemplaza a un abogado**, y eso
  tiene que quedar escrito en la salida al usuario y en el pie de cada documento.
- Productos que necesitan revisión profesional sí o sí: los que **graban o transcriben
  llamadas**, los que **identifican hablantes por voz** (riesgo BIPA, con acción privada y
  daños por persona), los que **analizan personas con IA** para decisiones que las afectan, y
  los que tratan **datos de salud, de menores o financieros**. En estos casos el borrador sirve
  para llegar preparado a la consulta, no para reemplazarla.

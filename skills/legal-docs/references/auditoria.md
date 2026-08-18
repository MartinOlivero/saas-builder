# Catálogo de auditoría

Cómo detectar cada hallazgo y cómo redactarlo. Dos familias:
**CONTRADICCIÓN** (el documento miente respecto del código) e **INCUMPLIMIENTO** (falta algo).

---

## Cómo correr la auditoría

```
1. Obtener los documentos     → WebFetch de la URL, o Read de los archivos del repo
2. Obtener el código          → esquema, package.json, .env.example, HTML, flujo de baja
3. Pasada A: señales de copia → grep sobre el texto legal (tabla § Señales de copia)
4. Pasada B: normas viejas    → grep de normas derogadas (tabla § Normas derogadas)
5. Pasada C: qué falta        → checklist de normativa-ar.md
6. Pasada D: contradicciones  → comparar afirmaciones contra el código (§ Contradicciones)
7. Ordenar por gravedad y escribir el informe
```

**Sin acceso al código, la pasada D no se puede hacer.** Decírselo al usuario explícitamente:
es la mitad del valor de la auditoría y la única parte que ninguna otra herramienta hace.

---

## Señales de copia — grep sobre el texto legal

Cada acierto es un **🟠 INCUMPLIMIENTO** de gravedad media, salvo que se indique otra cosa.
Lo grave no es la palabra: es que **el documento describe otro régimen legal**, y por lo tanto
probablemente también describa otro producto.

```bash
grep -inE "rgpd|gdpr|dpo|delegado de protecci|portabilidad|derecho al olvido|interés legítimo" docs/
grep -inE "ccpa|do not sell|residentes de california|california consumer" docs/
grep -inE "lgpd|anpd|titular dos dados|encarregado" docs/
grep -inE "dnpdp|disposición 11/2006|disposición 9/2008|424/2020|coprec" docs/
grep -inE "a la brevedad|plazo razonable|lo antes posible" docs/
grep -inE "72 horas|setenta y dos horas" docs/
```

| Señal en el texto | Qué delata | Gravedad |
| --- | --- | --- |
| "RGPD", "GDPR", "DPO", "delegado de protección de datos", "interés legítimo", "derecho de portabilidad", "derecho al olvido" | Copiada de Europa. **Ninguna de esas figuras existe en la Ley 25.326** | 🟠 media |
| "No vendemos tu información personal", "Do Not Sell My Info", "residentes de California" | Plantilla de CCPA | 🟠 media |
| "LGPD", "ANPD", "titular dos dados", "encarregado" | Copiada de Brasil | 🟠 media |
| "a la brevedad", "en un plazo razonable" para responder pedidos | No conoce los plazos reales: **10 días corridos** y **5 días hábiles** | 🟠 media |
| "notificaremos dentro de las 72 horas" | Plazo del RGPD. Argentina **no obliga** a notificar brechas: el documento se autoimpone una obligación que después no cumple | 🔴 **alta** |
| No menciona a la **AAIP** ni cómo reclamar | Falta el órgano de control argentino | 🟠 media |
| No dice quién es el responsable con **razón social, CUIT y domicilio** | Lo primero que se mira y lo más común que falte | 🔴 **alta** |
| Jurisdicción en los tribunales de la ciudad del proveedor | Contradice el art. 36 de la Ley 24.240, que es de orden público → **la cláusula se tiene por no escrita** | 🔴 **alta** |
| Cláusula que excluye toda responsabilidad por daños | Art. 37 LDC: se tiene por no escrita. Da falsa seguridad | 🟠 media |
| Cobra online y no hay **botón de arrepentimiento** | Incumple la Disp. 954/2025 | 🔴 **alta** |
| Suscripción sin **botón de baja de servicio** | Incumple la Disp. 954/2025. **Es el hallazgo más frecuente en 2026**: la obligación es nueva y casi nadie la implementó | 🔴 **alta** |
| No dice dónde están alojados los datos | Casi siempre están en EEUU, que **no** es país adecuado: falta declarar la transferencia | 🔴 **alta** |
| Sin fecha de versión | No se puede saber a qué se comprometió y desde cuándo | 🟡 baja |
| Traducción literal del inglés ("nosotros valoramos su privacidad", "usted acepta por la presente") | Traducido de plantilla; suele venir acompañado de todo lo demás | 🟡 baja |

---

## Normas derogadas o inexistentes

Citar una norma muerta es prueba de que el documento no se revisó. Cada una es
🟠 INCUMPLIMIENTO, salvo las dos primeras que suelen implicar faltantes reales.

| Si el documento cita… | Estado | Qué corresponde |
| --- | --- | --- |
| **Resolución 424/2020** | **Derogada** por Disp. 954/2025, art. 10 | Disp. 954/2025 — y verificar que además exista el botón de baja |
| **Resolución 316/2018** | **Derogada** por Disp. 954/2025, art. 10 | Disp. 954/2025 |
| **COPREC** / Ley 26.993 | **Disuelto** por Decreto 55/2025 | Ventanilla Única Federal |
| **Disposiciones 11/2006 y 9/2008** | Derogadas | Res. AAIP 47/2018 |
| **Res. AAIP 240/2022** (sanciones) | Derogada | Res. AAIP 126/2024 |
| **DNPDP** | Cambió de nombre y de organismo | **AAIP** |
| "Directiva 95/46/CE" | Derogada en Europa en 2018 | No corresponde citarla en Argentina |

### Caso aparte: la norma correcta, pero en su versión anterior

Distinto de citar una norma inventada, y bastante más difícil de ver: el documento cita el
régimen que corresponde, pero congelado en la versión con la que se escribió. La redacción
suena bien y el autor sabía lo que hacía — la norma se movió después.

Se detecta comparando **la exigencia que el texto describe** contra la vigente, no el número:

| El texto describe | Versión | Hoy exige |
| --- | --- | --- |
| Botón de arrepentimiento "de acceso fácil y directo desde la home, destacado en visibilidad y tamaño" | Res. 424/2020 | **"a simple vista, en lugar destacado y en el primer acceso"** (Disp. 954/2025). Un link en el pie cumplía antes y **ya no**: "primer acceso" no se satisface con algo que exige scrollear |
| Solo botón de arrepentimiento | Res. 424/2020 | **También botón de baja de servicio** (Disp. 954/2025, art. 4) |
| Reclamos ante el COPREC | Ley 26.993 | **Ventanilla Única Federal** (Decreto 55/2025) |

Señal de alerta en el código: un **comentario que cita textualmente el requisito viejo**
para justificar dónde se puso algo. Es la prueba de que se implementó contra la norma
anterior, y de que nadie volvió a mirarla desde entonces.

```bash
grep -rniE "424/2020|316/2018|coprec|resoluci[oó]n 424" --include="*.html" --include="*.tsx" --include="*.js" .
```

Redactarlo sin condescendencia: **no es un error de quien lo escribió**, es normativa que
cambió. Pero hay que corregirlo igual.

---

## Antes de comparar: el repo no es el sistema

Dos formas de equivocarse leyendo código, las dos comprobadas en una auditoría real. Ambas
producen hallazgos **falsos**, que es peor que no encontrar nada: hacen perder tiempo y
queman la credibilidad del informe.

### 1. Las migraciones son historial, no estado

`migrations/*.sql` acumulado dice lo que **alguna vez existió**, no lo que existe hoy. Una
migración posterior puede haber revertido a la anterior, y si leés la que crea sin leer la
que borra, reportás como vigente algo que se eliminó.

> Caso real: se reportaron 7 políticas RLS peligrosas leídas de `..._rls-policies.sql`.
> Dos archivos más abajo, `..._cierra-acceso-anonimo.sql` las dropeaba a todas. El hallazgo
> era correcto para agosto y falso para el presente.

**Cómo evitarlo:**
- Consultá el **estado**, no el historial: `SELECT * FROM pg_policies`,
  `information_schema.columns`, `\d+ tabla`.
- Si no tenés acceso a la base, leé las migraciones **en orden cronológico** y aplicá
  mentalmente los `DROP` y `ALTER`. Nunca hagas `grep` sobre todo el directorio junto.
- Barato y efectivo: `grep -l "drop policy\|drop table\|drop column" migrations/*.sql`
  antes de afirmar que algo existe.

### 2. El cifrado puede no estar en el esquema

Buscar `pgcrypto`, `bytea` o `encrypt` en el SQL encuentra el cifrado **de base de datos**.
No encuentra el cifrado **de aplicación**, que es igual de válido y bastante común: la
columna es `text` y guarda un ciphertext que la app cifra y descifra.

> Caso real: se reportaron tokens OAuth "en texto plano" porque la columna era `text`.
> Estaban cifrados con AES-256-GCM y una clave del gestor de secretos, en el código de una
> función de servidor. La columna `text` guardaba `enc1:<iv>.<ct>`.

**Cómo evitarlo** — buscar también en el código, no solo en el esquema:

```bash
grep -rniE "createCipheriv|AES-256|aes-256-gcm|encrypt\(|decrypt\(|ENCRYPTION_KEY|crypto\.subtle" \
  --include="*.ts" --include="*.js" --include="*.py" .
```

Y si una columna guarda algo que parece un secreto, **mirá un valor** (o el formato que
escribe el código): un prefijo tipo `enc1:`, `v1:` o una cadena base64 sin estructura suele
ser ciphertext, no el dato.

### La regla general

Un hallazgo de la pasada D **se afirma contra el sistema, no contra el repositorio**. Si no
podés consultar el sistema, decilo en el informe: "verificado contra el código, no contra la
base". Es una frase que cuesta nada y evita que alguien salga a arreglar un problema que no
tiene.

## Caso especial: verificar una afirmación de aislamiento

Casi toda política de seguridad de un SaaS multi-tenant dice alguna variante de **"cada
organización ve solo sus datos"** o **"cada usuario ve solo lo suyo"**. Es la afirmación más
fácil de escribir y la más difícil de verificar, porque *parece* comprobada apenas encontrás
RLS activo. No alcanza.

Cuatro chequeos, en orden. Los cuatro tienen que dar bien para que la frase sea cierta:

**1. ¿Todas las tablas con datos tienen RLS activo?**
```sql
SELECT tablename FROM pg_tables WHERE schemaname='public'
  AND tablename NOT IN (SELECT tablename FROM pg_tables WHERE rowsecurity);
```
Una tabla sin RLS **pero con grants a `anon`/`authenticated`** es lectura y escritura abierta.
Una tabla de logs o debug suele ser la olvidada, y suele guardar payloads crudos.

**2. ¿Hay políticas otorgadas al rol anónimo?**
```sql
SELECT tablename, policyname FROM pg_policies WHERE 'anon' = ANY(roles);
```
Debería dar cero. La clave anónima viaja en el bundle del navegador: es pública por diseño.

**3. ¿Hay políticas con condición trivialmente verdadera?**
```sql
SELECT tablename, policyname, roles FROM pg_policies
 WHERE qual = 'true' OR with_check = 'true';
```
Aceptable solo para un rol de administración server-side. Para un rol de usuario, anula el
aislamiento.

**4. ⚠️ ¿Las políticas de UPDATE permiten cambiar columnas de privilegio?**

Este es el que se pasa por alto, y el más grave. **RLS filtra filas, no columnas.** Una
política que parece impecable:

```sql
CREATE POLICY self_update ON profiles FOR UPDATE USING (id = auth.uid());
```

deja que el usuario edite **cualquier columna de su propia fila** — incluidas `role`,
`org_id`, `plan` o `is_admin`. O sea: se asciende a administrador y se muda a la organización
que quiera, con un PATCH a su propio perfil.

> Caso real: en un CRM multi-tenant, un usuario recién registrado (que entra como rol básico
> y sin organización) podía hacer PATCH sobre su perfil, ponerse `role='super_admin'` y el
> `org_id` de otra empresa, y quedar adentro con permisos totales. Verificado con un usuario
> de prueba: HTTP 200, aplicado. **Mientras eso existió, la frase "separación por organización"
> del documento era falsa para cualquiera que se registrara.**

Cómo detectarlo:
```bash
# ¿Hay policies de UPDATE sobre tablas que tengan columnas de privilegio?
grep -rniE "for update" migrations/*.sql
grep -rniE "\b(role|rol|org_id|tenant_id|plan|is_admin|is_superuser)\b" migrations/*.sql
```
Si las dos listas se cruzan en una tabla, hay que ver cómo se impide el cambio de esa columna.
Las defensas válidas son un **trigger `BEFORE UPDATE`** que rechace el cambio, una vista con
`WITH CHECK OPTION`, o revocar el `UPDATE` de esa columna (`REVOKE UPDATE (role) ON ...`).
Que la interfaz no muestre el campo **no es una defensa**: la API acepta el PATCH igual.

### Cómo redactarlo

Si el aislamiento falla, es 🔴 **CONTRADICCIÓN**, no incumplimiento — el documento afirma una
protección que no existe. Y va con una nota que el usuario necesita leer: **esto se arregla en
el producto antes que en el texto.** Cambiar la frase del documento para que deje de mentir es
la solución equivocada: la promesa estaba bien, lo que faltaba era cumplirla.

Si el aislamiento está bien, decilo en el informe con los números —cuántas tablas con RLS,
cuántas políticas anónimas, si las columnas de privilegio están protegidas—, porque es la
afirmación que un cliente técnico va a querer ver respaldada.

## Contradicciones documento ↔ código

**La razón de ser del modo auditoría.** Cada una de estas es una afirmación falsa firmada por
el usuario. Todas son 🔴 y van al principio del informe.

| El documento afirma | Cómo verificarlo en el código | Es contradicción si… |
| --- | --- | --- |
| "Ciframos los datos en reposo" | Buscar `pgcrypto`, `encrypt`, columnas `bytea`, KMS, config del proveedor | El esquema guarda texto plano y nadie activó cifrado a nivel volumen. **Cuidado:** "el proveedor cifra el disco" ≠ "la aplicación cifra el dato". Precisar cuál |
| "Eliminamos tus datos al darte de baja" | Leer el endpoint de baja / delete account | La baja hace `UPDATE ... SET active=false` o `deleted_at=now()` y no borra nada |
| "No compartimos tus datos con terceros" | `grep -rE "facebook|fbq|gtag|googletagmanager|hotjar|clarity|mixpanel|posthog|segment" --include="*.html" --include="*.tsx" --include="*.js"` | Hay un píxel o una analítica cargando. **El más frecuente de todos** |
| Tabla con N proveedores | Contar los reales: `package.json`, `.env.example`, imports de SDKs, `vercel.json`, webhooks | Los del código son más que los declarados. Casi siempre lo son |
| Tabla de proveedores sin fuentes ni CDN | `grep -rhoE "https?://[a-zA-Z0-9.-]+" --include="*.html"` sobre **todos** los HTML | Hay `fonts.googleapis.com`, `cdn.jsdelivr.net`, `unpkg.com` o similar. **Cada uno recibe la IP del visitante y casi ninguno se declara.** Google Fonts es el caso típico: aparece hasta en la propia página de la política. Arreglo más simple que declararlo: descargar la fuente y servirla desde el dominio propio |
| "Realizamos respaldos periódicos" | Buscar cron de backup, config del proveedor, script de restore | No hay nada, o hay respaldo pero nadie probó restaurarlo (entonces el documento promete de más) |
| "Disponibilidad del 99,9%" | Buscar monitoreo, statuspage, SLO | No hay nada que lo mida. Un SLA sin medición es una obligación contractual a ciegas |
| "Solo personal autorizado accede" | Roles en la base, RLS, quién tiene credenciales de producción | Todo el equipo comparte la misma credencial de admin |
| "Conservamos los datos por X tiempo" | Buscar job de retención o purga | No existe purga: los datos se conservan indefinidamente |
| "Usamos autenticación de dos factores" | Buscar TOTP, WebAuthn, el flujo de login | No está implementado |
| "Los datos se alojan en Argentina" | Región del hosting y de la base | Están en `us-east-1`, `iad1`, `sfo1`. Muy frecuente y **agrava** el faltante de transferencia internacional |
| "Cumplimos con el RGPD" | — | Casi siempre es falso y además innecesario. Si no hay usuarios en la UE, sobra; si los hay, hay que cumplirlo de verdad |

### Al revés: lo que el producto hace y el documento no declara

Igual de importante y se pasa por alto. Es 🟠 INCUMPLIMIENTO por omisión.

- Proveedor de IA (OpenAI, Anthropic) recibiendo contenido del usuario, sin declarar.
- Logs que guardan IP, user-agent o payloads con datos personales, sin mención.
- Emails transaccionales por un tercero (Resend, SendGrid) que ve la dirección del usuario.
- Webhooks que salen hacia servicios externos.
- Datos sensibles del art. 7 en el esquema (salud, orientación, opiniones) sin el
  tratamiento reforzado que exige la ley. **Esto es 🔴, no 🟠.**

---

## Formato del informe

Ordenar por gravedad: primero todas las 🔴, después las 🟠, después las 🟡. Dentro de cada
grupo, primero las contradicciones.

Encabezar con un resumen de una línea y el conteo. Nada de introducción larga.

```markdown
# Auditoría de legales — [producto] — [fecha]

3 contradicciones con el código, 5 incumplimientos, 2 observaciones menores.
Documentos revisados: privacidad.html, terminos.html · Código: sí

---

## 🔴 Contradicciones — el documento dice algo que el código desmiente

### 1. Promete que no comparte datos con terceros, pero carga el píxel de Meta
- **Dice el documento:** "No compartimos tu información con terceros bajo ninguna
  circunstancia" — privacidad.html:64
- **Dice el código:** `fbq('init', ...)` en index.html:212; también GA4 en layout.tsx:31
- **Por qué importa:** el píxel envía identificadores del visitante a Meta (EEUU). Es una
  cesión no declarada (art. 11) y además una transferencia internacional sin base legal
  declarada (art. 12).
- **Qué hacer:** o se saca el píxel, o se declara — tabla de proveedores, finalidad
  publicitaria y consentimiento para la transferencia.

---

## 🟠 Incumplimientos — falta algo que la norma exige

### 4. No hay botón de baja de servicio
- **Falta:** el producto cobra suscripción mensual y no expone el "BOTÓN DE BAJA DE SERVICIO".
- **Norma:** Disposición 954/2025, art. 4.
- **Qué hacer:** link visible en el primer acceso de la home, sin login previo, que dispare
  la baja y devuelva un código de identificación dentro de las 24 horas.
```

**Al cerrar:** ofrecer aplicar las correcciones, sin aplicarlas. Si el usuario acepta,
separar lo que se arregla **en el texto** (redacción, plazos, normas) de lo que se arregla
**en el producto** (implementar el botón, activar el cifrado, borrar de verdad) — porque
esto último no lo resuelve reescribiendo un párrafo.

Y recordar el límite: esta auditoría detecta contradicciones verificables y faltantes contra
un checklist. **No es un dictamen legal.**

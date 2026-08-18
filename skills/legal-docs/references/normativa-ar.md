# Normativa argentina verificada

> **Verificado contra fuente primaria el 2026-08-17.** Cada fila salió de InfoLeg, el
> Boletín Oficial o argentina.gob.ar, no de memoria. Antes de usar este archivo en otra
> fecha, correr § Verificación obligatoria: en 2025 cambiaron tres cosas centrales.

---

## Verificación obligatoria (correr en cada uso, antes de escribir)

Tres consultas. Toman un minuto y evitan escribir un documento que cita una norma derogada.

**1. ¿Sigue vigente la Ley 25.326?**
Al 2026-08-17 **sí**. Hay tres proyectos de reforma en el Congreso: Pablo Carro, Martín
Doñate, y el **1751-D-2026 de Martín Yeza** (presentado el 22/04/2026, 72 artículos,
**derogaría la ley entera**; incorpora responsabilidad proactiva, privacidad por diseño,
portabilidad, oposición a decisiones automatizadas, notificación de incidentes y un sandbox
regulatorio para IA). Ninguno estaba sancionado a esa fecha.
→ Si alguno se sancionó, **todo este archivo queda viejo**. Avisar al usuario y frenar.

**2. ¿Cambió la lista de países con nivel adecuado?**
Se actualiza por resolución de la AAIP. Verificar en
`argentina.gob.ar/transferencias-internacionales`.

**3. ¿Sigue vigente la Disposición 954/2025 (los dos botones)?**
Es la norma más nueva y más volátil del conjunto: en 5 años el botón de arrepentimiento
cambió de norma tres veces (Res. 316/2018 → Res. 424/2020 → Disp. 954/2025).

**Fuentes primarias:**

| Norma | URL |
| --- | --- |
| Ley 25.326 | `servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm` |
| Res. AAIP 47/2018 (seguridad) | `argentina.gob.ar/normativa/nacional/resolución-47-2018-312662/texto` |
| Res. AAIP 126/2024 (sanciones) | `servicios.infoleg.gob.ar/infolegInternet/anexos/395000-399999/399750/texact.htm` |
| Disp. 954/2025 (botones) | `boletinoficial.gob.ar/detalleAviso/primera/330827/20250904` |
| Transferencia internacional | `argentina.gob.ar/transferencias-internacionales` |
| Obligaciones del responsable | `argentina.gob.ar/aaip/datospersonales/responsables/obligaciones` |

---

## ⚠️ Cambios recientes que casi ninguna política refleja

Estos tres son de 2024-2025 y son el mejor detector de documento desactualizado. Un
documento argentino escrito antes de 2025 y no revisado los tiene todos mal.

| Cambio | Antes | Ahora |
| --- | --- | --- |
| **Botones de consumo** | Res. 424/2020 (arrepentimiento) | **Derogada.** Rige la **Disp. 954/2025**, que además suma el **BOTÓN DE BAJA DE SERVICIO** |
| **Régimen sancionatorio** | Res. AAIP 240/2022 | **Derogada.** Rige la **Res. AAIP 126/2024** |
| **Reclamos de consumo** | COPREC (Ley 26.993) | **Disuelto** por Decreto 55/2025. Hoy: **Ventanilla Única Federal** |

Citar COPREC o la Res. 424/2020 en un documento de 2026 es prueba de que nadie lo revisó.

---

## Protección de datos — Ley 25.326 (vigente)

| Qué | Artículo | Detalle |
| --- | --- | --- |
| Información al titular al recolectar | 6 | Finalidad, destinatarios, identidad del responsable, si es obligatorio responder, y los derechos de acceso / rectificación / supresión |
| Datos sensibles | 7 | Salud, origen racial o étnico, opiniones políticas, convicciones religiosas, vida sexual. Nadie está obligado a darlos; requieren interés general o finalidad estadística disociada |
| Seguridad de los datos | 9 | Medidas técnicas y organizativas. **Inc. 2: prohibido registrar datos en bases que no reúnan condiciones de seguridad** |
| Deber de confidencialidad | 10 | Secreto profesional que **subsiste después de terminada la relación** |
| Cesión | 11 | Requiere consentimiento previo del titular |
| Transferencia internacional | 12 | Prohibida a países sin nivel adecuado, **salvo consentimiento expreso** u otro mecanismo (ver abajo) |
| Derecho de acceso | 14.2 | **10 días corridos** para responder |
| Gratuidad del acceso | 14.3 | Gratis a intervalos **no menores a 6 meses**, salvo interés legítimo acreditado |
| Rectificación / supresión | 16.2 | **5 días hábiles**. Notificar al cesionario dentro del **5º día hábil** (16.4) |
| Gratuidad de la rectificación | 19 | Sin cargo para el titular |
| Registro de bases | 21 y **24** | El 24 obliga a **los privados que formen bases que no sean de uso exclusivamente personal** |
| Tratamiento por cuenta de terceros | 25 | El encargado solo puede usar los datos para el servicio; al terminar, **destruirlos** (o conservarlos hasta 2 años con autorización) |

**Dos particularidades que sorprenden a quien viene del RGPD:**

- **Protege también a las personas jurídicas** (arts. 1 y 2: "persona física o de existencia
  ideal"). Los datos de empresas clientes **también** están protegidos. En el RGPD no.
- **Excepción de fuente de acceso público irrestricto** (art. 5.2.a): si el dato se obtuvo de
  una fuente abierta a cualquiera, no hace falta consentimiento. Es lo que habilita usar
  padrones y registros públicos.

**Figuras del RGPD que NO existen acá** — si aparecen en un documento, está copiado:
portabilidad, derecho al olvido, DPO / delegado de protección de datos, interés legítimo
como base de licitud, evaluación de impacto obligatoria, notificación de brechas en 72 horas.

### Brechas de seguridad: no hay obligación legal de notificar

La Ley 25.326 **no obliga** a notificar incidentes de seguridad ni a la AAIP ni a los
titulares. La Res. 47/2018 lo trata como medida recomendada, y el proyecto Yeza lo
incorporaría como obligación.

**Consecuencia práctica:** una plantilla GDPR que promete "te notificaremos dentro de las
72 horas" está creando una obligación contractual que la ley no impone. Si después no se
cumple, es un incumplimiento del propio contrato. Redactar el compromiso que el equipo
pueda sostener ("te avisaremos sin demora indebida"), o no prometer plazo.

---

## Seguridad — Resolución AAIP 47/2018

Aprueba las *Medidas de seguridad recomendadas para el tratamiento y conservación de datos
personales*. **Derogó las Disposiciones 11/2006 y 9/2008.**

Sirve como **esqueleto de la política de seguridad**, con estos ocho títulos:

| # | Título | Qué cubre |
| --- | --- | --- |
| A | Recolección de datos | Completitud e integridad, minimizar errores, confidencialidad en la recolección |
| B | Control de acceso | Autenticación, segregación de roles, protección de identidad |
| C | Control de cambios | Identificar y autorizar a quien modifica entornos con datos personales |
| D | Respaldo y recuperación | Procesos de respaldo para recuperar ante incidentes |
| E | Gestión de vulnerabilidades | Revisión continua, control de integridad y trazabilidad |
| F | Destrucción de la información | Borrado seguro con control eficaz |
| G | Incidentes de seguridad | Detección, evaluación, contención y respuesta |
| H | Entornos de desarrollo | Separación de entornos, propios o de terceros |

Escribir estos ocho títulos con lo que el producto **realmente** hace. Si no hay gestión de
vulnerabilidades, el título va igual y dice qué se hace en su lugar — o pasa al apartado
"Lo que esta política no promete".

---

## Transferencia internacional — Disp. DNPDP 60/2016 + Res. AAIP 34/2019

**Países con nivel adecuado** (lista oficial vigente):

Estados miembros de la **Unión Europea y del Espacio Económico Europeo** · **Reino Unido de
Gran Bretaña e Irlanda del Norte** · **Confederación Suiza** · **Guernsey** · **Jersey** ·
**Isla de Man** · **Islas Feroe** · **Canadá** (solo sector privado) · **Principado de
Andorra** · **Nueva Zelanda** · **República Oriental del Uruguay** · **Estado de Israel**
(solo datos con tratamiento automatizado).

> ⚠️ **Estados Unidos NO está en la lista.** Y ahí viven casi todos los proveedores de un
> SaaS chico: Vercel, Supabase, Resend, Stripe, AWS, OpenAI, Anthropic, Cloudflare.
> **Esto le aplica a casi todos los proyectos.** Las skills internacionales no lo ven porque
> para el RGPD hay otros mecanismos.

**Mecanismos para transferir a países no adecuados:**

1. **Consentimiento expreso del titular** — el más simple, y es el que la política puede
   recabar directamente. Para un SaaS chico, casi siempre es la vía.
2. Excepciones del art. 12 de la Ley 25.326.
3. **Cláusulas contractuales modelo** — Disp. 60/2016, actualizadas por la **Res. AAIP
   198/2023** (modelo de la Red Iberoamericana). Hay modelos para cesión, para prestación
   de servicios y entre responsables.
4. **Contratos personalizados** — requieren aprobación de la AAIP.
5. **Normas Corporativas Vinculantes** (Res. AAIP 159/2018) — para grupos económicos.

**En el documento:** tabla de proveedores con nombre, para qué se usa, y país. Después, la
base legal de la transferencia. Sin la tabla, la declaración es genérica y no sirve.

---

## Sanciones — Resolución AAIP 126/2024 (vigente desde 01/06/2024)

Deroga la Disp. DNPDP 7/05 y las Res. AAIP 12/18, 240/22, 243/19 y 244/22.

| Gravedad | Multa | Ejemplos |
| --- | --- | --- |
| Leve | $1.000 a $80.000 | No inscribirse en el Registro Nacional de Bases de Datos; no informar modificaciones; incumplir el principio de gratuidad |
| Grave | $80.001 a $90.000 | Tratamiento sin legitimación; recolección sin consentimiento; incumplir derechos de acceso o rectificación; contactar con fines publicitarios a inscriptos en el Registro "No Llame" (Ley 26.951) |
| Muy grave | $90.001 a $100.000 | Fraude en la recolección; tratamiento ilegítimo; obstruir inspecciones; **transferencias internacionales sin protección adecuada** |

**El tope real no son $100.000.** En caso de acumulación de conductas sancionables, el
máximo es **la escala que corresponda multiplicada por 500**. Además de multa, para
infracciones muy graves puede haber apercibimientos, suspensión de 31 a 365 días, y clausura
o cancelación de la base de datos — que para un SaaS es el fin del producto.

**Atenúan:** cooperar con la AAIP y demostrar medidas correctivas implementadas. El pago
voluntario reduce la graduación. Tener los documentos en orden y una política de seguridad
real no es solo evitar la multa: es el atenuante.

---

## Consumidor — Ley 24.240, CCyC y Disposición 954/2025

| Qué | Norma | Detalle |
| --- | --- | --- |
| Deber de información | LDC 4 | Cierta, clara y detallada sobre características esenciales y condiciones de comercialización |
| Revocación | LDC 34 / **CCyC 1110** | **10 días corridos** desde la celebración o la entrega, lo que ocurra último, sin costo ni responsabilidad. Si vence en día inhábil, se prorroga al primer hábil siguiente. **Es irrenunciable** |
| Deber de informar la revocación | **CCyC 1111** | Hay que informar el derecho a revocar **en forma clara y oportuna**. No alcanza con tenerlo en el contrato |
| Jurisdicción | LDC 36 | **El juez del domicilio del consumidor**. Es de **orden público**: una cláusula que fije otro tribunal se tiene por no escrita |
| Cláusulas abusivas | LDC 37 / CCyC 1117-1122 | Se **tienen por no escritas** las que desnaturalizan obligaciones o limitan responsabilidad por daños |
| Contratos a distancia | CCyC 1105 | Los celebrados sin presencia física simultánea — todo SaaS |
| Reclamos | Decreto 55/2025 | COPREC **disuelto**. Hoy la vía es la **Ventanilla Única Federal** |

### Los dos botones — Disposición 954/2025

Deroga expresamente la Res. 316/2018 y la **Res. 424/2020**, y consolida ambas obligaciones
en un texto único. **Plazo de adecuación: 60 días corridos** desde su entrada en vigencia.

| | BOTÓN DE ARREPENTIMIENTO | BOTÓN DE BAJA DE SERVICIO |
| --- | --- | --- |
| Para qué | Revocar la aceptación dentro de los 10 días corridos | Cancelar un servicio en curso |
| Quién | Quien comercialice bienes o servicios a distancia | Quien preste servicios de forma continua |
| Ubicación | **"A simple vista, en lugar destacado y en el primer acceso"** | Igual |
| Registro previo | **Prohibido exigirlo**, ni ningún otro trámite | Igual |
| Respuesta | Informar el **código de identificación dentro de las 24 horas** | Igual |

**Abrir la página y mirarla.** "Destacado en visibilidad y tamaño" es una propiedad de lo
**renderizado**, y ningún grep la ve. Caso real: el botón existía, decía lo correcto y estaba
donde correspondía, pero una regla CSS le ganaba en especificidad y le pisaba el color del
texto — quedaba verde oscuro sobre verde, casi ilegible. Cumplía en el HTML e incumplía en
la pantalla. Levantar el sitio y sacar una captura cuesta un minuto.

**Errores frecuentes de implementación:** ponerlo detrás del login (viola "sin registro
previo"); ponerlo solo en el pie con letra chica (viola "lugar destacado y primer acceso");
que sea un `mailto:` sin acuse (no genera código de identificación en 24 horas); tener el de
arrepentimiento y no el de baja, siendo un producto por suscripción.

**Ojo con el alcance:** un profesional que contrata una herramienta **para su actividad** no
es consumidor final, y en rigor estas obligaciones no le aplican. Pero la frontera es difusa
—un monotributista que usa un SaaS de facturación puede argumentar consumo— y el riesgo es
asimétrico. Ante la duda, incluirlos.

---

## Otras normas que suelen aplicar

| Tema | Norma | Cuándo importa |
| --- | --- | --- |
| Registro Nacional de Bases de Datos | Ley 25.326 art. 24 | **Casi siempre.** Exento solo el uso exclusivamente personal o doméstico. Trámite online ante la AAIP, requiere clave fiscal nivel 2+ |
| Registro "No Llame" | Ley 26.951 | Si hay contacto telefónico con fines de publicidad u oferta |
| Facturación | RG de ARCA (ex AFIP) | Factura electrónica obligatoria desde el primer día. Monotributo: tipo C, sin discriminar IVA. Tipo E para exportación de servicios |
| Menores de edad | CCyC art. 26 (autonomía progresiva) | La Ley 25.326 **no fija una edad**. El proyecto de reforma propone 16 años. Si el producto puede tener menores, tratarlo con criterio y consultar — no inventar una edad |
| Cookies | — | **Argentina no tiene norma específica** de cookies ni ePrivacy. Si la cookie trata datos personales, se aplica la Ley 25.326: informar y obtener consentimiento. Un banner tipo RGPD no es obligatorio, pero informarlo en la política sí |

---

## Checklist de cumplimiento

Correr al cerrar el modo Generar y como primera pasada del modo Auditar.

**En los documentos**
- [ ] Identificación completa del responsable: razón social o nombre, **CUIT**, domicilio
- [ ] Correo de contacto para ejercer derechos
- [ ] Finalidad del tratamiento, destinatarios y derechos del titular (art. 6)
- [ ] Plazos correctos: **10 días corridos** (acceso) / **5 días hábiles** (rectificación)
- [ ] Mención de la **AAIP** como órgano de control y cómo reclamar ante ella
- [ ] Tabla de proveedores con país
- [ ] Transferencia internacional declarada **+ base legal** (consentimiento o cláusulas modelo)
- [ ] Política de seguridad con la estructura de los 8 títulos de la Res. 47/2018
- [ ] Apartado "lo que esta política no promete", si corresponde
- [ ] Términos con precio, renovación, cancelación y **jurisdicción del domicilio del consumidor**
- [ ] Sin cláusulas de limitación de responsabilidad que el art. 37 tendría por no escritas
- [ ] **Fecha de versión** visible en cada documento
- [ ] Aviso de que esto requiere revisión profesional

**Fuera de los documentos**
- [ ] **Botón de arrepentimiento** en el primer acceso, sin registro previo
- [ ] **Botón de baja de servicio**, si hay suscripción
- [ ] Circuito que devuelva el **código de identificación en 24 horas**
- [ ] Enlaces visibles en el pie **del sitio y de la aplicación**
- [ ] Inscripción en el **Registro Nacional de Bases de Datos** (trámite ante la AAIP)
- [ ] Facturación electrónica habilitada

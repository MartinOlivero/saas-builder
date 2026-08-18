# Normativa europea verificada — RGPD

> **Verificado contra fuente el 2026-08-18** (EUR-Lex, textos del Reglamento (UE) 2016/679,
> EDPB y decisiones de la Comisión). No es de memoria. Antes de usarlo en otra fecha, correr
> § Verificación obligatoria.

Reglamento (UE) 2016/679, **RGPD** (GDPR en inglés). Aplica desde el 25/05/2018.

---

## Verificación obligatoria (correr en cada uso, antes de escribir)

**1. ¿Sigue en pie el EU-US Data Privacy Framework?**
Al 2026-08-18 **sí**: la decisión de adecuación de julio de 2023 sigue vigente y el Tribunal
General de la UE la confirmó en septiembre de 2025. **Pero hay un recurso pendiente ante el
TJUE**, presentado el 31/10/2025. Si cae, todas las transferencias a EEUU que se apoyaban en
el DPF quedan sin base legal de un día para el otro — le pasó a Safe Harbor (2015) y a
Privacy Shield (2020). Es el tercer intento; los dos anteriores fueron anulados.

**2. ¿Sigue Argentina en la lista de países adecuados?**
Al 2026-08-18 **sí**, revalidada por la Comisión Europea el 15/01/2024. La Comisión pidió que
Argentina **complete su reforma legislativa** para modernizar el marco. Si la reforma se
frustra o empeora, la adecuación puede revisarse.

**3. ¿Cambió la lista de países adecuados?**
Se actualiza por decisión de la Comisión. Brasil se incorporó en enero de 2026.

**Fuentes primarias:**

| Qué | Dónde |
| --- | --- |
| Texto del RGPD | `eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679` |
| Decisiones de adecuación | `commission.europa.eu` → Data protection → International dimension |
| Lista de certificados DPF | `data-privacy-framework.gov` (buscador oficial por empresa) |
| Directrices | `edpb.europa.eu` (Comité Europeo de Protección de Datos) |

---

## Lo primero: ¿te aplica? — Artículo 3

Casi todos los que creen que no les aplica, se equivocan. **No depende de dónde estés, sino de
a quién le vendés.**

| Apartado | Qué dice | Traducción práctica |
| --- | --- | --- |
| 3.1 | Tratamiento en el contexto de las actividades de un **establecimiento en la Unión**, esté o no el tratamiento en la UE | Tenés oficina, filial o empleados en la UE |
| **3.2.a** | **"la oferta de bienes o servicios, independientemente de si se requiere un pago del interesado"**, a interesados **en la Unión** | **Le vendés a gente en la UE. Con esto alcanza.** El "gratis también cuenta" es literal |
| **3.2.b** | **"el control de su comportamiento"** en la medida en que tenga lugar en la Unión | Analítica, cookies de seguimiento, perfilado de visitantes europeos |

**Un SaaS argentino sin oficina en Europa que vende suscripciones a clientes europeos entra
por 3.2.a.** No hay umbral mínimo de facturación ni de cantidad de usuarios.

Señales de que aplica y suelen pasarse por alto: precios en euros, la web traducida a un
idioma de la UE, publicidad dirigida a un país europeo, envíos o soporte en la UE.

### Artículo 27 — el representante en la UE

**La obligación que nadie conoce.** Si el RGPD te aplica por el art. 3.2 y **no** estás
establecido en la Unión, tenés que designar **por escrito un representante en la UE**, en un
Estado miembro donde estén los interesados. Es un punto de contacto para las autoridades y
para los titulares.

**Excepción del 27.2** — no hace falta si el tratamiento:
- es **ocasional**, **y**
- no incluye a gran escala categorías especiales (art. 9) ni datos penales, **y**
- es **improbable que entrañe un riesgo** para derechos y libertades.

Ojo: las tres condiciones son acumulativas. Un SaaS con clientes europeos recurrentes
difícilmente sea "ocasional". Hay empresas que prestan este servicio por una cuota anual.

---

## Bases de licitud — Artículo 6

Todo tratamiento necesita **al menos una**. Elegirla y declararla, no enumerarlas todas.

| | Base | Para un SaaS |
| --- | --- | --- |
| a | **Consentimiento** para fines específicos | Marketing, cookies no esenciales. Revocable en cualquier momento, y tiene que ser tan fácil retirarlo como darlo |
| b | **Ejecución de un contrato** con el interesado, o medidas precontractuales | **La base natural del producto**: la cuenta, el cobro, prestar el servicio |
| c | **Obligación legal** del responsable | Conservar facturación |
| d | Intereses vitales | Casi nunca |
| e | Interés público o ejercicio de poder público | No aplica a un SaaS privado |
| f | **Interés legítimo**, salvo que prevalezcan los derechos del interesado | Seguridad, prevención de fraude, analítica propia. **Requiere ponderación documentada**, y no vale para datos de menores sin cuidado extra |

> Error clásico de plantilla: pedir consentimiento para todo. Si la base real es el contrato
> (b), pedir consentimiento es peor: el usuario puede retirarlo y quedás sin base para prestar
> el servicio que te contrató.

**No existe en la Ley 25.326:** el interés legítimo como base autónoma. Si un documento
argentino lo invoca, está copiado de Europa.

---

## Derechos y plazos — Artículos 12 a 22

| Derecho | Artículo |
| --- | --- |
| Acceso | 15 |
| Rectificación | 16 |
| **Supresión ("derecho al olvido")** | 17 |
| Limitación del tratamiento | 18 |
| **Portabilidad** — recibir los datos en formato estructurado y de uso común | 20 |
| Oposición | 21 |
| **No ser objeto de decisiones automatizadas** con efectos jurídicos o significativos | 22 |

**Plazo (art. 12.3): un mes** desde la recepción de la solicitud. Prorrogable **dos meses más**
si la complejidad lo justifica, informando la prórroga dentro del primer mes.

**Gratuito (art. 12.5).** Se puede cobrar o negar solo si la solicitud es "manifiestamente
infundada o excesiva", y **la carga de probarlo es del responsable**.

> ⚠️ **Argentina es más exigente en plazos que Europa**: 10 días corridos para el acceso y
> 5 días hábiles para la rectificación, contra un mes del RGPD. Un documento que promete
> "un mes" a un titular argentino está incumpliendo.

---

## Encargado del tratamiento — Artículo 28

Si tratás datos por cuenta de otro (todo SaaS B2B lo hace), hace falta un **contrato escrito**
—el DPA, *data processing agreement*— que incluya como mínimo: objeto, duración, naturaleza y
fin del tratamiento, tipo de datos y categorías de interesados, y las obligaciones del
encargado.

Puntos que el contrato tiene que resolver sí o sí:
- Tratar los datos **solo siguiendo instrucciones documentadas** del responsable.
- **Subencargados**: autorización previa, y el encargado responde por ellos. (Tus proveedores
  —hosting, IA, mails— son subencargados y hay que listarlos.)
- Confidencialidad del personal, medidas del art. 32, asistencia al responsable con los
  derechos y con las brechas.
- **Suprimir o devolver** los datos al terminar el servicio.
- Someterse a auditorías.

Es el equivalente funcional del art. 25 de la Ley 25.326, bastante más detallado.

---

## Registro de actividades — Artículo 30

Registro interno de los tratamientos. **Exento si la empresa tiene menos de 250 empleados**,
salvo que el tratamiento no sea ocasional, entrañe riesgo, o incluya categorías especiales —
excepciones tan amplias que en la práctica **casi todo SaaS lo necesita**.

No se publica: se muestra a la autoridad si lo pide.

---

## Seguridad y brechas — Artículos 32 a 34

**Art. 32:** medidas técnicas y organizativas apropiadas al riesgo. Menciona expresamente
seudonimización y cifrado, confidencialidad/integridad/disponibilidad/resiliencia, capacidad
de restaurar el acceso tras un incidente, y **verificación periódica de la eficacia**.

**Art. 33 — notificación a la autoridad: "sin dilación indebida y, cuando sea posible, en un
plazo máximo de 72 horas"** desde que se tuvo conocimiento. Si se pasa, hay que explicar por
qué. Debe informar: naturaleza de la violación, categorías y número aproximado de afectados,
datos de contacto del DPO, consecuencias probables y medidas adoptadas.

**El encargado no notifica a la autoridad: notifica al responsable** sin dilación indebida.
El responsable decide.

**Art. 34 — notificación a los afectados:** solo si el riesgo es **alto**. Se exceptúa si los
datos estaban cifrados de forma que resulten ininteligibles.

> ⚠️ Contraste con Argentina: **la Ley 25.326 no obliga a notificar brechas.** Un documento
> argentino que promete las 72 horas se está autoimponiendo una obligación europea. Al revés,
> un producto con clientes europeos que no tiene circuito de 72 horas está incumpliendo.

---

## DPIA y DPO — cuándo NO hacen falta

Dos figuras que las plantillas meten siempre y que un SaaS chico normalmente **no necesita**.

**DPIA (art. 35)** — obligatoria cuando hay alto riesgo, en particular:
- (a) **evaluación sistemática y exhaustiva de aspectos personales basada en tratamiento
  automatizado, incluida la elaboración de perfiles**, en la que se basen decisiones con
  efectos jurídicos o que afecten significativamente;
- (b) tratamiento **a gran escala** de categorías especiales o datos penales;
- (c) **observación sistemática a gran escala** de zona de acceso público.

> El supuesto (a) alcanza a productos que analizan o puntúan personas con IA. Un CRM que
> evalúa vendedores o califica prospectos con un modelo entra en la conversación.

**DPO (art. 37)** — obligatorio solo si: es autoridad pública; **o** la actividad principal
requiere **observación habitual y sistemática a gran escala**; **o** la actividad principal es
tratamiento **a gran escala de categorías especiales**.

**Un SaaS pequeño típico no está obligado a designar DPO.** Se puede designar voluntariamente
(37.4), pero entonces quedás sujeto a las obligaciones de los arts. 38 y 39. No lo pongas en
el documento si no lo tenés.

---

## Transferencias internacionales — Artículos 44 a 49

Orden de preferencia:

**1. Decisión de adecuación (art. 45).** Los datos fluyen sin garantías adicionales.
Con decisión vigente al 2026-08-18: **Andorra, Argentina, Brasil, Canadá (sector comercial),
Corea del Sur, Islas Feroe, Guernsey, Isla de Man, Israel, Japón, Jersey, Nueva Zelanda,
Reino Unido, Suiza, Uruguay**, y **Estados Unidos limitado a organizaciones certificadas en el
Data Privacy Framework**.

> 🇦🇷 **Argentina está en la lista.** Un SaaS argentino puede recibir datos personales desde
> la UE **sin cláusulas contractuales adicionales**. Es una ventaja competitiva real frente a
> un competidor estadounidense, y casi nadie la aprovecha en su comunicación.

**2. Garantías adecuadas (art. 46).** Cláusulas Contractuales Tipo (SCC) de la Comisión —
versión de junio de 2021, con cuatro módulos según quién transfiere a quién—, normas
corporativas vinculantes (art. 47), códigos de conducta.

Tras **Schrems II** no alcanza con firmar las SCC: hay que hacer una **evaluación de impacto
de la transferencia (TIA)** y sumar medidas suplementarias si el país de destino no protege
lo suficiente frente a accesos gubernamentales.

**3. Excepciones (art. 49).** Consentimiento explícito informado del riesgo, necesidad
contractual. Son para casos **ocasionales**, no para la operación habitual — a diferencia de
Argentina, donde el consentimiento expreso sí sirve como base general.

### Verificar el DPF de cada proveedor

Que un proveedor sea estadounidense **no** significa que esté cubierto: la certificación es
voluntaria y por empresa. Se verifica por nombre en `data-privacy-framework.gov`. Y hay que
mirar el alcance: algunas certifican solo datos de RRHH.

---

## Cookies — no es el RGPD, es ePrivacy

La obligación de **consentimiento previo** para almacenar o leer información en el dispositivo
viene de la **Directiva 2002/58/CE (ePrivacy)**, modificada por la 2009/136/CE, traspuesta por
cada Estado miembro. El RGPD define el **estándar** que ese consentimiento debe cumplir
(libre, específico, informado, inequívoco, y tan fácil de retirar como de dar).

ePrivacy es *lex specialis*: se mira primero.

| Regla | Detalle |
| --- | --- |
| Consentimiento **previo** | Antes de instalar la cookie, no después. Exentas solo las **estrictamente necesarias** |
| Sin casillas premarcadas | Opt-in real (TJUE, *Planet49*) |
| Rechazar tan fácil como aceptar | "Aceptar todo" y "Rechazar todo" al mismo nivel. Sin *dark patterns* |
| Retirable | Enlace permanente para cambiar preferencias |
| Registro | Hay que poder demostrar el consentimiento obtenido |

> ⚠️ Contraste con Argentina: **no hay norma específica de cookies.** El banner al estilo
> europeo no es obligatorio acá. Si el producto vende a la UE, sí lo es.

---

## Multas — Artículo 83

Dos niveles. Se aplica **el importe mayor** entre la cifra fija y el porcentaje.

| Nivel | Máximo | Qué infracciones |
| --- | --- | --- |
| **Art. 83.4** | **10.000.000 €** o el **2%** de la facturación anual mundial total | Obligaciones de responsable y encargado (arts. 8, 11, **25-39**, 42-43): seguridad, brechas, DPIA, registro, contratos de encargado |
| **Art. 83.5** | **20.000.000 €** o el **4%** de la facturación anual mundial total | Principios y **consentimiento** (arts. 5-7, 9), **derechos de los interesados** (12-22), **transferencias internacionales** (44-49), incumplir órdenes de la autoridad |

**"Facturación mundial"** es del grupo empresarial, no de la unidad que infringió.

> Comparación que conviene tener presente: el máximo argentino por infracción es de $100.000,
> con un tope por acumulación de esa escala ×500. El europeo empieza en 10 millones de euros.
> Vender a Europa cambia el orden de magnitud del riesgo, no solo el papeleo.

---

## Diferencias clave con Argentina

La tabla que evita la mitad de los errores cuando un producto toca las dos jurisdicciones.

| Tema | Argentina (Ley 25.326) | UE (RGPD) |
| --- | --- | --- |
| Plazo de acceso | **10 días corridos** | **1 mes**, +2 de prórroga |
| Plazo de rectificación | **5 días hábiles** | Mismo mes del art. 12 |
| Portabilidad | **No existe** | Art. 20 |
| Derecho al olvido | **No existe** como tal | Art. 17 |
| Interés legítimo como base | **No existe** | Art. 6.1.f |
| DPO / delegado | **No existe** | Art. 37, obligatorio solo en tres supuestos |
| Notificación de brechas | **No obligatoria** | **72 horas** a la autoridad (art. 33) |
| Evaluación de impacto | No obligatoria | Art. 35 en alto riesgo |
| Cookies | Sin norma específica | Consentimiento previo (ePrivacy) |
| Protege personas jurídicas | **Sí** (arts. 1 y 2) | **No**, solo personas físicas |
| Fuente de acceso público irrestricto | Excepción del art. 5.2.a | Sin equivalente directo |
| Registro de bases ante la autoridad | **Obligatorio** (art. 24) | **No** existe registro público; sí registro interno (art. 30) |
| Representante local si sos extranjero | No previsto | **Art. 27** |
| Multa máxima | $100.000 por infracción (×500 acumulado) | 20M € o 4% de facturación mundial |

**Cuando ambas aplican, se cumple la más exigente de cada fila.** Un producto argentino que
vende a Europa responde pedidos de acceso en 10 días corridos —el plazo argentino— y además
notifica brechas en 72 horas —la obligación europea.

---

## Checklist RGPD para un SaaS

**Determinar antes de escribir**
- [ ] ¿Aplica el art. 3? (vender a personas en la UE alcanza)
- [ ] ¿Hace falta representante en la UE (art. 27)?
- [ ] Base de licitud elegida y declarada para cada finalidad (art. 6)
- [ ] ¿Hay tratamiento de categorías especiales (art. 9)?

**En los documentos**
- [ ] Identidad y datos de contacto del responsable, y del representante en la UE si lo hay
- [ ] Información completa del art. 13/14: finalidad, base legal, destinatarios, transferencias, plazo de conservación
- [ ] Los siete derechos, con el plazo de **un mes** y la forma de ejercerlos
- [ ] Derecho a **retirar el consentimiento** y a **reclamar ante la autoridad de control**
- [ ] Transferencias declaradas con su mecanismo (adecuación / SCC / DPF)
- [ ] Decisiones automatizadas y perfilado, si los hay (art. 22)
- [ ] Política de cookies con consentimiento previo y rechazo igual de fácil

**Fuera de los documentos**
- [ ] Registro de actividades de tratamiento (art. 30)
- [ ] DPA firmado con cada encargado y subencargado (art. 28)
- [ ] Circuito de notificación de brechas en **72 horas** (art. 33)
- [ ] DPIA si el tratamiento es de alto riesgo (art. 35)
- [ ] Verificado el DPF de cada proveedor estadounidense
- [ ] Medidas del art. 32, con verificación periódica de eficacia

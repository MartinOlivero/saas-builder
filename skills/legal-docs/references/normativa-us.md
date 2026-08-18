# Normativa de Estados Unidos verificada

> **Verificado contra fuente el 2026-08-18.** Antes de usarlo en otra fecha, correr
> § Verificación obligatoria: el mapa estatal cambia varias veces por año.

**Lo primero que hay que entender: no existe una ley federal de privacidad.** Hay un mosaico
de leyes estatales, reglas federales sectoriales y una autoridad federal (FTC) que castiga
promesas incumplidas. Escribir "cumplimos con la ley de privacidad de EEUU" no significa nada.

---

## Verificación obligatoria (correr en cada uso)

1. **¿Cuántos estados tienen ley de privacidad en vigor?** Al 2026-08-18 son **20 en vigor**
   y unas 24 promulgadas. Cambia cada año: verificar en el rastreador de la IAPP o de MultiState.
2. **¿Cambió algún estado de one-party a all-party consent?** La lista de abajo se mueve poco,
   pero Michigan, Connecticut, Oregon y Vermont son discutidos y hay jurisprudencia nueva.
3. **¿Hay ley federal?** Se propone en cada Congreso y nunca sale. Si alguna vez sale,
   este archivo queda viejo entero.

---

## 🔴 Grabación de llamadas — lo más grave, y va primero

**En EEUU grabar una llamada sin permiso puede ser un delito penal, no una multa
administrativa.** Es la diferencia de fondo con Argentina y con Europa, y la que más
sorprende a quien construye un producto que graba.

**Base federal:** 18 U.S.C. § 2511 — régimen de **una parte**: alcanza con que uno de los
participantes consienta. La mayoría de los estados sigue ese criterio.

**Pero 11 estados exigen el consentimiento de TODAS las partes:**

> **California · Delaware · Florida · Illinois · Maryland · Massachusetts · Montana ·
> Nevada · New Hampshire · Pennsylvania · Washington**

**Otros 4 son ambiguos o discutidos** — Connecticut, Michigan, Oregon y Vermont. La práctica
de los call centers que cumplen bien es **tratar los 15 como all-party**.

### La regla que decide todo: gana la ley más estricta

**Si cualquier participante está en un estado all-party, la llamada necesita consentimiento de
todos.** Y vos no controlás dónde está el prospecto: puede atender desde California mientras
tu cliente llama desde Texas.

**Consecuencia práctica para un producto que graba:** la única política operable es **pedir
consentimiento de todos, siempre**, sin importar el estado. Cualquier lógica del tipo "si es
one-party grabamos sin avisar" es inaplicable, porque requiere saber en tiempo real dónde está
cada participante.

Detalles que cambian según el estado: Massachusetts prohíbe la grabación **secreta** en vez de
contar consentimientos; Illinois tiene un historial legislativo enredado; y varios tratan
distinto la llamada telefónica de la conversación presencial.

---

## 🔴 BIPA — la voz como dato biométrico (Illinois)

*Biometric Information Privacy Act*, 740 ILCS 14. **Es la ley de privacidad más litigada de
Estados Unidos**, y la que más daño hace a un producto chico.

| Qué | Detalle |
| --- | --- |
| Daños | **$1.000 por violación negligente** y **$5.000 por violación imprudente**, **por persona y por ocurrencia** |
| Quién demanda | **Derecho de acción privado** — no hace falta que actúe un regulador. Es lo que la vuelve tan litigada |
| Requisitos | Aviso **por escrito**, consentimiento **escrito** antes de recolectar, política pública de retención y destrucción |

### Por qué le importa a un producto que transcribe

**Un "voiceprint" no requiere que vendas biometría.** La jurisprudencia reciente alcanza a
herramientas de transcripción con IA, reconocimiento de hablante y analítica de voz: **si el
sistema distingue quién habla por características vocales, eso puede ser recolección de
voiceprint.**

> Esto incluye la **diarización** —etiquetar "habló A, después habló B"— que hace prácticamente
> cualquier transcriptor moderno de reuniones. Un producto puede estar recolectando voiceprints
> sin que nadie en el equipo lo haya pensado nunca en esos términos.

**Y la responsabilidad no se terceriza:** la organización que usa la herramienta puede
responder aunque la transcripción la haga un proveedor externo. Que el vendor sea el que
procesa no te saca del reclamo.

Texas (CUBI) y Washington tienen leyes biométricas propias, sin acción privada: las hace
cumplir el fiscal general. Illinois es la peligrosa.

---

## Leyes estatales de privacidad

**20 en vigor al 2026-08-18:** California, Colorado, Connecticut, Delaware, Indiana, Iowa,
Kentucky, Maryland, Minnesota, Montana, Nebraska, New Hampshire, New Jersey, Oregon,
Rhode Island, Tennessee, Texas, Utah, Virginia y Washington.

Se parecen bastante entre sí —derechos de acceso, corrección, eliminación, portabilidad y
opt-out de venta y publicidad dirigida— pero **los umbrales de aplicación cambian mucho**, y
ahí está la trampa.

| Estado | Umbral | Comentario |
| --- | --- | --- |
| **California** (CCPA/CPRA) | **USD 26.625.000** de facturación bruta anual (desde 1/1/2025); **o** 100.000 residentes de CA; **o** 50% de los ingresos por vender/compartir datos | Cualquiera de los tres alcanza |
| **Rhode Island** | **35.000** residentes | El más bajo: atrapa productos chicos |
| Indiana, Kentucky y la mayoría | 100.000 residentes (o 25.000 + 50% de ingresos por venta de datos) | El estándar de facto |
| **Texas y Nebraska** | **Sin umbral numérico** | Aplica a cualquiera que no sea *small business* según la SBA (en general, menos de 500 empleados) |

> **La buena noticia para un SaaS chico:** con los umbrales típicos, un producto con pocos
> miles de usuarios estadounidenses **no queda alcanzado** por casi ninguna. Decirlo es más
> honesto que fingir cumplimiento total.
>
> **La mala:** aun exento, **no se pueden vender datos sensibles sin consentimiento**, y la
> exención no te salva de la FTC, del TCPA ni de BIPA — que son las tres que de verdad muerden
> a los productos chicos.

**Derecho de acción privado:** solo California, y limitado a brechas de seguridad por falta de
medidas razonables. El resto lo hace cumplir el fiscal general estatal.

---

## FTC — Sección 5: el que sí te alcanza siempre

*Federal Trade Commission Act*, § 5(a): prohíbe **prácticas desleales o engañosas** en el
comercio. No tiene umbral. Alcanza a cualquier negocio digital, incluidos SaaS extranjeros que
venden a consumidores estadounidenses.

**Qué considera engañoso:** prometer algo sobre tus prácticas de datos y no cumplirlo. La FTC
ha tratado como engañosas afirmaciones como:

- *"nunca vendemos tus datos"* — y compartirlos con terceros
- *"tu información está cifrada"* — sin cifrado real
- *"cumplimos con el RGPD"* — sin cumplirlo

> **Esto es exactamente la categoría 🔴 CONTRADICCIÓN de `auditoria.md`, con fuerza de ley
> federal.** En EEUU, la política de privacidad que miente no es un problema reputacional: es
> una infracción. Y "no adherir a los pasos, estándares y promesas de tu aviso de privacidad"
> es la formulación que usa la propia FTC.

Corolario para redactar: **cada promesa que se saca del documento reduce exposición real.** El
apartado "lo que esta política no promete" no es un gesto de honestidad, es gestión de riesgo.

---

## TCPA — llamadas y SMS automatizados

*Telephone Consumer Protection Act*. Muy relevante para cualquier producto de ventas.

| Qué | Detalle |
| --- | --- |
| Daños | **USD 500 a 1.500 por llamada o mensaje**, **sin tope para acciones de clase** |
| Quién demanda | **Acción privada.** Es una industria litigiosa entera |
| Consentimiento | **Prior express written consent** para marketing a celulares, con divulgación clara y aviso de que el consentimiento **no es condición de compra** |
| ¿B2B zafa? | **Casi no.** La excepción es angosta: llamadas marcadas manualmente a números fijos de empresa con fines no comerciales. No cubre SMS automatizados ni marcadores |

Un CRM que dispara SMS o llamadas automatizadas expone a su cliente a esto. Conviene que los
términos le trasladen esa obligación explícitamente.

---

## Otras que pueden aplicar

| Norma | Cuándo importa |
| --- | --- |
| **CAN-SPAM** | Emails comerciales: remitente y asunto no engañosos, dirección física, baja funcional procesada en 10 días hábiles. Sin acción privada |
| **COPPA** | Menores de 13. Consentimiento verificable de los padres. Si el producto puede tenerlos, cambia todo |
| **HIPAA** | Datos de salud, y **solo** si sos *covered entity* o *business associate*. No aplica por tocar datos de salud sin más |
| **GLBA** | Datos financieros de instituciones financieras |
| **Washington My Health My Data** | Datos de salud en sentido amplio, **con acción privada**. Definición muy ancha de "health data" |

---

## Diferencias con Argentina y la UE

| Tema | Argentina | UE (RGPD) | Estados Unidos |
| --- | --- | --- | --- |
| Ley general | Sí, una | Sí, una | **No.** 20 estatales + sectoriales |
| ¿Aplica a un SaaS chico? | Sí, siempre | Sí, sin umbral | **Depende del umbral estatal** — muchos quedan exentos |
| Grabar llamadas | Sin norma específica | Base legal + información | **11-15 estados exigen consentimiento de todos. Puede ser delito** |
| Biometría de voz | Sin régimen propio | Categoría especial (art. 9) | **BIPA: acción privada, $1.000-$5.000 por persona por ocurrencia** |
| Mentir en la política | Riesgo contractual | Infracción de principios | **Práctica engañosa federal (FTC §5)** |
| Cookies | Sin norma específica | Consentimiento previo | Sin regla federal; opt-out en leyes estatales |
| Demandas de particulares | Vía judicial ordinaria | Art. 82 | **Acción privada en BIPA, TCPA y CCPA (brechas)** — el verdadero riesgo |

**La lectura que le sirve a un SaaS chico:** en Argentina y en Europa el riesgo es
regulatorio y gradual. En Estados Unidos el riesgo es **litigio privado**, llega sin aviso de
ningún organismo, y las tres puertas más usadas —BIPA, TCPA y FTC— **no tienen umbral de
tamaño**.

---

## Checklist para un SaaS que vende a EEUU

**Determinar primero**
- [ ] ¿Supera el umbral de algún estado? (California, Rhode Island y Texas/Nebraska son los que más atrapan)
- [ ] ¿El producto graba o transcribe llamadas? → tratar **todos** los estados como all-party
- [ ] ¿Identifica hablantes por voz? → **riesgo BIPA**, aunque no se venda como biométrico
- [ ] ¿Dispara llamadas o SMS automatizados? → TCPA
- [ ] ¿Puede haber menores de 13? → COPPA

**En los documentos**
- [ ] Categorías de información recolectada y finalidades
- [ ] Si aplica alguna ley estatal: derechos y cómo ejercerlos, con el plazo de ese estado
- [ ] "Do Not Sell or Share My Personal Information" si hay venta o publicidad dirigida
- [ ] **Cada afirmación verificada contra el código** — la FTC castiga la promesa incumplida
- [ ] Aviso de grabación y su consentimiento, si el producto graba

**Fuera de los documentos**
- [ ] Mecanismo real para atender pedidos de derechos
- [ ] Aviso y **consentimiento escrito** antes de grabar, con política de retención (BIPA)
- [ ] Consentimiento expreso escrito antes de SMS o llamadas automatizadas (TCPA)
- [ ] Baja funcional en emails comerciales, procesada en 10 días hábiles (CAN-SPAM)

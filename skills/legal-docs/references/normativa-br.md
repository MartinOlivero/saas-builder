# Normativa brasileña verificada — LGPD

> **Verificado contra fuente el 2026-08-18** (Lei 13.709/2018, resoluciones de la ANPD).
> Antes de usarlo en otra fecha, correr § Verificación obligatoria.

**Lei Geral de Proteção de Dados Pessoais (LGPD), Lei 13.709/2018.** Vigente desde 2020,
sanciones desde agosto de 2021. Autoridad: **ANPD** (Autoridade Nacional de Proteção de Dados).

Está inspirada en el RGPD y se le parece bastante, pero **no es igual**, y las diferencias
caen justo donde duelen: plazos, transferencias internacionales y el encargado.

---

## Verificación obligatoria

1. **¿La ANPD reconoció ya algún país como adecuado?** Al 2026-08-18 **no había emitido
   ninguna decisión de adecuación**. Si aparece la primera —se espera que la UE y países como
   Argentina y Uruguay— cambia el mecanismo de transferencia y este archivo queda viejo.
2. **¿Hay resoluciones nuevas de la ANPD?** Legisla activamente por resolución; verificar en
   `gov.br/anpd`.
3. **¿Cambiaron las reglas del encarregado?** El art. 41 § 3 faculta a la ANPD a definir
   hipótesis de dispensa.

**Fuentes:** `planalto.gov.br` (texto de la ley) · `gov.br/anpd` (resoluciones y guías).

---

## ¿Te aplica? — Artículo 3

**Aplicación extraterritorial amplia.** No importa dónde esté la empresa ni dónde estén los
servidores. La LGPD aplica cuando:

- la operación de tratamiento se realiza **en territorio nacional**; **o**
- la actividad tiene por objeto **ofrecer o suministrar bienes o servicios a personas ubicadas
  en Brasil**, o tratar datos de personas ubicadas en Brasil; **o**
- los datos fueron **recolectados en territorio nacional**.

Un SaaS argentino con clientes brasileños queda alcanzado por el segundo supuesto. Igual
criterio que el art. 3.2 del RGPD.

---

## Bases legales — Artículo 7

**Diez hipótesis**, cuatro más que el RGPD. Las que importan a un SaaS:

| | Base |
| --- | --- |
| I | **Consentimiento** del titular |
| II | Cumplimiento de obligación legal o regulatoria |
| V | **Ejecución de contrato** o de diligencias preliminares a pedido del titular |
| VI | Ejercicio regular de derechos en proceso judicial, administrativo o arbitral |
| IX | **Legítimo interés** del controlador o de tercero |
| X | Protección del crédito |

Para **datos sensibles** (art. 11) la lista es más corta y **no incluye el legítimo interés**:
ahí hace falta consentimiento específico y destacado, u otra de las hipótesis del art. 11.

---

## Derechos y plazos — Artículos 18 y 19

Derechos del art. 18: confirmación de la existencia del tratamiento, acceso, corrección,
anonimización o bloqueo, **portabilidad**, eliminación, información sobre compartición,
información sobre la posibilidad de no consentir, y **revocación del consentimiento**.

> ⏱️ **Plazo: 15 días** desde el requerimiento (art. 19 II). **Prorrogable por igual período**
> con justificación fundada y comunicación al titular.
>
> Es el plazo intermedio de las cuatro jurisdicciones: más corto que el mes europeo, más largo
> que los 10 días corridos argentinos.

Hay además una respuesta **inmediata** en formato simplificado para la confirmación y el
acceso (art. 19 I).

---

## Encarregado — Artículo 41

**A diferencia del RGPD, la LGPD exige que el controlador designe un encarregado**, sin los
tres supuestos acotados del art. 37 europeo. El § 3 faculta a la ANPD a establecer hipótesis
de dispensa, y las guías han flexibilizado el criterio para agentes de tratamiento de pequeño
porte, pero **la regla de base es que hace falta**.

La identidad y el contacto del encarregado deben ser **públicos**, típicamente en la política
de privacidad.

> Diferencia práctica: un SaaS chico **no** necesita DPO en Europa y **sí** necesita
> encarregado en Brasil. No hace falta que sea una persona dedicada full time.

---

## Incidentes de seguridad — Artículo 48 y Resolución CD/ANPD 15/2024

El controlador debe **comunicar a la ANPD y al titular** el incidente que pueda acarrear
**riesgo o daño relevante**. La Resolución CD/ANPD 15/2024 fijó las reglas de notificación:
qué informar, en qué plazo y en qué forma.

Contraste: Argentina **no obliga** a notificar; la UE fija **72 horas**; Brasil obliga con
reglas propias de la ANPD.

---

## Transferencia internacional — Artículo 33 y Resolución CD/ANPD 19/2024

> ⚠️ **La ANPD todavía no reconoció a ningún país como adecuado.** Al 2026-08-18 no hay
> ninguna decisión de adecuación vigente — ni siquiera para la UE.

Consecuencia directa: **toda transferencia de datos fuera de Brasil necesita un mecanismo
contractual.** El principal son las **cláusulas-padrão contratuais** aprobadas por la
Resolución CD/ANPD 19/2024 (23/08/2024), de incorporación **obligatoria** — el período de
gracia venció el **23/08/2025**.

Otros mecanismos: cláusulas contractuales específicas aprobadas por la ANPD, normas
corporativas globales, sellos y códigos de conducta.

> **Para un SaaS argentino con clientes brasileños:** no alcanza con declarar la transferencia
> en la política. Hay que **firmar las cláusulas-padrão de la ANPD** con el cliente brasileño,
> y esto es una obligación concreta que casi nadie cumple.

---

## Sanciones — Artículo 52

| Sanción | Detalle |
| --- | --- |
| Advertencia | Con plazo para adoptar medidas correctivas |
| **Multa simple** | Hasta **2% de la facturación en Brasil** del último ejercicio, excluidos tributos, **limitada a R$ 50.000.000 por infracción** |
| Multa diaria | Con el mismo tope |
| Publicidad de la infracción | Reputacional |
| Bloqueo o eliminación de los datos | Puede terminar con la operación |
| Suspensión parcial o total del funcionamiento de la base | Ídem |

La facturación es **la de Brasil**, no la global — a diferencia del RGPD, que toma la mundial.

---

## Diferencias con RGPD y con Argentina

| Tema | Argentina | UE (RGPD) | Brasil (LGPD) |
| --- | --- | --- | --- |
| Plazo de respuesta | **10 días corridos** | 1 mes (+2) | **15 días** (+15) |
| Portabilidad | No existe | Sí | **Sí** |
| Legítimo interés | No existe | Sí | **Sí** (no para datos sensibles) |
| DPO / encarregado | No existe | Solo en 3 supuestos | **Regla general: obligatorio** |
| Notificar brechas | No obligatorio | 72 h | **Obligatorio**, reglas de la ANPD |
| Países adecuados | Lista propia | Lista de la Comisión | **Ninguno todavía** |
| Transferencia sin adecuación | Consentimiento expreso sirve | SCC + evaluación | **Cláusulas-padrão obligatorias** |
| Multa máxima | $100.000 (×500 acumulado) | 20M € o 4% mundial | **R$ 50M por infracción o 2% de facturación en Brasil** |

---

## Checklist LGPD

- [ ] ¿Aplica el art. 3? (ofrecer servicios a personas en Brasil alcanza)
- [ ] Base legal elegida y declarada por finalidad (art. 7); si hay datos sensibles, art. 11
- [ ] **Encarregado designado, con identidad y contacto públicos** (art. 41)
- [ ] Los nueve derechos del art. 18, con el plazo de **15 días**
- [ ] Mención de la **ANPD** y cómo reclamar
- [ ] **Cláusulas-padrão de la Resolución 19/2024 firmadas** con quien transfiere fuera de Brasil
- [ ] Circuito de notificación de incidentes a la ANPD y a los titulares (art. 48)
- [ ] Registro de operaciones de tratamiento (art. 37)

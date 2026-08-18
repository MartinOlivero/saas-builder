# Normativa del Reino Unido verificada — UK GDPR

> **Verificado contra fuente el 2026-08-18** (UK GDPR, Data Protection Act 2018, Data (Use and
> Access) Act 2025, ICO). Antes de usarlo en otra fecha, correr § Verificación obligatoria.

**No leer este archivo solo.** El UK GDPR es el RGPD europeo retenido en derecho británico tras
el Brexit: **el 90% es idéntico**. Este archivo cubre **solo las diferencias**. Para todo lo
demás —bases de licitud, derechos, encargado, seguridad, DPIA— vale `normativa-eu.md`.

Marco: **UK GDPR + Data Protection Act 2018**, reformados por el **Data (Use and Access) Act
2025** (DUAA). Autoridad: **ICO** (Information Commissioner's Office).

---

## Verificación obligatoria

1. **¿Qué partes del DUAA están en vigor?** Recibió *Royal Assent* el **19/06/2025**; las
   disposiciones centrales entraron en vigor el **05/02/2026** y otras el **19/06/2026**. Es
   una reforma escalonada: verificar qué rige en la fecha de uso.
2. **¿Sigue vigente la adecuación UE→UK?** Al 2026-08-18 **sí**: renovada en diciembre de 2025
   y vigente **hasta diciembre de 2031**. La Comisión evaluó el DUAA y concluyó que el Reino
   Unido mantiene un nivel "esencialmente equivalente".
3. **¿Cambió el marco de *data bridges*?** El DUAA formalizó el mecanismo británico de
   transferencias, que evalúa si el país de destino logra resultados comparables sin exigir
   equivalencia formal.

**Fuentes:** `legislation.gov.uk` · `ico.org.uk`.

---

## ¿Te aplica?

Mismo criterio que el art. 3 del RGPD: alcanza a quien **ofrece bienes o servicios a personas
en el Reino Unido** o **monitorea su comportamiento**, esté establecido donde esté.

**Y si vendés a la UE y al Reino Unido, te aplican los dos regímenes.** Son regímenes
separados desde el Brexit: dos autoridades, dos posibles multas por el mismo hecho.

### Representante en el Reino Unido

Igual que el art. 27 del RGPD: quien no está establecido en el Reino Unido y queda alcanzado
debe designar un **representante en el Reino Unido**, con las mismas excepciones acotadas.

> Un SaaS argentino que vende a Europa y al Reino Unido puede necesitar **dos representantes**:
> uno en un Estado miembro de la UE y otro en el Reino Unido.

---

## Las diferencias que importan

### 1. Multas — el cambio del DUAA

| Norma | Antes | Desde el DUAA |
| --- | --- | --- |
| UK GDPR | £17,5 M o 4% de la facturación mundial | Sin cambios |
| **PECR** (cookies y marketing electrónico) | £500.000 | **£17,5 M o 4%** — alineado con el UK GDPR |

**Ese es el cambio más relevante en la práctica.** El régimen de cookies y marketing directo
británico pasó de una multa acotada a una del orden del RGPD: multiplicó por 35 el techo.

### 2. Derecho a reclamar directamente al responsable

**Nuevo, en vigor desde el 19/06/2026.** El titular puede presentar una queja **directamente
al responsable**, y el responsable está obligado a:

- proporcionar un **formulario de queja** que se pueda completar electrónicamente;
- **acusar recibo dentro de los 30 días**;
- tomar medidas para resolverla sin dilación indebida;
- informar al titular el avance y el resultado.

> Es una obligación **operativa**, no de redacción: hay que tener el formulario y el circuito
> que lo atienda. Un documento que lo promete sin que exista es una contradicción de manual.

### 3. Poderes del ICO

El DUAA le dio al ICO facultades nuevas: **obligar a testigos a declarar** en entrevistas y
**exigir informes técnicos**.

### 4. PECR — cookies

El equivalente británico de ePrivacy son las **PECR** (*Privacy and Electronic Communications
Regulations*). Mismo principio que en la UE: consentimiento previo salvo cookies estrictamente
necesarias. Lo que cambió es el techo de la multa.

---

## Transferencias

**Desde el Reino Unido hacia afuera:** decisiones de adecuación británicas (heredadas de la UE
al Brexit, más las propias), el **UK Addendum** a las cláusulas contractuales de la UE, o el
**IDTA** (*International Data Transfer Agreement*) británico. **Las SCC europeas solas no
alcanzan**: hay que sumarles el UK Addendum.

**Desde la UE hacia el Reino Unido:** libre, por la adecuación vigente hasta diciembre de 2031.

---

## Diferencias con la UE, en una tabla

| Tema | UE (RGPD) | Reino Unido |
| --- | --- | --- |
| Norma | Reglamento (UE) 2016/679 | UK GDPR + DPA 2018 + DUAA 2025 |
| Autoridad | La de cada Estado miembro | **ICO** |
| Multa RGPD | 20 M € o 4% | **£17,5 M o 4%** |
| Multa cookies/marketing | Según el Estado miembro | **£17,5 M o 4%** desde el DUAA |
| Queja directa al responsable | No previsto | **Sí, con formulario y acuse en 30 días** |
| Representante | Art. 27, en un Estado miembro | Equivalente, **en el Reino Unido** |
| Transferencias | SCC de la Comisión | **SCC + UK Addendum**, o IDTA |

---

## Checklist adicional para el Reino Unido

Además de todo el checklist de `normativa-eu.md`:

- [ ] ¿Hace falta representante en el Reino Unido, además del de la UE?
- [ ] **Formulario de queja** electrónico y circuito que acuse recibo en 30 días
- [ ] Si se usan las SCC europeas, **UK Addendum firmado** (o IDTA en su lugar)
- [ ] Banner de cookies conforme a PECR — el techo de multa ya no es simbólico
- [ ] Mención del **ICO** como autoridad y cómo reclamar ante él

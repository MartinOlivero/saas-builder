# Esqueletos de los documentos

**Esto no es una plantilla para rellenar.** Es el orden de las secciones y qué tiene que
resolver cada una. El contenido sale del producto: si dos productos distintos generan el
mismo texto, la skill falló.

Regla de redacción: **frases verificables**. "Guardamos tu correo y tu CUIT" es verificable.
"Nos tomamos tu privacidad muy en serio" no dice nada y ocupa el lugar de algo que sí.

---

## Política de Privacidad

| # | Sección | Qué resuelve |
| --- | --- | --- |
| 1 | Responsable de la base de datos | Razón social o nombre, **CUIT**, domicilio, correo de contacto. Art. 6. **Sin esto no se publica** |
| 2 | Qué datos tratamos | Del esquema real, campo por campo. **Incluir un "qué NO tratamos"**: es donde se ve que alguien leyó el código |
| 3 | Con qué finalidad | Una por una. Nada de "para mejorar la experiencia" |
| 4 | Base legal | Consentimiento, ejecución del contrato, o fuente de acceso público irrestricto (art. 5.2.a) |
| 5 | Con quién compartimos | Tabla de proveedores: nombre · para qué · país |
| 6 | Transferencia internacional | Si algún proveedor está fuera de la lista de países adecuados. Declarar el mecanismo (art. 12) |
| 7 | Cuánto tiempo conservamos | Plazo real. Si no hay purga, decir que se conservan mientras la cuenta esté activa y qué pasa después |
| 8 | Cómo protegemos los datos | Resumen; el detalle va en la política de seguridad |
| 9 | Tus derechos | Acceso, rectificación, actualización, supresión. **10 días corridos** / **5 días hábiles**. Gratuito. Cómo ejercerlos |
| 10 | AAIP | Órgano de control y que se puede reclamar ante ella |
| 11 | Cookies y seguimiento | Cuáles, para qué, cómo desactivarlas |
| 12 | Menores de edad | Qué política tiene el producto. No inventar una edad legal |
| 13 | Cambios en esta política | Cómo se avisan |
| 14 | Fecha de versión + aviso profesional | |

### Cláusula de derechos (la redacción importa)

```
Podés pedirnos acceso a tus datos personales escribiendo a [correo]. Te vamos a responder
dentro de los DIEZ (10) días corridos, sin cargo (art. 14 de la Ley 25.326). Si los datos
son inexactos o están incompletos, los rectificamos, actualizamos o suprimimos dentro de
los CINCO (5) días hábiles de tu pedido, también sin cargo (art. 16).

La AGENCIA DE ACCESO A LA INFORMACIÓN PÚBLICA, órgano de control de la Ley 25.326, tiene
la atribución de atender denuncias y reclamos de quienes vean afectados sus derechos por
incumplimiento de las normas de protección de datos personales.
```

### Cláusula de transferencia internacional

```
Algunos de nuestros proveedores están radicados en los Estados Unidos de América, país que
no integra la lista de los que la Agencia de Acceso a la Información Pública considera con
nivel adecuado de protección. Al aceptar esta política prestás tu CONSENTIMIENTO EXPRESO
para esa transferencia, en los términos del artículo 12 de la Ley 25.326. Los proveedores,
su función y su país figuran en la tabla del punto [N].
```

> Si el producto no está dispuesto a apoyarse en el consentimiento, la alternativa son las
> cláusulas contractuales modelo (Disp. 60/2016 y Res. AAIP 198/2023) firmadas con cada
> proveedor. Es más sólido y bastante más trabajo. Decírselo al usuario y que elija.

---

## Términos y Condiciones

| # | Sección | Qué resuelve |
| --- | --- | --- |
| 1 | Quién presta el servicio | Identificación completa. **Si quien cobra es otra entidad, decirlo acá** |
| 2 | Qué es el servicio y qué no es | El "qué no es" evita la mayor parte de los conflictos |
| 3 | La cuenta | Cómo se crea, requisitos, responsabilidad sobre la credencial |
| 4 | Precio, pago y renovación | Moneda, impuestos, **cómo y cuándo se renueva**, cómo se avisan los aumentos |
| 5 | Cancelación y baja | Qué pasa con los datos. Enlazar el **botón de baja** |
| 6 | Derecho de revocación | 10 días corridos, irrenunciable. Enlazar el **botón de arrepentimiento** (CCyC 1111: hay que informarlo en forma clara y oportuna) |
| 7 | Disponibilidad | Solo prometer lo que se mide. Sin monitoreo, no hay SLA |
| 8 | Uso permitido | Qué está prohibido y qué pasa si se incumple |
| 9 | Propiedad intelectual | Del servicio y **de los datos que sube el usuario** — decir claramente que siguen siendo del usuario |
| 10 | Responsabilidad | Ver la advertencia de abajo |
| 11 | Confidencialidad | Art. 10: el deber subsiste después de terminada la relación |
| 12 | Cambios en los términos | Preaviso |
| 13 | Ley aplicable y jurisdicción | Ver la advertencia de abajo |
| 14 | Contacto | |
| 15 | Fecha de versión + aviso profesional | |

### ⚠️ Jurisdicción — el error más caro

```
❌ NUNCA:  "Las partes se someten a los Tribunales Ordinarios de la Ciudad de [ciudad del
            proveedor], renunciando a cualquier otro fuero."

✅ Cuando hay relación de consumo:
            "Para toda controversia serán competentes los tribunales del domicilio del
            consumidor, conforme el artículo 36 de la Ley 24.240."
```

El art. 36 es de **orden público**: pactar en contra no lo cambia, la cláusula se tiene por
no escrita. Lo único que consigue es mostrar que el documento se copió de otro lado.

### ⚠️ Responsabilidad

Las exclusiones totales de responsabilidad, traducidas de plantillas en inglés, chocan con
el art. 37 de la Ley 24.240 y con los arts. 1117-1122 del CCyC: se tienen por no escritas.
Limitar de forma acotada y realista (por ejemplo, al monto abonado en los últimos meses, y
sin excluir dolo ni culpa grave) protege más que una exclusión total que no se sostiene.

---

## Política de Seguridad

Estructura sobre los **ocho títulos de la Res. AAIP 47/2018** — así se lee como cumplimiento
y no como marketing. Adaptar los nombres al producto, mantener la cobertura.

| Res. 47/2018 | Sección | Qué escribir |
| --- | --- | --- |
| A | Recolección y minimización | Qué se pide y qué se decide no pedir |
| B | Control de acceso | Autenticación, roles, quién llega a producción |
| C | Control de cambios | Cómo se despliega y quién puede |
| D | Respaldo y recuperación | Frecuencia real, dónde, si se probó restaurar |
| E | Gestión de vulnerabilidades | Actualización de dependencias, revisiones |
| F | Destrucción de datos | Qué se borra, cuándo, con qué método |
| G | Incidentes de seguridad | Detección y respuesta. **Cuidado con prometer plazos de aviso** |
| H | Entornos de desarrollo | Separación de entornos, si hay datos reales en desarrollo |
| — | Cifrado y transporte | TLS, cifrado en reposo — **solo lo que exista** |
| — | Proveedores | Qué proveedor ve qué |
| — | **Lo que esta política no promete** | ↓ |
| — | Revisión y fecha | |

### El apartado que hace la diferencia

```markdown
## Lo que esta política no promete

Preferimos decirlo antes que dar a entender lo contrario:

- No tenemos certificación ISO 27001 ni SOC 2.
- No ofrecemos un acuerdo de nivel de servicio (SLA) con disponibilidad garantizada.
- No tenemos segundo factor de autenticación todavía.
- Nuestros respaldos se restauran manualmente; no hay recuperación automática.
```

Un cliente técnico detecta el maquillaje en treinta segundos. La franqueza rinde más, y
además evita el peor escenario: haber prometido por escrito algo que no existe.

---

## Botón de arrepentimiento (página)

Requisitos duros de la Disp. 954/2025: **primer acceso, lugar destacado, sin registro previo,
código de identificación en 24 horas.**

| Sección | Contenido |
| --- | --- |
| Título | Literalmente **"BOTÓN DE ARREPENTIMIENTO"** |
| Quién puede usarlo y hasta cuándo | 10 días corridos desde la contratación o la entrega, lo que ocurra último |
| El mecanismo | Formulario accesible **sin login**. Pedir lo mínimo para identificar la operación |
| Qué pasa después | **Código de identificación dentro de las 24 horas**, por el mismo medio. Plazo de devolución |
| Vía alternativa | Un correo, para quien no pueda usar el formulario |
| Pasados los 10 días | Qué opciones quedan (cancelar la suscripción → enlazar el botón de baja) |
| Otras vías de reclamo | Defensa del Consumidor / **Ventanilla Única Federal**. **No mencionar COPREC: fue disuelto** |

## Botón de baja de servicio (página)

Mismos requisitos formales. Es una página distinta y una obligación distinta: el de
arrepentimiento revoca una contratación reciente, el de baja cancela un servicio en curso.

| Sección | Contenido |
| --- | --- |
| Título | Literalmente **"BOTÓN DE BAJA DE SERVICIO"** |
| El mecanismo | **Sin login.** Identificar la suscripción con el mínimo dato posible |
| Efectos | Desde cuándo deja de cobrarse, hasta cuándo hay acceso, qué pasa con los datos |
| Confirmación | Código de identificación **dentro de las 24 horas** |

> Implementación: si el botón exige entrar a la cuenta, **no cumple**. Es el error más común,
> porque técnicamente es lo cómodo. Hace falta un flujo público con verificación por correo.

---

## Aviso de cierre (obligatorio en todo documento generado)

```
Este documento fue redactado a partir de la arquitectura real de [producto] y de la
normativa argentina vigente al [fecha]: Ley 25.326, Res. AAIP 47/2018, Res. AAIP 126/2024,
Disp. DNPDP 60/2016 y Res. AAIP 34/2019, Ley 24.240 y Disposición 954/2025.

No reemplaza el asesoramiento de un abogado. Antes de publicarlo, conviene que lo revise
un profesional matriculado, especialmente si el producto trata datos sensibles (art. 7 de
la Ley 25.326), datos de menores, o tiene usuarios fuera de la Argentina.

Última actualización: [fecha]
```

Y en la respuesta al usuario —no solo en el pie del documento— decir qué quedó pendiente
fuera del texto: inscripción en el Registro Nacional de Bases de Datos, implementar los
botones, enlazar los documentos en el pie del sitio y de la app.

# PRD — Interfaz de docentes de Miseño

**Borrador 0.2 · 10 de noviembre de 2026 · Para iterar**

El sistema se llama **Miseño**. Scan es el nombre anterior, conservado únicamente en nombres de archivos históricos. Esta revisión incorpora la segunda conversación y los dos moodboards aportados por el equipo.

## 1. Contexto y propósito

Miseño es un sistema contratado por colegios que personaliza el recorrido educativo de alumnos de primaria a partir de información del niño, sus docentes y su familia. El tutor organiza actividades, adapta explicaciones y propone agrupamientos.

La interfaz docente permite seguir lo que ocurre en el aula, identificar dónde hace falta intervención humana y aportar criterio pedagógico al recorrido de cada alumno.

El proyecto explora un futuro en el que parte de la enseñanza está delegada a un sistema. El prototipo debe hacer visibles las tensiones sobre responsabilidad, carga de trabajo, confianza en las métricas y autonomía docente.

Este documento propone un alcance inicial. Las alternativas discutidas en la conversación no se consideran decisiones cerradas.

## 2. Usuarios y momentos de uso

**Usuario principal:** docente de primaria a cargo de un grupo de alumnos con recorridos personalizados.

La conversación propone tres momentos de trabajo:

- **Antes de la jornada:** revisar planes y situaciones que merecen atención. La revisión y aprobación de cada plan todavía no está definida.
- **Durante la jornada:** atender dificultades, acompañar vínculos y organizar actividades en el espacio físico.
- **Después de la jornada:** revisar avances, registrar observaciones y preparar ajustes o conversaciones con las familias.

**Supuesto de diseño:** el docente necesita una visión del grupo y acceso al detalle individual. La interfaz debe evitar que tenga que abrir cada perfil para descubrir qué necesita atención.

## 3. Objetivo de la experiencia

Que el docente pueda responder:

- ¿Qué está pasando con mi grupo y quién necesita acompañamiento?
- ¿Qué está aprendiendo este alumno y qué apoyos ya se probaron?
- ¿Qué propone Miseño y qué puedo hacer frente a esa propuesta?
- ¿Qué información aportaron la familia y mis propias observaciones?

## 4. Rol docente propuesto

El docente acompaña situaciones que requieren presencia humana, observa lo que ocurre fuera de la pantalla y aporta contexto pedagógico que el sistema puede no captar.

**Propuesta inicial:** puede registrar observaciones, atender derivaciones del tutor y dejar planteada una revisión del recorrido. El poder para editar, aprobar, rechazar o suspender decisiones de Miseño debe definirse antes de prototipar esos controles.

La conversación también explora que el docente revise planes propuestos o decida contenidos. Esas alternativas tienen consecuencias distintas sobre su responsabilidad y carga laboral; este borrador no elige una como acuerdo del equipo.

## 5. Funcionalidades iniciales

| Función | Qué permite hacer | Estado |
|---|---|---|
| Vista del grupo | Identificar actividades en curso y situaciones que requieren atención sin entrar en cada alumno. | Propuesta de interfaz |
| Bandeja de situaciones | Consultar derivaciones del tutor y registrar su atención. | Basada en la conversación y el prototipo infantil |
| Ficha del alumno | Revisar temas, avances, dificultades y apoyos utilizados. | Propuesta de interfaz |
| Recorrido pedagógico | Consultar planes, cambios de materias, horarios y métodos. | Basada en el sistema conversado |
| Observación docente | Registrar lo observado en el aula para aportar contexto al sistema. | Basada en la conversación |
| Revisión de decisiones | Señalar una discrepancia con una propuesta de Miseño y dejar un registro. | Mecanismo propuesto; autoridad pendiente |
| Proyectos grupales | Consultar integrantes, actividad y criterios disponibles del agrupamiento. | Basada en la conversación |
| Contexto familiar | Consultar aportes pertinentes de la familia, identificados por su origen. | Propuesta; visibilidad pendiente |
| Historial de intervenciones | Recuperar cambios, observaciones y acciones del docente. | Propuesta de interfaz |

## 6. Derivación por dificultad académica

**Situación:** Joaquín sigue sin comprender un ejercicio de fracciones después de varios apoyos del tutor.

1. El tutor deriva la dificultad al docente. En el HTML infantil actual, esta derivación se anuncia y se registra como evento local; todavía no hay comunicación real entre interfaces.
2. En la vista del grupo aparece una situación pendiente asociada a Joaquín y al ejercicio.
3. El docente abre el detalle y consulta el enunciado, las respuestas y los métodos que ya se probaron.
4. Se acerca al alumno y lo acompaña presencialmente.
5. Registra una observación, por ejemplo: “Reconoce las partes, pero todavía confunde qué representa el denominador”.
6. Marca la intervención como realizada. El historial conserva qué ocurrió y qué observó el docente.

**Pendiente:** definir si cerrar esta intervención devuelve al alumno al ejercicio, mantiene la actividad actual o habilita una propuesta nueva del sistema.

**Criterio propuesto:** distinguir entre haber atendido una situación y haber resuelto la dificultad. Una intervención no implica que el aprendizaje esté logrado.

## 7. Revisión de un cambio de recorrido

**Situación:** Miseño propone sumar bloques de Matemática y dejar Música en pausa.

1. El docente identifica el cambio en el recorrido del alumno.
2. Consulta qué cambió, cuándo, cuál es su estado y qué fundamento ofrece Miseño.
3. Contrasta esa propuesta con lo que observó en clase y con el marco de contenidos de la escuela.
4. Registra una discrepancia o solicita revisar el cambio.
5. Puede consultar el estado de esa revisión y su resultado.

**Decisión central pendiente:** si el cambio requiere aprobación previa del docente, entra en vigencia automáticamente o puede ser suspendido por él. La interfaz debe reflejar con precisión la alternativa que el equipo elija.

La calidad de la explicación de Miseño también queda abierta: el prototipo infantil ofrece una justificación genérica. Mostrar más detalle al docente sería una decisión nueva de diseño.

## 8. Estructura tentativa de pantallas

- **Mi grupo:** panorama de la jornada y accesos a alumnos.
- **Situaciones:** pendientes, intervenciones en curso e historial de atención.
- **Recorridos:** planes individuales y cambios propuestos o aplicados.
- **Proyectos:** actividades grupales e integrantes.

Desde estas secciones se accede a la ficha de cada alumno, con su recorrido, observaciones, contexto disponible e intervenciones anteriores. La estructura es exploratoria.

## 9. Información y estados

**Propuestas para el prototipo:**

- Identificar si un dato proviene del alumno, la familia, el docente o una interpretación de Miseño.
- Distinguir fecha de registro y momento al que refiere la observación.
- Mostrar cuándo una lectura está desactualizada o no está disponible.
- Para situaciones de atención, explorar los estados “Pendiente”, “En atención” y “Atendida”, con registro de quién intervino.
- Para cambios de recorrido, distinguir propuestas y cambios aplicados. Sus estados finales dependerán del modelo de autoridad acordado.
- Mostrar foco y ánimo como lecturas del sistema, sin convertirlas automáticamente en una evaluación del alumno.

Las lecturas de la pulsera están simuladas en el HTML infantil. Su interpretación y presentación docente requieren definición propia.

## 10. Límites y decisiones pendientes

- **Autoridad pedagógica:** ¿qué decide el docente y qué decide Miseño? ¿Puede modificar un plan directamente?
- **Carga de revisión:** ¿revisa todos los recorridos o solamente cambios y situaciones seleccionadas? ¿En qué tiempo de su jornada?
- **Contenidos comunes:** ¿cómo se muestran los mínimos educativos que deben sostener los recorridos personalizados?
- **Agrupamientos:** ¿puede cambiar los equipos propuestos? ¿Qué información necesita para hacerlo?
- **Información emocional y familiar:** ¿qué ve, en qué circunstancias y cómo se gestionan datos sensibles o versiones contradictorias?
- **Límite del tutor:** ¿qué situaciones emocionales derivan a una persona y qué acción concreta se espera del docente?
- **Relación con familias:** ¿puede comunicarse desde esta interfaz o solamente registrar la necesidad de una conversación?
- **Responsabilidad de la empresa:** ¿cuándo interviene el representante pedagógico mencionado en la conversación?
- **Errores y desacuerdos:** ¿cómo se cuestiona una lectura de Miseño y quién resuelve la revisión?

## 11. Alcance del primer prototipo

**Propuesta actualizada:** priorizar el caso de discrepancia de información descrito en la sección 13. Construir una vista de grupo, un detalle de situación con evidencias y fuentes, y un registro de intervención con seguimiento. La derivación académica y el cambio de Matemática y Música quedan como casos secundarios.

Usar datos de ejemplo coherentes con el prototipo infantil. Evolucionar su lenguaje visual hacia el sistema de diseño de Miseño descrito en la sección 14. El HTML existente es un antecedente; los moodboards orientan la próxima iteración.

La integración real entre interfaces, los datos biométricos, la mensajería y los cambios automáticos del algoritmo quedan fuera de este primer prototipo propuesto.

## 12. Qué buscamos validar

En una primera prueba, observar si el docente puede:

- Encontrar al alumno que requiere acompañamiento y entender qué ocurrió.
- Recuperar los apoyos ya utilizados antes de intervenir.
- Registrar una observación y distinguir atención de resolución.
- Comprender qué propone Miseño y cuáles son sus propias atribuciones.
- Distinguir observaciones humanas de inferencias del sistema.

También explorar si la interfaz genera sobrecarga, favorece una confianza excesiva en las métricas o permite que el docente aporte una lectura diferente.

**Primera decisión para iterar:** definir si el docente supervisa un recorrido que Miseño ejecuta, aprueba sus cambios o lo dirige. Esa elección determina los controles y responsabilidades de toda la interfaz.

## 13. Caso prioritario de información contradictoria

### Problema que queremos explorar

La personalización puede sostener una adaptación inadecuada cuando utiliza información contradictoria, desactualizada o interpretada sin suficiente contexto. El docente necesita poder reconstruir qué ocurrió y aportar una lectura diferente.

La segunda conversación plantea dos hipótesis distintas: una menor red de acompañamiento fuera de la escuela y una discrepancia entre los datos que aporta la familia y las interacciones del niño. El prototipo no debe asumir que poca participación familiar equivale a un problema de aprendizaje ni que una discrepancia demuestra desinterés de los padres.

### Escenario de ejemplo

La familia de Tomi declaró que le gusta el fútbol. Miseño utiliza ese interés para presentar ejercicios. En varias sesiones, Tomi expresa que no le gusta esa temática y necesita apoyo. El sistema registra dificultades y el docente investiga si la adaptación está contribuyendo al problema.

Este escenario es ficticio. Los resultados de una actividad no permiten atribuir por sí solos una causa a la dificultad del alumno.

### Recorrido principal

1. El docente encuentra una situación pendiente: “Dificultad persistente · Revisar adaptación”.
2. Consulta las actividades, respuestas, apoyos utilizados y la interpretación de Miseño.
3. Abre “Información utilizada” y compara el aporte familiar con las expresiones del alumno. Cada registro muestra fuente, fecha y contexto.
4. Consulta qué relación con esos datos declara el sistema al explicar la adaptación. Si esa explicación no está disponible, la interfaz lo indica.
5. Habla con el alumno y registra su propia observación.
6. Deja la discrepancia “En revisión” y solicita revisar la adaptación. Esta acción es la propuesta del prototipo; no presupone autoridad para cambiar el plan directamente.
7. El historial conserva los aportes originales, la intervención y el estado de seguimiento.

### Requisitos del caso

- Mostrar en paralelo versiones contradictorias sin reemplazar una automáticamente por otra.
- Diferenciar una declaración explícita del alumno de un interés inferido por el sistema.
- No presentar como diagnóstico la alerta de dificultad.
- Permitir asociar una observación docente con las evidencias revisadas.
- Distinguir “Intervención realizada”, “Discrepancia en revisión” y “Dificultad resuelta”.
- Mostrar “Sin nuevos registros” cuando falta información, en lugar de interpretarlo como ausencia de acompañamiento.
- No dar por aprobado, aplicado o enviado un cambio si el prototipo solo registró una solicitud.

### Criterios de aceptación propuestos

- Desde la vista del grupo se puede abrir el caso y reconocer qué requiere atención.
- El docente puede identificar quién aportó cada dato y cuándo, sin confundirlo con la interpretación de Miseño.
- Puede guardar una observación y recuperar tanto esa observación como los registros previos.
- Una solicitud de revisión muestra su estado y qué efecto tiene sobre el plan actual. Si ese efecto está pendiente de diseño, el prototipo no simula una modificación efectiva.
- Cerrar una intervención no borra la discrepancia ni marca automáticamente un aprendizaje como logrado.

## 14. Sistema de diseño de Miseño

### Referencias y dirección visual

Referencias locales conservadas junto al PRD:

- [Moodboard de materialidad y carácter](moodboard_miseno_materialidad.png): robustez, juego, minimalismo y uso diurno; objetos compactos, cantos redondeados, materiales claros y acentos vivos.
- [Moodboard de interfaz y atmósfera](moodboard_miseno_interfaz.png): blancos y grises luminosos, superficies translúcidas, volúmenes suaves, esferas, recorridos y nodos con luz difusa y gradientes multicolor.

**Interpretación propuesta:** un entorno educativo diurno, claro y tangible, con una presencia tecnológica suave. La robustez se traduce en controles estables y estados inequívocos; lo lúdico aparece en formas y acentos. La interfaz docente necesita legibilidad y una jerarquía que permita trabajar con varios alumnos.

Los moodboards no especifican colores exactos, tipografías ni dimensiones. Los valores siguientes son propuestas de implementación para validar con el equipo.

### Paleta inicial

| Token | Valor propuesto | Uso |
|---|---|---|
| Fondo | `#F3F4F1` | Superficie general clara, ligeramente cálida |
| Superficie | `#FFFFFF` | Tarjetas, formularios y detalle de evidencias |
| Superficie secundaria | `#E9ECEB` | Agrupaciones, zonas de apoyo y controles inactivos |
| Texto principal | `#202A34` | Títulos y contenido |
| Texto secundario | `#53616C` | Metadatos y explicaciones |
| Acción principal | `#315DCE` | Botones, enlaces y selección |
| Foco | `#2449AA` | Indicador de navegación por teclado |
| Acento agua | `#89DCD6` | Nodos y visualizaciones de apoyo |
| Acento lavanda | `#B7ADE6` | Contextos y presencia del sistema |
| Acento coral | `#F19B83` | Detalles lúdicos e ilustraciones |
| Atención | `#8B520D` sobre `#FFF0D8` | Situaciones que requieren revisión |
| Confirmación | `#23674F` sobre `#E0F1E8` | Acciones completadas |
| Error | `#A43545` sobre `#FCE8EC` | Fallos o validación de formularios |

Agua, lavanda y coral se usan como acentos, no como texto pequeño sobre blanco. Los gradientes combinan estos tonos en elementos de presencia, sin colocarlos detrás de tablas o textos extensos. Verificar el contraste de cada combinación al implementar.

### Tipografía y jerarquía

- **Títulos:** Fredoka, pesos 400 y 500, como continuidad propuesta con el prototipo existente. Usarla con moderación para conservar el carácter amable.
- **Texto y datos:** Atkinson Hyperlegible, pesos 400 y 700. Alternativas locales: Verdana y sans-serif del sistema.
- **Escala orientativa:** título de pantalla 32 px; sección 24 px; tarjeta 20 px; cuerpo 16–18 px; metadatos 14 px. Interlineado del cuerpo entre 1,45 y 1,6.
- Evitar párrafos centrados y mayúsculas extensas. Alinear datos comparables y utilizar cifras tabulares en horarios y cantidades.

La elección tipográfica procede del antecedente HTML, no de una identificación exacta de las fuentes de los moodboards.

### Espacio, superficies y materialidad

- Retícula basada en múltiplos de 4 px: 4, 8, 12, 16, 24, 32 y 48.
- Márgenes de escritorio de 32 px y separación entre paneles de 24 px. En pantallas pequeñas, márgenes de 16 px.
- Tarjetas con 20–24 px de radio y relleno de 24 px; controles con 12–16 px de radio.
- Superficies de vidrio esmerilado en la estructura general, con una alternativa opaca cuando no haya soporte o el fondo afecte la lectura. Formularios y evidencias sobre fondos sólidos.
- Sombras suaves y bordes sutiles; evitar que los indicadores o controles dependan de relieves poco visibles.
- La referencia a materiales físicos informa la sensación de objetos estables y táctiles. No implica incorporar texturas fotográficas de césped o cartón detrás de la información.

### Componentes principales

| Componente | Contenido y comportamiento |
|---|---|
| Cabecera | Marca Miseño, espacio docente y grupo actual |
| Navegación | Mi grupo, Situaciones, Recorridos y Proyectos; selección visible y etiquetada |
| Tarjeta de alumno | Nombre, actividad y situación concreta; sin puntuación global de valor del alumno |
| Tarjeta de situación | Motivo, fecha, estado y acción para revisar |
| Panel de evidencias | Registros comparables con fuente, fecha, contexto y acceso al detalle |
| Etiqueta de origen | Alumno, Familia, Docente o Inferencia de Miseño; siempre con texto |
| Panel de discrepancia | Versiones en paralelo y estado de revisión, sin declarar un ganador automático |
| Formulario de intervención | Observación, contexto, acción realizada y seguimiento |
| Línea de tiempo | Eventos, cambios y responsables con secuencia temporal legible |
| Confirmación | Qué se guardó, dónde y qué sucederá después |

Los componentes deben contemplar estado vacío, carga, error y datos desactualizados. Las acciones no disponibles deben explicar su motivo.

### Nodos, árboles y presencia del sistema

La segunda conversación propone un árbol o grafo para el recorrido infantil. Para docentes, explorar una red simplificada de temas y relaciones con acceso al detalle y una alternativa en lista. La vista general debe seguir permitiendo encontrar pendientes sin interpretar un grafo complejo.

La esfera o el halo de Miseño puede usar luz difusa y gradientes para señalar presencia o procesamiento. Su animación no sustituye etiquetas como “Guardando” o “En revisión”.

La idea del árbol que pierde vitalidad, las luces rojas y verdes y los rankings se discutieron como recursos narrativos. No quedan adoptados en esta versión como indicadores docentes. Si se exploran, deben documentarse como una variante y evaluarse por la presión y comparación que generan.

### Movimiento e interacción

- Transiciones cortas, de aproximadamente 150–250 ms, para cambios de estado y apertura de paneles.
- Evitar destellos, pulsos permanentes y celebraciones que compitan con la atención al grupo.
- Respetar la preferencia de movimiento reducido.
- Usar iconos simples y redondeados con etiquetas. Reservar el color saturado para acciones o información relevante.
- Mantener visible el contexto del alumno al abrir una situación o registrar una intervención.

### Accesibilidad y adaptación

- Verificar contraste mínimo de 4,5:1 en texto normal y 3:1 en texto grande y controles relevantes.
- Ofrecer foco visible, navegación por teclado, etiquetas de formulario y mensajes de error asociados al campo.
- Proponer áreas de interacción de al menos 44 × 44 px, sin reducirlas para aumentar la densidad.
- Ningún estado depende solo de rojo, verde, brillo o animación.
- En escritorio, usar navegación estable y panel principal con detalle contextual. En pantallas pequeñas, apilar paneles manteniendo acceso a situación, evidencias y acción.
- El origen de un dato debe seguir siendo legible sin color y los gráficos deben ofrecer información equivalente en texto.

## 15. Definiciones abiertas para la próxima iteración

La prioridad es acordar qué ocurre cuando el docente encuentra una discrepancia: quién puede corregir un dato, cómo se conserva su procedencia, qué efecto tiene la revisión sobre la adaptación y quién valida el resultado.

El nombre Miseño está confirmado por la solicitud actual. La arquitectura física, las capacidades de la pulsera, la voz del tutor y la automatización real siguen fuera del alcance de este PRD docente inicial.

# PRD — Interfaz de docentes de Miseño

**Borrador 0.5 · 25 de noviembre de 2026 · Para iterar**

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

Usar datos de ejemplo coherentes con el prototipo infantil. La interfaz docente comparte el sistema de diseño de la app del alumno (sección 14): misma tipografía, mismos tonos por materia y mismos personajes.

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

### Decisión: un solo lenguaje para alumnos y docentes

Desde la versión 0.3, la interfaz docente usa el mismo sistema visual que la app del alumno (`scan-alumno`, v1.1). Un docente que mira la pantalla de un chico reconoce los mismos colores, profes y momentos del día que ve en la suya. La diferencia está en la densidad y el tono: el alumno ve un momento por vez; el docente ve el grupo entero y necesita comparar.

Los moodboards de materialidad e interfaz (`moodboard_miseno_materialidad.png`, `moodboard_miseno_interfaz.png`) siguen como referencia de carácter: diurno, claro, objetos estables con cantos redondeados y acentos vivos. La esfera translúcida de la versión 0.2 se reemplaza por Guio, que ya es la presencia de Miseño para los alumnos.

### Tipografía

| Uso | Fuente | Dónde |
|---|---|---|
| Interfaz y lectura | IBM Plex Sans 400, 500 y 600 | Títulos, cuerpo, botones |
| Voz y metadatos | IBM Plex Mono 400 y 500 | Lo que dice Guio, citas textuales de alumno y familia, fechas, horarios, etiquetas |

La regla es la misma que en la app del alumno: **lo que alguien dijo va en mono**. Así se distingue de un vistazo una declaración (de la familia, del alumno o de Miseño) del texto de la interfaz.

Escala: título de pantalla 32 px; sección 22 px; tarjeta 18 px; cuerpo 16 px; metadatos 12–14 px.

### Color

**Tono base (Miseño):** fondo `#E8F6FC`, suave `#BEE6F6`, nodo `#36BDE6`, botón `#0B7DA3`, texto `#08374A`. Es el mismo tono con el que abre la app del alumno.

**Un tono por materia**, con los valores de la app del alumno (fondo · suave · nodo · botón · texto):

| Materia | Profe | Tono |
|---|---|---|
| Matemática | Numi | `#FDEDEF` · `#F7C6CD` · `#E4566A` · `#B42A3E` · `#4D0F19` |
| Lengua | Otto | `#FEF1E6` · `#F9D0AE` · `#EF8638` · `#A64E0E` · `#4A2309` |
| Ciencias | Fini | `#EBF7EC` · `#C0E6C8` · `#42BE62` · `#1D7D3A` · `#0D3B1C` |
| Dibujo | Dona | `#F2EDFF` · `#D9CBFF` · `#8A4FFF` · `#6131D6` · `#25104F` |
| Gastronomía | Rolo | `#FFEEF5` · `#FFC7DD` · `#FF5FA2` · `#C42A6C` · `#4D0C29` |
| Huerta | Numi y Fini | `#F2F8E4` · `#D5E9AE` · `#8DBF3F` · `#4D7A12` · `#1F3307` |
| Recreo | — | `#FDF7DE` · `#F4E29C` · `#E2B41C` · `#7E6000` · `#3B2E00` |
| Historia, Música | sin profe todavía | neutro `#EEF3F5` · `#D3DEE3` · `#7C939E` · `#3E5A66` · `#1E3640` |

En la interfaz docente el tono de materia identifica, no alarma: tiñe avatares, chips de materia, el encabezado del alumno y los nodos de la jornada. **Las acciones principales siempre usan el botón de Miseño (`#0B7DA3`)**, nunca el rojo de Matemática, para que un botón no se lea como alerta.

**Estados y orígenes** (con texto siempre; nunca solo color):

| Significado | Colores |
|---|---|
| Atención / pendiente | `#633806` sobre `#FAEEDA` (el "casi" del alumno) |
| Hecho / confirmado | `#085041` sobre `#E1F5EE` (el "ok" del alumno) |
| Error | `#9E2234` sobre `#FDEDEF` |
| Origen Familia | verde ok |
| Origen Alumno | `#3D1F80` sobre `#F2EDFF` |
| Origen Docente | contorno suave, sin relleno |
| Origen Miseño | tono base + Guio en miniatura |

### Personajes

Los mismos de la app del alumno (`img/`, estado *reposo* salvo que se indique):

- **Guio** es Miseño: marca en la cabecera, saludo de inicio (estado *habla*), interpretación y recomendaciones (estado *piensa*), avisos de confirmación y la pestaña "Miseño" junto a "Familia".
- **Numi, Otto, Fini, Dona y Rolo** firman sus materias: aparecen en la jornada, en la ficha del alumno y en cada derivación ("Derivó Numi"). Así el docente sabe qué profe virtual pidió ayuda.
- Los personajes acompañan una etiqueta; nunca la reemplazan.

### Formas y componentes

- Tarjetas blancas planas sobre el fondo de tono, radio 24 px, sin sombras ni vidrio esmerilado.
- Botones en píldora (radio 99 px), mínimo 48 px de alto: primario relleno; secundario blanco con borde suave, como "Repetir" en la app del alumno.
- Etiquetas y chips en píldora y mono; el chip de materia lleva el punto de color del nodo.
- **La jornada:** la misma línea de tiempo vertical del alumno (Matemática 8:30 · Lengua 9:30 · Recreo 10:20 · Huerta 10:40), con nodos huecos, el actual relleno con halo y los profes debajo. En móvil se vuelve horizontal.
- Las líneas de tiempo del historial usan los mismos nodos.

### Estructura de la interfaz (v0.4, a partir del Figma de Candela)

- **Menú lateral fijo:** Grupo, Recorridos, Reuniones y Proyectos, con la marca arriba y el docente abajo. En móvil pasa a una barra superior.
- **Inicio:** solo tres tarjetas grandes, sin logo ni texto (la marca sería redundante): Grupo en celeste, Recorridos en verde, Proyectos en rosa. Grupo muestra cuántas situaciones esperan.
- **Grupo:** la jornada a la izquierda; arriba "Para acompañar"; abajo todo el grupo con búsqueda y filtro por materia. Cada tarjeta abre la ficha del alumno.
- **Ficha del alumno (nueva):** anillo con la inicial, edad, cumpleaños y familia; intereses (hobbies y barras por área); aprendizaje como árbol (una rama por materia, una hoja llena por logro); amigos principales (abren su ficha); su progreso comparado consigo mismo; estado sensorial del día, tomado del check-in de la app del alumno; información médica restringida; próxima reunión.
- **Recorridos:** carrusel de alumnos y encabezado en el tono de su materia, con "Ver ficha" y "Registrar intervención".
- **Reuniones (nueva):** próximas y pasadas, con familias y con el equipo. Para cada una, Miseño propone temas a partir de las fuentes (Guio piensa) y el docente registra acuerdos. Se puede agendar una nueva.
- **Proyectos:** chip de materia y profes del proyecto. La huerta pasa a llamarse "El recetario de la huerta", como en la app del alumno.

### Árbol de aprendizaje (v0.5)

- **Forma:** una rama por materia que sale del tronco y crece de 1º a 6º grado. Cada hoja es un dominio de contenido de ese grado.
- **Ramas:** todos los chicos tienen las cuatro del núcleo (Lengua, Matemática, Ciencias, Historia). Las optativas (Dibujo, Música, Programación, Gastronomía) aparecen solo en quien las cursa y desde el grado en que empezó; el tramo anterior se dibuja punteado.
- **Fuentes:** Lengua y Matemática, Common Core (grados 1 a 6, con su código: 3.NF, RL.5…). Ciencias e Historia, NAP de Ciencias Naturales y Ciencias Sociales. Dibujo y Música, NAP de Educación Artística en 1º ciclo y propuesta propia en 2º ciclo. Programación, NAP de Educación Digital, Programación y Robótica (que se organizan por ciclo) repartidos por grado. Gastronomía, propuesta propia.
- **Estados de cada hoja:** logrado (llena), en curso (más grande, con borde), a reforzar (llena con anillo ámbar punteado) y por venir (vacía). Ninguno depende solo del color.
- **Dónde vive:** en la ficha como tarjeta chica; al tocarla se abre a pantalla completa. Al tocar una hoja, un panel muestra el contenido, el grado, el código y la fuente, y las actividades donde lo trabajó, con acceso a Recorridos.

### Menos texto (v0.5)

- Cada pantalla tiene una sola acción con palabra; las secundarias son íconos con etiqueta flotante (al pasar el mouse o con el teclado) y `aria-label`.
- Sin subtítulos de pantalla ni notas que expliquen la interfaz. Se conservan los datos (fechas, fuentes, resultados).

### Datos sensibles en la ficha

- La información médica no se muestra en el prototipo: queda como espacio restringido que carga la familia o el equipo de orientación.
- El estado sensorial muestra solo el check-in del día (ánimo y sueño) y lo que Guio le dijo al alumno; no se guarda un historial visible.
- La curva de progreso compara al alumno consigo mismo; nunca muestra posiciones ni promedios del grupo.

### Movimiento y accesibilidad

- Entradas cortas (240 ms), aparición desde abajo como en el alumno; el logo de Guio entra con un pequeño rebote en el splash.
- Sin pulsos permanentes ni celebraciones; respeta `prefers-reduced-motion`.
- Contraste mínimo 4,5:1 en texto; foco visible de 3 px en el color de botón; áreas táctiles de 44 px o más.
- Ningún estado depende solo del color ni de un personaje.

### Pendientes del sistema

- Historia y Música no tienen profe en la app del alumno: definir si se suman personajes o si esas materias quedan fuera del día del alumno.
- La jornada del docente está fija al día de Joaquín; falta decidir si cada alumno tiene horarios distintos y cómo se resume eso para el grupo.

## 15. Definiciones abiertas para la próxima iteración

La prioridad es acordar qué ocurre cuando el docente encuentra una discrepancia: quién puede corregir un dato, cómo se conserva su procedencia, qué efecto tiene la revisión sobre la adaptación y quién valida el resultado.

El nombre Miseño está confirmado por la solicitud actual. La arquitectura física, las capacidades de la pulsera, la voz del tutor y la automatización real siguen fuera del alcance de este PRD docente inicial.

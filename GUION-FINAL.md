# Módulo Administrativo

**Orden en el evento:** LDP → **nosotros (LDE Backend, Módulo Administrativo)** → Harness
**Duración objetivo:** 12 minutos
**Slides:** 5
**Presentadores:** 4 (Tyrone, Abner, Marvin, Alejandro)

> Este documento es la versión final. Contiene, por cada slide:
> **(a)** qué va en pantalla — para el equipo de diseño (fuente única con `prompt-google-slides.md`),
> **(b)** el diálogo con nombre delante de cada línea — guion para los presentadores.

> **Ángulo central:** el módulo Administrativo es el corazón de la seguridad de la banca empresa. Cada acción sobre un usuario arrastraba su propia lógica de aprobación duplicada seis veces. Con IA, el refactor postergado se hizo viable en un solo día — con tests, sin bajar el listón de seguridad. **El foco de la charla es cómo la IA nos apoyó, no cómo la implementamos.**

---

## Roles de presentadores

| Presentador | Slides | Rol |
| :--- | :--- | :--- |
| **Tyrone** | Slide 1 (apertura) | Intro breve: da la bienvenida y presenta al equipo |
| **Abner** | Slide 1 (contexto) · Slide 2 · cierre de Slide 5 | Contexto del módulo Administrativo + reencuadre "antes vs. después del día del dev" + cierre emocional |
| **Marvin** | Slide 3 | Los cambios grandes dejaron de ser un evento |
| **Alejandro** | Slides 4 y 5 | Motor de aprobaciones (el caso) + los números y el chiste |

**Handoffs (4 en toda la charla, cada uno con cambio de posición — sin interrupciones cruzadas):**

1. Dentro de Slide 1: **Tyrone → Abner** (tras la bienvenida)
2. Al final de Slide 2: **Abner → Marvin**
3. Al final de Slide 3: **Marvin → Alejandro**
4. Al final de Slide 5, para la línea de cierre: **Alejandro → Abner**

> **Nota:** Abner presenta de corrido desde el contexto (Slide 1) hasta el reencuadre (Slide 2). El paso de Slide 1 a Slide 2 es solo cambio de filmina — mismo presentador, sin handoff.

Cada presentador cierra sus propios slides. Nadie interrumpe a nadie. Los cambios son físicos (uno se corre, el otro camina al centro), no de diálogo.

---

## FILMINA 1 — Apertura + contexto del módulo (Tyrone → Abner)

### En pantalla

**Título grande, 3 líneas:**

> **El módulo Administrativo tenía 6 caminos para lo mismo.**
> **Con IA lo unificamos en un motor.**
> **Un enfoque unificado para la eficiencia operativa.**

**Debajo, en tipografía chica y discreta:**

> *crear · editar · bloquear · desbloquear · eliminar · reenviar invitación*

### Diseño

- Portada tipográfica pura, sin imágenes.
- Línea 1: gris apagado. Línea 2: color de acento, la más grande. Línea 3: tono medio.

### Diálogo (~2:00 — Tyrone ~0:30 · Abner ~1:30)

**Tyrone** *(al centro del escenario, cálido — abre la charla)*:
> "Buenas tardes a todos. Somos parte del equipo de LDE Backend. Yo soy Tyrone, y me acompañan Abner, Marvin y Alejandro."

**Tyrone** *(mira al público)*:
> "En los próximos minutos les vamos a contar, en primera persona, cómo la IA nos apoyó en el módulo más sensible de toda nuestra aplicación."

**Tyrone** *(presenta a Abner, prepara handoff)*:
> "Para arrancar, Abner les va a contar de qué se trata ese módulo y por qué era tan delicado."

*[Tyrone se corre un paso a un lado. Abner camina al centro.]*

**Abner** *(toma el centro, cálido)*:
> "Gracias, Tyrone. ¿Qué es el módulo Administrativo? Es donde vive la seguridad de la banca empresa. Es el que decide quién es usuario de nuestros clientes corporativos, qué puede hacer cada uno, y quién autoriza cada cambio."

**Abner**:
> "Cada vez que se crea un usuario, se le asigna un permiso, se bloquea una cuenta o se aprueba una operación sensible, esa decisión pasa por este módulo. Un bug ahí no es una casilla mal alineada — es un usuario que aprueba algo que no debía. Es una operación que se ejecuta sin la firma correcta. Es un riesgo de negocio y de compliance."

**Abner** *(pausa, cambia el ritmo)*:
> "Y era también el más frágil del sistema. Cada acción sobre un usuario — crearlo, editarlo, bloquearlo, desbloquearlo, eliminarlo, reenviarle la invitación — tenía **su propia lógica de aprobación duplicada**. Seis caminos distintos para hacer conceptualmente lo mismo."

**Abner** *(baja un poco el tono, honesto)*:
> "Cambiar una regla implicaba tocar seis lugares y no olvidarse de ninguno. En un módulo de seguridad, ese margen de error es inaceptable. Unificar todo eso era un refactor de varios sprints con riesgo muy alto y un gran entendimiento de las reglas de negocio. Con las estimaciones tradicionales — no era pereza, era prudencia."

**Abner** *(pausa dramática)*:
> "Y sin embargo — en un solo día, el 22 de junio — el equipo lo unificó. Con tests. Sin bajar el listón de seguridad."

**Abner** *(deja la pregunta en el aire, avanza a la siguiente filmina)*:
> "¿Qué cambió para que ese refactor postergado durante meses se hiciera en un día?"

*[Abner se queda en el centro. Cambia la filmina a la Slide 2.]*

---

## FILMINA 2 — La IA amplió nuestra capacidad, no cambió nuestro criterio (Abner)

### En pantalla

**Título:**

> **La IA amplió nuestra capacidad, no cambió nuestro criterio.**

**Dos columnas comparativas, mismo tamaño, lado a lado:**

- **Columna izquierda (gris, "Antes de la IA"):**
  - Refactors sensibles → **postergados**
  - Cambios grandes → **paraban al equipo**
  - Tests → **si sobraba tiempo**
  - Refactor del motor → **inviable en el corto plazo**

- **Columna derecha (color de acento, "Con IA"):**
  - Refactors sensibles → **se hacen con red de seguridad**
  - Cambios grandes → **no detienen al resto del equipo**
  - Tests → **parte del entregable, siempre**
  - Refactor del motor → **1 día**

**Debajo, ancho completo, tipografía media:**

> *"El mismo equipo, con más capacidad para lo que siempre supimos que había que hacer."*

### Diseño

- Cuadro comparativo limpio, dos columnas del mismo ancho.
- Cada fila del "Antes" alineada horizontalmente con su contraparte del "Con IA".
- Ícono minimalista al inicio de cada fila (o número: 1, 2, 3, 4) — no íconos genéricos de IA.
- **Sin código, sin logos, sin jerga técnica en pantalla.**
- La leyenda inferior ocupa un ancho completo, en tono medio, sin comillas grandes.

### Diálogo (~2:30)

**Abner** *(sigue en el centro, calmo, retoma su propia pregunta)*:
> "Esa pregunta — qué cambió — tiene una respuesta fácil y una respuesta interesante. La fácil es 'somos más rápidos'. Y sería cierta a medias — porque quedarse en esa mitad se queda corto."

**Abner** *(al público)*:
> "Lo interesante no es que el equipo haga lo mismo en menos tiempo. Es que **ganó capacidad para hacer cosas que antes eran inviables** — no por falta de criterio, sino porque el costo y el riesgo las mantenían fuera de alcance. Ese es el cambio que queremos mostrarles."

**Abner** *(señala la columna izquierda)*:
> "El día del dev backend antes de la IA se parecía a esto. Los refactors del control de acceso — el corazón de la seguridad — se posponían sprint tras sprint, porque el costo de tocar seis lugares a la vez era demasiado alto. Los cambios transversales — los que afectan varias APIs a la vez — implicaban parar al equipo entero para coordinar. Los tests se escribían si sobraba tiempo, después de la funcionalidad. Y el refactor que les acabo de describir — unificar seis caminos en un motor — era, en términos prácticos, inviable en el corto plazo."

**Abner** *(pausa breve, señala la columna derecha)*:
> "El día del dev backend con IA se parece a esto otro. Los refactors sensibles se hacen — con red de seguridad, con tests, con revisión. Los cambios transversales dejaron de detener al resto del equipo. Los tests son parte del entregable, no un extra que aparece si hay tiempo. Y el refactor 'inviable' tomó un día."

**Abner** *(pausa, cambia de tono, mira al público)*:
> "¿Qué es lo que hace la diferencia? No es que la IA escriba código más rápido — es que aplica la disciplina que como equipo no siempre alcanzábamos a mantener. No se olvida de un test. No se olvida de un permiso. No rompe una convención porque estaba cansada un viernes."

**Abner** *(al público, con énfasis pero sin épica)*:
> "Y esa disciplina — sostenida, sin excepciones — es lo que hizo posible tocar el módulo más sensible del sistema sin bajar el listón. Los próximos dos slides son evidencia concreta de eso."

**Abner** *(mira hacia Marvin, prepara handoff)*:
> "Marvin les cuenta el primer ejemplo — los cambios grandes."

*[Abner se corre un paso. Marvin camina al centro.]*

---

## FILMINA 3 — Los cambios grandes dejaron de ser un evento (Marvin)

### En pantalla

**Título:**

> **Los cambios grandes dejaron de ser un evento.**

**Dos diagramas horizontales lado a lado, mismo tamaño:**

- **Izquierda (gris, "Antes"):** 6 APIs con flechas rojas de bloqueo convergiendo hacia una figura central con cartel *"TODOS PAREN"*. Caótico, embudo.
- **Derecha (color de acento, "Ahora"):** las mismas 6 APIs. Un dev aplica el cambio en local; un ícono discreto de IA propaga; siluetas de otros devs trabajan en paralelo con flechas verdes hacia sus features. Fluido.

**Pie:** *"Antes: reunión + roadshow + 5-6 PRs. Ahora: un dev aplica · IA propaga · el resto del equipo no se detiene."*

### Diseño

- Los dos diagramas ocupan la mitad superior de la filmina, mismo tamaño (no como el slide 4).
- Pie en una sola línea, tipografía media.

### Diálogo (~2:30)

**Marvin** *(entra al centro, retoma el hilo)*:
> "Gracias, Abner. El primer ejemplo concreto de ese cambio: **los cambios grandes**."

**Marvin** *(al público, define el terreno)*:
> "En backend, cada tanto aparece lo que llamamos un cambio transversal — un ajuste que impacta a varias APIs al mismo tiempo. Una regla de autenticación que se comparte, un contrato entre servicios que se ajusta, una librería que hay que subir de versión, un patrón que se decide cambiar. No es un feature nuevo. Es infraestructura invisible que sostiene lo que ya existe."

**Marvin** *(contando el mundo pre-IA)*:
> "En el mundo de antes, este tipo de cambio era el **peor** tipo de trabajo. Había que parar al equipo entero. Reunión para explicar por qué. Roadshow para asegurarse de que todos lo aplicaran igual. Cinco o seis pull requests que salían en cascada. Alguien inevitablemente rompía algo. Alguien inevitablemente quedaba esperando la review de otro. Y todo esto — atención — sin agregar una sola funcionalidad nueva. Solo mantener lo que ya funcionaba."

**Marvin** *(pausa)*:
> "El resultado natural era que hacíamos los cambios **estrictamente necesarios**. Todo lo que era 'mejora' o 'limpieza' se postergaba porque el costo de coordinación era prohibitivo."

**Marvin** *(historia concreta — reemplazar placeholder)*:
> "Les cuento uno concreto de las últimas semanas: **[DESCRIBIR EL CAMBIO TRANSVERSAL — ej: bump de una librería compartida, ajuste de una regla de aprobación entre servicios, unificación de un contrato, migración de un patrón]**. En el mundo de antes, ese cambio hubiera implicado la coordinación que les acabo de describir — fácil, dos o tres días con parte del equipo dedicado."

**Marvin** *(contraste)*:
> "Con IA, ese mismo cambio se aplicó en local en una de las APIs. La IA lo propagó a las demás respetando el patrón, con tests, sin descoordinar nada. Quedó terminado en **[X horas]**. Y — esto es lo importante — nadie más del equipo tuvo que parar. Siguieron con sus features."

**Marvin** *(cierra la reflexión)*:
> "El multiplicador es lo interesante: si antes cada cambio transversal me costaba **X horas a mí y obligaba a robarles horas al resto del equipo**, había un techo natural — solo hacíamos los imprescindibles. Ahora se pueden hacer los que hacen falta para mantener el código sano, sin ese impuesto de coordinación."

**Marvin** *(remate)*:
> "Los cambios grandes dejaron de ser un evento. Son otro ticket más. Y con eso, dejamos de acumular deuda técnica en los rincones que antes daban miedo tocar."

**Marvin** *(mira a Alejandro, prepara handoff)*:
> "Y el rincón más grande que llevábamos posponiendo era el que Abner les mencionó al arranque. Alejandro les cuenta cómo terminó."

*[Marvin se corre a un lado. Alejandro camina al centro.]*

> **NOTA:** el ejemplo concreto del cambio transversal es lo que sostiene este slide. Antes del ensayo, decidir cuál se cuenta — cuanto más pequeño y familiar, mejor. Tener a mano: qué se cambió, cuántas APIs impactó, cuánto tomó real, cuánto hubiera tomado antes.

---

## FILMINA 4 — El motor de aprobaciones · antes vs. después (Alejandro)

### En pantalla

**Título:**

> **6 acciones duplicadas → 1 motor. En un día.**

**Dos diagramas lado a lado (el pico visual del deck):**

- **Izquierda (gris, "Antes", MÁS GRANDE — 55% del ancho):** seis cajas separadas y repetidas — *Crear · Editar · Bloquear · Desbloquear · Eliminar · Reenviar invitación* — cada una con un bloque interno idéntico *"aprobación + permisos"*. Repetición visible a distancia.
- **Derecha (color de acento, "Ahora", MÁS CHICA — 35% del ancho):** una sola caja central grande — **"Motor de Aprobaciones"** — con las seis acciones entrando como flechas.

**Badge en la esquina inferior derecha:** *"1 día · +2.200 líneas de tests · −4.600 líneas duplicadas"*

**Pie:** *"La IA no es más lista que nosotros. Es más disciplinada."*

### Diseño

- **La diferencia de tamaño entre el "antes" y el "ahora" es el elemento dominante.** El refactor borró más líneas de las que agregó — que el ojo entienda "se hizo más chico" en 2 segundos.
- Sin hashes de commit en la filmina visible.
- Sin bullets en pantalla — solo los diagramas, el badge y el pie.

### Diálogo (~3:00)

**Alejandro** *(entra con energía, va al punto)*:
> "Este es el caso que Abner les describió al arranque. Y que se hizo posible por lo que acaba de contar Marvin."

**Alejandro** *(señala el "antes")*:
> "En el diagrama de la izquierda, el antes: seis cajitas, seis lógicas de aprobación duplicadas. Crear un usuario, editarlo, bloquearlo, desbloquearlo, eliminarlo, reenviar la invitación — cada una con su propio bloque interno de 'aprobación y permisos'. Repetido seis veces. Con pequeñas diferencias que solo el equipo conocía."

**Alejandro** *(al público, aterriza el problema)*:
> "Cambiar una regla implicaba tocar **seis lugares** y no olvidarse de ninguno. En un módulo de seguridad, ese margen de error es inaceptable. Cada vez que aparecía una regla nueva de compliance, el equipo tenía que aplicarla seis veces, revisarla seis veces, testearla seis veces. Un solo olvido y una acción sensible quedaba sin protección."

**Alejandro** *(pausa, cambia el tono, más honesto)*:
> "Este refactor estaba postergado desde hacía muchos sprints. No por falta de ganas — el equipo lo pedía en cada planning. Era por costo. Unificar las seis lógicas exigía entender profundamente qué reglas se compartían, cuáles diferían por acción, y garantizar que ninguna combinación quedara fuera. Estimado tradicional: entre **tres y cinco sprints**, con riesgo alto de bug de seguridad si se ejecutaba mal."

**Alejandro** *(señala el "después")*:
> "El diagrama de la derecha: un solo motor. Todas las acciones entran ahí. Las reglas viven en un lugar. Los tests cubren cada combinación. Cambiar una regla ahora es tocar **un solo lugar**. Fin."

**Alejandro** *(pausa, cambia el tono)*:
> "¿Y cuántos días tomó ese refactor de 'tres a cinco sprints'?"

*[pausa 2-3 segundos]*

**Alejandro**:
> "Un día. 22 de junio."

**Alejandro** *(leyendo el badge, con énfasis en cada número)*:
> "Cinco mil novecientas líneas agregadas. **Dos mil doscientas de ellas son tests**. Y en paralelo se borraron **cuatro mil seiscientas líneas de lógica duplicada**. El módulo terminó con **menos código y más tests** que el día anterior."

**Alejandro** *(al público, honesto — momento clave)*:
> "Y quiero dejar algo claro, porque es fácil malinterpretar esto: **la IA no diseñó el motor**. Lo diseñó el equipo. La IA hizo otra cosa — garantizó que no se olvidara ninguna de las seis acciones, que los tests estuvieran desde el arranque, y que las reglas del negocio se aplicaran sin excepciones."

**Alejandro** *(historia concreta de disciplina)*:
> "Un ejemplo específico: uno de los caminos, el de reenviar invitación, tenía una regla particular que solo aplicaba en ciertos escenarios de la banca empresa. Detectar esa excepción en un refactor manual hubiera sido responsabilidad del dev — recordar, revisar, no olvidar. La IA la identificó desde la primera pasada y propuso una prueba unitaria específica para cubrirla. Ese tipo de cosas es lo que hizo posible el 'en un día'."

**Alejandro** *(el punchline)*:
> "La IA no es más lista que nosotros. Es más disciplinada. Y esa disciplina — aplicar el patrón sin olvidarse de un permiso, un enmascaramiento, ni un test — es lo que hizo posible tocar un módulo de seguridad en un día **sin bajar el listón**."

**Alejandro** *(prepara el último slide, sin moverse — mismo presentador continúa)*:
> "Ahora, los números que sostienen esta historia."

---

## FILMINA 5 — Los números y la invitación (Alejandro · cierre de Abner)

### En pantalla

**Título:**

> **Los números que sostienen la historia.**

**Dos columnas con un solo número gigante cada una, lado a lado:**

- **Columna izquierda (gris) — "Antes de la IA · 1 mayo → 8 junio":**
  - **+5%** (número cartelesco, gris apagado)
  - Subtítulo debajo: *"Desvío tiempo real vs. estimado"*

- **Columna derecha (color de acento) — "Con IA · 9 junio → 13 julio":**
  - **−17%** (número cartelesco, verde #0E9F6E)
  - Subtítulo debajo: *"Desvío tiempo real vs. estimado"*

**Debajo, ocupando todo el ancho:** *"Mismo equipo. Mismo módulo. Otra herramienta."*

**Pie discreto:** *"El método está en el repo — replicable por cualquier equipo de LAFISE."*

### Diseño

- Un solo número gigante por columna, CARTELESCO — que se lea desde el fondo del auditorio.
- Máximo respiro visual — el slide vive de dos porcentajes y una leyenda de cierre.
- La leyenda "Mismo equipo. Mismo módulo. Otra herramienta." ocupa la mitad inferior, grande.

### Diálogo (~2:30)

**Alejandro** *(sigue en el centro)*:
> "Los números. Corto y directo."

**Alejandro** *(señala la columna izquierda, luego la derecha)*:
> "En Jira, el desvío entre lo estimado y lo real. **Antes de la IA — del 1 de mayo al 8 de junio — +5%.** Entregábamos ligeramente por encima del estimado. **Con IA — del 9 de junio en adelante — −17%.** Entregamos consistentemente por debajo del estimado."

**Alejandro** *(al público, honesto — la salvaguarda)*:
> "Y este es el número **conservador**: mucho del trabajo con IA no queda registrado explícitamente en la tarea. El uso real es mayor que lo que muestran los números."

**Alejandro** *(tono más reflexivo, sin épica)*:
> "Pero el punto no es la velocidad. El punto es que se hizo viable un refactor postergado del control de acceso — el módulo más sensible del sistema — **sin bajar el listón de seguridad**. Y que los cambios grandes que antes paraban al equipo entero, hoy se aplican sin fricción."

**Alejandro** *(cambia a tono coloquial, con sonrisa — introduce el chiste)*:
> "Y hay una consecuencia inesperada que tengo que confesar. Hasta hace poco, cuando algo se atrasaba en LDE, la respuesta fácil era 'el backend'. **Éramos nosotros**. Ahora que la IA nos aceleró, el cuello de botella se mudó."

**Alejandro** *(mirando a un punto del público con una sonrisa)*:
> "Perdón, **[NOMBRE DEL PRODUCT LEAD]** — nos toca ir a hablar."

*[pausa 2-3 segundos para la risa]*

**Alejandro** *(recupera el tono, sin épica)*:
> "Fuera de broma: lo que aprendimos en el módulo administrativo **es replicable por cualquier equipo de LAFISE**. Está documentado, está medido, y está disponible."

**Alejandro** *(mira a Abner, prepara handoff)*:
> "Abner, cierre."

*[Alejandro se corre un paso. Abner camina al centro para el cierre.]*

**Abner** *(cerrando, cálido, mira al público)*:
> "Lo que les mostramos hoy no es una promesa. Es lo que ya está pasando en el módulo más sensible de LAFISE Digital Empresas. Con gusto acompañamos a los primeros equipos que quieran replicarlo. Gracias."

*[Aplauso. Fin de la exposición.]*

---

## Notas transversales de estilo (para los 4 presentadores)

- **Foco de la charla:** cómo la IA nos apoyó, **no cómo la implementamos**. Nada de detalles de setup, arquitectura interna, ni herramientas específicas del equipo.
- **Tono:** colaborativo, no acusatorio, no presumido. Cualquier frase que suene a "nosotros sí pudimos" debe reescribirse.
- **El protagonista es el impacto de la IA**, no las personas. Cuando alguien diga "nosotros", que el crédito quede en la disciplina de la herramienta y en los resultados.
- **Sin callback a LDP:** el arranque de Tyrone es standalone. LDP no cubre lo que nosotros vamos a apalancar, así que no hay tejido conectivo — no forzarlo en vivo tampoco.
- **Sin interrupciones cruzadas.** Cada presentador cierra sus propios slides. Los handoffs son de posición, no de diálogo.
- **Palabras y conceptos PROHIBIDOS** *(no van en pantalla ni en el discurso — decisión del equipo)***:**
  - `workspace unificado`, `workspace del equipo`, cualquier mención al workspace en general.
  - `memoria compartida`, `conocimiento persistente`, `el conocimiento vive en el repo`.
  - `skills`, `reglas del equipo`, `marco de trabajo`, `marco unificado`.
  - `pipeline`, `executor`, `applicator`, `FeatureType`, `handler`, `catalog`, `Engram`, `MCP`, `preflight-hard-stop`, hashes de commit.
- **Palabras que SÍ van en pantalla:** *permisos, aprobaciones, usuarios, cambios grandes, refactor, motor, tests, seguridad, disciplina.*
- **Palabras y números a evitar en toda la charla (son del talk del harness que va después nuestro):**
  - Términos: *"arnés"*, *"harness"*, *"las cinco piezas"*, *"los cinco componentes"*.
  - Números macro: *"11 equipos"*, *"4 países"*, *"más de 85 devs"*, *"4.295 anotaciones"*, *"×125"*.
- **Chiste con el product lead:** en Slide 5 solamente, dicho por Alejandro. Si no hay confianza con el nombre nombrado, reemplazar por *"el equipo de producto"*. **Avisarle antes al product lead** si va con nombre.
- **Pausas dramáticas** después de cada número ancla. Silencio > relleno.
- **Cerrar con invitación abierta**, nunca con logro.
- **Sin nombres propios en las filminas visibles.**

---

## Lo que falta completar antes de la presentación

1. **Ejemplo concreto de cambio transversal para Filmina 3.**
   - Elegir uno real de las últimas semanas.
   - Anotar: qué se cambió, cuántas APIs impactó, cuánto tomó (real), cuánto hubiera tomado (estimado antes).
   - Reemplazar `[DESCRIBIR EL CAMBIO TRANSVERSAL]` y `[X horas]` en el diálogo de Marvin.

2. **Nombre del product lead para el chiste de Filmina 5.**
   - Decidir si va con nombre o queda como *"el equipo de producto"*.
   - Si va con nombre — **avisarle antes** para que sepa que se viene.
   - Reemplazar `[NOMBRE DEL PRODUCT LEAD]` en el diálogo de Alejandro.

3. **Ensayo mínimo de coreografía.**
   - Un pase completo con los 4 en un mismo espacio, ~30 minutos.
   - Enfocarse en los 4 handoffs: Tyrone → Abner, Abner → Marvin, Marvin → Alejandro, Alejandro → Abner (cierre).
   - Cronometrar cada slide para no pasarse de 12 minutos totales.
   - No memorizar palabra por palabra — memorizar el orden de cada bloque.

4. **Regenerar Slide 2 en Google Slides.**
   - El prompt `prompt-google-slides.md` ya está actualizado con el nuevo cuadro comparativo antes/con IA.
   - Regenerar la diapositiva 2 en el deck (usar el prompt de iteración "Si el slide 2 tiene la versión vieja").
   - Verificar contra el checklist manual (punto 2) que no queden íconos genéricos ni términos prohibidos.

---

## Anexo — Referencias

- **Deck largo con detalles técnicos y comandos para regenerar cifras:** `2026-07-13-ai-success-case-modulo-administrativo.md` (carpeta padre).
- **PPTX text (input del equipo de diseño):** `Modulo Administrativo LDE - PPTX.txt` (carpeta padre).
- **Prompt para generar los slides con IA:** `prompt-google-slides.md` (misma carpeta).

## Fin del documento

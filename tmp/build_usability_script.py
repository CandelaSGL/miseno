from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
pages=[
[
('title','Prueba con usuarios'),('subtitle','Miseño · Aceptación de una próxima actividad'),
('meta','Guión de moderación | 11 de noviembre de 2026 | 25 a 30 minutos'),
('h','Objetivo'),
('p','Evaluar si una docente puede entender una recomendación de Miseño, contrastarla con los registros del alumno y decidir si corresponde aceptarla como próxima actividad. Comprobar si identifica qué cambió, quién tomó la decisión y dónde puede recuperar el registro.'),
('h','Hipótesis'),
('bullet','La docente encuentra la recomendación del alumno seleccionado y distingue una propuesta de una actividad ya programada.'),
('bullet','Antes de aceptar, consulta respuestas y apoyos utilizados; no se limita a la interpretación de la IA.'),
('bullet','Comprende que aceptar programa la próxima actividad y deja una decisión docente registrada, sin alterar las actividades realizadas.'),
('h','Ficha de la sesión'),
('p','Participante (código): __________   Fecha: __________\nModerador/a: __________________   Observador/a: __________________\nExperiencia docente: __________   Grado/s: __________\nConsentimiento de grabación: Sí / No'),
('h','Preparación del moderador'),
('p','Convocar docentes de primaria. Usar computadora con mouse o trackpad. Abrir miseno_docentes.html desde el mismo navegador durante toda la sesión. Verificar que Joaquín no tenga una próxima actividad aceptada y que no haya marcas de registros consultados de una sesión anterior.'),
('note','Solo antes de cada sesión: en las herramientas de desarrollo del navegador ejecutar localStorage.removeItem("miseno-docentes-v1") y recargar. Esto restablece únicamente los datos de esta interfaz. No hacerlo durante la prueba.'),
],
[
('title','Intro'),('meta','Leer al participante'),
('p','Ante todo, muchas gracias por venir y participar. Mi nombre es [nombre del moderador]. Estamos trabajando en Miseño, una interfaz para docentes que reúne información del alumno y propuestas de actividades de una IA.'),
('p','Queremos entender si esta herramienta ayuda a revisar una propuesta y decidir qué actividad conviene hacer después. Estamos probando la interfaz, no tus conocimientos ni tu desempeño como docente. No hay obligación de estar de acuerdo con la IA.'),
('p','Te voy a leer algunas tareas y te las voy a dejar al lado para que puedas consultarlas. Necesitamos que digas en voz alta lo que hacés, lo que pensás y lo que esperás que ocurra. Para esta sesión vamos a trabajar con el caso simulado de Joaquín; no ingreses información de alumnos reales.'),
('p','Nos gustaría grabar la pantalla y el audio para revisar la sesión internamente. No se publicará. ¿Nos das tu consentimiento para grabar? Podés participar sin grabación y pedir una pausa o terminar cuando quieras.'),
('note','Esperar la respuesta. Iniciar la grabación solo si acepta. Si no acepta, continuar con notas. Si acepta: “La grabación está iniciada; avisame si necesitás que la detengamos”.'),
('p','Durante las tareas puede haber preguntas que prefiera retomar al final para ver cómo se entiende la herramienta por sí sola. Todo lo que nos digas nos ayuda a mejorar. ¿Tenés alguna duda antes de empezar?'),
('h','Guión'),('sub','Preguntas previas'),
('bullet','¿En qué grado o grados trabajás? ¿Cómo decidís qué necesita practicar más un alumno?'),
('bullet','¿Qué registros consultás antes de elegir una actividad de refuerzo?'),
('bullet','¿Qué herramientas digitales usás para planificar o seguir aprendizajes?'),
('bullet','¿Usaste alguna vez recomendaciones de IA? ¿Qué necesitás saber para confiar en una propuesta?'),
],
[
('title','Escenarios y tareas'),
('h','Escenario y contexto'),('p','Estás preparando el próximo bloque de Matemática del Grupo A. Querés revisar cómo viene Joaquín con fracciones y elegir una práctica adecuada. Miseño tiene registros de sus actividades y una propuesta para continuar.'),
('note','Comenzar en categorías, después del splash. Leer una tarea por vez, sin indicar rutas ni botones. Tiempo conjunto: 7 minutos.'),
('h','Tarea 1'),('sub','Consigna para el participante'),
('p','Averiguá qué propone la herramienta para que Joaquín siga practicando y explicame qué necesidad intenta atender.'),
('sub','Convierte cuando'),
('p','Encuentra la recomendación de Joaquín y explica que propone reforzar el denominador con partes iguales y apoyo visual. La reconoce como propuesta.'),
('sub','Observar sin leer al participante'),
('bullet','Dónde busca; uso del carrusel; distinción entre recomendación, registro y aporte familiar.'),
('h','Tarea 2'),('sub','Consigna para el participante'),
('p','Antes de decidir, revisá qué hizo Joaquín en las actividades anteriores. Contame si encontrás evidencia que respalde o cuestione la propuesta y qué apoyos se utilizaron.'),
('sub','Convierte cuando'),
('p','Abre un registro y cita una evidencia: confusión del denominador con las piezas elegidas o ayuda para distinguir las partes del entero. Identifica el apoyo utilizado y fundamenta su evaluación.'),
('sub','Observar sin leer al participante'),
('bullet','Si abre detalles, distingue respuestas de inferencias y considera apoyos antes de concluir.'),
],
[
('title','Escenarios y tareas'),('meta','Continuación | 6 a 8 minutos'),
('h','Tarea 3'),('sub','Consigna para el participante'),
('p','Con lo que revisaste, decidí si usarías la actividad sugerida en el próximo bloque de Matemática. Si te parece adecuada, dejala preparada. Si no, contame qué cambiarías y cómo intentarías pedirlo.'),
('sub','Convierte cuando'),
('p','En el camino de aceptación: revisa objetivo, consigna, duración y apoyos; confirma su evaluación y acepta. La actividad queda como próxima, aceptada por Clara López. La interfaz no debe comunicar que Joaquín ya la realizó.'),
('note','Si no está de acuerdo, no forzar la aceptación. Registrar “desacuerdo pedagógico”, observar si pide un ajuste o consulta a la IA y distinguirlo de un problema de usabilidad. La conversación de IA es simulada y los pedidos de ajuste no modifican el plan por sí solos.'),
('sub','Observar sin leer al participante'),
('bullet','Si entiende la confirmación de contraste o la marca sin revisar. Qué espera del botón de aceptación. Si distingue aceptación efectiva de un pedido de cambio pendiente.'),
('h','Tarea 4'),('sub','Consigna para el participante'),
('p','Mostrame cómo comprobarías qué quedó preparado para Joaquín y dónde buscarías después el registro de tu decisión.'),
('sub','Convierte cuando'),
('p','Si aceptó: encuentra la próxima actividad y su estado; recupera en Intervenciones la aceptación con docente, fecha y seguimiento. Explica que los registros anteriores siguen disponibles. Si pidió un ajuste: identifica el pedido como pendiente y entiende que no programó una actividad.'),
('sub','Preguntas neutrales durante las tareas'),
('p','“¿Qué estás buscando ahora?” · “¿Qué esperás que pase?” · “¿Qué te indica eso?” · “¿Qué harías si yo no estuviera?”'),
('note','Si queda bloqueada, preguntar primero qué intentaría. Si necesita una pista de navegación, darla y registrar la ayuda; no contar el resultado como éxito autónomo. Detener una tarea ante frustración o a pedido del participante.'),
],
[
('title','Preguntas finales'),('meta','4 a 5 minutos'),
('bullet','¿Qué te permitió decidir si la sugerencia era adecuada? ¿Qué información faltó?'),
('bullet','¿Qué esperabas encontrar al abrir un registro? ¿Lo encontraste?'),
('bullet','¿Qué cambió al aceptar o pedir un ajuste? ¿Qué quedó pendiente?'),
('bullet','¿Quién sentís que tomó la decisión y qué responsabilidad tendría cada parte?'),
('bullet','¿Dónde volverías para revisar esa decisión o el resultado de la práctica?'),
('bullet','Del 1 al 7, ¿qué tan fácil o difícil fue completar este proceso? ¿Por qué?'),
('h','Habilitamos al observador a preguntar'),
('p','¿[Nombre del observador] tiene alguna pregunta sobre algo que haya ocurrido durante la prueba? Retomar también las dudas que quedaron pendientes. Agradecer la participación y detener la grabación, si la hubo.'),
('h','Registro del moderador'),
('p','Para cada tarea anotar: resultado, tiempo aproximado, errores, ayudas y una cita textual. Clasificar como: autónoma / con ayuda / no completada. Registrar por separado el desacuerdo pedagógico; no equivale automáticamente a un fallo de uso.'),
('p','Tarea 1: __________  Tiempo: ______  Ayudas: __________________\nTarea 2: __________  Tiempo: ______  Ayudas: __________________\nTarea 3: __________  Tiempo: ______  Ayudas: __________________\nTarea 4: __________  Tiempo: ______  Ayudas: __________________'),
('p','Decisión: aceptó / pidió ajuste / no decidió\nEvidencia citada: __________________________________________\n¿Comprendió el estado final y encontró el registro? __________\nFacilidad (1 a 7): _____'),
('h','Criterio de lectura de resultados'),
('p','Evaluar por separado descubrimiento, contraste de evidencia, decisión y comprensión del estado final. La aceptación sin revisar registros no valida el flujo completo. Consolidar patrones entre sesiones; no convertir una preferencia individual en una conclusión general.'),
('meta','Estructura adaptada de Template Guión de Usabilidad.pdf, aportado por la usuaria.'),
]
]
styles={
'title':ParagraphStyle('title',fontName='Courier-Bold',fontSize=20,leading=25,spaceAfter=14),
'subtitle':ParagraphStyle('subtitle',fontName='Courier',fontSize=12,leading=17,spaceAfter=8,textColor=colors.HexColor('#555555')),
'meta':ParagraphStyle('meta',fontName='Courier',fontSize=9,leading=13,spaceAfter=15,textColor=colors.HexColor('#555555')),
'h':ParagraphStyle('h',fontName='Courier',fontSize=15,leading=19,spaceBefore=13,spaceAfter=9,keepWithNext=True),
'sub':ParagraphStyle('sub',fontName='Courier-Bold',fontSize=10,leading=14,spaceBefore=7,spaceAfter=5,keepWithNext=True),
'p':ParagraphStyle('p',fontName='Courier',fontSize=10,leading=14,spaceAfter=9),
'bullet':ParagraphStyle('bullet',fontName='Courier',fontSize=10,leading=14,leftIndent=13,firstLineIndent=-10,spaceAfter=7),
'note':ParagraphStyle('note',fontName='Courier-Oblique',fontSize=9,leading=13,spaceBefore=4,spaceAfter=9,textColor=colors.HexColor('#444444')),
}
story=[];md=[]
for i,blocks in enumerate(pages):
    for kind,text in blocks:
        safe=escape(text).replace('\n','<br/>')
        if kind=='bullet':safe='• '+safe
        story.append(Paragraph(safe,styles[kind]))
        prefix={'title':'# ','h':'## ','sub':'### ','bullet':'- ','note':'> '}.get(kind,'')
        md.append(prefix+text+'\n')
    if i<len(pages)-1:story.append(PageBreak());md.append('\n---\n')
def footer(c,doc):
    c.setFont('Courier',8);c.setFillColor(colors.HexColor('#666666'));c.drawString(60,34,'Miseño | Guión de prueba de usuario');c.drawRightString(552,34,str(doc.page))
pdf=OUT/'Guion_usabilidad_Miseno_proxima_actividad.pdf'
doc=SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=60,rightMargin=60,topMargin=45,bottomMargin=48,title='Guión de prueba de usuario de Miseño',author='Miseño')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
(ROOT/'Guion_usabilidad_Miseno_proxima_actividad.md').write_text('\n'.join(md),encoding='utf-8')
tmp=ROOT/'tmp/pdfs';tmp.mkdir(parents=True,exist_ok=True)
render=pdfium.PdfDocument(str(pdf))
for i in range(len(render)):render[i].render(scale=1.3).to_pil().save(str(tmp/f'guion_{i+1}.png'))
print(f'{pdf}\nPáginas: {len(render)}')

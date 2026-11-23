from pathlib import Path
import re
p=Path('miseno_docentes.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'<header class="topbar">.*?</header>','',s,flags=re.S)
s=re.sub(r'<footer class="footer">.*?</footer>','',s,flags=re.S)
s=s.replace("let state=initial(),page='launch'", "let selectedProfile=null;\nlet state=initial(),page='launch'")
s=s.replace("{group:'Grupo',students:'Alumnos',paths:'Recorridos',projects:'Proyectos'}", "{group:'Grupo',paths:'Recorridos',projects:'Proyectos'}")
s=s.replace("['students','Alumnos','Datos y fichas individuales'],",'')
a=s.index('function group(){');b=s.index('\nfunction situations()',a)
s=s[:a]+'''function group(){const list=pupils.filter(p=>(p.name+' '+p.short+' '+p.subject).toLowerCase().includes(query.toLowerCase()));return title('Grupo A','Actividades actuales y datos de los alumnos.')+`<div class="group-layout ${selectedProfile?'has-profile':''}"><section class="card"><div class="toolbar"><input type="search" id="search" aria-label="Buscar alumno o materia" placeholder="Buscar alumno o materia" value="${esc(query)}"></div><div class="student-list">${list.map(p=>`<button class="student" data-profile="${p.id}" aria-expanded="${selectedProfile===p.id}" aria-controls="student-profile"><div class="split">${avatar(p)}<div><strong>${p.name}</strong><div class="small muted">${p.subject}</div></div></div><p>${p.activity}</p><span class="tag">${status(p)}</span></button>`).join('')||'<p class="empty">No hay alumnos que coincidan con la búsqueda.</p>'}</div></section><aside id="student-profile" aria-label="Ficha del alumno" ${selectedProfile?'':'hidden'}>${selectedProfile?profilePanel(pupil(selectedProfile)):''}</aside></div>`}
function profilePanel(p){return `<section class="card profile-panel"><div class="row"><div class="split">${avatar(p)}<h2 id="profile-heading" tabindex="-1">${p.name}</h2></div><button class="close" data-action="close-profile" aria-label="Cerrar ficha del alumno">×</button></div><dl><dt>Nombre de uso</dt><dd>${p.short}</dd><dt>Grupo</dt><dd>Grupo A · Primaria</dd><dt>Actividad actual</dt><dd>${p.activity}</dd><dt>Estado</dt><dd>${status(p)}</dd></dl><p class="small muted">Otros datos personales: sin cargar.</p><div class="actions"><button class="btn secondary" data-student="${p.id}">Ver recorrido</button><button class="btn ghost" data-history="${p.id}">Ver historial</button></div></section>`}
''' +s[b:]
s=s.replace("student=b.dataset.profile;page='students';render(true)","student=b.dataset.profile;selectedProfile=b.dataset.profile;page='group';render();$('#profile-heading').focus()")
# A route retained by old events now opens the integrated group view.
s=s.replace("if(page==='detail'||page==='situations')page='paths';", "if(page==='detail'||page==='situations')page='paths';if(page==='students')page='group';")
insert="actions['close-profile']=()=>{const id=selectedProfile;selectedProfile=null;render();const trigger=document.querySelector('[data-profile=\"'+id+'\"]');if(trigger)trigger.focus()};\n"
s=s.replace("actions['edit-adaptation']=",insert+"actions['edit-adaptation']=")
# Remove the obsolete standalone directory, now merged into Grupo.
a=s.index('function students(){');b=s.index('\nfunction recommendations()',a)
s=s[:a]+s[b:]
s=s.replace('{launch,group,students,paths,projects}', '{launch,group,paths,projects}')
s=s.replace('Prototipo docente de Miseño:', 'Espacio docente de Miseño:')
# Remove staging copy while preserving accurate action states.
replacements={
'Datos ilustrativos del prototipo · No constituyen un diagnóstico ni una comparación con otros alumnos.':'Estos registros no constituyen un diagnóstico ni una comparación con otros alumnos.',
'Otros datos personales: sin cargar en este prototipo.':'Otros datos personales: sin cargar.',
'La solicitud local no cambia el plan ni se envía al equipo pedagógico.':'La solicitud queda registrada. El plan permanece sin cambios.',
'Solicitud registrada en este prototipo':'Solicitud de revisión registrada',
'La discrepancia permanece abierta. El plan actual no se modificó y no se envió un pedido externo.':'La discrepancia permanece abierta. El plan actual no se modificó.',
'Esta es una simulación local. El responsable y el plazo de resolución todavía no están definidos en el PRD.':'Responsable y plazo de resolución: pendientes de asignación.',
'Registrar solicitud local':'Registrar solicitud',
'Revisión registrada localmente. El plan no cambió; no se envió a la escuela.':'Revisión registrada. El plan no cambió.',
'La solicitud no modifica el recorrido ni se envía a la escuela.':'La solicitud no modifica el recorrido.',
'Solicitud local registrada':'Solicitud registrada',
'Pedido de revisión del plan guardado localmente.':'Pedido de revisión del plan guardado.',
'Registrada localmente · Plan sin modificar':'Registrada · Plan sin modificar',
'Propuesta guardada localmente. El plan no se modificó.':'Propuesta guardada. El plan no se modificó.',
'Se conserva en este navegador. No modifica el plan ni resuelve automáticamente una discrepancia.':'No modifica el plan ni resuelve automáticamente una discrepancia.',
'Intervención guardada en el historial local. La dificultad sigue en seguimiento.':'Intervención guardada en el historial. La dificultad sigue en seguimiento.',
'Fundamento: registros ilustrativos de la actividad actual.':'Fundamento: registros de la actividad actual.',
'Los indicadores representan avance ilustrativo dentro del tema.':'Los indicadores representan el avance dentro del tema.',
'El plan ilustrativo suma dos bloques semanales y deja Música en pausa.':'El plan suma dos bloques semanales y deja Música en pausa.',
'Avance ilustrativo en ':'Avance en ',
' · Ejemplo':'', ' · ejemplo':'',
' en este ejemplo':'', ' del ejemplo':'', ' de ejemplo':'',
'en el plan de ejemplo':'en el plan',
}
for old,new in replacements.items():s=s.replace(old,new)
# Adjust the landing and student panel layout on desktop and mobile.
css='''
.launch-options{grid-template-columns:repeat(3,1fr)}.group-layout{display:grid;grid-template-columns:minmax(0,1fr);gap:24px;align-items:start}.group-layout.has-profile{grid-template-columns:minmax(0,1fr) 360px}.has-profile .student-list{grid-template-columns:repeat(2,minmax(0,1fr))}.profile-panel{position:sticky;top:115px;border:1px solid #d5dfea}.profile-panel dl{grid-template-columns:110px minmax(0,1fr)}.profile-panel dd{overflow-wrap:anywhere}.student[aria-expanded=true]{border-color:#315dce;background:#f0f4fd;box-shadow:0 0 0 1px #315dce}.profile-panel .actions{flex-direction:column}.profile-panel h2{font-size:24px}.launch-options button:nth-child(2) .launch-icon{background:#e0f1e8}.launch-options button:nth-child(3) .launch-icon{background:#fae8df}@media(max-width:1050px){.group-layout.has-profile{grid-template-columns:minmax(0,1fr) 310px}.has-profile .student-list{grid-template-columns:1fr}}@media(max-width:760px){.group-layout.has-profile{grid-template-columns:1fr}.group-layout.has-profile>#student-profile{grid-row:1}.profile-panel{position:static}.has-profile .student-list{grid-template-columns:repeat(2,minmax(0,1fr))}.launch-options{grid-template-columns:1fr}.launch-options button{min-height:140px}.launch-screen{padding:32px 0}.launch-options button{gap:10px}.launch-icon{width:46px;height:46px}}@media(max-width:480px){.has-profile .student-list{grid-template-columns:1fr}}
'''
s=s.replace('</style>',css+'\n</style>')
p.write_text(s,encoding='utf-8')
Path('tmp/miseno_check.js').write_text(re.search(r'<script>(.*?)</script>',s,re.S).group(1),encoding='utf-8')
print('Grupo con fichas laterales; navegación reducida; franja y aclaraciones retiradas.')

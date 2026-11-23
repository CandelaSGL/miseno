from pathlib import Path
import re
p=Path('miseno_docentes.html');s=p.read_text(encoding='utf-8')
s=s.replace("function studentRecords(){if(tab==='interventions')", "function studentRecords(){if(tab==='activities')return activitiesWithRecords();if(tab==='interventions')")
start=s.index('function compactInsights(){');end=s.index('\nfunction legacyStudentRecords()',start)
part=s[start:end]
part=part.replace('<h3 style="margin-top:22px">Recomendación</h3>', '<h3 style="margin-top:22px">Recomendación</h3>')
part=part.replace('<div class="actions"><button class="btn secondary" data-action="edit-adaptation">Proponer ajuste</button></div>', '${recommendationActions()}')
s=s[:start]+part+s[end:]
s=s.replace('\nrender();\nsetTimeout','\n'+Path('tmp/accept_activity_flow.js').read_text(encoding='utf-8')+'\nrender();\nsetTimeout')
s=s.replace('</style>','\n.next-activity{margin-bottom:22px;border:1px solid #cdd9f0}.table-wrap td .tag{margin-top:5px}.next-activity h2{font-size:23px}\n</style>')
p.write_text(s,encoding='utf-8');Path('tmp/miseno_check.js').write_text(re.search(r'<script>(.*?)</script>',s,re.S).group(1),encoding='utf-8')
print('Flujo de próxima actividad incorporado')

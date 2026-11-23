from pathlib import Path
import re
p=Path('miseno_docentes.html');s=p.read_text(encoding='utf-8')
s=s.replace("tab=b.dataset.tab;render();$('#tab-'+tab).focus()", "selectJourneyTab(b.dataset.tab)")
s=s.replace("render();$('#tab-'+tab).focus()", "selectJourneyTab(tab)")
s=s.replace("if(b.dataset.insight){insightTab=b.dataset.insight;render()}", "if(b.dataset.insight){selectInsight(b.dataset.insight)}")
extra=r'''
// Update only the selected panel: keep navigation, carousel and sidebar mounted.
function selectJourneyTab(next){if(!['activities','evidence','interventions'].includes(next))return;tab=next;const panel=$('#detail-panel');if(!panel)return;panel.innerHTML=studentRecords();panel.setAttribute('aria-labelledby','tab-'+tab);for(const id of ['activities','evidence','interventions']){const button=$('#tab-'+id);button.setAttribute('aria-selected',String(id===tab));button.tabIndex=id===tab?0:-1}$('#tab-'+tab).focus()}
function selectInsight(next){insightTab=next;const capsule=$('.insight-capsule');if(!capsule)return;const template=document.createElement('template');template.innerHTML=compactInsights();const nextCapsule=template.content.firstElementChild;capsule.querySelector('.capsule-content').replaceWith(nextCapsule.querySelector('.capsule-content'));capsule.querySelectorAll('[data-insight]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.insight===next)));capsule.querySelector('[data-insight="'+next+'"]').focus()}
'''
s=s.replace('\nrender();\nsetTimeout','\n'+extra+'\nrender();\nsetTimeout')
# No fade from opacity zero on navigation; the translucent surfaces remain visible.
s=s.replace('</style>','\n.journey-layout,#detail-panel,.capsule-content{animation:none!important}\n</style>')
p.write_text(s,encoding='utf-8');Path('tmp/miseno_check.js').write_text(re.search(r'<script>(.*?)</script>',s,re.S).group(1),encoding='utf-8')

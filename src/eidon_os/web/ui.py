DASHBOARD_HTML = r'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Eidon OS</title>
<style>
:root{color-scheme:dark;--bg:#0a1020;--panel:#111a2f;--panel2:#17213a;--text:#f6f8fb;--muted:#9aa7bd;--line:#26324b;--accent:#5b8cff;--accent2:#8b5cf6;--ok:#34d399;--warn:#f59e0b;--danger:#f87171}
*{box-sizing:border-box}body{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;background:radial-gradient(circle at top right,#1a1d4a 0,#0a1020 36%),var(--bg);color:var(--text)}
.shell{display:grid;grid-template-columns:240px 1fr;min-height:100vh}.side{border-right:1px solid var(--line);padding:28px 18px;background:#09101d;position:sticky;top:0;height:100vh}.brand{font-size:22px;font-weight:700;margin-bottom:6px}.version{color:var(--muted);font-size:13px;margin-bottom:28px}.nav{display:grid;gap:8px}.nav a{color:var(--muted);text-decoration:none;padding:10px 12px;border-radius:10px}.nav a.active,.nav a:hover{background:var(--panel2);color:var(--text)}
main{padding:34px;max-width:1440px;width:100%}.hero{display:flex;justify-content:space-between;gap:20px;align-items:end;margin-bottom:26px}.hero h1{margin:0 0 8px;font-size:34px}.hero p{margin:0;color:var(--muted)}.badge{padding:8px 12px;border:1px solid var(--line);border-radius:999px;color:var(--ok);background:#0e2a24}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}.card{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:16px;padding:18px}.label{color:var(--muted);font-size:13px}.value{font-size:28px;font-weight:700;margin-top:8px}.section{margin-top:22px}.section h2{font-size:18px;margin:0 0 12px}.twocol{display:grid;grid-template-columns:1.35fr 1fr;gap:16px}.list{display:grid;gap:10px}.row{display:flex;justify-content:space-between;gap:18px;padding:12px 0;border-bottom:1px solid var(--line)}.row:last-child{border-bottom:0}.title{font-weight:600}.meta{color:var(--muted);font-size:13px;margin-top:4px}.empty{color:var(--muted);padding:8px 0}.footer{margin-top:30px;color:var(--muted);font-size:12px}
.ai-shell{display:grid;grid-template-columns:360px 1fr;gap:16px}.field{display:grid;gap:7px;margin-bottom:14px}.field label{font-size:13px;color:var(--muted)}input,select,textarea,button{font:inherit}input,select,textarea{width:100%;border:1px solid var(--line);background:#0b1324;color:var(--text);border-radius:10px;padding:11px 12px;outline:none}textarea{min-height:94px;resize:vertical}input:focus,select:focus,textarea:focus{border-color:var(--accent)}button{border:0;border-radius:10px;padding:10px 14px;cursor:pointer;background:var(--accent);color:white;font-weight:600}button.secondary{background:var(--panel2);border:1px solid var(--line)}button:disabled{opacity:.55;cursor:not-allowed}.statusline{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted);margin-bottom:16px}.dot{width:9px;height:9px;border-radius:50%;background:var(--danger)}.dot.ok{background:var(--ok)}.notice{font-size:12px;color:var(--muted);line-height:1.5;padding:10px 12px;background:#0b1324;border-radius:10px;border:1px solid var(--line)}.chatlog{display:grid;gap:12px;min-height:220px;max-height:430px;overflow:auto;padding-right:4px}.msg{padding:12px 14px;border-radius:12px;line-height:1.55;white-space:pre-wrap}.msg.user{background:#15203a;margin-left:14%}.msg.ai{background:#0c182c;border:1px solid var(--line);margin-right:8%}.actions{font-size:12px;color:var(--muted);margin-top:8px}.chatbar{display:grid;gap:10px;margin-top:14px}.chat-actions{display:flex;justify-content:space-between;gap:12px;align-items:center}.danger-toggle{display:flex;align-items:center;gap:8px;color:var(--muted);font-size:13px}.danger-toggle input{width:auto}.small{font-size:12px;color:var(--muted)}
@media(max-width:1050px){.ai-shell{grid-template-columns:1fr}.shell{grid-template-columns:1fr}.side{display:none}.grid{grid-template-columns:repeat(2,1fr)}.twocol{grid-template-columns:1fr}}@media(max-width:560px){main{padding:22px}.grid{grid-template-columns:1fr}.hero{align-items:start;flex-direction:column}.chat-actions{align-items:stretch;flex-direction:column}}
</style>
</head>
<body>
<div class="shell">
<aside class="side">
<div class="brand">🏛️ Eidon OS</div><div class="version">v0.5.0 • Eidon Web</div>
<nav class="nav"><a class="active" href="#overview">Visão geral</a><a href="#activities">Atividades</a><a href="#goals">Metas</a><a href="#eidon-ai">✦ Eidon IA</a><a href="#">Projetos</a><a href="#">Conhecimento</a></nav>
</aside>
<main>
<section class="hero" id="overview"><div><h1>Personal Intelligence</h1><p>Seu conhecimento, projetos e evolução em uma única interface.</p></div><div class="badge">● Núcleo local conectado</div></section>
<section class="grid" id="metrics"></section>
<section class="section twocol"><div class="card" id="activities"><h2>Atividades recentes</h2><div class="list" id="activity-list"></div></div><div class="card" id="goals"><h2>Metas ativas</h2><div class="list" id="goal-list"></div></div></section>

<section class="section" id="eidon-ai">
<h2>Eidon IA</h2>
<div class="ai-shell">
<div class="card">
<div class="title">Integração de inteligência</div>
<div class="meta" style="margin-bottom:16px">A IA acessa o Eidon através de ferramentas controladas. O banco local continua sendo a fonte da verdade.</div>
<div class="statusline"><span class="dot" id="ai-dot"></span><span id="ai-status">Verificando integração...</span></div>
<div class="field"><label>Provedor</label><select id="provider"><option value="openai">OpenAI / ChatGPT</option></select></div>
<div class="field"><label>Modelo</label><input id="model" value="gpt-5" placeholder="gpt-5"></div>
<div class="field"><label>API key</label><input id="api-key" type="password" autocomplete="off" placeholder="sk-... (não é exibida novamente)"></div>
<button id="save-ai">Conectar IA</button>
<div class="notice" style="margin-top:14px">A chave informada aqui fica somente na memória do processo local do Eidon Web. Para persistir com segurança, configure <b>OPENAI_API_KEY</b> no ambiente. Nunca coloque a chave no GitHub.</div>
</div>
<div class="card">
<div class="title">Conversar com o Eidon</div>
<div class="meta" style="margin-bottom:14px">Consulte dados ou peça para registrar atividades, metas, projetos e conhecimento.</div>
<div class="chatlog" id="chatlog"><div class="msg ai">Conecte seu provedor de IA para começar. Depois você poderá pedir, por exemplo: “Registre 90 minutos de estudo de Python” ou “Como estou evoluindo este mês?”</div></div>
<div class="chatbar">
<textarea id="chat-input" placeholder="Pergunte ao Eidon..."></textarea>
<div class="chat-actions">
<label class="danger-toggle"><input type="checkbox" id="allow-destructive"> Autorizar exclusões nesta mensagem</label>
<button id="send-chat">Enviar</button>
</div>
<div class="small">Exclusões só são permitidas quando esta autorização estiver marcada.</div>
</div>
</div>
</div>
</section>
<div class="footer">A IA acessa o Eidon; o Eidon não pertence à IA.</div>
</main></div>
<script>
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
async function loadDashboard(){
 const [d,a,g]=await Promise.all([fetch('/api/dashboard').then(r=>r.json()),fetch('/api/activities?limit=8').then(r=>r.json()),fetch('/api/goals').then(r=>r.json())]);
 const m=[['Projetos',d.projects],['Conhecimentos',d.knowledge_items],['Atividades',d.activities],['Horas registradas',d.total_hours]];
 document.querySelector('#metrics').innerHTML=m.map(x=>`<div class="card"><div class="label">${esc(x[0])}</div><div class="value">${esc(x[1])}</div></div>`).join('');
 document.querySelector('#activity-list').innerHTML=a.length?a.map(x=>`<div class="row"><div><div class="title">${esc(x.title)}</div><div class="meta">${esc(x.category)} • ${esc(x.occurred_at)}</div></div><div>${esc(x.duration_minutes)} min</div></div>`).join(''):'<div class="empty">Nenhuma atividade registrada.</div>';
 document.querySelector('#goal-list').innerHTML=g.length?g.map(x=>`<div class="row"><div><div class="title">${esc(x.indicator)}</div><div class="meta">${esc(x.area)} • ${esc(x.period)}</div></div><div>${esc(x.target)} ${esc(x.unit)}</div></div>`).join(''):'<div class="empty">Nenhuma meta ativa.</div>';
}
async function loadAIStatus(){
 const s=await fetch('/api/ai/status').then(r=>r.json());
 document.querySelector('#provider').value=s.provider;document.querySelector('#model').value=s.model;
 document.querySelector('#ai-dot').classList.toggle('ok',!!s.configured);
 document.querySelector('#ai-status').textContent=s.configured?`Conectado • ${s.provider} • ${s.model}`:'IA ainda não configurada';
}
function addMsg(type,text,actions){const log=document.querySelector('#chatlog');const el=document.createElement('div');el.className=`msg ${type}`;el.textContent=text;if(actions&&actions.length){const a=document.createElement('div');a.className='actions';a.textContent='Ações: '+actions.map(x=>x.tool||'tool').join(', ');el.appendChild(a)}log.appendChild(el);log.scrollTop=log.scrollHeight}
document.querySelector('#save-ai').addEventListener('click',async()=>{
 const btn=document.querySelector('#save-ai');btn.disabled=true;
 try{const r=await fetch('/api/ai/config',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({provider:document.querySelector('#provider').value,model:document.querySelector('#model').value,api_key:document.querySelector('#api-key').value||null})});const data=await r.json();if(!r.ok)throw new Error(data.detail||'Falha ao configurar');document.querySelector('#api-key').value='';await loadAIStatus();addMsg('ai','Integração configurada. O Eidon IA já pode consultar e registrar informações no núcleo local.')}catch(e){addMsg('ai','Erro: '+e.message)}finally{btn.disabled=false}
});
document.querySelector('#send-chat').addEventListener('click',async()=>{
 const input=document.querySelector('#chat-input');const message=input.value.trim();if(!message)return;const btn=document.querySelector('#send-chat');addMsg('user',message);input.value='';btn.disabled=true;
 try{const r=await fetch('/api/ai/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message,allow_destructive:document.querySelector('#allow-destructive').checked})});const data=await r.json();if(!r.ok)throw new Error(data.detail||'Falha na IA');addMsg('ai',data.message||'Concluído.',data.actions);document.querySelector('#allow-destructive').checked=false;await loadDashboard()}catch(e){addMsg('ai','Erro: '+e.message)}finally{btn.disabled=false}
});
loadDashboard().catch(()=>{document.querySelector('#metrics').innerHTML='<div class="card"><div class="label">Status</div><div class="value">Erro ao carregar</div></div>'});
loadAIStatus().catch(()=>{document.querySelector('#ai-status').textContent='Falha ao verificar IA'});
</script>
</body></html>'''

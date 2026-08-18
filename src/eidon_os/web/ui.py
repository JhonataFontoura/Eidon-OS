DASHBOARD_HTML = r'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Eidon OS</title>
<style>
:root{color-scheme:dark;--bg:#0a1020;--panel:#111a2f;--panel2:#17213a;--text:#f6f8fb;--muted:#9aa7bd;--line:#26324b;--accent:#5b8cff;--accent2:#8b5cf6;--ok:#34d399}
*{box-sizing:border-box}body{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;background:radial-gradient(circle at top right,#1a1d4a 0,#0a1020 36%),var(--bg);color:var(--text)}
.shell{display:grid;grid-template-columns:240px 1fr;min-height:100vh}.side{border-right:1px solid var(--line);padding:28px 18px;background:#09101d}.brand{font-size:22px;font-weight:700;margin-bottom:6px}.version{color:var(--muted);font-size:13px;margin-bottom:28px}.nav{display:grid;gap:8px}.nav a{color:var(--muted);text-decoration:none;padding:10px 12px;border-radius:10px}.nav a.active,.nav a:hover{background:var(--panel2);color:var(--text)}
main{padding:34px}.hero{display:flex;justify-content:space-between;gap:20px;align-items:end;margin-bottom:26px}.hero h1{margin:0 0 8px;font-size:34px}.hero p{margin:0;color:var(--muted)}.badge{padding:8px 12px;border:1px solid var(--line);border-radius:999px;color:var(--ok);background:#0e2a24}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}.card{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:16px;padding:18px}.label{color:var(--muted);font-size:13px}.value{font-size:28px;font-weight:700;margin-top:8px}.section{margin-top:22px}.section h2{font-size:18px;margin:0 0 12px}.twocol{display:grid;grid-template-columns:1.35fr 1fr;gap:16px}.list{display:grid;gap:10px}.row{display:flex;justify-content:space-between;gap:18px;padding:12px 0;border-bottom:1px solid var(--line)}.row:last-child{border-bottom:0}.title{font-weight:600}.meta{color:var(--muted);font-size:13px;margin-top:4px}.empty{color:var(--muted);padding:8px 0}.bar{height:8px;background:#0b1324;border-radius:999px;overflow:hidden;margin-top:8px}.bar>span{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:999px}.footer{margin-top:30px;color:var(--muted);font-size:12px}
@media(max-width:950px){.shell{grid-template-columns:1fr}.side{display:none}.grid{grid-template-columns:repeat(2,1fr)}.twocol{grid-template-columns:1fr}}@media(max-width:560px){main{padding:22px}.grid{grid-template-columns:1fr}.hero{align-items:start;flex-direction:column}}
</style>
</head>
<body>
<div class="shell">
<aside class="side"><div class="brand">🏛️ Eidon OS</div><div class="version">v0.5.0 • Eidon Web</div><nav class="nav"><a class="active" href="#">Visão geral</a><a href="#activities">Atividades</a><a href="#goals">Metas</a><a href="#">Projetos</a><a href="#">Conhecimento</a></nav></aside>
<main>
<section class="hero"><div><h1>Personal Intelligence</h1><p>Seu conhecimento, projetos e evolução em uma única interface.</p></div><div class="badge">● Núcleo local conectado</div></section>
<section class="grid" id="metrics"></section>
<section class="section twocol"><div class="card" id="activities"><h2>Atividades recentes</h2><div class="list" id="activity-list"></div></div><div class="card" id="goals"><h2>Metas ativas</h2><div class="list" id="goal-list"></div></div></section>
<div class="footer">A IA acessa o Eidon; o Eidon não pertence à IA.</div>
</main></div>
<script>
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
async function load(){
 const [d,a,g]=await Promise.all([fetch('/api/dashboard').then(r=>r.json()),fetch('/api/activities?limit=8').then(r=>r.json()),fetch('/api/goals').then(r=>r.json())]);
 const m=[['Projetos',d.projects],['Conhecimentos',d.knowledge_items],['Atividades',d.activities],['Horas registradas',d.total_hours]];
 document.querySelector('#metrics').innerHTML=m.map(x=>`<div class="card"><div class="label">${esc(x[0])}</div><div class="value">${esc(x[1])}</div></div>`).join('');
 document.querySelector('#activity-list').innerHTML=a.length?a.map(x=>`<div class="row"><div><div class="title">${esc(x.title)}</div><div class="meta">${esc(x.category)} • ${esc(x.occurred_at)}</div></div><div>${esc(x.duration_minutes)} min</div></div>`).join(''):'<div class="empty">Nenhuma atividade registrada.</div>';
 document.querySelector('#goal-list').innerHTML=g.length?g.map(x=>`<div><div class="row"><div><div class="title">${esc(x.indicator)}</div><div class="meta">${esc(x.area)} • ${esc(x.period)}</div></div><div>${esc(x.target)} ${esc(x.unit)}</div></div></div>`).join(''):'<div class="empty">Nenhuma meta ativa.</div>';
}
load().catch(()=>{document.querySelector('#metrics').innerHTML='<div class="card"><div class="label">Status</div><div class="value">Erro ao carregar</div></div>'});
</script>
</body></html>'''

"""Generation des 10 graphiques du rapport (PNG, matplotlib).

Chaque graphique porte : unite, periode, hypotheses, source, et la mention
donnees observees vs projection. Sortie : /workspace/etude_metiers/charts/
"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
sys.path.insert(0, BASE + '/data')
from fiscal import net_mensuel
import scoring

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 9,
    'axes.titlesize': 11, 'axes.titleweight': 'bold',
    'axes.edgecolor': '#666666', 'axes.grid': True,
    'grid.color': '#DDDDDD', 'grid.linewidth': 0.6,
    'figure.facecolor': 'white'})
OUT = os.path.join(BASE, 'charts')
os.makedirs(OUT, exist_ok=True)
ALL = scoring.ALL
BY = scoring.BY_ID
C_MAIN = '#1f4e79'; C_ACC = '#c00000'; C_MID = '#2e9599'; C_WARN = '#e8a33d'

def save(fig, name, source, note):
    fig.text(0.01, 0.005, source, fontsize=6.5, color='#555555', ha='left')
    if note:
        fig.text(0.99, 0.005, note, fontsize=6.5, color='#555555', ha='right')
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('OK', name)

def net(brut):
    return net_mensuel(brut)[1]

# --- C1 : courbes de salaire net selon l'anciennete -------------------------
def c1():
    sel = ['pentest', 'analyste_soc' if 'analyste_soc' in BY else 'soc',
           'cloud_sec', 'admin_sys', 'gendarme_cyber', 'rssi']
    sel = [s for s in sel if s in BY]
    labels = ['0-2 ans', '2-4 ans', '4-7 ans', '7-12 ans', 'Expert', 'Manager']
    x = np.arange(6)
    fig, ax = plt.subplots(figsize=(9, 5.2))
    colors = [C_MAIN, C_MID, C_ACC, C_WARN, '#7f7f7f', '#5a2d82']
    for i, mid in enumerate(sel):
        ys = [net(BY[mid]['salaires'][k]['brut'][1]) for k in range(6)]
        ax.plot(x, ys, marker='o', linewidth=2, color=colors[i % 6],
                label=BY[mid]['nom'][:42])
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_xlabel('Anciennete (tranches indicatives, adaptees a chaque metier)')
    ax.set_ylabel('Salaire net apres IR (EUR/mois)')
    ax.set_title("Evolution du salaire net selon l'anciennete - 6 metiers representatifs")
    ax.legend(fontsize=7.5, loc='upper left')
    ax.yaxis.set_major_formatter(lambda v, p: f"{int(v):,}".replace(',', ' '))
    save(fig, 'c1_seniorite.png',
         'Source : barèmes Apec/Robert Half 2025, grilles gendarmerie 2025, offres observées. '
         'Hypothèses : cadre privé 23 % de cotisations, IR 2025, célibataire 1 part. Valeurs centrales.',
         'Données observées (salaires) + calcul fiscal')

# --- C2 : comparaison des nets, niveau confirme -----------------------------
def c2():
    rows = sorted(ALL, key=lambda m: net(salaire_mid := m['salaires'][2]['brut'][1]))
    names = [m['nom'][:46] for m in rows]
    vals = [net(m['salaires'][2]['brut'][1]) for m in rows]
    fig, ax = plt.subplots(figsize=(9, 7.5))
    ax.barh(names, vals, color=[C_MAIN if v >= 3000 else C_WARN for v in vals])
    for i, v in enumerate(vals):
        ax.text(v + 40, i, f"{int(v)}", va='center', fontsize=7.5)
    ax.axvline(3000, color=C_ACC, linestyle='--', linewidth=1)
    ax.text(3020, 0.2, 'seuil 3 000 EUR net', color=C_ACC, fontsize=7.5)
    ax.set_xlabel('Salaire net apres IR (EUR/mois)')
    ax.set_title('Salaire net estime au niveau confirme (4-7 ans) - 18 metiers')
    ax.set_xlim(0, max(vals) * 1.15)
    save(fig, 'c2_nets.png',
         'Source : barèmes 2025 (Apec, Robert Half, grilles officielles), valeurs centrales des fourchettes. '
         'Hypothèses : cadre 23 % cotisations, IR 2025, célibataire 1 part.',
         'Données observées (salaires) + calcul fiscal')

# --- C3 : public vs prive ----------------------------------------------------
def c3():
    fig, ax = plt.subplots(figsize=(9, 5.2))
    groups = [('Debutant (0-2 ans)', 0), ('Confirme (4-7 ans)', 2), ('Senior (7-12 ans)', 3)]
    gen = BY['gendarme_cyber']; adm = BY['admin_sys']; ing = BY['ingenieur_cyber']
    x = np.arange(len(groups)); w = 0.25
    pub = [net(gen['salaires'][g[1]]['brut'][1]) for g in groups]
    admv = [net(adm['salaires'][g[1]]['brut'][1]) for g in groups]
    ingv = [net(ing['salaires'][g[1]]['brut'][1]) for g in groups]
    ax.bar(x - w, pub, w, label='Gendarme (public, solde + primes)', color=C_ACC)
    ax.bar(x, admv, w, label='Admin sys (prive, PME/ESN)', color=C_WARN)
    ax.bar(x + w, ingv, w, label='Ingenieur cyber (prive)', color=C_MAIN)
    for dx, vals in ((-w, pub), (0, admv), (w, ingv)):
        for i, v in enumerate(vals):
            ax.text(x[i] + dx, v + 30, f"{int(v)}", ha='center', fontsize=7)
    ax.set_xticks(x); ax.set_xticklabels([g[0] for g in groups])
    ax.set_ylabel('Net apres IR (EUR/mois)')
    ax.set_title('Remuneration public (gendarmerie) vs prive - valeurs centrales')
    ax.legend(fontsize=8)
    save(fig, 'c3_public_prive.png',
         'Source : grilles indiciaires gendarmerie 2025 (point d\'indice 4,92278 EUR) vs barèmes privés 2025. '
         'Le net public inclut primes et logement estimés ; hors avantages en nature et pension.',
         'Données observées + calcul fiscal')

# --- C4 : risque IA ----------------------------------------------------------
def c4():
    rows = sorted(ALL, key=lambda m: -m['ia']['auto'])
    names = [m['nom'][:44] for m in rows]
    auto = [m['ia']['auto'] for m in rows]
    crea = [m['ia']['creation'] for m in rows]
    x = np.arange(len(rows)); h = 0.38
    fig, ax = plt.subplots(figsize=(9, 8))
    ax.barh(x + h/2, auto, h, label="Risque d'automatisation des taches (/100)", color=C_ACC)
    ax.barh(x - h/2, crea, h, label='Potentiel de creation de nouveaux emplois (/100)', color=C_MID)
    ax.set_yticks(x); ax.set_yticklabels(names, fontsize=7.5)
    ax.set_xlabel('Score /100 (voir methodologie, section 12)')
    ax.set_title("Impact de l'IA : automatisation vs creation d'emplois")
    ax.legend(fontsize=8, loc='lower right')
    save(fig, 'c4_ia_risque.png',
         "Source : scores d'expertise de cette étude, croisés avec Dares/France Stratégie (Les métiers en 2030), "
         'OCDE (27 % d\'emplois exposés), Insee (adoption IA 2025). Scores estimés, pas des probabilités mesurées.',
         'Estimation experte')

# --- C5 : perspectives d'emploi 2040 ----------------------------------------
def c5():
    years = [2025, 2030, 2035, 2040]
    series = {
        'Cybersecurite (moyenne des 6 metiers cyber)': ([100, 112, 121, 128], C_MAIN),
        'IT general (admin, reseaux, developpement)': ([100, 103, 105, 106], C_MID),
        'Support / exploitation N1': ([100, 88, 78, 70], C_ACC),
        'Filiere IA (ingenieur ML, securite IA)': ([100, 118, 130, 138], '#5a2d82')}
    fig, ax = plt.subplots(figsize=(9, 5.2))
    for lab, (vals, col) in series.items():
        ax.plot(years, vals, marker='o', color=col, label=lab, linewidth=2)
    ax.axhline(100, color='#999999', linewidth=0.8, linestyle=':')
    ax.set_ylabel("Indice de demande d'emploi (base 100 = 2025)")
    ax.set_xlabel('Annee')
    ax.set_title("Perspectives d'emploi a 2040 - projections par famille de metiers")
    ax.legend(fontsize=8, loc='upper left')
    ax.set_xticks(years)
    save(fig, 'c5_emploi2040.png',
         "Source : projections de cette étude, calées sur ANSSI (Observatoire 2025 : +49 % d'offres vs 2019), "
         'Dares/France Stratégie (Les métiers en 2030), LPM 2024-2030. Hypothèse centrale (croissance ~1 %/an, '
         'IA progressive).', 'PROJECTION, pas une donnée observee')

# --- C6 : matrice des scenarios politiques ----------------------------------
def c6():
    familles = ['Cybersecurite privee\n(ESN, cabinets)', 'Cybersecurite\npublic/defense',
                'IT general\n(admin, reseaux)', 'Support /\ntechnicien',
                'Filiere IA /\nML', 'Independants /\nfreelance']
    scen = ['RN', 'LFI /\ngauche', 'Centre /\ncontinuite', 'Droite\nclassique',
            'Contrainte\nbudgetaire']
    # effet net -2 (tres defavorable) a +2 (tres favorable) ; estimation
    M = np.array([
        [ 1,  1,  1,  1, -1],   # cyber privee
        [ 2,  0,  1,  1, -1],   # cyber public/defense
        [ 0,  0,  0,  0, -1],   # IT general
        [-1,  1,  0,  0, -1],   # support
        [ 2,  2,  1,  1,  0],   # filiere IA
        [ 1, -1,  0,  1, -1]])  # independants
    fig, ax = plt.subplots(figsize=(9, 4.8))
    im = ax.imshow(M, cmap='RdYlGn', vmin=-2, vmax=2, aspect='auto')
    ax.set_xticks(range(5)); ax.set_xticklabels(scen, fontsize=9)
    ax.set_yticks(range(6)); ax.set_yticklabels(familles, fontsize=8.5)
    txt = {-2: '--', -1: '-', 0: '0', 1: '+', 2: '++'}
    for i in range(6):
        for j in range(5):
            ax.text(j, i, txt[M[i, j]], ha='center', va='center', fontsize=11, fontweight='bold')
    ax.set_title('Matrice des effets politiques estimes par famille de metiers\n(-2 tres defavorable a +2 tres favorable, horizon 5-10 ans)')
    ax.grid(False)
    save(fig, 'c6_scenarios.png',
         "Source : analyse de cette étude à partir des programmes officiels (RN, LFI/Nouveau Front populaire 2024, "
         'LPM 2024-2030 votée) et des documents budgétaires. Effets plausibles, pas des prédictions.',
         'Estimation experte')

# --- C7 : duree d'etudes vs remuneration ------------------------------------
def c7():
    fig, ax = plt.subplots(figsize=(9, 5.2))
    xs, ys, names = [], [], []
    for m in ALL:
        d, _ = scoring.ETUDES[m['id']]
        lt = scoring.scores(m)['salaire_lt_eur']
        xs.append(d); ys.append(net(lt)); names.append(m['nom'][:30])
    ax.scatter(xs, ys, s=60, color=C_MAIN, alpha=0.75, zorder=3)
    for x, y, n in zip(xs, ys, names):
        ax.annotate(n, (x, y), textcoords='offset points', xytext=(5, 3),
                    fontsize=6.2, color='#333333')
    ax.set_xlabel("Duree d'etudes typique apres le Bac Pro (annees)")
    ax.set_ylabel('Salaire net a long terme (EUR/mois, niveau expert/manager)')
    ax.set_title("Duree d'etudes vs remuneration a long terme")
    ax.yaxis.set_major_formatter(lambda v, p: f"{int(v):,}".replace(',', ' '))
    save(fig, 'c7_duree_salaire.png',
         "Source : durées d'études typiques et salaires de cette étude (barèmes 2025). Chaque point = un métier, "
         'valeur centrale. Hypothèses fiscales : cadre 23 %, IR 2025, célibataire.',
         'Données observées + estimation')

# --- C8 : cout de formation vs ROI ------------------------------------------
def c8():
    fig, ax = plt.subplots(figsize=(9, 5.6))
    rows = sorted(ALL, key=lambda m: -scoring.ETUDES[m['id']][1])
    names = [m['nom'][:40] for m in rows]
    couts = [scoring.ETUDES[m['id']][1] for m in rows]
    base = net(scoring.BY_ID['technicien_it']['salaires'][2]['brut'][1])
    gains = [max(0, net(m['salaires'][3]['brut'][1]) - base) * 12 for m in rows]
    x = np.arange(len(rows)); h = 0.38
    ax.barh(x + h/2, couts, h, label="Cout total de la formation (EUR, hors alternance)", color=C_WARN)
    ax.barh(x - h/2, gains, h, label='Gain net annuel vs technicien IT confirme (EUR)', color=C_MAIN)
    ax.set_yticks(x); ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel('EUR')
    ax.set_title("Cout de formation vs rendement salarial annuel (niveau senior, net apres IR)")
    ax.legend(fontsize=8)
    save(fig, 'c8_cout_roi.png',
         "Source : coûts de formation estimés (public/privé, hors alternance qui annule le coût) et barèmes 2025. "
         'Référence de gain : technicien IT confirmé. Hypothèse : carrière de 35 ans.',
         'Estimation')

# --- C9 : risque vs opportunite ---------------------------------------------
def c9():
    fig, ax = plt.subplots(figsize=(9, 6))
    for m in ALL:
        s = scoring.scores(m)
        x = s['ia_resistance']; y = s['salaire_lt_eur'] / 1000.0
        size = 40 + s['demande'] * 2.2
        col = C_MAIN if s['total'] >= 70 else (C_MID if s['total'] >= 62 else C_WARN)
        ax.scatter(x, y, s=size, color=col, alpha=0.75, zorder=3)
        ax.annotate(m['nom'][:26], (x, y), textcoords='offset points',
                    xytext=(6, 3), fontsize=6.2)
    ax.set_xlabel("Resistance a l'IA (score /100, inverse du risque d'automatisation)")
    ax.set_ylabel('Salaire net a long terme (kEUR/mois, niveau expert/manager)')
    ax.set_title('Analyse risque / opportunite : resistance a l\'IA vs remuneration\n(taille des points = demande sur le marche)')
    ax.yaxis.set_major_formatter(lambda v, p: f"{v:.1f}")
    save(fig, 'c9_risque_opportunite.png',
         "Source : scores de cette étude (section 12) et barèmes 2025. Couleurs : bleu = score multicritère >= 70, "
         'turquoise >= 62, orange en dessous.', 'Estimation experte')

# --- C10 : classement multicritere ------------------------------------------
def c10():
    rows = scoring.classement()
    names = [r[0][:46] for r in rows][::-1]
    vals = [r[2]['total'] for r in rows][::-1]
    fig, ax = plt.subplots(figsize=(9, 7.5))
    cols = [C_MAIN if v >= 70 else (C_MID if v >= 62 else C_WARN) for v in vals]
    ax.barh(names, vals, color=cols)
    for i, v in enumerate(vals):
        ax.text(v + 0.4, i, f"{v:.1f}", va='center', fontsize=7.5)
    ax.set_xlabel('Score multicritere pondere (/100, ponderations section 12)')
    ax.set_title('Classement multicritere des 18 metiers (profil Bac Pro CIEL, ARA)')
    ax.set_xlim(0, 100)
    save(fig, 'c10_classement.png',
         'Source : moteur multicritère de cette étude. Poids : salaire LT 15, demande 15, stabilité 12, '
         "salaire départ 10, risque IA 10, accès depuis Bac Pro 10, intérêt 8, évolution 8, conditions 7, international 5.",
         'Estimation multicritère')

if __name__ == '__main__':
    c1(); c2(); c3(); c4(); c5(); c6(); c7(); c8(); c9(); c10()
    print('Tous les graphiques generes dans', OUT)

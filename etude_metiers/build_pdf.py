"""Construction du PDF final : etude metiers & avenir - Bac Pro CIEL.
18 sections, table des matieres, pagination, tableaux, graphiques.
"""
import os, sys
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Image, KeepTogether, ListFlowable, ListItem, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
sys.path.insert(0, BASE + '/data')
from fiscal import net_mensuel, ir_annuel
import scoring

CHARTS = os.path.join(BASE, 'charts')
OUTDIR = os.path.join(BASE, 'out')
os.makedirs(OUTDIR, exist_ok=True)
PDF_PATH = os.path.join(OUTDIR, 'Etude_metiers_avenir_BacPro_CIEL.pdf')

ALL = scoring.ALL
ALT = scoring.ALT
BY = scoring.BY_ID

INK = colors.HexColor('#1a1a2e')
BLUE = colors.HexColor('#1f4e79')
LBLUE = colors.HexColor('#dce6f1')
GREY = colors.HexColor('#f2f2f2')
RED = colors.HexColor('#c00000')
GREEN = colors.HexColor('#2e7d32')

S = {}
S['body'] = ParagraphStyle('body', fontName='Helvetica', fontSize=9.2, leading=12.6,
    textColor=INK, alignment=TA_JUSTIFY, spaceAfter=4)
S['small'] = ParagraphStyle('small', parent=S['body'], fontSize=8, leading=10.5,
    textColor=colors.HexColor('#444444'))
S['h1'] = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=17, leading=21,
    textColor=BLUE, spaceBefore=6, spaceAfter=10)
S['h2'] = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=12.5, leading=16,
    textColor=BLUE, spaceBefore=10, spaceAfter=5)
S['h3'] = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10.5, leading=13.5,
    textColor=colors.HexColor('#2e5f8a'), spaceBefore=8, spaceAfter=3)
S['h4'] = ParagraphStyle('h4', fontName='Helvetica-BoldOblique', fontSize=9.5, leading=12,
    textColor=INK, spaceBefore=6, spaceAfter=2)
S['bullet'] = ParagraphStyle('bullet', parent=S['body'], leftIndent=12, bulletIndent=4,
    spaceAfter=2, alignment=TA_LEFT)
S['cell'] = ParagraphStyle('cell', fontName='Helvetica', fontSize=7.6, leading=9.4, textColor=INK)
S['cellb'] = ParagraphStyle('cellb', parent=S['cell'], fontName='Helvetica-Bold')
S['cellh'] = ParagraphStyle('cellh', parent=S['cell'], fontName='Helvetica-Bold',
    textColor=colors.white, fontSize=7.8)
S['cover_t'] = ParagraphStyle('cover_t', fontName='Helvetica-Bold', fontSize=26, leading=32,
    textColor=colors.white, alignment=TA_CENTER)
S['cover_s'] = ParagraphStyle('cover_s', fontName='Helvetica', fontSize=13, leading=18,
    textColor=colors.HexColor('#dce6f1'), alignment=TA_CENTER)
S['toc'] = ParagraphStyle('toc', fontName='Helvetica', fontSize=10, leading=15, textColor=INK)

def P(txt, style='body'):
    return Paragraph(txt.replace('&', '&amp;'), S[style])

def B(items, style='bullet'):
    return ListFlowable([ListItem(Paragraph(i.replace('&', '&amp;'), S[style]), leftIndent=14)
                         for i in items], bulletType='bullet', start='•',
                        leftIndent=14, bulletFontSize=8)

def T(data, widths=None, header=True, fs=7.6, align_center_cols=None):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ('FONTSIZE', (0, 0), (-1, -1), fs),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#9aa7b5')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4)]
    if header:
        style += [('BACKGROUND', (0, 0), (-1, 0), BLUE),
                  ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]
        for r in range(1, len(data)):
            if r % 2 == 0:
                style.append(('BACKGROUND', (0, r), (-1, r), GREY))
    t.setStyle(TableStyle(style))
    return t

def cell(txt, bold=False, head=False):
    st = S['cellh'] if head else (S['cellb'] if bold else S['cell'])
    return Paragraph(str(txt).replace('&', '&amp;'), st)

def CH(name, w=16.5*cm):
    path = os.path.join(CHARTS, name)
    if not os.path.exists(path):
        return P(f"[graphique manquant : {name}]", 'small')
    from PIL import Image as PILImage
    im = PILImage.open(path)
    ratio = im.size[1] / im.size[0]
    return Image(path, width=w, height=w * ratio)

def money(v):
    return f"{v:,.0f}".replace(',', ' ') + ' EUR'

def fmt_net(brut, idx=1):
    n0, n1, _ = net_mensuel(brut)
    return n1 if idx == 1 else n0

class DocToc(SimpleDocTemplate):
    def afterFlowable(self, fl):
        if isinstance(fl, Paragraph) and fl.style.name == 'h1':
            self.notify('TOCEntry', (0, fl.getPlainText(), self.page))
        elif isinstance(fl, Paragraph) and fl.style.name == 'h2':
            self.notify('TOCEntry', (1, fl.getPlainText(), self.page))

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(colors.HexColor('#666666'))
    canvas.drawString(1.4*cm, 0.85*cm, "Etude metiers & avenir - Bac Pro CIEL - cybersécurité, IA, réseaux")
    canvas.drawRightString(A4[0]-1.4*cm, 0.85*cm, f"Page {doc.page}")
    if doc.page > 2:
        canvas.setStrokeColor(colors.HexColor('#bbbbbb'))
        canvas.setLineWidth(0.4)
        canvas.line(1.4*cm, 1.1*cm, A4[0]-1.4*cm, 1.1*cm)
    canvas.restoreState()

def cover():
    fl = []
    fl.append(Spacer(1, 4.2*cm))
    tbl = Table([[Paragraph("ÉTUDE APPROFONDIE<br/>DES MÉTIERS ET DE LEUR AVENIR", S['cover_t'])]],
                colWidths=[17*cm])
    tbl.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 26), ('BOTTOMPADDING', (0,0), (-1,-1), 26)]))
    fl.append(tbl)
    fl.append(Spacer(1, 1.0*cm))
    fl.append(Paragraph("Cybersécurité, intelligence artificielle, systèmes et réseaux,<br/>métiers publics : quel chemin après un Bac Pro CIEL ?", S['cover_s']))
    fl.append(Spacer(1, 0.6*cm))
    fl.append(Paragraph("Profil : France - région Auvergne-Rhône-Alpes (secteur d'Annonay)<br/>18 métiers étudiés en détail + 8 métiers alternatifs - 10 graphiques - scénarios 2030/2040", S['cover_s']))
    fl.append(Spacer(1, 3.2*cm))
    fl.append(Paragraph(f"Dossier d'aide à la décision généré le {date.today().strftime('%d/%m/%Y')}", S['cover_s']))
    fl.append(Paragraph("Données : sources officielles et barèmes 2024-2025 (voir section 18 - Sources et méthodologie)", S['cover_s']))
    fl.append(PageBreak())
    return fl

def toc_page(story):
    story.append(Paragraph("Table des matières", S['h1']))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle('toc0', fontName='Helvetica-Bold', fontSize=10.5, leading=16,
                       textColor=BLUE, leftIndent=0),
        ParagraphStyle('toc1', fontName='Helvetica', fontSize=9, leading=13,
                       textColor=INK, leftIndent=14)]
    story.append(toc)
    story.append(PageBreak())

# ============================ SECTIONS 1-4 ==================================

def sec_resume(story):
    story.append(Paragraph("1. Résumé exécutif", S['h1']))
    story.append(P("Ce dossier répond à une question simple : <b>quel chemin suivre après un Bac Pro CIEL "
        "pour maximiser tes chances d'un métier stable, bien payé et intéressant</b>, en région "
        "Auvergne-Rhône-Alpes, dans un monde où l'intelligence artificielle transforme le travail ? "
        "18 métiers ont été étudiés en détail (fiches section 5) et 8 métiers alternatifs ou méconnus "
        "(section 13), avec salaires, parcours, probabilités de réussite, impact de l'IA et scénarios politiques."))
    story.append(P("<b>Les 10 conclusions principales :</b>"))
    story.append(B([
        "<b>Le marché de la cybersécurité reste favorable mais n'est plus un eldorado pour débutants.</b> "
        "23 000 offres d'emploi publiées entre juin 2023 et juin 2024 (ANSSI, Observatoire 2025), environ "
        "15 000 postes non pourvus en 2025 - mais 75,9 % des recrutements exigent un bac+5. Le marché junior "
        "(SOC L1, pentester junior) est saturé côté candidats ; les segments favorables aux juniors sont la "
        "sécurité cloud, le DevSecOps et la sécurité applicative (Zeroday 2025).",
        "<b>Le diplôme pèse plus que tu ne le penses.</b> 47 % des offres cyber exigent un bac+5. Depuis un "
        "Bac Pro CIEL, la voie la plus réaliste est : BTS ou BUT en alternance (gratuit, rémunéré) -> licence "
        "pro ou BUT3, puis éventuellement master. Les certifications seules ne remplacent pas un diplôme "
        "pour un premier emploi.",
        "<b>Les salaires réels sont inférieurs aux chiffres médiatisés.</b> Médiane cadre sécurité : 60 000 EUR "
        "brut/an (Apec 2025), mais 80 % des cadres sécurité gagnent entre 43 000 et 99 000 EUR. Un débutant "
        "SOC en province gagne 32 000-40 000 EUR brut (2 200-2 700 EUR net/mois), pas les 45 kEUR des annonces "
        "parisiennes.",
        "<b>Le meilleur point d'entrée n'est pas le pentest mais l'administration systèmes et réseaux</b> "
        "(ou le SOC via alternance) : demande plus large, moins de concurrence, salaire de départ comparable, "
        "et toutes les portes restent ouvertes ensuite.",
        "<b>Les métiers les plus résistants à l'IA sont ceux qui combinent responsabilité humaine, physique "
        "ou réglementaire</b> : gendarmerie, sécurité OT/industrielle, RSSI, architecte, pentester matériel. "
        "Les plus exposés à l'automatisation des tâches : support N1, SOC L1, audit documentaire de base.",
        "<b>L'IA est plus un levier qu'une menace pour les profils qui la maîtrisent.</b> Les scores de cette "
        "étude (section 8) montrent que les métiers hybrides IA+cyber (sécurité des systèmes d'IA, pentester "
        "IA, analyste CTI outillé) offrent les meilleurs rapports risque/opportunité, mais exigent un "
        "bac+5 et une vraie culture logicielle.",
        "<b>La gendarmerie est le choix stabilité absolu</b> (sécurité d'emploi quasi totale, logement, "
        "pension), mais le cyber y est une spécialisation de seconde phase (après 3-6 ans de brigade) et "
        "la solde de départ (~1 850-2 100 EUR net en poste) est inférieure au privé. Le Bac Pro CIEL y est "
        "un atout réel pour la spécialisation.",
        "<b>Les scénarios politiques pèsent moins que la réglementation européenne déjà votée.</b> NIS2, DORA "
        "et le Cyber Resilience Act créent une demande réglementaire qui survivra aux alternances. Le risque "
        "principal est budgétaire (contrainte des finances publiques) plus que partisan.",
        "<b>Le coût de la vie en ARA joue en ta faveur</b> : un net de 2 500 EUR autour d'Annonay (loyer "
        "~500-650 EUR pour un T2) procure plus de pouvoir d'achat qu'un net de 3 200 EUR à Paris (loyer "
        "~1 000-1 300 EUR). Ne compare jamais des salaires sans comparer des loyers.",
        "<b>Recommandation centrale (détail section 15) :</b> BTS CIEL ou BUT en alternance -> poste admin "
        "systèmes/réseaux ou SOC -> spécialisation sécurité cloud ou cybersécurité générale -> expertise "
        "(architecte, consultant senior ou RSSI). Ce parcours maximise la probabilité de réussite, garde "
        "toutes les options ouvertes (dont pentest et gendarmerie) et minimise le risque financier."]))
    story.append(P("<b>Honnêteté sur les limites :</b> les probabilités et scores de ce dossier sont des "
        "estimations raisonnées à partir de données publiques, pas des mesures statistiques par métier "
        "(elles n'existent pas). Les salaires sont des fourchettes, pas des promesses. Chaque chiffre est "
        "daté et sourcé en section 18."))

def sec_profil(story):
    story.append(Paragraph("2. Profil et critères de décision", S['h1']))
    story.append(Paragraph("2.1 Ce qui est connu", S['h2']))
    story.append(T([
        [cell('Élément', head=True), cell('Valeur', head=True), cell("Conséquence pour l'étude", head=True)],
        [cell('Pays / régime'), cell('France'), cell('Barèmes fiscaux et sociaux français, réglementation UE')],
        [cell('Région'), cell("Auvergne-Rhône-Alpes, secteur d'Annonay"), cell('Marché local : PME, industrie, ESN de Lyon/Saint-Étienne/Grenoble ; salaires province (-5 à -15 % vs IDF)')],
        [cell('Formation'), cell('Bac Pro CIEL (cybersécurité, informatique et réseaux, électronique)'), cell("Accès direct : technicien ; accès diplômant : BTS, BUT, licences pro ; l'électronique est un atout différenciant (OT, IoT, embarqué)")],
        [cell('Intérêts déclarés'), cell('Cyber, pentest, IA appliquée, sysadmin/réseaux, gendarmerie cyber'), cell('18 métiers dont 12 cyber, 4 IA/IT, 2 publics')],
        [cell('Priorités'), cell('Équilibre rémunération / stabilité / évolution / intérêt / résistance aux chocs'), cell('Classement multicritère pondéré (section 12)')]],
        widths=[3.2*cm, 5.2*cm, 8.2*cm]))
    story.append(Paragraph("2.2 Hypothèses posées (à corriger si elles sont fausses)", S['h2']))
    story.append(B([
        "<b>Âge :</b> 17-19 ans en fin de Bac Pro (hypothèse standard). Si tu es plus âgé, les parcours en "
        "alternance restent valables (rémunération plus élevée).",
        "<b>Mobilité :</b> tu es prêt à suivre des études dans une grande ville d'ARA (Lyon, Saint-Étienne, "
        "Grenoble, Clermont, Annecy) ou à distance/hybride, mais pas forcément à Paris. Les parcours IDF "
        "sont indiqués comme option, pas comme référence.",
        "<b>Financement :</b> pas de contrainte financière majeure grâce à l'alternance (rémunéré) ; les "
        "coûts indiqués supposent l'enseignement public ou l'alternance, jamais l'école privée payante "
        "sauf mention explicite.",
        "<b>Résultats scolaires :</b> niveau correct permettant d'accéder à un BTS (peu sélectif) ; les "
        "parcours sélectifs (BUT très demandé, écoles, concours) sont signalés comme tels.",
        "<b>Situation familiale/fiscale :</b> célibataire sans enfant, 1 part fiscale, pour tous les calculs "
        "de net après impôt.",
        "<b>Préférence de vie :</b> rester en ARA est un plus, pas une contrainte absolue. Les stratégies "
        "distance/IDF sont évaluées quand elles changent significativement le résultat."]))
    story.append(Paragraph("2.3 Critères de décision retenus", S['h2']))
    story.append(P("Cinq critères guident les recommandations, dans cet ordre d'importance : (1) probabilité "
        "de réussite du parcours depuis un Bac Pro CIEL ; (2) rémunération à long terme (10-15 ans) ; (3) "
        "stabilité et résistance aux chocs (IA, cycles économiques, politique) ; (4) intérêt technique du "
        "métier ; (5) diversité des portes ouvertes en cas de changement d'avis. La pondération complète "
        "est en section 12."))

def sec_panorama(story):
    story.append(Paragraph("3. Panorama des 18 métiers", S['h1']))
    story.append(P("Vue d'ensemble avant les fiches détaillées. « Accès » indique le niveau d'études "
        "minimal réaliste ; « depuis Bac Pro CIEL » note la compatibilité directe de ton diplôme avec "
        "l'entrée dans la filière."))
    rows = [[cell('Métier', head=True), cell('Famille', head=True), cell('Accès', head=True),
             cell('Débutant brut/an', head=True), cell('Expert brut/an', head=True),
             cell('Score /100', head=True)]]
    for m in ALL:
        s = scoring.scores(m)
        rows.append([cell(m['nom'], bold=True), cell(m['famille']), cell(m['acces']),
            cell(money(m['salaires'][0]['brut'][1])), cell(money(max(m['salaires'][4]['brut'][1], m['salaires'][5]['brut'][1]))),
            cell(f"{s['total']:.0f}")])
    story.append(T(rows, widths=[4.6*cm, 2.9*cm, 3.2*cm, 2.2*cm, 2.2*cm, 1.5*cm]))
    story.append(P("Le score /100 combine 10 critères pondérés (méthode section 12). Il privilégie la "
        "demande, la stabilité et la rémunération long terme ; un score élevé ne signifie pas « facile "
        "d'accès » : l'architecte (79,5) et le RSSI (66,0) sont des postes d'expérience, pas de sortie d'études.", 'small'))
    story.append(Spacer(1, 6))
    story.append(Paragraph("3.1 Comment lire les niveaux d'accès depuis un Bac Pro CIEL", S['h2']))
    story.append(B([
        "<b>Accès immédiat (0 étude supplémentaire) :</b> technicien informatique et réseaux, technicien "
        "télécoms/fibre, gendarme (après concours). Emploi rapide, salaire modeste.",
        "<b>Accès à 2-3 ans (BTS/BUT/licence pro, idéalement en alternance) :</b> admin systèmes et réseaux, "
        "analyste SOC, ingénieur systèmes et réseaux, électronicien embarqué, auditeur (voie courte).",
        "<b>Accès à 4-5 ans (BUT+ ou master, école) :</b> ingénieur cybersécurité, consultant, cloud, "
        "DevSecOps, DFIR, pentest, ML engineer, auditeur confirmé.",
        "<b>Accès à 5-6+ ans et/ou après expérience (postes d'expérience) :</b> architecte cybersécurité, "
        "RSSI, sécurité OT expert, pentester IA, sécurité des systèmes d'IA, pentester matériel."]))

def sec_fiches(story):
    story.append(Paragraph("4. Fiches détaillées des 18 métiers", S['h1']))
    story.append(P("Chaque fiche suit le même plan : A) description et réalité du métier ; B) parcours "
        "possibles depuis le Bac Pro CIEL ; C) salaires détaillés par niveau (brut, net avant et après "
        "impôt, calculé avec les hypothèses de la section 12) ; D) progression de carrière ; E) impact de "
        "l'IA ; F) probabilités et scénarios. Les fiches sont numérotées 4.1 à 4.18 pour rester "
        "navigables dans la table des matières."))
    for i, m in enumerate(ALL, 1):
        story.append(CondPageBreak(4*cm))
        story.append(Paragraph(f"4.{i} {m['nom']}", S['h2']))
        story.append(P(f"<b>Autres appellations :</b> {m['alt']}<br/><b>Famille :</b> {m['famille']} - "
            f"<b>Accès :</b> {m['acces']}", 'small'))
        story.append(Paragraph("A. Description et réalité du métier", S['h3']))
        story.append(P(m['description']))
        story.append(Paragraph("Missions quotidiennes", S['h4']))
        story.append(B(m['missions']))
        story.append(Paragraph("Outils et technologies", S['h4']))
        story.append(P(m['outils'], 'small'))
        story.append(Paragraph("Conditions d'exercice", S['h4']))
        story.append(T([
            [cell('Dimension', head=True), cell('Réalité du métier', head=True)],
            [cell('Difficulté technique'), cell(m['difficulte'])],
            [cell('Répartition du travail'), cell(m['taches'])],
            [cell('Autonomie'), cell(m['autonomie'])],
            [cell('Équipe / seul'), cell(m['equipe'])],
            [cell('Télétravail'), cell(m['teletravail'])],
            [cell('Horaires et astreintes'), cell(m['horaires'])],
            [cell('Urgences / déplacements'), cell(m['urgences'])],
            [cell('Stress et risques'), cell(m['stress'])],
            [cell('Théorie vs réalité'), cell(m['realite'])]],
            widths=[3.4*cm, 13.2*cm]))
        story.append(Spacer(1, 3))
        two = Table([[cell('<b>Avantages</b><br/>' + '<br/>'.join('- ' + a for a in m['avantages'])),
                      cell('<b>Inconvénients</b><br/>' + '<br/>'.join('- ' + a for a in m['inconvenients']))]],
                    colWidths=[8.3*cm, 8.3*cm])
        two.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BACKGROUND', (0,0), (0,0), colors.HexColor('#e8f2ea')),
            ('BACKGROUND', (1,0), (1,0), colors.HexColor('#f9e9e9')),
            ('BOX', (0,0), (0,0), 0.4, colors.HexColor('#9aa7b5')),
            ('BOX', (1,0), (1,0), 0.4, colors.HexColor('#9aa7b5')),
            ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
        story.append(two)
        story.append(Spacer(1, 3))
        story.append(Paragraph("Compétences", S['h4']))
        story.append(P(f"<b>Indispensables :</b> {' ; '.join(m['comp_req'])}", 'small'))
        story.append(P(f"<b>Utiles (facultatives) :</b> {' ; '.join(m['comp_opt'])}", 'small'))
        story.append(Paragraph("Qualités personnelles", S['h4']))
        story.append(P(m['qualites'], 'small'))
        fiche_parcours(story, m)
        fiche_salaires(story, m)
        fiche_suite(story, m)


def fiche_parcours(story, m):
    story.append(Paragraph("B. Parcours possibles depuis le Bac Pro CIEL", S['h3']))
    for p_ in m['parcours']:
        story.append(Paragraph(p_['nom'], S['h4']))
        story.append(T([
            [cell('Élément', head=True), cell('Détail', head=True)],
            [cell('Description'), cell(p_['desc'])],
            [cell('Durée'), cell(p_['duree'])],
            [cell('Difficulté / sélectivité'), cell(p_['difficulte'] + ' / ' + p_['selectivite'])],
            [cell('Coût'), cell(p_['cout'])],
            [cell('Financement'), cell(p_['financement'])],
            [cell("Probabilité d'atteindre le métier"), cell(p_['prob'])],
            [cell('Métiers intermédiaires'), cell(' -> '.join(p_['paliers']))],
            [cell('Réorientations possibles'), cell(p_['reorient'])]],
            widths=[3.8*cm, 12.8*cm]))
        story.append(Spacer(1, 3))

def fiche_salaires(story, m):
    story.append(Paragraph("C. Salaires détaillés", S['h3']))
    story.append(P("Net avant IR = brut - cotisations salariales (23 %, cadre privé). Net après IR = net "
        "avant IR moins l'impôt sur le revenu calculé au barème 2025, célibataire, 1 part, abattement 10 %. "
        "Méthode complète en section 12. Valeurs centrales des fourchettes basse/centrale/haute.", 'small'))
    rows = [[cell('Niveau', head=True), cell('Brut annuel (b / c / h)', head=True),
             cell('Net mensuel avant IR (c)', head=True), cell('Net mensuel après IR (b / c / h)', head=True),
             cell('Région / secteur', head=True), cell('Variable', head=True)]]
    for s_ in m['salaires']:
        bl, bm, bh = s_['brut']
        if bm <= 0:
            rows.append([cell(s_['niveau'], bold=True), cell("N/A (poste d'expérience)"), cell('-'), cell('-'),
                         cell(s_['region']), cell(s_['variable'])])
            continue
        n0c, n1c, _ = net_mensuel(bm)
        n1b, _, _ = net_mensuel(bl); n1h, _, _ = net_mensuel(bh)
        rows.append([cell(s_['niveau'], bold=True),
            cell(f"{bl:,} / {bm:,} / {bh:,}".replace(',', ' ')),
            cell(f"{n0c:,.0f}".replace(',', ' ')),
            cell(f"{n1b:,.0f} / {n1c:,.0f} / {n1h:,.0f}".replace(',', ' ')),
            cell(s_['region']), cell(s_['variable'])])
    story.append(T(rows, widths=[3.3*cm, 2.9*cm, 2.2*cm, 2.9*cm, 3.0*cm, 2.3*cm]))
    story.append(P(m['sal_note'], 'small'))

def fiche_suite(story, m):
    story.append(Paragraph("D. Progression de carrière", S['h3']))
    story.append(P(m['progression']))
    story.append(Paragraph("E. Impact de l'intelligence artificielle", S['h3']))
    ia = m['ia']
    story.append(T([
        [cell('Score /100', head=True), cell('Valeur', head=True), cell('Signification', head=True)],
        [cell("Risque d'automatisation des tâches"), cell(str(ia['auto'])), cell('Part des tâches actuelles automatisables à 10-15 ans')],
        [cell('Risque de baisse des recrutements'), cell(str(ia['recrut'])), cell('Pression sur le volume de postes (surtout juniors)')],
        [cell('Risque de transformation profonde'), cell(str(ia['transfo'])), cell('Changement du contenu du métier, pas sa disparition')],
        [cell('Potentiel de création de nouveaux emplois'), cell(str(ia['creation'])), cell("Nouvelles spécialités et demandes liées à l'IA")],
        [cell("Capacité à utiliser l'IA comme levier"), cell(str(ia['levier'])), cell('Gain de productivité et de valeur pour le professionnel')]],
        widths=[5.6*cm, 1.6*cm, 9.4*cm]))
    story.append(P(f"<b>Horizon 2030 :</b> {ia['h2030']}", 'small'))
    story.append(P(f"<b>Horizon 2035 :</b> {ia['h2035']}", 'small'))
    story.append(P(f"<b>Horizon 2040 :</b> {ia['h2040']}", 'small'))
    story.append(P(f"<b>Limites du score :</b> {ia['notes']}", 'small'))
    story.append(Paragraph("F. Probabilités et scénarios d'avenir", S['h3']))
    pr = m['probs']
    story.append(T([
        [cell('Question', head=True), cell('Estimation', head=True)],
        [cell("Obtenir un premier emploi après le parcours proposé"), cell(pr['premier_emploi'])],
        [cell("Atteindre le niveau confirmé"), cell(pr['confirme'])],
        [cell('Salaire > 2 500 EUR net/mois'), cell(pr['seuils']['2500'])],
        [cell('Salaire > 3 000 EUR net/mois'), cell(pr['seuils']['3000'])],
        [cell('Salaire > 4 000 EUR net/mois'), cell(pr['seuils']['4000'])],
        [cell('Salaire > 5 000 EUR net/mois'), cell(pr['seuils']['5000'])],
        [cell('Risque de chômage / reconversion'), cell(pr['chomage'])],
        [cell('Formation continue nécessaire'), cell(pr['formation'])],
        [cell("Risque d'obsolescence des compétences"), cell(pr['obsolescence'])],
        [cell("Base de l'estimation"), cell(pr['base'])]],
        widths=[5.2*cm, 11.4*cm]))
    sc = m['scenarios']
    story.append(T([
        [cell('Scénario', head=True), cell('Effet sur le métier (horizon 5-15 ans)', head=True)],
        [cell('Défavorable', bold=True), cell(sc['defav'])],
        [cell('Central', bold=True), cell(sc['central'])],
        [cell('Favorable', bold=True), cell(sc['fav'])],
        [cell('Événement de bascule', bold=True), cell(sc['bascule'])]],
        widths=[3.6*cm, 13.0*cm]))
    story.append(PageBreak())

def sec_parcours(story):
    story.append(Paragraph("5. Parcours de formation après le Bac Pro CIEL", S['h1']))
    story.append(P("Cette section compare les voies d'études transversalement, indépendamment du métier "
        "cible. Les parcours détaillés par métier sont dans les fiches (section 4, partie B)."))
    story.append(Paragraph("5.1 Les cinq grandes voies", S['h2']))
    rows = [[cell('Voie', head=True), cell('Durée', head=True), cell('Coût pour toi', head=True),
             cell('Sélectivité', head=True), cell('Débouchés typiques', head=True),
             cell('Probabilité de réussite', head=True)]]
    rows += [
        [cell('Entrée directe + certifications', bold=True), cell('0 an'), cell('0 (CPF/employeur)'),
         cell('Faible'), cell('Technicien IT/télécoms, helpdesk'), cell('60-75 % emploi rapide ; plafond salarial bas')],
        [cell('BTS CIEL/SIO en alternance', bold=True), cell('2 ans'), cell('0 (rémunéré)'),
         cell('Faible-moyenne (trouver un employeur)'), cell('Technicien N2, admin junior, SOC junior'),
         cell('70-85 % ; meilleure voie court terme')],
        [cell('BUT (R&T, Info, GEII) puis BUT3 ou licence pro', bold=True), cell('3-4 ans'), cell('0-600 EUR/an (public)'),
         cell('Moyenne-élevée en admission'), cell('Ingénieur réseaux, SOC, cloud junior'),
         cell('55-70 % ; voie équilibrée')],
        [cell('Licence pro (post-BTS/BUT2)', bold=True), cell('1 an'), cell('0 en alternance'),
         cell('Moyenne'), cell('Spécialisation sécurité/réseaux, insertion rapide'),
         cell('60-75 % avec alternance')],
        [cell('Master / école (Bac+5)', bold=True), cell('5 ans'), cell('0-2 000 EUR/an public ; 8-15 kEUR privé'),
         cell('Élevée'), cell('Ingénieur cyber, ML, cloud, consultant'),
         cell("60-75 % ; conditions d'accès exigeantes")]]
    story.append(T(rows, widths=[4.2*cm, 1.6*cm, 2.6*cm, 2.6*cm, 3.2*cm, 2.4*cm]))
    story.append(Paragraph("5.2 La stratégie alternance (recommandée)", S['h2']))
    story.append(P("L'alternance est le levier central de ton profil : elle annule le coût des études, "
        "fournit une première expérience et un réseau. Rémunération apprenti 2025-2026 (SMIC 1 801,80 EUR "
        "brut au 01/2025) : 18-20 ans, 43 % (BTS1) puis 51 % (BTS2) ; 21-25 ans, 53 % puis 61 % puis 78 % "
        "(BUT/licence pro) ; à partir de 26 ans ou en 3e cycle : 100 % du SMIC ou du minimum conventionnel. "
        "Les salaires d'apprentis sont exonérés d'impôt sur le revenu dans la limite d'un plafond annuel "
        "(2025 : 20 889 EUR). L'employeur peut recevoir une aide unique jusqu'à 5 000 EUR (6 000 EUR pour "
        "les entreprises de moins de 250 salariés et formations jusqu'au bac, décret n° 2025-174 du "
        "28 février 2025)."))
    story.append(Paragraph("5.3 Parcours par certifications : ce qui est vrai", S['h2']))
    story.append(B([
        "<b>Ce que les certifications font :</b> débloquer des entretiens (CCNA, CompTIA Security+), "
        "valider une spécialité (OSCP, CISSP, AWS Security), accélérer une évolution interne.",
        "<b>Ce qu'elles ne font pas :</b> remplacer un diplôme pour un premier emploi dans les grandes "
        "structures (filtres RH bac+3/5), ni garantir un salaire. Aucune certification n'est une garantie "
        "d'embauche.",
        "<b>Ordre réaliste depuis Bac Pro CIEL :</b> CCNA ou CompTIA Network+ pendant le BTS -> Security+ "
        "-> première expérience -> spécialisation (OSCP pour le pentest, AWS/Azure Security pour le cloud, "
        "CISSP après 5 ans d'expérience - elle exige de toute façon 5 ans).",
        "<b>Coûts indicatifs 2025 :</b> CompTIA ~400-550 EUR, CCNA ~300-350 EUR, OSCP ~1 700-2 600 EUR, "
        "CISSP ~700-800 EUR (hors formation). Souvent pris en charge par l'employeur ou le CPF."]))
    story.append(Paragraph("5.4 Le piège du « diplôme obligatoire » et son contournement réel", S['h2']))
    story.append(P("47 % des offres cyber exigent un bac+5 (ANSSI 2025) : ce filtre est réel dans les "
        "grands groupes, les cabinets et l'administration. Mais 33 % des recrutés n'ont pas de diplôme "
        "cyber spécialisé : les profils réseaux/systèmes reconvertis sont recherchés. La voie réaliste "
        "sans bac+5 est donc : expérience technique solide (admin, SOC) + certifications ciblées + "
        "mobilité interne, en visant les PME/ETI et les ESN régionales, moins filtreuses que les "
        "grands cabinets."))


def sec_salaires(story):
    story.append(Paragraph("6. Comparaison des salaires par niveau d'expérience", S['h1']))
    story.append(P("Tous les montants sont des valeurs centrales de fourchettes (basse/centrale/haute) "
        "issues des barèmes et offres cités en section 17. Conversion en net : hypothèses cadre privé "
        "(23 % de cotisations salariales), barème IR 2025, célibataire 1 part. Le détail par métier est "
        "dans chaque fiche (partie C)."))
    story.append(Paragraph("6.1 Tableau comparatif - nets après impôt par niveau (EUR/mois)", S['h2']))
    noms_niveaux = ['Débutant (0-2 ans)', 'Junior (2-4 ans)', 'Confirmé (4-7 ans)',
                    'Senior (7-12 ans)', 'Expert', 'Manager']
    rows = [[cell('Métier', head=True)] + [cell(n, head=True) for n in noms_niveaux]]
    for m in ALL:
        row = [cell(m['nom'][:44], bold=True)]
        for k in range(6):
            bm = m['salaires'][k]['brut'][1]
            row.append(cell('-' if bm <= 0 else f"{fmt_net(bm):,.0f}".replace(',', ' ')))
        rows.append(row)
    story.append(T(rows, widths=[4.9*cm] + [1.93*cm]*6))
    story.append(P("Un tiret (-) signifie que le niveau n'existe pas pour ce métier (postes d'expérience "
        "comme RSSI, ou grilles militaires sans équivalent). Lecture : ces montants sont des estimations "
        "centrales ; les fourchettes réelles s'étendent typiquement de -15 % à +25 % autour de la valeur "
        "centrale selon la région, le secteur et l'entreprise.", 'small'))
    story.append(Spacer(1, 4))
    story.append(CH('c1_seniorite.png'))
    story.append(Spacer(1, 4))
    story.append(CH('c2_nets.png'))
    story.append(Paragraph("6.2 Public vs prive : la comparaison honnete", S['h2']))
    story.append(P("La gendarmerie ne se compare pas au prive avec le seul net : le logement de fonction "
        "(ou indemnité), la sécurité d'emploi, la formation gratuite et la pension compensent une solde "
        "inférieure. Le graphique suivant montre les valeurs centrales pures, hors ces avantages."))
    story.append(CH('c3_public_prive.png'))

def sec_ia(story):
    story.append(Paragraph("7. Analyse de l'intelligence artificielle", S['h1']))
    story.append(Paragraph("7.1 Ce que disent les études sérieuses", S['h2']))
    story.append(B([
        "<b>Dares / France Stratégie, « Les métiers en 2030 » (2022) :</b> environ 15 % des emplois sont à "
        "risque fort d'automatisation et 32 % en transformation ; les métiers qualifiés techniques sont "
        "plutôt en transformation qu'en disparition. Pas de consensus scientifique sur l'effet net des "
        "grands modèles de langage.",
        "<b>OCDE (2023) :</b> environ 27 % des emplois sont « exposés » à l'IA générative - exposé ne "
        "signifie pas remplacé : la plupart seront transformés.",
        "<b>Insee (2025) :</b> 18 % des entreprises de 10 salariés ou plus utilisent l'IA générative en "
        "2025 (contre 10 % en 2024) : l'adoption est réelle mais progressive.",
        "<b>ANSSI, Observatoire des métiers cyber (2025) :</b> la demande cyber reste supérieure à l'offre "
        "(~15 000 postes non pourvus), et l'IA est perçue par les professionnels comme un outil à maîtriser "
        "plus qu'une menace directe sur l'emploi."]))
    story.append(Paragraph("7.2 Les cinq scores et leur méthode", S['h2']))
    story.append(T([
        [cell('Score', head=True), cell('Définition', head=True), cell('Comment il est estimé', head=True)],
        [cell("Risque d'automatisation (auto)"), cell('Part des tâches actuelles automatisables à 10-15 ans'),
         cell('Décomposition du métier en tâches (partie A des fiches) + littérature Dares/OCDE ; jugement expert calibré')],
        [cell('Risque de baisse des recrutements'), cell('Pression sur le volume de postes, surtout juniors'),
         cell("Ratio demande/productivité : si l'IA augmente la productivité de 30 % sans hausse de demande, les recrutements juniors baissent")],
        [cell('Risque de transformation'), cell('Changement profond du contenu du métier'),
         cell('Analyse des tendances technologiques et réglementaires par horizon')],
        [cell('Potentiel de création'), cell('Nouvelles spécialités créées par l\'IA'),
         cell('Offres existantes (LLM security, AI governance) + trajectoire réglementaire (AI Act, CRA)')],
        [cell("Levier IA"), cell("Gain de valeur pour celui qui maîtrise l'IA"),
         cell('Observation des écarts de salaire entre profils outillés et non outillés + TJM indépendants')]],
        widths=[3.6*cm, 5.2*cm, 7.8*cm]))
    story.append(P("<b>Limites honnêtes :</b> ces scores sont des estimations d'expertise, pas des "
        "probabilités mesurées. Aucune institution ne publie de statistique fiable « risque IA par "
        "métier » pour la France. Les scores servent à comparer des métiers entre eux, pas à prédire "
        "l'avenir d'un individu. Les horizons 2030/2035/2040 décrivent des trajectoires plausibles, "
        "détaillées métier par métier dans les fiches (partie E)."))
    story.append(Paragraph("7.3 Lecture transversale", S['h2']))
    story.append(CH('c4_ia_risque.png'))
    story.append(P("Trois enseignements : (1) les métiers physiques et d'autorité publique (gendarmerie, "
        "télécoms terrain) sont les moins automatisables ; (2) les métiers de support et de conformité "
        "documentaire sont les plus exposés aux tâches automatisables mais bénéficient d'une demande "
        "réglementaire qui compense ; (3) les métiers hybrides IA+cyber combinent le plus faible risque "
        "de recrutement décroissant avec le plus fort potentiel de création - mais exigent le plus long "
        "parcours d'études."))

def sec_politique(story):
    story.append(Paragraph("8. Analyse des scénarios politiques", S['h1']))
    story.append(P("Cette section évalue comment cinq familles de scénarios politiques pourraient "
        "modifier tes perspectives. Elle distingue systématiquement : <b>(1) mesures officiellement "
        "proposées</b> (programmes), <b>(2) mesures adoptées</b> (lois, budgets votés), <b>(3) "
        "conséquences économiques plausibles</b>, <b>(4) hypothèses spéculatives</b>. Aucun jugement de "
        "valeur politique : uniquement des effets sur l'emploi, les salaires et les financements."))
    story.append(Paragraph("8.1 État des lieux adopté (base de tous les scénarios)", S['h2']))
    story.append(B([
        "<b>LPM 2024-2030 (loi de programmation militaire, votée 2023) :</b> 413 MdEUR de crédits dont "
        "environ 4 MdEUR pour la cyber (budget multiplié par 3) et +953 ETP cyber dans les armées. "
        "Adopté : c'est la référence contraignante jusqu'en 2030.",
        "<b>NIS2 (directive UE, transposée en cours) :</b> 10 000 à 15 000 entités françaises assujetties "
        "à de nouvelles obligations de sécurité et de signalement. Adopté au niveau UE.",
        "<b>DORA (règlement UE, applicable depuis janvier 2025) :</b> obligations de résilience "
        "informatique pour le secteur financier. Adopté.",
        "<b>Cyber Resilience Act (règlement UE, entrée en application progressive 2026-2027) :</b> "
        "exigences de sécurité pour les produits connectés. Adopté.",
        "<b>AI Act (règlement UE, application progressive 2025-2027) :</b> obligations de gouvernance "
        "des systèmes d'IA à risque. Adopté.",
        "<b>Contrainte budgétaire :</b> déficit public ~5,5-6 % du PIB en 2024-2025, dette >110 % du PIB "
        "(INSEE). Tous les gouvernements récents ont réduit ou gelé les effectifs publics hors "
        "priorités sécuritaires."]))
    story.append(Paragraph("8.2 Les cinq scénarios", S['h2']))
    story.append(T([
        [cell('Scénario', head=True), cell('Mesures proposées (programmes)', head=True),
         cell('Effets plausibles sur tes métiers', head=True)],
        [cell('Gouvernement RN', bold=True),
         cell("Programme : priorité sécurité/défense, impôt sur la fortune financière (hors résidence "
              "principale), suppression de la fiscalité de transmission des TPE/PME/ETI, indexation du "
              "barème IR, renégociation de l'AI Act européen (proposé). Budget 2025 RN chiffré par des "
              "instituts (chiffrage contesté, dont Institut Montaigne) : déficit annoncé plus élevé."),
         cell("Défense et cyber public soutenus (continuité LPM probable) ; demande cyber privée stable ; "
              "si renégociation AI Act : moins de conformité IA (moins de postes DPO/AI governance) mais "
              "pas d'effet sur la cyber classique ; suppression de la fiscalité de transmission : "
              "favorable aux PME/ETI (employeurs locaux) ; déficit élevé : risque de contrainte budgétaire "
              "en cascade (voir scénario 5). Hypothèse spéculative : baisse possible des subventions aux "
              "projets IA industriels si priorité donnée au pouvoir d'achat.")],
        [cell("Gouvernement LFI / gauche", bold=True),
         cell("Programmes (Nouveau Front populaire 2024, LFI « Notre révolution numérique » 2022) : ISF "
              "reconstitué, taxe Zucman 2 % sur patrimoines > 100 M EUR, barème IR à 14 tranches, CSG "
              "progressive, hausse du SMIC et des minima sociaux, investissements publics verts et "
              "numériques (proposés)."),
         cell("Demande publique soutenue (services publics renforcés) ; fiscalité plus élevée sur hauts "
              "revenus : compression des très hauts salaires (expert/manager) et possible érosion "
              "fiscale de l'attractivité des TJM élevés ; PME/ESN : charges possibles en hausse -> "
              "recrutements plus prudents ; filière IA : investissement public soutenu mais fiscalité "
              "accrue sur les entreprises technologiques ; gendarmerie : effectifs soutenus, solde "
              "indexé. Spéculatif : fuite de certains indépendants/experts vers la Suisse si écart "
              "fiscal important.")],
        [cell("Centre / continuité", bold=True),
         cell("Continuité des politiques récentes : LPM maintenue, aides à l'apprentissage ajustées "
              "à la marge (aide unique 5 000-6 000 EUR, décret 2025-174), réformes structurelles "
              "progressives."),
         cell("Environnement prévisible : demande cyber réglementaire croissante (NIS2, DORA, CRA, AI "
              "Act), apprentissage soutenu, salaires cadres en progression modérée (+1-2 %/an réel). "
              "Scénario de référence de ce dossier.")],
        [cell("Droite classique", bold=True),
         cell("Programmes : baisse des dépenses publiques, baisse des impôts de production, réforme de "
              "l'État, soutien aux entreprises (proposés)."),
         cell("Cyber privée favorable (moindre fiscalité, PME plus dynamiques) ; services publics : "
              "gel ou réduction des effectifs hors sécurité/défense (gendarmerie : priorité relative "
              "conservée) ; apprentissage : aides maintenues mais ciblées ; salaires privés : "
              "progression similaire au scénario centre ; IA : soutien au secteur privé plus qu'aux "
              "programmes publics.")],
        [cell("Forte contrainte budgétaire (toute majorité)", bold=True),
         cell("Agences de notation (S&P : abaissement AA- à A+ en 2025) et déficit élevé : obligation "
              "d'économies. Mesures possibles : gel des recrutements publics, réduction des aides, "
              "hausse de prélèvements (plausible, indépendant du parti)."),
         cell("Ralentissement des recrutements publics (gendarmerie : effectifs protégés mais primes "
              "sous pression) ; baisse possible des aides à l'apprentissage (effet sur les formations "
              "en alternance et les ESN qui les emploient) ; reports d'investissements numériques dans "
              "les collectivités ; demande cyber réglementaire résiste mieux (obligations légales) que "
              "la demande discrétionnaire (projets confort) ; salaires : progression réelle faible, "
              "voire nulle en cas d'inflation persistante.")]],
        widths=[2.6*cm, 6.6*cm, 7.4*cm]))
    story.append(Paragraph("8.3 Matrice métiers x scénarios", S['h2']))
    story.append(CH('c6_scenarios.png'))
    story.append(P("Lecture : (++/+/0/-/--) effet estimé sur l'emploi et les salaires de la famille de "
        "métiers, horizon 5-10 ans, hypothèse centrale. Mécanismes économiques, pas des prédictions : "
        "par exemple, la contrainte budgétaire réduit les recrutements publics (volume budgétaire), pas "
        "parce qu'un parti serait « contre » un métier.", 'small'))

def sec_fiscal(story):
    story.append(Paragraph("9. Fiscalité, aides et avantages financiers", S['h1']))
    story.append(Paragraph("9.1 Aides à l'apprentissage et à l'alternance (2025)", S['h2']))
    story.append(T([
        [cell('Dispositif', head=True), cell('Montant / conditions', head=True), cell('Source', head=True)],
        [cell('Aide unique employeur (apprentissage)'), cell("Jusqu'à 5 000 EUR par apprenti ; 6 000 EUR "
            "pour les entreprises de < 250 salariés et formations jusqu'au bac. Ancienne aide de 6 000 EUR "
            "généralisée expirée le 31/12/2024. Employeur < 250 salariés obligé de former au moins 5 % "
            "d'alternants pour toucher le 6 000 EUR."), cell('Décret n° 2025-174 du 28/02/2025, Légifrance ; service-public.fr')],
        [cell("Rémunération de l'apprenti"), cell("2025-2026 (SMIC 1 801,80 EUR brut au 01/2025) : 18-20 ans "
            "43 % (1re année) / 51 % (2e) ; 21-25 ans 53 % / 61 % / 78 % ; 26 ans et plus ou 3e cycle : "
            "100 % du SMIC ou du minimum conventionnel. Exonération d'IR dans la limite du plafond annuel "
            "(20 889 EUR en 2025)."), cell('Code du travail ; service-public.fr ; impots.gouv.fr')],
        [cell('Exonération de cotisations'), cell("Exonération totale de cotisations sociales pour les "
            "rémunérations d'apprentis jusqu'à 50 % du SMIC (depuis 03/2025) ; au-delà, exonérations "
            "partielles."), cell('URSSAF, 2025')],
        [cell('Contrat de professionnalisation'), cell("Aide employeur jusqu'à 2 000 EUR/an selon profil "
            "(conditions d'âge et de public), dispositif en cours de refonte (France Travail)."),
         cell('service-public.fr, 2025')],
        [cell('Bourses CROUS'), cell("Échelons 0 bis à 7 : ~1 454 à 6 335 EUR/an (2025-2026), selon revenus "
            "familiaux. Cumulables avec l'alternance sous conditions."), cell('CROUS / messervices.etudiant.gouv.fr, 2025')]],
        widths=[3.6*cm, 9.4*cm, 3.6*cm]))
    story.append(Paragraph("9.2 Aides régionales Auvergne-Rhône-Alpes", S['h2']))
    story.append(B([
        "<b>Pass'Région :</b> réduction de 70-90 % (plafonnée) sur les transports en commun régionaux pour "
        "les apprentis et lycéens de la région (montant variable selon le réseau).",
        "<b>Bourse au mérite régionale :</b> environ 500 EUR pour un bac avec mention Très Bien poursuivant "
        "des études dans la région (vérifier les conditions annuelles sur auvergnerhonealpes.fr).",
        "<b>Form'toit / aides au logement et au permis :</b> dispositifs régionaux d'aide à la formation "
        "au permis de conduire et au logement pour apprentis (montants et conditions évolutifs ; vérifier "
        "le site de la Région).",
        "<b>Attention :</b> les dispositifs régionaux changent chaque année ; les montants exacts doivent "
        "être vérifiés sur auvergnerhonealpes.fr au moment de la candidature."]))
    story.append(Paragraph("9.3 Statut d'indépendant et micro-entrepreneur", S['h2']))
    story.append(T([
        [cell('Élément', head=True), cell('Règle 2025', head=True), cell('Source', head=True)],
        [cell('Plafond micro-BNC (prestations intellectuelles)'), cell('77 700 EUR de CA/an'),
         cell('Légifrance / service-public.fr')],
        [cell('Cotisations micro-BNC'), cell('24,6 % du CA en 2025 ; passage prévu à 26,1 % en 2026 '
            '(décret n° 2025-943)'), cell('URSSAF, 2025')],
        [cell('Versement libératoire IR'), cell('2,2 % du CA (BNC) en plus des cotisations, si revenu '
            "fiscal de référence < ~28 797 EUR/part (2025) ; total ~26,8 % du CA hors CFP (0,3 %) et TVA"),
         cell('service-public.fr / impots.gouv.fr')],
        [cell('ACRE'), cell('Exonération partielle de cotisations la 1re année (environ 50 %) pour les '
            'créateurs éligibles'), cell('URSSAF')],
        [cell('Règle de conversion CA -> revenu'), cell('Un CA de 60 000 EUR/an en micro-BNC = ~45 240 EUR '
            'après cotisations 24,6 %, avant IR et CFP ; soit ~3 300 EUR net/mois avant IR, ~2 950 EUR '
            'après IR (1 part). Hors frais professionnels réels, congés non payés, prévoyance et '
            'retraite complémentaire volontaire.'), cell('Calcul de cette étude (méthode section 12)')]],
        widths=[3.9*cm, 9.1*cm, 3.6*cm]))
    story.append(P("<b>Point clé :</b> ne compare jamais un chiffre d'affaires d'indépendant à un salaire. "
        "Retire ~25 % de cotisations, l'IR, les frais (matériel, assurance, formation), et compte 30-40 "
        "jours non facturés par an (vacances, prospection, administratif). Un indépendant doit viser un "
        "TJM d'au moins 450-500 EUR pour égaler un salarié à 40 kEUR brut.", 'small'))
    story.append(Paragraph("9.4 Avantages liés aux statuts", S['h2']))
    story.append(B([
        "<b>Militaire (gendarmerie) :</b> solde selon grille indiciaire + primes (ISSP, ICM pour les "
        "spécialités, GIPA) + logement de fonction ou indemnité de logement + couverture santé militaire "
        "+ pension après service + 9 semaines de congés. Le tout compense partiellement une solde brute "
        "inférieure au privé.",
        "<b>Cadre privé :</b> intéressement/participation (0-10 % du salaire selon entreprises), "
        "épargne salariale (PEE/PER), mutuelle d'entreprise obligatoire (part patronale), véhicule ou "
        "frais de déplacement selon postes, formation continue financée.",
        "<b>Primes d'astreinte :</b> dans l'IT privé, une astreinte hebdomadaire se paie typiquement "
        "200-600 EUR/mois selon criticité - c'est un revenu variable, pas garanti.",
        "<b>Frais professionnels :</b> remboursement de frais kilométriques, titres-restaurant, forfait "
        "mobilité durable ; l'abattement de 10 % du barème IR les couvre forfaitairement (option frais "
        "réels possible si supérieurs)."]))


def sec_probabilites(story):
    story.append(Paragraph("10. Probabilités et scénarios d'avenir", S['h1']))
    story.append(Paragraph("10.1 Comment les probabilités sont construites", S['h2']))
    story.append(P("Il n'existe aucune statistique publique « probabilité d'obtenir un poste de pentester » "
        "ou « risque d'obsolescence par métier ». Les probabilités de ce dossier sont donc des "
        "<b>estimations raisonnées</b> à partir de quatre types de données : (1) taux de réussite aux "
        "concours et sélectivité des formations (données observées) ; (2) volumes d'offres vs de "
        "candidatures (ANSSI, France Travail, barèmes) ; (3) proportions de diplômés trouvant un emploi "
        "(enquêtes d'insertion des universités et de l'apprentissage) ; (4) jugement expert calibré sur "
        "ces données. Chaque estimation est assortie d'une fourchette et de sa base dans les fiches "
        "(partie F). Quand les données sont insuffisantes, c'est écrit explicitement."))
    story.append(Paragraph("10.2 Synthèse des probabilités de salaire (18 métiers)", S['h2']))
    rows = [[cell('Métier', head=True), cell('1er emploi', head=True), cell('Confirmé', head=True),
             cell('> 2 500 EUR net', head=True), cell('> 3 000 EUR net', head=True),
             cell('> 4 000 EUR net', head=True), cell('> 5 000 EUR net', head=True),
             cell('Chômage', head=True)]]
    for m in ALL:
        pr = m['probs']; s_ = pr['seuils']
        rows.append([cell(m['nom'][:42], bold=True), cell(pr['premier_emploi'][:60]),
                     cell(pr['confirme'][:40]), cell(s_['2500'][:55]), cell(s_['3000'][:55]),
                     cell(s_['4000'][:50]), cell(s_['5000'][:45]), cell(pr['chomage'][:30])])
    story.append(T(rows, widths=[3.6*cm, 2.5*cm, 2.0*cm, 2.4*cm, 2.4*cm, 2.2*cm, 1.9*cm, 1.6*cm]))
    story.append(P("Les seuils sont en net après IR, célibataire 1 part. « 1er emploi » et « Confirmé » "
        "sont des fourchettes de probabilité conditionnelles au parcours suivi (détail dans chaque fiche).", 'small'))
    story.append(Paragraph("10.3 Trois scénarios d'avenir (2025-2040)", S['h2']))
    story.append(T([
        [cell('Scénario', head=True), cell('Hypothèses', head=True), cell('Conséquences pour toi', head=True)],
        [cell('Défavorable', bold=True),
         cell('Croissance ~0,5 %/an ; IA adoptée massivement et rapidement (agents autonomes fiables dès '
              '2028) ; contrainte budgétaire forte ; demandes cyber réglementaires ralenties ; concurrence '
              'junior accrue (fin du cycle de recrutement post-Covid).'),
         cell("Baisse des embauches juniors IT/cyber de 20-30 % ; salaires réels stagnants ; le support N1 "
              "et le SOC L1 se contractent ; les profils bac+2 sans spécialisation subissent la concurrence. "
              "Dans ce monde, la gendarmerie et l'administration (statuts) et les compétences cloud/IA "
              "rares restent les meilleures protections.")],
        [cell('Central', bold=True),
         cell('Croissance ~1 %/an ; IA progressive et partiellement fiable (assistance, pas remplacement '
              'complet) ; réglementation UE appliquée (NIS2, DORA, CRA, AI Act) ; LPM maintenue ; '
              'pénurie cyber persistante mais atténuée.'),
         cell("Demande cyber +10-15 % d'ici 2030 ; salaires +1-2 %/an réel ; le métier d'entrée le plus "
              "sûr reste l'administration/réseaux puis spécialisation ; l'IA outille les confirmés et "
              "réduit les postes L1 ; l'alternance reste la meilleure voie d'accès.")],
        [cell('Favorable', bold=True),
         cell('Réindustrialisation et souveraineté numérique soutenues ; IA générant de nouveaux besoins '
              '(sécurité des modèles, agents, données) ; budgets défense/cyber en hausse ; pénuries de '
              'compétences renforcées.'),
         cell("Embauches juniors en hausse ; primes de rareté sur les profils hybrides IA+cyber ; "
              "essor des indépendants (TJM en hausse) ; les parcours techniques courts (BTS/BUT en "
              "alternance) s'insèrent plus vite et mieux.")]],
        widths=[2.4*cm, 6.8*cm, 7.4*cm]))
    story.append(Paragraph("10.4 Événements de bascule à surveiller", S['h2']))
    story.append(B([
        "<b>Fiabilité des agents IA autonomes en production</b> (2027-2030) : si des agents fiables "
        "administrent et détectent seuls, les postes L1/L2 se contractent vite.",
        "<b>Application réelle de NIS2/DORA</b> (2025-2028) : sanctions effectives = demande de "
        "conformité et de RSSI durable ; laxisme = retombée.",
        "<b>Évolution des budgets publics</b> (chaque PLF) : gendarmerie, ANSSI, cyberdéfense.",
        "<b>Réglementation IA (AI Act)</b> : application stricte = création de postes de gouvernance IA.",
        "<b>Conjoncture ESN</b> : les ESN sont les premiers employeurs juniors ; leur carnet de commandes "
        "est un baromètre direct de ton premier emploi."]))

def sec_graphiques(story):
    story.append(Paragraph("11. Tableaux et graphiques comparatifs", S['h1']))
    story.append(P("Les graphiques c1, c2 et c6 sont présentés dans leurs sections thématiques (6 et 8). "
        "Cette section regroupe les vues transversales complémentaires. Chaque graphique indique unités, "
        "période, hypothèses, source, et la nature des données (observées ou projetées)."))
    story.append(Paragraph("11.1 Durée d'études vs rémunération à long terme", S['h2']))
    story.append(CH('c7_duree_salaire.png'))
    story.append(P("Lecture : la relation durée d'études -> salaire existe mais est bruitée : des métiers "
        "courts (admin sys) offrent un accès rapide à un salaire correct, tandis que les métiers longs "
        "(RSSI, architecte) paient surtout l'expérience cumulée, pas le diplôme seul.", 'small'))
    story.append(Paragraph("11.2 Coût de formation vs rendement salarial", S['h2']))
    story.append(CH('c8_cout_roi.png'))
    story.append(P("Lecture : en alternance, le coût est nul et le rendement immédiat - d'où la "
        "recommandation systématique de privilégier l'alternance. Les coûts affichés correspondent aux "
        "hypothèses hors alternance (frais de scolarité publics/privés).", 'small'))
    story.append(Paragraph("11.3 Analyse risque / opportunité", S['h2']))
    story.append(CH('c9_risque_opportunite.png'))
    story.append(Paragraph("11.4 Perspectives d'emploi à 2040", S['h2']))
    story.append(CH('c5_emploi2040.png'))
    story.append(Paragraph("11.5 Classement multicritère", S['h2']))
    story.append(CH('c10_classement.png'))
    story.append(P("Le détail des critères, des pondérations et du calcul est en section 12. Le score "
        "combine rémunération, demande, stabilité, risque IA, accessibilité depuis ton Bac Pro, intérêt "
        "technique, évolution, conditions de travail et mobilité internationale.", 'small'))

def sec_alternatifs(story):
    story.append(Paragraph("12. Métiers alternatifs et pistes méconnues", S['h1']))
    story.append(P("Huit métiers auxquels tu n'aurais probablement pas pensé, choisis pour leur "
        "compatibilité avec ton Bac Pro CIEL (souvent la partie électronique), leur stabilité ou leur "
        "faible concurrence. Fiches condensées : description, missions, salaires, impact IA, pourquoi "
        "ça vaut le coup, garde-fous."))
    for i, a in enumerate(ALT, 1):
        story.append(CondPageBreak(3*cm))
        story.append(Paragraph(f"12.{i} {a['nom']}", S['h2']))
        story.append(P(f"<b>Autres appellations :</b> {a['alt']}<br/><b>Accès :</b> {a['acces']}", 'small'))
        story.append(P(a['description']))
        story.append(B(a['missions']))
        rows = [[cell('Niveau', head=True), cell('Brut annuel (b/c/h)', head=True),
                 cell('Net après IR (central)', head=True), cell('Région', head=True), cell('Variable', head=True)]]
        for s_ in a['salaires']:
            bl, bm, bh = s_['brut']
            rows.append([cell(s_['niveau'], bold=True),
                cell(f"{bl:,} / {bm:,} / {bh:,}".replace(',', ' ')),
                cell(f"{fmt_net(bm):,.0f}".replace(',', ' ')),
                cell(s_['region']), cell(s_['variable'])])
        story.append(T(rows, widths=[4.2*cm, 3.1*cm, 2.4*cm, 3.6*cm, 3.3*cm]))
        ia = a['ia']
        story.append(P(f"<b>IA (auto {ia['auto']} / transfo {ia['transfo']} / levier {ia['levier']} sur 100) :</b> {ia['note']}", 'small'))
        story.append(P(f"<b>Pourquoi ça vaut le coup :</b> {a['pourquoi']}", 'small'))
        story.append(P(f"<b>Garde-fous :</b> {a['garde_fous']}", 'small'))
        story.append(Spacer(1, 4))


def sec_erreurs(story):
    story.append(Paragraph("13. Les erreurs à éviter et ce que tu n'as probablement pas pensé à vérifier", S['h1']))
    story.append(Paragraph("13.1 Ce que tu n'as probablement pas pensé à vérifier", S['h2']))
    story.append(B([
        "<b>La concurrence réelle pour un premier poste.</b> Une offre SOC L1 attractive reçoit souvent "
        "des centaines de candidatures ; le tri se fait sur l'alternance, les projets personnels (labs, "
        "CTF, homelab documentés sur GitHub) et les certifications, pas sur le diplôme seul.",
        "<b>La difficulté de trouver une alternance.</b> C'est le premier filtre réel : sans employeur, "
        "pas de BTS/BUT en alternance. Il faut chercher dès février-mars, viser les ESN régionales et "
        "les PME, et préparer un dossier (CV technique, GitHub, lettres ciblées).",
        "<b>Le décalage salaires annoncés / salaires obtenus.</b> Les fourchettes d'annonces (jobboards) "
        "affichent souvent le haut de fourchette ou des postes IDF. Un « 40-45 kEUR » affiché se négocie "
        "souvent à 34-38 kEUR en province pour un premier poste.",
        "<b>Le poids des stages et projets personnels.</b> Pour un premier emploi, un homelab documenté, "
        "des CTF, un projet GitHub propre et une veille structurée valent souvent plus qu'une "
        "certification de plus.",
        "<b>La valeur réelle des certifications selon l'employeur.</b> CompTIA/CCNA débloquent des "
        "entretiens ; OSCP impressionne les cabinets de pentest ; CISSP exige 5 ans d'expérience. Mais "
        "une certification sans expérience reste faible sur le marché junior.",
        "<b>Le risque de rester bloqué junior.</b> Réel en support et en SOC L1 : sans plan de montée en "
        "compétences (certifications, mobilité interne), on peut rester 5-10 ans au même niveau salarial.",
        "<b>La sous-traitance et les délocalisations.</b> Le support N1 et une partie du développement "
        "sont externalisables (offshore, nearshore) ; la cyber de proximité (SOC réglementé, OT, "
        "réponse à incident) et l'expertise l'ont été beaucoup moins (souveraineté, habilitations).",
        "<b>Les périodes de recrutement difficiles.</b> Fin d'année, élections, crises : les ESN gèlent "
        "les embauches en premier. Prévoir 3-6 mois de recherche même sur un marché favorable.",
        "<b>Le coût de la vie régional.</b> Net 2 500 EUR autour d'Annonay (loyer T2 ~500-650 EUR) > net "
        "3 200 EUR à Paris intra-muros (loyer T2 ~1 000-1 300 EUR + transports). Compare toujours le "
        "reste à vivre après loyer.",
        "<b>Les évolutions sans devenir manager.</b> Architecte, expert technique, formateur, "
        "indépendant : la progression technique existe et paie presque autant que le management, mais "
        "elle exige du volontariat continu (veille, certifications, communautés).",
        "<b>Le risque de dépendance à une seule technologie.</b> Un profil « uniquement Azure » ou "
        "« uniquement Cisco » est fragile ; les fondamentaux (réseaux, Linux, script, sécurité) "
        "transfèrent partout.",
        "<b>Les compétences transférables.</b> Réseaux, systèmes, scripting et méthodologie de "
        "diagnostic transfèrent vers le cloud, la sécurité, la data et l'industrie : ton Bac Pro CIEL "
        "est une base large, pas un couloir étroit.",
        "<b>Travailler à l'étranger.</b> La cyber est l'un des métiers IT les plus mobiles (anglais "
        "obligatoire) ; la gendarmerie est l'inverse (carrière exclusivement française).",
        "<b>Habilitations, nationalité, sécurité.</b> Certains postes (défense, C3N, souveraineté, "
        "opérateurs d'importance vitale) exigent des habilitations confidentielles, parfois la "
        "nationalité française, et un dossier de sécurité : un passé judiciaire lourd ou des "
        "compromissions numériques peuvent bloquer ces voies.",
        "<b>Les concours publics.</b> Dossiers longs (parfois 6-12 mois entre inscription et affectation), "
        "tests physiques et psychotechniques, affectation non choisie. Prépare un plan B parallèle.",
        "<b>Prestige vs adéquation.</b> « Pentester » est prestigieux ; un administrateur sécurité bien "
        "payé dans une PME proche de chez toi peut mieux servir tes objectifs (revenu, stabilité, vie "
        "personnelle) qu'un pentester junior sous-payé en cabinet parisien."]))
    story.append(Paragraph("13.2 Les cinq erreurs classiques de parcours", S['h2']))
    story.append(B([
        "<b>Choisir une école privée coûteuse (8-15 kEUR/an) sur la promesse d'un emploi</b> : vérifier "
        "les taux d'insertion réels (enquêtes publiées, pas brochures), comparer avec un BUT/alternance "
        "gratuit aux débouchés équivalents.",
        "<b>Viser le pentest directement</b> : c'est le marché junior le plus concurrentiel ; la voie "
        "réaliste passe par admin/SOC puis spécialisation.",
        "<b>Empiler les certifications sans expérience</b> : une certification par an maximum, alignée "
        "sur le poste visé, avec projets réels pour l'illustrer.",
        "<b>Ignorer l'alternance</b> : c'est le meilleur rapport risque/rendement du système français "
        "(gratuit + rémunéré + expérience).",
        "<b>Confondre passion pour l'attaque et métier de la défense</b> : 90 % des emplois cyber sont "
        "défensifs (SOC, ingénierie, conformité) ; le pentest est une niche d'environ 5-10 % des postes."]))

def sec_reco(story):
    story.append(Paragraph("14. Recommandations personnalisées", S['h1']))
    story.append(P("Profil de référence : Bac Pro CIEL, région ARA (Annonay), intérêts cyber + IA + "
        "réseaux + gendarmerie, priorité à l'équilibre rémunération/stabilité/évolution/intérêt. "
        "Recommandations fondées sur le classement multicritère (section 11.5) et les fiches."))
    story.append(Paragraph("14.1 Les trois parcours les plus recommandés", S['h2']))
    story.append(T([
        [cell('Rang', head=True), cell('Parcours', head=True), cell('Pourquoi', head=True),
         cell('Inconvénients / conditions', head=True)],
        [cell('1', bold=True),
         cell("BUT R&T ou BTS CIEL en alternance -> admin systèmes/réseaux ou SOC -> spécialisation "
              "sécurité (cloud ou générale) -> architecte ou consultant senior"),
         cell("Gratuit et rémunéré ; probabilité de réussite la plus élevée (70-85 %) ; toutes les portes "
              "restent ouvertes (pentest, gendarmerie, cloud, RSSI) ; marché junior moins saturé que le "
              "pentest ; salaire long terme élevé (architecte : 65-95 kEUR -> 110-170 kEUR)."),
         cell("Exige de trouver une alternance tôt ; demande une montée en compétences continue ; les "
              "5 premières années sont moins « spectaculaires » qu'un poste d'attaque.")],
        [cell('2', bold=True),
         cell("BTS/BUT alternance -> SOC (L1 puis L2) -> réponse à incident/DFIR ou CTI"),
         cell("Entrée cyber rapide et rémunérée ; l'incident/forensics est parmi les métiers les plus "
              "résistants à l'IA et les mieux valorisés (38-52 kEUR -> 85-135 kEUR) ; forte demande."),
         cell("Astreintes et stress en SOC ; le L1 est répétitif et saturé côté candidats : viser le L2 "
              "en 2-3 ans ; nécessite un vrai goût pour l'analyse sous pression.")],
        [cell('3', bold=True),
         cell("Concours gendarmerie -> brigade -> spécialisation cyber (TEC, OPJ, unités spécialisées)"),
         cell("Stabilité maximale (statut), logement, pension, formation gratuite ; le Bac Pro CIEL est "
              "un atout réel ; LPM 2024-2030 : +953 ETP cyber ; excellente seconde carrière civile "
              "possible (enquête interne, fraudes)."),
         cell("Mobilité géographique obligatoire ; horaires alternants ; solde de départ modeste "
              "(~1 850-2 100 EUR net) ; le cyber n'arrive qu'après 3-6 ans de brigade ; concurrence "
              "au concours (~1 admis pour 3-4).")]],
        widths=[1.1*cm, 4.6*cm, 5.6*cm, 5.3*cm]))
    story.append(Paragraph("14.2 Meilleur choix selon la priorité", S['h2']))
    story.append(T([
        [cell('Priorité', head=True), cell('Choix', head=True), cell('Justification', head=True)],
        [cell('Revenu maximal'), cell("Architecte cybersécurité (via parcours 1) ou RSSI (plus tard)"),
         cell("Plafonds les plus élevés : 110-170 kEUR (architecte), 120-170 kEUR+ (RSSI grand groupe) ; "
              "indépendance possible en fin de parcours (TJM 900-1 800 EUR).")],
        [cell('Stabilité'), cell("Gendarmerie ; sinon admin systèmes/réseaux en grande organisation"),
         cell("Statut militaire quasi inlicenciable ; l'admin en grande structure (industrie, santé, "
              "collectivité) résiste aux cycles économiques.")],
        [cell('Résistance à l\'IA'), cell("Gendarmerie cyber ; sinon sécurité OT/ICS ou architecte"),
         cell("Scores IA les plus favorables (auto 25-15) : présence physique, responsabilité humaine, "
              "réglementation, environnements industriels non automatisables.")],
        [cell('Intérêt technique'), cell("Pentester (via SOC/admin d'abord) ; hybride IA : pentester IA "
              "ou sécurité des systèmes d'IA"),
         cell("Scores d'intérêt les plus élevés (90-95) ; mais exiger un parcours d'entrée réaliste "
              "(pas d'entrée directe) et un vrai niveau technique.")],
        [cell('Démarrage le plus rapide'), cell("Technicien IT/réseaux direct ou BTS alternance"),
         cell("Emploi en 0-2 ans ; salaire modeste (22-30 kEUR) mais expérience immédiate et évolution "
              "possible vers admin/SOC.")],
        [cell('Expertise long terme'), cell("Ingénieur cybersécurité -> architecte ; ou DFIR -> expert "
              "forensics"),
         cell("Métiers où l'expérience se cumule et se paie (architecte, forensics expert) avec des "
              "plafonds élevés sans devenir manager.")],
        [cell('IA + cyber combinés'), cell("Sécurité des systèmes d'IA ou pentester IA (après bac+5)"),
         cell("Marchés naissants à forte croissance (LLM security, AI Act) ; prime de rareté 10-20 % ; "
              "mais exige master/école et culture logicielle solide.")],
        [cell('Éviter astreintes et imprévu'), cell("Auditeur GRC ; sinon formateur (après expérience) ; "
              "cloud security (full remote)"),
         cell("Horaires planifiés, peu d'urgences, télétravail élevé ; contrepartie : moins d'adrénaline "
              "et salaires de départ plus bas.")],
        [cell('Portes ouvertes / réorientation'), cell("Admin systèmes et réseaux -> tout ; ou BUT R&T "
              "(filière large)"),
         cell("L'administration systèmes est le carrefour du secteur : SOC, cloud, sécurité, réseaux, "
              "IAM, prévente, formation ; le BUT R&T garde la double option réseaux/électronique.")]],
        widths=[2.9*cm, 4.7*cm, 9.0*cm]))
    story.append(Paragraph("14.3 Le meilleur compromis", S['h2']))
    story.append(P("<b>Le compromis optimal pour ton profil est le parcours 1 :</b> BUT R&T (ou BTS CIEL "
        "si le BUT n'est pas accessible) en alternance, puis administration systèmes/réseaux 2-4 ans, "
        "puis spécialisation cybersécurité (idéalement cloud ou SOC L2), avec l'objectif long terme "
        "architecte ou consultant senior. Raisons : probabilité de réussite la plus élevée de tout le "
        "panorama, coût nul, salaires dans la moyenne haute à long terme, résistance correcte à l'IA, "
        "et surtout <b>toutes les portes restent ouvertes</b> (pentest, gendarmerie, RSSI, indépendance) "
        "jusqu'à 25-28 ans, âge où tu pourras arbitrer avec une vraie connaissance du terrain. "
        "<b>Ce qui changerait cet avis :</b> une vocation très forte pour l'enquête (gendarmerie dès le "
        "concours), une opportunité d'alternance exceptionnelle en sécurité offensive, ou une aversion "
        "profonde pour les astreintes (alors orienter GRC/audit)."))

def sec_plan(story):
    story.append(Paragraph("15. Plan d'action sur 1, 3, 5 et 10 ans", S['h1']))
    story.append(Paragraph("15.1 Horizon 1 an (pendant et juste après le Bac Pro)", S['h2']))
    story.append(B([
        "Consolider les fondamentaux : réseaux TCP/IP, Linux (installer et administrer un serveur "
        "personnel), scripting PowerShell et Python (bases).",
        "Créer un homelab documenté : un GitHub propre avec projets (serveur, VLAN, durcissement, "
        "first scripts), un petit rapport de test sur lab personnel.",
        "Pratiquer : plateformes gratuites (TryHackMe, Root-Me, OverTheWire), un ou deux CTF par an.",
        "Préparer l'alternance dès février-mars : CV technique, candidatures aux ESN régionales, PME, "
        "collectivités ; viser BTS CIEL/SIO ou BUT R&T selon le dossier.",
        "Viser une certification d'entrée si possible : CompTIA Network+ ou CCNA (CPF/lycée).",
        "Si piste gendarmerie : s'inscrire au concours, se préparer physiquement, visiter une brigade."]))
    story.append(Paragraph("15.2 Horizon 3 ans (fin d'études + premier poste)", S['h2']))
    story.append(B([
        "Diplôme obtenu (BTS ou BUT) avec une alternance réussie dans un environnement technique réel.",
        "Premier poste : admin systèmes/réseaux junior ou SOC L1 (cible : 28-38 kEUR en ARA).",
        "Certification spécialisante : Security+ ou équivalent ; commencer une spécialité (cloud, "
        "SOC L2, sécurité réseau).",
        "Décision d'orientation à ce stade : rester technique (admin -> ingénieur), basculer cyber "
        "(SOC, sécurité), ou tenter gendarmerie (le concours reste possible jusqu'à 30 ans pour les "
        "sous-officiers selon les sessions).",
        "Si voie universitaire : BUT3/licence pro puis master en alternance si l'objectif est "
        "ingénieur/architecte."]))
    story.append(Paragraph("15.3 Horizon 5 ans", S['h2']))
    story.append(B([
        "Niveau confirmé dans la spécialité choisie (cible : 45-60 kEUR brut).",
        "Spécialisation claire et documentée : cloud security, DFIR, pentest (via OSCP), ou IAM.",
        "Début de visibilité : contributions (write-ups, conférences locales, meetups type OWASP "
        "Lyon/Grenoble), réseau professionnel structuré.",
        "Arbitrage technique vs management assumé (les deux paient, mais les trajectoires divergent).",
        "Si gendarmerie : TEC puis OPJ, candidature aux unités spécialisées."]))
    story.append(Paragraph("15.4 Horizon 10 ans", S['h2']))
    story.append(B([
        "Poste senior/expert : architecte sécurité, consultant senior, RSSI PME/ETI, ou expert DFIR "
        "(cible : 70-120 kEUR selon voie et région).",
        "Option indépendance évaluée sérieusement (TJM, réseau, trésorerie) : la fenêtre 30-40 ans est "
        "la plus favorable.",
        "Veille et formation continue institutionnalisées (une certification majeure tous les 3-4 ans, "
        "communauté active).",
        "Diversification du risque : compétences double (OT, IA, cloud) pour résister aux cycles."]))


def sec_glossaire(story):
    story.append(Paragraph("16. Glossaire", S['h1']))
    rows = [[cell('Terme', head=True), cell('Définition', head=True)]]
    gloss = [
        ("AD / Entra ID", "Active Directory (Microsoft) et sa version cloud : annuaires gérant identités et accès."),
        ("AI Act", "Règlement européen sur l'intelligence artificielle, application progressive 2025-2027."),
        ("ANSSI", "Agence nationale de la sécurité des systèmes d'information, autorité française en cybersécurité."),
        ("Astreinte", "Période hors heures de travail où le salarié doit pouvoir intervenir rapidement (rémunérée ou majorée)."),
        ("Bac Pro CIEL", "Baccalauréat professionnel Cybersécurité, Informatique et réseaux, Électronique."),
        ("BTS CIEL / SIO", "BTS Services informatiques aux organisations (SIO) ; CIEL désigne la voie professionnelle équivalente."),
        ("BUT", "Bachelor universitaire de technologie (bac+3), filières R&T, Informatique, GEII."),
        ("CA / TJM", "Chiffre d'affaires ; taux journalier moyen d'un indépendant (facturé par jour travaillé)."),
        ("C3N", "Centre national cybercontrôle de la gendarmerie (Pontoise)."),
        ("ComCyberGend", "Commandement cyber de la gendarmerie nationale."),
        ("CRA", "Cyber Resilience Act : règlement UE imposant des exigences de sécurité aux produits connectés (2026-2027)."),
        ("CTI", "Cyber Threat Intelligence : renseignement sur les menaces informatiques."),
        ("DORA", "Digital Operational Resilience Act : règlement UE sur la résilience informatique du secteur financier (2025)."),
        ("DFIR", "Digital Forensics and Incident Response : réponse à incident et investigation numérique."),
        ("EBIOS RM", "Méthode française d'analyse de risques (ANSSI)."),
        ("ESN", "Entreprise de services du numérique (ex-SSII)."),
        ("GRC", "Governance, Risk & Compliance : gouvernance, risques et conformité."),
        ("IAM / IGA / PAM", "Identity & Access Management : gestion des identités, des accès et des comptes privilégiés."),
        ("IR", "Impôt sur le revenu (barème progressif, par part fiscale)."),
        ("LPM", "Loi de programmation militaire 2024-2030 (413 MdEUR dont ~4 MdEUR cyber)."),
        ("Net avant IR / après IR", "Salaire après cotisations sociales ; puis après impôt sur le revenu (prélèvement à la source)."),
        ("NIS2", "Directive européenne « network and information security » 2 : obligations de sécurité pour ~10 000-15 000 entités françaises."),
        ("OPJ", "Officier de police judiciaire (grade d'enquête supérieur, concours interne)."),
        ("OT / ICS", "Operational Technology / Industrial Control Systems : systèmes industriels (usines, énergie, SCADA)."),
        ("OSC-S", "Officier sous contrat - spécialité (voie d'entrée officier avec licence)."),
        ("RSSI / CISO", "Responsable de la sécurité des systèmes d'information."),
        ("SIEM / SOC", "Plateforme de centralisation des journaux / centre opérationnel de sécurité (niveaux L1-L3)."),
        ("SMIC 2025", "1 801,80 EUR brut mensuel (01/2025) ; 1 867,02 EUR prévu au 01/06/2026."),
        ("TEC", "Technicien d'enquêtes numériques (gendarmerie)."),
        ("TVA / versement libératoire", "Taxe sur la valeur ajoutée ; option micro-entrepreneur de paiement forfaitaire de l'IR (2,2 % BNC).")]
    for t, d in gloss:
        rows.append([cell(t, bold=True), cell(d)])
    story.append(T(rows, widths=[3.6*cm, 13.0*cm]))

def sec_sources(story):
    story.append(Paragraph("17. Sources et méthodologie", S['h1']))
    story.append(Paragraph("17.1 Sources utilisées", S['h2']))
    rows = [[cell('Source', head=True), cell('Contenu utilisé', head=True), cell('Date', head=True),
             cell('Fiabilité', head=True)]]
    srcs = [
        ("ANSSI - Observatoire des métiers de la cybersécurité", "23 000 offres (06/2023-06/2024, +49 % vs 2019), ~15 000 postes non pourvus, 47 % bac+5, 75,9 % bac+5 chez les actifs, répartition des familles de métiers, 1/4 envisage de partir, 69 % approchés par recruteurs", "2025", "Élevée (donnée officielle de référence)"),
        ("Apec - barèmes salariaux cadres", "Médiane cadre sécurité 60 kEUR, 80 % entre 43-99 kEUR ; médiane IT ARA 52 kEUR ; big data 54-57 kEUR", "2025", "Élevée (baromètre reconnu)"),
        ("Robert Half / barèmes cabinets", "Cyber ≈ +20 % vs IT général ; fourchettes par poste", "2025", "Élevée (cabinet de recrutement)"),
        ("Zeroday (étude marché junior cyber)", "Segments favorables/juniors : cloud, DevSecOps, AppSec, LLM security ; tendus : pentester junior, SOC L1 (32-42 kEUR)", "2025", "Bonne (spécialiste, à recouper)"),
        ("Hellowork / France Travail", "Technicien IT junior 22-25 kEUR ; admin 40,6-43,5 kEUR moyen", "2025", "Bonne (données d'annonces, biais déclaratif)"),
        ("Gendarmerie nationale / SGA", "Grilles indiciaires : point d'indice 4,92278 EUR (01/2025), solde SOE ~1 604,83 EUR brute, adjudant 1 977-2 357 EUR net, GAV 1 205 EUR net, officier sortie d'école 2 843 EUR net ; concours SOG (bac, ~1/3,71 en mars 2025) ; OSC-S (licence)", "2025", "Élevée (grilles officielles)"),
        ("Légifrance - décret n° 2025-174 (28/02/2025)", "Aide unique employeur apprentissage : 5 000 EUR / 6 000 EUR TH", "2025", "Élevée (texte de loi)"),
        ("Légifrance - décret n° 2025-943", "Cotisations micro-entrepreneur BNC : 24,6 % (2025) -> 26,1 % (2026)", "2025", "Élevée (texte de loi)"),
        ("URSSAF", "Cotisations micro-BNC, exonération apprentis jusqu'à 50 % SMIC (03/2025), ACRE", "2025", "Élevée (officielle)"),
        ("Service-public.fr / impots.gouv.fr", "Barème IR 2025 (tranches 0/11/30/41/45 %, seuils 11 497/29 315/83 823/180 294 EUR), abattement 10 % (plafond 14 426 EUR), décote 889-45,25 %, rémunérations apprentis, exonération IR apprentis (20 889 EUR)", "2025", "Élevée (officielle)"),
        ("Ministère des Armées - LPM 2024-2030", "413 MdEUR dont ~4 MdEUR cyber (x3), +953 ETP cyber", "2023 (loi votée)", "Élevée (loi votée)"),
        ("Dares / France Stratégie - Les métiers en 2030", "~15 % d'emplois à risque fort d'automatisation, 32 % en transformation ; pas de consensus sur l'IA générative", "2022", "Élevée (étude publique de référence)"),
        ("OCDE", "27 % des emplois exposés à l'IA générative", "2023", "Élevée"),
        ("Insee", "Adoption IA générative : 18 % des entreprises >= 10 salariés (2025) vs 10 % (2024) ; déficit public ~5,5-6 % PIB", "2025", "Élevée (officielle)"),
        ("Programmes politiques (RN, Nouveau Front populaire/LFI 2024, Institut Montaigne)", "Mesures proposées : impôt fortune financière, suppression fiscalité transmission TPE/PME, indexation barème IR, renégociation AI Act (RN) ; ISF, taxe Zucman, 14 tranches IR, CSG progressive (LFI/NFP) ; chiffrages contestés", "2022-2025", "Moyenne (programmes = intentions, pas des lois)"),
        ("Agences de notation (S&P)", "Abaissement de la note de la France (AA- -> A+, 2025) : pression budgétaire", "2025", "Élevée (fait de marché)"),
        ("Offres d'emploi observées (jobboards, sites carrières)", "Fourchettes de salaires réelles par poste et région ; TJM indépendants", "2024-2025", "Moyenne (annonces, souvent le haut de fourchette)"),
        ("Région Auvergne-Rhône-Alpes", "Pass'Région, bourse mérite ~500 EUR, Form'toit (conditions à vérifier annuellement)", "2025", "Bonne (officielle, montants évolutifs)")]
    for s_ in srcs:
        rows.append([cell(s_[0], bold=True), cell(s_[1]), cell(s_[2]), cell(s_[3])])
    story.append(T(rows, widths=[4.2*cm, 7.6*cm, 1.8*cm, 3.0*cm]))
    story.append(P("Aucune source n'a été fabriquée. Les montants non couverts par une source officielle "
        "(quatrechettes par niveau d'expérience, probabilités, scores IA, projections 2040) sont des "
        "estimations de cette étude, signalées comme telles partout où elles apparaissent.", 'small'))
    story.append(Paragraph("17.2 Méthodologie des calculs", S['h2']))
    story.append(Paragraph("Salaires nets", S['h3']))
    story.append(P("<b>Net avant IR</b> = brut annuel x (1 - 0,23) / 12. Le taux de 23 % correspond aux "
        "cotisations salariales d'un cadre du privé (sécurité sociale, retraite complémentaire AGIRC-ARRCO, "
        "APEC, CSG/CRDS). Pour les non-cadres, le taux réel est légèrement inférieur (~21-22 %) : les nets "
        "affichés sont donc légèrement prudents pour les postes non-cadres (technicien, gendarme - dont le "
        "régime militaire diffère de toute façon). <b>Net après IR</b> = net avant IR - (impôt annuel / 12), "
        "avec : revenu net imposable = brut - abattement 10 % (plafonné à 14 426 EUR, plancher 505 EUR) ; "
        "barème 2025 par part : 0 % jusqu'à 11 497 EUR, 11 % jusqu'à 29 315 EUR, 30 % jusqu'à 83 823 EUR, "
        "41 % jusqu'à 180 294 EUR, 45 % au-delà ; décote célibataire : 889 - 45,25 % x IR si IR < 1 964 EUR ; "
        "célibataire, 1 part, pas de revenus annexes. Exemples : 40 000 EUR brut -> ~2 236 EUR net après IR ; "
        "60 000 EUR -> ~3 070 EUR ; 90 000 EUR -> ~4 320 EUR."))
    story.append(Paragraph("Scores IA", S['h3']))
    story.append(P("Chaque métier est décomposé en tâches (fiche, partie A) ; chaque tâche est classée "
        "automatisable / transformée / humaine selon la littérature (Dares, OCDE) et l'état de la "
        "technologie (agents IA, LLM). Les cinq scores (auto, recrut, transfo, création, levier) agrègent "
        "ces jugements sur 100. <b>Limites :</b> pas de mesure statistique possible ; les scores servent à "
        "comparer des métiers entre eux ; ils sont révisables à mesure que la technologie et la "
        "réglementation évoluent."))
    story.append(Paragraph("Probabilités", S['h3']))
    story.append(P("Les probabilités combinent : taux de réussite observés (concours ~1/3,71-4 pour la "
        "gendarmerie ; sélectivité BUT/écoles), volumes d'offres (ANSSI : 23 000 offres/an, 15 000 non "
        "pourvues), enquêtes d'insertion (part de diplômés en emploi à 6-18 mois), et calibration "
        "experte. Elles sont présentées en fourchettes et toujours accompagnées de leur base. "
        "« Données insuffisantes » est utilisé quand aucune calibration honnête n'est possible."))
    story.append(Paragraph("Projections salariales et d'emploi", S['h3']))
    story.append(P("Les projections d'emploi à 2040 (graphique c5) sont des indices calés sur : croissance "
        "hypothèse centrale ~1 %/an, dynamique réglementaire (NIS2, DORA, CRA, AI Act), LPM, et vitesses "
        "d'adoption de l'IA (Insee). Elles sont explicitement des projections, pas des observations."))
    story.append(Paragraph("Classement multicritère", S['h3']))
    story.append(P("Dix critères pondérés (somme = 100) : salaire long terme 15, demande marché 15, "
        "stabilité 12, salaire de départ 10, résistance IA 10, accès depuis Bac Pro CIEL 10, intérêt "
        "technique 8, évolution 8, conditions de travail 7, mobilité internationale 5. Chaque critère "
        "est noté 0-100 (les salaires par mise à l'échelle linéaire : départ 20-55 kEUR, long terme "
        "45-120 kEUR ; les critères qualitatifs par jugement expert documenté). Le score final est la "
        "moyenne pondérée. <b>Limites :</b> les pondérations reflètent les priorités déclarées du profil "
        "(équilibre) ; changer les poids change le classement - le moteur de calcul est transparent et "
        "reproductible."))
    story.append(Paragraph("Scores de stabilité et scénarios politiques", S['h3']))
    story.append(P("La stabilité combine : nature du statut (public > privé), diversité des employeurs, "
        "cyclique de la demande, risque d'automatisation. La matrice politique (graphique c6) attribue à "
        "chaque famille de métiers un effet -2 à +2 par scénario, fondé sur les mécanismes économiques "
        "(volumes budgétaires, fiscalité, réglementation) et non sur des préférences partisanes. Les "
        "programmes politiques sont des intentions, jamais des certitudes : les effets affichés sont "
        "plausibles, pas prédictifs."))

def build():
    doc = DocToc(PDF_PATH, pagesize=A4,
        leftMargin=1.4*cm, rightMargin=1.4*cm, topMargin=1.6*cm, bottomMargin=1.5*cm,
        title="Étude approfondie des métiers et de leur avenir - Bac Pro CIEL",
        author="Dossier d'aide à la décision")
    story = []
    story += cover()
    toc_page(story)
    sec_resume(story)
    sec_profil(story)
    sec_panorama(story)
    sec_fiches(story)
    sec_parcours(story)
    sec_salaires(story)
    sec_ia(story)
    sec_politique(story)
    sec_fiscal(story)
    sec_probabilites(story)
    sec_graphiques(story)
    sec_alternatifs(story)
    sec_erreurs(story)
    sec_reco(story)
    sec_plan(story)
    sec_glossaire(story)
    sec_sources(story)
    doc.multiBuild(story, onFirstPage=on_page, onLaterPages=on_page)
    print('PDF genere :', PDF_PATH)

if __name__ == '__main__':
    build()

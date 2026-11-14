# -*- coding: utf-8 -*-
"""CV Matheo Fanget - version etudes superieures / alternance.
Contenu technique issu du rapport de PFMP Cyberg (verifie avec Matheo)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

BLEU = HexColor('#1f4e79'); GRIS = HexColor('#444444'); CLAIR = HexColor('#eef2f7')

S = {
    'nom': ParagraphStyle('nom', fontName='Helvetica-Bold', fontSize=22, textColor=BLEU, leading=26),
    'titre': ParagraphStyle('titre', fontName='Helvetica-Bold', fontSize=11.5, textColor=GRIS, leading=15),
    'accroche': ParagraphStyle('accroche', fontName='Helvetica', fontSize=9.5, textColor=GRIS, leading=13),
    'h': ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=11.5, textColor=BLEU, spaceBefore=8, spaceAfter=3),
    'corps': ParagraphStyle('corps', fontName='Helvetica', fontSize=9.5, textColor=HexColor('#222222'), leading=13),
    'bul': ParagraphStyle('bul', fontName='Helvetica', fontSize=9.5, textColor=HexColor('#222222'), leading=12.6, leftIndent=10, bulletIndent=2),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.5, textColor=GRIS, leading=11),
}

def B(items, style='bul'):
    return [Paragraph(t, S[style], bulletText='\u2022') for t in items]

story = []
# ---- En-tete ----
story.append(Table([
    [Paragraph('MATHEO FANGET', S['nom']),
     Paragraph('42220 Saint-Julien-Molin-Molette<br/>06 51 42 81 02<br/>fangetmatheo270@gmail.com', S['small'])],
], colWidths=[11.5*cm, 6.5*cm], style=TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)])))
story.append(Paragraph('\u00c9l\u00e8ve en Terminale Bac Pro CIEL (Cybers\u00e9curit\u00e9, Informatique et R\u00e9seaux, \u00c9lectronique) \u2014 Lyc\u00e9e Marc Seguin, Annonay', S['titre']))
story.append(Spacer(1, 4))
story.append(Paragraph("<b>Objectif :</b> poursuite d'\u00e9tudes en BTS CIEL option A (informatique et r\u00e9seaux) ou BTS SIO option SISR, id\u00e9alement en alternance, \u00e0 la rentr\u00e9e 2026. \u00c9galement disponible pour un job \u00e9tudiant (05/07 au 15/08).", S['accroche']))
story.append(HRFlowable(width='100%', thickness=1.2, color=BLEU, spaceBefore=6, spaceAfter=2))

# ---- Experience ----
story.append(Paragraph('EXP\u00c9RIENCE', S['h']))
story.append(Paragraph('<b>Stagiaire \u2014 CYBERG (entreprise informatique, 30 collaborateurs) \u2014 Annonay</b> \u2014 plusieurs PFMP : 11\u201312/2025 et 06–07/2026', S['corps']))
story.append(Paragraph('Stages en infrastructure syst\u00e8mes & r\u00e9seaux et cybers\u00e9curit\u00e9 (tuteur : Th\u00e9o Cl\u00e9men\u00e7on)', S['small']))
story += B([
    "D\u00e9ploiement d'un <b>environnement virtualis\u00e9 sous Microsoft Hyper-V</b> : machines virtuelles Windows Server 2025 et Parrot OS (adressage IP, r\u00f4les).",
    "Cr\u00e9ation et configuration de <b>deux domaines Active Directory</b> (cybtest.local, cybtest2.local) : unit\u00e9s d'organisation, groupes de s\u00e9curit\u00e9 avec droits RO/RW \u2014 application du principe de <b>moindre privil\u00e8ge</b>.",
    "Administration et diagnostic avec <b>PowerShell</b> : commandes d'administration, lecture des erreurs, v\u00e9rification des r\u00e9sultats.",
    "<b>\u00c9tude des principales attaques r\u00e9seau</b> et de leurs d\u00e9fenses : SYN/UDP Flood, IP Spoofing, ARP Poisoning (MITM), BGP Hijacking \u2014 protections associ\u00e9es (SYN Cookies, BCP 38, DHCP Snooping, Dynamic ARP Inspection, RPKI/ROA).",
    "<b>Mise en pratique encadr\u00e9e</b> : test SYN Flood avec <b>hping3</b> depuis Parrot OS sur un r\u00e9seau de test isol\u00e9, dans le respect du cadre l\u00e9gal (jamais sans autorisation).",
    "Remise en \u00e9tat de <b>plus de 100 t\u00e9l\u00e9phones et 10 PC portables</b> : r\u00e9initialisation usine Android/Windows, contr\u00f4le avant restitution.",
    "Interventions clients aux c\u00f4t\u00e9s des techniciens : diagnostic, maintenance de postes, configuration d'\u00e9quipements r\u00e9seau, support utilisateur.",
    "Outils professionnels : TeamViewer, TacticalRMM (prise en main \u00e0 distance), gestion de tickets (Walnut), Keeper (gestionnaire de mots de passe).",
])
story.append(Spacer(1, 3))
story.append(Paragraph('<b>Stagiaire \u2014 Adquat \u2014 Saint-Chamond</b> (03/2025)', S['corps']))
story += B([
    "D\u00e9veloppement de programmes informatiques r\u00e9pondant aux besoins d'utilisateurs.",
    "Cr\u00e9ation de sites internet (visibilit\u00e9 en ligne du projet).",
])
story.append(Spacer(1, 3))
story.append(Paragraph("<b>Stage d'observation \u2014 ATEC BVF \u2014 Annonay</b> (06/2023)", S['corps']))
story += B([
    "D\u00e9couverte de la gestion de chantier, de l'\u00e9conomie de la construction et de la coordination d'\u00e9quipe.",
])

# ---- Formation ----
story.append(Paragraph('FORMATION', S['h']))
story += B([
    "<b>Bac Pro CIEL</b> (Cybers\u00e9curit\u00e9, Informatique et R\u00e9seaux, \u00c9lectronique) \u2014 Lyc\u00e9e Marc Seguin, Annonay \u2014 en cours, session 2026.",
    "<b>Dipl\u00f4me National du Brevet</b> \u2014 Saint-Joseph, Bourg-Argental \u2014 2024.",
])

# ---- Competences ----
story.append(Paragraph('COMP\u00c9TENCES TECHNIQUES', S['h']))
story.append(Table([
    [Paragraph('<b>Syst\u00e8mes</b>', S['corps']), Paragraph('Windows Server 2025, Active Directory (domaines, OU, groupes et droits), PowerShell, Linux (Parrot OS)', S['corps'])],
    [Paragraph('<b>Virtualisation</b>', S['corps']), Paragraph('Microsoft Hyper-V (d\u00e9ploiement et administration de VMs)', S['corps'])],
    [Paragraph('<b>R\u00e9seaux</b>', S['corps']), Paragraph('TCP/IP, ARP, TCP/UDP/ICMP, VLAN, routage, bases BGP', S['corps'])],
    [Paragraph('<b>Cybers\u00e9curit\u00e9</b>', S['corps']), Paragraph('Attaques DoS/usurpation/MITM et protections associ\u00e9es, hping3, moindre privil\u00e8ge, segmentation, chiffrement', S['corps'])],
    [Paragraph('<b>Support</b>', S['corps']), Paragraph('TeamViewer, TacticalRMM, gestion de tickets, Keeper, Windows/Android (postes et mobiles)', S['corps'])],
], colWidths=[3.4*cm, 14.6*cm], style=TableStyle([
    ('BACKGROUND', (0,0), (0,-1), CLAIR), ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 2.5), ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4)])))

story.append(Paragraph('COMP\u00c9TENCES PERSONNELLES', S['h']))
story.append(Paragraph("M\u00e9thode de diagnostic (observer, formuler des hypoth\u00e8ses, v\u00e9rifier) \u2022 Travail en \u00e9quipe et communication avec les clients \u2022 Respect des proc\u00e9dures de s\u00e9curit\u00e9 \u2022 Autonomie progressive \u2022 S\u00e9rieux et ponctualit\u00e9", S['corps']))

story.append(Paragraph('LANGUES', S['h']))
story.append(Paragraph("Fran\u00e7ais : langue maternelle \u2022 Anglais : interm\u00e9diaire (documentation technique) \u2022 Allemand : notions", S['corps']))

story.append(Paragraph("CENTRES D'INT\u00c9R\u00caT", S['h']))
story.append(Paragraph("Escalade \u2022 Musique \u2022 Informatique (labs personnels, environnement virtualis\u00e9, cybers\u00e9curit\u00e9)", S['corps']))

doc = SimpleDocTemplate('/workspace/github__uwusexycat270-bot__mistral/cv/CV_Matheo_Fanget.pdf',
    pagesize=A4, leftMargin=1.5*cm, rightMargin=1.5*cm, topMargin=1.1*cm, bottomMargin=0.9*cm,
    title='CV Matheo Fanget', author='Matheo Fanget')
doc.build(story)
print('CV genere')

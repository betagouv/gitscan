# Synthèse d'activité : suitenumerique (du 01/11 au 15/11/2026)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des capacités de collaboration et une sécurisation accrue des services. L'intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub) et l'enrichissement des outils collaboratifs dans [docs](/repos/suitenumerique/docs) (mentions, sous-documents) améliorent significativement l'expérience de travail partagé. Parallèlement, la gestion des fichiers et des transferts gagne en fiabilité et en contrôle avec les évolutions de [drive](/repos/suitenumerique/drive) et [transfers](/repos/suitenumerique/transfers).

L'accessibilité et l'inclusion sont également au cœur des développements, notamment via [meet](/repos/suitenumerique/meet) qui étend son support linguistique et optimise son interface pour les utilisateurs malvoyants. Ces changements renforcent la robustesse globale de la suite pour un usage professionnel exigeant.

## Sécurité
- Renforcement de la protection des données : hachage des jetons au repos dans [menshen](/repos/suitenumerique/menshen) et protection contre les attaques SSRF dans [transfers](/repos/suitenumerique/transfers) et [file-scanner](/repos/suitenumerique/file-scanner).
- Amélioration de la détection et de l'audit : introduction d'un moteur de détection de malwares via ICAP dans [django-lasuite](/repos/suitenumerique/django-lasuite) et mise en place d'un système d'audit complet dans [meet](/repos/suitenumerique/meet).
- Correction de vulnérabilités : résolution de nombreuses failles critiques (CVE) sur [meet](/repos/suitenumerique/meet), [projects](/repos/suitenumerique/projects) et [conversations](/repos/suitenumerique/conversations).
- Sécurisation de l'authentification : durcissement de l'OIDC et de la gestion des jetons dans [accounts](/repos/suitenumerique/accounts) et [dictaphone](/repos/suitenumerique/dictaphone).

## Autres changements notables
- Évolutions architecturales majeures : migration des workers vers Dramatiq dans [st-ansible](/repos/suitenumerique/st-ansible) et refonte du site [docs-website](/repos/suitenumerique/docs-website) avec Astro.
- Intégration de nouveaux services : déploiement de la messagerie Matrix dans [hub](/repos/suitenumerique/hub) et mise en place de l'infrastructure SIP pour [roomkit-visio](/repos/suitenumerique/roomkit-visio).
- Optimisation des performances et de l'observabilité : utilisation d'index de chemin dans [drive](/repos/suitenumerique/drive) et intégration de métriques de monitoring (Sentry/Prometheus) dans [menshen](/repos/suitenumerique/menshen) et [accounts](/repos/suitenumerique/accounts).

## Dépôts les plus actifs
- [meet](/repos/suitenumerique/meet) : Améliorations majeures de l'accessibilité, de l'internationalisation et de la sécurité.
- [menshen](/repos/suitenumerique/menshen) : Modernisation du client Python et renforcement de la sécurité des jetons.
- [docs](/repos/suitenumerique/docs) : Nouvelles fonctionnalités de collaboration et outils d'administration enrichis.
- [hub](/repos/suitenumerique/hub) : Intégration complète et temps réel de la messagerie Matrix.
- [transfers](/repos/suitenumerique/transfers) : Sécurisation intensive de l'API et amélioration de l'expérience de téléchargement.
- [drive](/repos/suitenumerique/drive) : Nouveaux outils d'administration et optimisation des performances de recherche.

# Synthèse d'activité : suitenumerique (du 20/05 au 29/08/2026)

## Résumé de l'activité
L'activité récente est marquée par une montée en puissance majeure des services de communication et de collaboration. L'intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub), le lancement du support mobile pour [messages](/repos/suitenumerique/messages) et [dictaphone](/repos/suitenumerique/dictaphone), ainsi que l'apport de l'intelligence artificielle dans [conversations](/repos/suitenumerique/conversations) transforment l'expérience utilisateur. 

Parallèlement, la gestion de l'information et des fichiers est renforcée par de nouveaux outils de suivi de quota dans [drive](/repos/suitenumerique/drive) et des fonctionnalités de partage sécurisé dans [transfers](/repos/suitenumerique/transfers). L'organisation poursuit également sa modernisation technique avec des migrations vers des architectures plus performantes (Vite, Astro, Django-ninja).

## Sécurité
- Renforcement de la protection des transferts avec l'introduction du chiffrement de bout en bout (E2EE) en option dans [transfers](/repos/suitenumerique/transfers).
- Amélioration de la sécurité réseau et des données avec le blocage des requêtes SSRF dans [file-scanner](/repos/suitenumerique/file-scanner) et la protection contre les fichiers PDF malveillants dans [conversations](/repos/suitenumerique/conversations).
- Sécurisation de la gestion des identités via le chiffrement des données sensibles et le support de l'authentification sociale dans [accounts](/repos/suitenumerique/accounts).
- Correction de vulnérabilités critiques par la mise à jour de bibliothèques de base dans [people](/repos/suitenumerique/people).

## Autres changements notables
- **Modernisation des architectures** : Migrations technologiques importantes vers Vite pour [calendars](/repos/suitenumerique/calendars) et [conversations](/repos/suitenumerique/conversations), vers Astro pour [docs-website](/repos/suitenumerique/docs-website), et vers le framework `django-ninja` pour [menshen](/repos/suitenumerique/menshen).
- **Consolidation de l'écosystème** : Transition vers une structure monorepo pour [ui-kit](/repos/suitenumerique/ui-kit), incluant la fusion de la bibliothèque Cunningham React.
- **Nouveaux services** : Lancement et initialisation de nouveaux projets tels que [st-domain-parking](/repos/suitenumerique/st-domain-parking), [gallene-deployment](/repos/suitenumerique/gallene-deployment) et le SDK [gallene-sdk](/repos/suitenumerique/gallene-sdk).

## Dépôts les plus actifs
- [drive](/repos/suitenumerique/drive) : Évolutions majeures sur la gestion des quotas, le partage de masse et la sécurité des fichiers.
- [hub](/repos/suitenumerique/hub) : Intégration complète et profonde de la messagerie Matrix.
- [dictaphone](/repos/suitenumerique/dictaphone) : Améliorations significatives de l'expérience mobile et du traitement audio.
- [conversations](/repos/suitenumerique/conversations) : Refonte de l'interface utilisateur et montée en puissance des fonctionnalités d'IA.
- [ui-kit](/repos/suitenumerique/ui-kit) : Migration vers une structure monorepo et enrichissement de la bibliothèque de composants.

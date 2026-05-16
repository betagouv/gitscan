# Synthèse d'activité : suitenumerique (du 29 avril au 14 mai 2026)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité intense, marquée par des améliorations significatives sur plusieurs de ses produits. st-home a bénéficié d'une refonte majeure de sa carte de déploiement et d'une modernisation de son infrastructure. L'application "Gaufre" (via les dépôts `docs` et `drive`) a vu des améliorations notables en termes d'expérience utilisateur, notamment avec l'ajout de la prévisualisation de fichiers PDF et un nouveau processus d'onboarding. Plusieurs dépôts ont également mis l'accent sur la sécurité, avec des mises à jour de dépendances et des corrections de vulnérabilités (notamment `people`, `find` et `calendars`). Enfin, des efforts importants ont été déployés pour améliorer la qualité du code et l'infrastructure de développement, en particulier avec la migration du frontend de `hub` vers Next.js et TypeScript.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction de vulnérabilités dans `people` via la mise à jour de plusieurs dépendances (urllib3, Django, Pillow, pytest, next).
- Correction d'une vulnérabilité potentielle d'élévation de privilèges dans `people`.
- Correction d'une vulnérabilité de sécurité dans `find` avec la mise à jour de `requests` et `pytest`.
- Amélioration de la sécurité de l'authentification dans `dictaphone` avec l'implémentation de JWT/PKCE.
- Modification du format du mot de passe des canaux CalDAV dans `calendars` pour une meilleure sécurité.

## Autres changements notables
- Refonte majeure de l'infrastructure de `st-home` avec le remplacement de Nginx par Caddy.
- Migration complète du frontend de `hub` vers Next.js et TypeScript, modernisant ainsi l'architecture et améliorant la maintenabilité.
- Implémentation initiale de l'échange de jetons OAuth 2.0 dans `menshen`.
- Refonte de l'interface d'administration dans `django-lasuite`.
- Importation des scripts de déploiement et du Dockerfile de `deburau/galene-docker` dans `gallene-deployment`.

## Dépôts les plus actifs
- [ui-kit](/repos/suitenumerique/ui-kit) : Ajout d'un nouveau composant de prévisualisation de fichiers et amélioration de la couverture des tests.
- [st-home](/repos/suitenumerique/st-home) : Refonte de la carte de déploiement et modernisation de l'infrastructure.
- [hub](/repos/suitenumerique/hub) : Migration complète du frontend vers Next.js et TypeScript.
- [conversations](/repos/suitenumerique/conversations) : Amélioration de la pertinence de la recherche et ajout de la gestion des fichiers de projet.
- [drive](/repos/suitenumerique/drive) : Amélioration de la prévisualisation des fichiers PDF et de la gestion des téléchargements.
- [docs](/repos/suitenumerique/docs) : Ajout d'un squelette de chargement et intégration de Crisp pour le support utilisateur.

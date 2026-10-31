# Synthèse d'activité : gip-inclusion (du 20/10 au 28/10)

## Résumé de l'activité
L'activité de cette période est marquée par une transformation profonde de l'expérience utilisateur sur plusieurs plateformes clés. Les efforts se sont concentrés sur la refonte des parcours d'orientation et de suivi dans [les-emplois](/repos/gip-inclusion/les-emplois) et [dora](/repos/gip-inclusion/dora), ainsi que sur le rebranding complet de [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) vers l'identité "Match Europe". Ces évolutions visent à simplifier les interactions pour les usagers et à offrir des outils de pilotage plus précis, notamment via la détection des fins de parcours et la gestion automatisée des candidatures spontanées.

Parallèlement, l'organisation renforce ses capacités d'automatisation et de fiabilité technique. L'outil [relecteur](/repos/gip-inclusion/relecteur) franchit une étape majeure dans l'assistance à la revue de code par IA, tandis que les capacités de reporting et d'enrichissement des données sont accrues dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) et [export_merged_pull_requests](/repos/gip-inclusion/export_merged_pull_requests).

## Sécurité
- **Protection des données et authentification** : Mise en place de la double authentification (MFA) et d'un suivi d'audit renforcé dans [les-emplois](/repos/gip-inclusion/les-emplois), gestion sécurisée des jetons et durcissement des contrôles d'accès dans [data-inclusion](/repos/gip-inclusion/data-inclusion), et protection des points de terminaison avec mécanismes de *rate-limiting* dans [dora](/repos/gip-inclusion/dora) et [rdv-insertion](/repos/gip-inclusion/rdv-insertion).
- **Sécurisation des infrastructures et des flux** : Implémentation de politiques de sécurité (CSP) pour [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et [autometa](/repos/gip-inclusion/autometa), suppression des mots de passe codés en dur dans [fluo-proto](/repos/gip-inclusion/fluo-proto), et utilisation de SOPS pour la gestion des secrets sensibles dans [infrastructure](/repos/gip-inclusion/infrastructure).

## Autres changements notables
- **Migrations et infrastructures** : Déploiement majeur de l'environnement "emplois-cnav" via Kubernetes dans [infrastructure](/repos/gip-inclusion/infrastructure), transition vers des conteneurs *serverless* pour [fluo-proto](/repos/gip-inclusion/fluo-proto), et migration du stockage vers RustFS pour [les-emplois](/repos/gip-inclusion/les-emplois) et [autometa](/repos/gip-inclusion/autometa).
- **Évolutions techniques majeures** : Mise en œuvre de l'internationalisation (i18n) pour [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025) et intégration de nouveaux systèmes de tracking et d'analytics dans [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms).

## Dépôts les plus actifs
- [les-emplois](/repos/gip-inclusion/les-emplois) : Refonte majeure de l'expérience d'orientation, de la gestion des dossiers et de l'infrastructure.
- [relecteur](/repos/gip-inclusion/relecteur) : Avancées significatives sur l'automatisation de la revue de code et l'évaluation par IA.
- [dora](/repos/gip-inclusion/dora) : Refonte de l'interface utilisateur et renforcement de la sécurité.
- [data-inclusion](/repos/gip-inclusion/data-inclusion) : Optimisation des pipelines de données et durcissement de la sécurité.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding complet et amélioration des fonctionnalités de matching.
- [infrastructure](/repos/gip-inclusion/infrastructure) : Déploiement complet d'un nouvel environnement (Kubernetes, réseaux, bases de données).

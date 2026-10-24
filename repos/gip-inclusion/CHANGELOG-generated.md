# Synthèse d'activité : gip-inclusion (du 30/06 au 22/10)

## Résumé de l'activité
L'activité récente est marquée par une modernisation profonde des interfaces utilisateurs, notamment pour [dora](/repos/gip-inclusion/dora) et [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms), visant à améliorer la navigation, le suivi des parcours et l'expérience de matching. L'organisation renforce également ses capacités d'analyse de données et d'automatisation, avec des avancées majeures sur [relecteur](/repos/gip-inclusion/relecteur) pour la revue de code assistée par IA et sur [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) pour le reporting métier.

Parallèlement, les efforts se sont concentrés sur la stabilisation des infrastructures et la sécurisation des flux de données, garantissant une meilleure fiabilité des services déployés et une gestion plus robuste des environnements de production.

## Sécurité
- **Sécurisation des accès et des données** : renforcement de la politique de sécurité (CSP) pour l'intégration iframe dans [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil), protection de la mémoire lors des calculs statistiques dans [rdv-insertion](/repos/gip-inclusion/rdv-insertion), et suppression des mots de passe codés en dur dans [fluo-proto](/repos/gip-inclusion/fluo-proto).
- **Gestion des secrets et des identités** : implémentation de SOPS pour la sécurisation des données sensibles et optimisation des permissions IAM dans [infrastructure](/repos/gip-inclusion/infrastructure).
- **Sécurisation des échanges** : mise en place de liens sécurisés par e-mail pour le téléchargement des exports dans [dora](/repos/gip-inclusion/dora).

## Autres changements notables
- **Infrastructures et déploiements** : déploiement complet de l'environnement "emplois-cnav" via [infrastructure](/repos/gip-inclusion/infrastructure) et transition vers un modèle de déploiement de conteneurs serverless pour les prototypes dans [fluo-proto](/repos/gip-inclusion/fluo-proto).
- **Migrations technologiques** : migration vers RustFS pour [les-emplois](/repos/gip-inclusion/les-emplois) et [autometa](/repos/gip-inclusion/autometa), et passage vers SeaweedFS pour le stockage de [dora](/repos/gip-inclusion/dora).
- **Évolutions architecturales et fonctionnelles** : mise en œuvre de l'internationalisation (i18n) pour [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025) et refonte du moteur d'évaluation de [relecteur](/repos/gip-inclusion/relecteur) pour une meilleure résilience face aux limites des API d'IA.

## Dépôts les plus actifs
- [dora](/repos/gip-inclusion/dora) : Refonte majeure de l'interface utilisateur, de la recherche interne et de l'infrastructure de stockage.
- [relecteur](/repos/gip-inclusion/relecteur) : Extension massive des capacités de revue de code automatique et de génération de tests.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding vers "Match Europe" et optimisation des outils de matching et d'analytics.
- [infrastructure](/repos/gip-inclusion/infrastructure) : Déploiement de nouveaux environnements et renforcement de la gestion des secrets et du DNS.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Enrichissement important des modèles de données et optimisation de l'orchestration des flux.

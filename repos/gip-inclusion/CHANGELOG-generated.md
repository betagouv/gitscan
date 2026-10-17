# Synthèse d'activité : gip-inclusion (du 01/07 au 13/10)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une transformation majeure de l'identité visuelle de plusieurs plateformes ([les-emplois](/repos/gip-inclusion/les-emplois), [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms)) et une amélioration significative de l'expérience utilisateur. Les nouveaux outils de matching, les tableaux de bord enrichis ([immersion-facile](/repos/gip-inclusion/immersion-facile), [dora](/repos/gip-inclusion/dora)) et l'introduction de modes de démonstration ([inclusion-connect](/repos/gip-inclusion/inclusion-connect)) facilitent l'usage quotidien pour les acteurs de l'inclusion.

Parallèlement, un effort conséquent a été déployé sur la robustesse des fondations techniques, notamment avec le déploiement de nouveaux environnements d'infrastructure ([infrastructure](/repos/gip-inclusion/infrastructure)) et l'optimisation des capacités de reporting et d'analyse de données ([pilotage-airflow](/repos/gip-inclusion/pilotage-airflow), [autometa](/repos/gip-inclusion/autometa)).

## Sécurité
- Renforcement de l'authentification (OAuth, gestion des jetons) dans [rdv-insertion](/repos/gip-inclusion/rdv-insertion) et [les-emplois](/repos/gip-inclusion/les-emplois).
- Sécurisation des échanges et de l'intégration (politique CSP pour les iframes) dans [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil).
- Amélioration de la gestion des secrets et des accès (SOPS, IAM) dans [infrastructure](/repos/gip-inclusion/infrastructure).
- Suppression des mots de passe en clair et mise en place du rate limiting dans [fluo-proto](/repos/gip-inclusion/fluo-proto) et [dora](/repos/gip-inclusion/dora).
- Gestion sécurisée des clés API par client dans [autometa-jobs](/repos/gip-inclusion/autometa-jobs).
- Mise en place d'un système d'audit complet pour la traçabilité des données dans [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav).

## Autres changements notables
- Déploiement complet de l'infrastructure pour l'environnement "emplois-cnav" ([infrastructure](/repos/gip-inclusion/infrastructure)).
- Migration vers des architectures plus modernes, incluant le passage au serverless ([fluo-proto](/repos/gip-inclusion/fluo-proto)) et de nouveaux systèmes de stockage ([autometa](/repos/gip-inclusion/autometa), [dora](/repos/gip-inclusion/dora)).
- Mise en place de l'internationalisation (i18n) pour le [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025).
- Transition de domaine et nettoyage des configurations pour [la-communaute](/repos/gip-inclusion/la-communaute).

## Dépôts les plus actifs
- [infrastructure](/repos/gip-inclusion/infrastructure) : Déploiement majeur de l'environnement emplois-cnav et renforcement de la sécurité.
- [les-emplois](/repos/gip-inclusion/les-emplois) : Rebranding complet et refonte des tunnels d'orientation.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Transition vers l'identité Match Europe et amélioration du matching.
- [dora](/repos/gip-inclusion/dora) : Refonte de l'interface de gestion et migration du stockage.
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Enrichissement des modèles de reporting et optimisation des pipelines.
- [rdv-insertion](/repos/gip-inclusion/rdv-insertion) : Amélioration de la fiabilité des données et de l'API.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Optimisation de l'expérience utilisateur et de la sécurité des intégrations.

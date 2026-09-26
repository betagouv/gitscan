# Synthèse d'activité : gip-inclusion (du 01/09 au 24/09)

## Résumé de l'activité
L'activité récente est marquée par une transformation majeure de l'identité et des fonctionnalités de plusieurs services clés, notamment avec le rebranding de [les-emplois](/repos/gip-inclusion/les-emplois) vers "La plateforme de l'inclusion" et de [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) vers "Match Europe". Ces évolutions visent à offrir une expérience utilisateur enrichie grâce à de nouveaux tableaux de bord pour les bénéficiaires ([immersion-facile](/repos/gip-inclusion/immersion-facile)) et des outils de mise en relation (matching) plus performants et intuitifs.

Parallèlement, l'organisation renforce ses capacités de pilotage et d'analyse grâce à un enrichissement massif des modèles de données ([pilotage-airflow](/repos/gip-inclusion/pilotage-airflow), [dora](/repos/gip-inclusion/dora)) et à une amélioration de l'intelligence de recherche ([data-inclusion](/repos/gip-inclusion/data-inclusion)). Ces avancées permettent un suivi plus précis des parcours et une gestion territoriale optimisée.

## Sécurité
- Renforcement de la sécurité des échanges et de l'authentification via l'implémentation du SSO et le durcissement des politiques de sécurité (CSP) pour les intégrations en iframe dans [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil).
- Amélioration de la sécurité des protocoles d'authentification (OIDC) et mise à jour des bibliothèques OAuth2 dans [inclusion-connect](/repos/gip-inclusion/inclusion-connect).
- Sécurisation de l'orchestrateur par l'introduction de clés d'accès spécifiques par client dans [autometa-jobs](/repos/gip-inclusion/autometa-jobs).
- Suppression des secrets codés en dur au profit de variables d'environnement dans [fluo-proto](/repos/gip-inclusion/fluo-proto).
- Renforcement de la protection des données bénéficiaires et mise en place d'une piste d'audit pour la traçabilité dans [les-emplois](/repos/gip-inclusion/les-emplois) et [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav).

## Autres changements notables
- Migration majeure de l'infrastructure de données vers Airflow 3 dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow).
- Modernisation du déploiement des prototypes via l'adoption de conteneurs serverless dans [fluo-proto](/repos/gip-inclusion/fluo-proto).
- Mise en place de l'internationalisation (i18n) pour supporter plusieurs langues sur le [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025).
- Migration du stockage vers SeaweedFS pour [dora](/repos/gip-inclusion/dora).
- Automatisation complète du pipeline CI/CD pour [autometa-jobs](/repos/gip-inclusion/autometa-jobs).

## Dépôts les plus actifs
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Migration vers Airflow 3 et enrichissement significatif des modèles de données métiers.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding vers Match Europe et optimisation des processus de matching et de suivi.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Optimisation de l'intégration iframe, de la sécurité et du suivi analytique.
- [dora](/repos/gip-inclusion/dora) : Amélioration de la gestion territoriale, de la recherche géographique et modernisation de l'infrastructure.
- [les-emplois](/repos/gip-inclusion/les-emplois) : Rebranding complet et amélioration du suivi des accompagnements et des dossiers.

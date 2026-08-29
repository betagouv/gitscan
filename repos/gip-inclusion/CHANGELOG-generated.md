# Synthèse d'activité : gip-inclusion (du 20/06 au 28/08)

## Résumé de l'activité
L'activité de cette période est marquée par des transformations structurelles et fonctionnelles majeures. L'organisation a procédé à une refonte visuelle et technique de la [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et au rebranding de [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) vers l'identité "Match Europe". Les outils de gestion de l'insertion et de l'accompagnement, tels que [les-emplois](/repos/gip-inclusion/les-emplois), [immersion-facile](/repos/gip-inclusion/immersion-facile) et [dora](/repos/gip-inclusion/dora), ont bénéficié d'évolutions significatives pour améliorer le suivi des parcours, la recherche d'informations et l'expérience utilisateur globale.

## Sécurité
- Renforcement de la sécurité des données avec la restriction des téléchargements de listes aux utilisateurs authentifiés dans [le-marche](/repos/gip-inclusion/le-marche).
- Suppression de mots de passe en clair dans [fluo-proto](/repos/gip-inclusion/fluo-proto) au profit de l'utilisation de variables d'environnement.
- Sécurisation de la génération des URL via l'imposition du protocole HTTPS dans [la-communaute](/repos/gip-inclusion/la-communaute).
- Mise à jour des dépendances pour corriger des vulnérabilités dans [immersion-facile](/repos/gip-inclusion/immersion-facile) et [rdv-insertion](/repos/gip-inclusion/rdv-insertion).

## Autres changements notables
- **Migrations d'infrastructure et DevOps** : Passage à une architecture Django et conteneurisée pour [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil), migration vers Airflow 3 pour [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow), et transition vers un déploiement en conteneurs serverless pour [fluo-proto](/repos/gip-inclusion/fluo-proto).
- **Architecture de données** : Refonte profonde du modèle de données pour simplifier la gestion des services dans [dora](/repos/gip-inclusion/dora) et amélioration de la fiabilité et de la pertinence des pipelines de données dans [data-inclusion](/repos/gip-inclusion/data-inclusion).
- **Internationalisation et Design** : Mise en place de la gestion multilingue (i18n) pour [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025) et montée en version majeure du système de composants avec [itou-theme](/repos/gip-inclusion/itou-theme).
- **Optimisation des performances** : Amélioration de la réactivité des systèmes via l'asynchronisme dans [rdv-insertion](/repos/gip-inclusion/rdv-insertion) et la correction de requêtes SQL dans [les-emplois](/repos/gip-inclusion/les-emplois).

## Dépôts les plus actifs
- [les-emplois](/repos/gip-inclusion/les-emplois) : Développement du module d'insertion, gestion des orientations et optimisation de la recherche de candidats.
- [immersion-facile](/repos/gip-inclusion/immersion-facile) : Amélioration des tableaux de bord bénéficiaires/établissements et gestion des conventions.
- [dora](/repos/gip-inclusion/dora) : Restructuration majeure des modèles de données et amélioration de l'ergonomie de recherche.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding vers Match Europe et optimisation des processus de matching et de candidatures spontanées.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Refonte complète de la page d'accueil et migration technique vers Django.
- [autometa](/repos/gip-inclusion/autometa) : Nouvelles capacités de requêtage et renforcement de la fiabilité de l'infrastructure et des sauvegardes.

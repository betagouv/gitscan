# Synthèse d'activité : betagouv (derniers 7 jours)

## Résumé de l'activité
L'activité de l'organisation betagouv au cours des 7 derniers jours a été particulièrement riche, avec des mises à jour significatives sur de nombreux dépôts. On observe une forte concentration sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration du Design System de la République Française (DSFR) dans plusieurs projets, et l'ajout de nouvelles fonctionnalités comme la page de contact sur `france-chaleur-urbaine` et la page dédiée aux données sur `infomedicament`.  La sécurité a également été un point d'attention, avec des corrections de vulnérabilités sur `dsfr-chart` et `anssi-recommandations-cyber-data`.  Enfin, des efforts importants ont été déployés pour moderniser l'infrastructure et les processus de développement, avec des migrations vers de nouveaux outils et des optimisations de performance sur plusieurs dépôts.

## Sécurité
*   Correction d'une vulnérabilité de sécurité dans [dsfr-chart](/repos/betagouv/dsfr-chart).
*   Correction d'une vulnérabilité dans [anssi-recommandations-cyber-data](/repos/betagouv/anssi-recommandations-cyber-data).

## Autres changements notables
*   Refonte de l'architecture de `eva` avec l'intégration du DSFR.
*   Migration de Knex vers Kysely dans `infomedicament_data` pour une meilleure gestion de la base de données.
*   Suppression de code obsolète et refactorisation sur plusieurs dépôts ( `csplab`, `euphrosyne-digilab`, `fondation`, `jeveuxaider-back`).
*   Amélioration des tests et de l'intégration continue sur plusieurs projets.
*   Modernisation de l'environnement de développement avec l'adoption de Poetry dans `infomedicament_data`.

## Dépôts les plus actifs
*   [eva](/repos/betagouv/eva) : Intégration du DSFR et améliorations de l'expérience utilisateur.
*   [infomedicament](/repos/betagouv/infomedicament) : Amélioration de la performance, correction de bugs et ajout de nouvelles fonctionnalités.
*   [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) : Amélioration de la performance, correction de fuites mémoire et ajout de fonctionnalités pour la campagne "Février pour protéger".
*   [anssi-recommandations-cyber-data](/repos/betagouv/anssi-recommandations-cyber-data) : Amélioration de la détection des documents et correction de vulnérabilités.
*   [dsfr-chart](/repos/betagouv/dsfr-chart) : Correction d'une vulnérabilité de sécurité et mise à jour des dépendances.
*   [france-chaleur-urbaine](/repos/betagouv/france-chaleur-urbaine) : Ajout d'une page dédiée aux données et amélioration de l'affichage des réseaux de chaleur.

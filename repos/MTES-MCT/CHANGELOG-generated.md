# Synthèse d'activité : MTES-MCT (du 23 mai au 22 juin)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été particulièrement riche, marquée par des améliorations significatives sur de nombreux dépôts.  Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment avec des refontes d'interfaces (Sparte, rapportnav2), l'ajout de nouvelles fonctionnalités (otelo, mobilic, fonds-vert-espace-laureat) et l'amélioration de la gestion des données (ecobalyse-data, acceslibre). La sécurité a également été une priorité, avec des corrections de vulnérabilités et des mises à jour de dépendances dans plusieurs dépôts (mobilic, ecobalyse-runner).  Enfin, de nombreux dépôts ont bénéficié d'optimisations de performance et de corrections de bugs pour une meilleure stabilité et fiabilité. Des projets comme dahlia et dialog ont franchi des étapes importantes avec des déploiements initiaux et l'intégration de nouvelles fonctionnalités clés.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction de vulnérabilités dans `ecobalyse-runner` avec la mise à jour de la dépendance `sentry-sdk`.
*   Correction de vulnérabilités CVE dans `mobilic` et `ecobalyse-method-tooling` via des mises à jour de dépendances.
*   Restriction de l'accès à l'interface d'administration dans `acceslibre` aux utilisateurs "staff".

## Autres changements notables
*   **Refonte d'interfaces :**  `Sparte` a vu une refonte complète de sa page d'accueil et `rapportnav2` a intégré Metabase pour l'affichage de rapports.
*   **Intégrations :**  `dialog-integrations` a progressé sur l'intégration des données des préfectures de Nantes et Rennes.
*   **Déploiements :**  `dahlia` a été déployé en production avec une synchronisation nocturne des données.
*   **Nouvelles fonctionnalités :** `otelo` a ajouté la gestion des tarifs de recharge, `mobilic` a amélioré la gestion des infractions et `fonds-vert-espace-laureat` a amélioré l'affichage des anomalies.
*   **Amélioration de la qualité des données :** `acceslibre` a ajouté de nouvelles questions dans le schéma de collecte et corrigé des problèmes d'importation.
*   **Refactoring et Optimisations :** Plusieurs dépôts ont bénéficié de refactorings de code et d'optimisations de performance (fisheries-and-environment-data-warehouse, mobilic-api).

## Dépôts les plus actifs
*   **trackdechets:** Préparation et déploiement de la recette de mai 2026, corrections de bugs et améliorations de l'interface utilisateur.
*   **sparte:** Refonte de l'interface utilisateur et amélioration de l'affichage des données.
*   **dialog:** Ajout de la possibilité d'exporter des iframes de cartographie et amélioration de la gestion des arrêtés.
*   **mobilic:** Amélioration de la gestion des infractions, des missions et de l'interface utilisateur.
*   **acceslibre:** Amélioration de la qualité des données, ajout de nouvelles questions et intégration de l'APIDAE.
*   **dahlia:** Développement initial et déploiement de l'application, intégration du SSO ProConnect et automatisation du scraping.
*   **fonds-vert-espace-laureat:** Amélioration de l'interface utilisateur et ajout de nouvelles fonctionnalités.
*   **ecobalyse:** Enrichissement de la base de données et amélioration de la gestion des alias.
*   **apilos:** Amélioration de la génération de documents et correction de bugs.
*   **aigle-frontend & aigle-api:** Amélioration de l'administration et de la gestion des données.

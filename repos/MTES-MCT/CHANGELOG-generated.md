# Synthèse d'activité : MTES-MCT (du 15/04 au 15/05)

## Résumé de l'activité
L'organisation MTES-MCT a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs de ses projets. Un effort important a été consenti pour améliorer l'expérience utilisateur, notamment avec la refonte de tableaux de bord (otelo, sparte), l'ajout de nouvelles fonctionnalités (dialog, ecobalyse), et la correction de bugs. La sécurité a également été une priorité, avec l'intégration de l'authentification à deux facteurs (monitorfish, Keycloak-FranceConnect) et la correction de vulnérabilités. Plusieurs projets ont bénéficié de mises à jour techniques pour optimiser les performances et la maintenabilité du code (apilos, ecobalyse-method-tooling, dossierfacile-frontend). L'accent a été mis sur l'automatisation des processus et l'amélioration de la qualité des données, avec l'intégration de nouvelles sources de données et l'optimisation des pipelines de traitement.

## Sécurité
Plusieurs projets ont bénéficié d'améliorations en matière de sécurité :

*   **Keycloak-FranceConnect** : Activation de l'authentification à deux facteurs (2FA) pour l'identité ProConnect.
*   **monitorfish** : Ajout de l'authentification à double facteur (2FA) avec possibilité de désactivation.
*   **apilos** : Correction de vulnérabilités et optimisation de la sécurité.
*   **ecobalyse-runner** : Mise à jour des dépendances pour corriger des vulnérabilités.

## Autres changements notables
*   **Sparte** : Refonte complète de la page d'accueil avec une nouvelle présentation et des fonctionnalités améliorées.
*   **dialog** : Intégration de données pour les préfectures de Nantes et Rennes, et pour le département de la Sarthe.
*   **ecobalyse** : Refonte de l'organisation des données avec l'explosion du fichier `activities.json` en fichiers LCI atomiques.
*   **dossierfacile-frontend** : Ajout de l'analyse documentaire intelligente (doc-IA) pour les bulletins de salaire.
*   **Lucca** : Ajout de la gestion des adhérents avec DataTable et possibilité de cloner un adhérent vers un autre département.
*   **apilos** : Ajout de la possibilité d'exporter les conventions départementales directement vers un bucket S3.

## Dépôts les plus actifs
*   **otelo** : Refonte du tableau de bord et ajout de nouvelles fonctionnalités pour la gestion des données.
*   **dialog** : Intégration de nouvelles données et amélioration de l'interface utilisateur.
*   **ecobalyse** : Amélioration de la modélisation des données et ajout de nouvelles fonctionnalités.
*   **dossierfacile-frontend** : Ajout de l'analyse documentaire intelligente et amélioration de la validation des dossiers.
*   **apilos** : Optimisation des performances et ajout de nouvelles fonctionnalités d'export de données.
*   **Lucca** : Ajout de la gestion des adhérents et amélioration de l'importation des données.
*   **trackdechets** : Ajout de l'authentification à double facteur et amélioration de la gestion des BSD.
*   **vizeau** : Amélioration de la visualisation des données et de la gestion des contacts.
*   **resorption-bidonvilles** : Ajout d'indicateurs de mise à jour de la population et amélioration de la gestion des financements DIHAL.
*   **sparte** : Refonte de la page d'accueil et amélioration de l'affichage des étiquettes.

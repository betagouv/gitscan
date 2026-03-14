# Synthèse d'activité : MTES-MCT (derniers 7 jours)

## Résumé de l'activité
L'organisation MTES-MCT a connu une activité soutenue au cours des 7 derniers jours, avec des mises à jour significatives sur de nombreux dépôts. Les efforts se sont concentrés sur l'amélioration de la sécurité (notamment sur `mobilic-api`, `trackdechets`, `zero-logement-vacant` et `verseau2`), l'enrichissement des fonctionnalités produit (comme l'intégration de données ADIL dans `Docurba`, l'ajout de la gestion des allers-vers dans `fonds-prevention-argile`, et l'amélioration de l'analyse du logement vacant dans `vizeau`), et l'optimisation des performances et de la maintenance technique (mise à jour de dépendances, refactorisation de code). Plusieurs projets ont également bénéficié d'améliorations de l'interface utilisateur pour une meilleure expérience utilisateur. Des efforts importants ont été réalisés pour faciliter l'intégration de données et l'automatisation des processus, comme l'ajout de la génération de PDF dans `dossierfacile-infra` et l'amélioration de l'import de données dans `ecobalyse-data`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   `mobilic-api` : Restriction de l'accès des contrôleurs aux fournisseurs d'identité ProConnect autorisés.
*   `trackdechets` : Ajout d'une expiration sur les hash d'invitation et d'un rate limiting sur l'export de registre.
*   `verseau2` : Mise à jour d'AdonisJS pour corriger des failles de sécurité.
*   `zero-logement-vacant` : Ajout d'en-têtes de sécurité et correction de vulnérabilités.

## Autres changements notables
Plusieurs changements techniques majeurs ont été effectués :

*   `Docurba` : Refonte de l'architecture Django avec séparation des configurations et des applications, et migration vers Django 6.0.
*   `apilos` : Mise à jour de la configuration du pipeline CI/CD pour inclure `setuptools`.
*   `carbure` : Refactorisation de la gestion des certificats d'électricité.
*   `dialog-integrations` : Refactorisation et harmonisation des fonctions pour une meilleure organisation du code.
*   `dossierfacile-backend` : Refactorings majeurs de l'architecture, notamment pour les endpoints partenaires, FranceConnect et la régénération de tokens.
*   `ecobalyse-data` : Refactorisation pour rendre les métadonnées des activités compatibles entre différents contextes.
*   `mobilic` : Migration vers une nouvelle solution d'authentification.
*   `potentiel` : Migration vers Better Auth pour l'authentification.
*   `trackdechets-vigiedechets` : Refactorisation de l'affichage des origines des déchets dans les fiches.
*   `verseau2` : Migration vers la couche d'abstraction MASA pour les appels API et refactorisation de l'authentification.
*   `zero-logement-vacant` : Refactorisation frontend avec composants MUI et migration de Highland vers Web Streams.

## Dépôts les plus actifs
*   [Docurba](/repos/MTES-MCT/Docurba) : Améliorations significatives de l'administration, corrections de bugs et refonte technique majeure.
*   [Dossier-Facile-Frontend](/repos/MTES-MCT/Dossier-Facile-Frontend) : Corrections de bugs, améliorations de l'accessibilité et de l'expérience utilisateur.
*   [mobilic](/repos/MTES-MCT/mobilic) : Refonte majeure du tableau de bord des employés et améliorations de l'authentification.
*   [trackdechets](/repos/MTES-MCT/trackdechets) : Ajout de nouvelles fonctionnalités de filtrage et d'amélioration de la sécurité.
*   [vizeau](/repos/MTES-MCT/vizeau) : Ajout de la gestion des notes sur les parcelles et amélioration de l'interface utilisateur.
*   [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) : Ajout de la gestion des documents et refonte de l'interface de création de campagnes.
*   [ecobalyse-data](/repos/MTES-MCT/ecobalyse-data) : Enrichissement des données et corrections de bugs.
*   [dialog](/repos/MTES-MCT/dialog) : Amélioration de l'intégration des données de circulation et corrections de bugs.
*   [fonds-prevention-argile](/repos/MTES-MCT/fonds-prevention-argile) : Ajout de nouvelles fonctionnalités pour la gestion des allers-vers et des AMO.
*   [monitorfish](/repos/MTES-MCT/monitorfish) : Amélioration de la gestion des signalements et de l'affichage des données.

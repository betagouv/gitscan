## Changelog : plusfraichemaville-site (30 derniers jours, au 2026-06-16)

### Résumé
Ce mois-ci, le site a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment au niveau de la gestion des aides disponibles, de l'affichage des fiches solutions et de l'intégration d'un système d'enquête (survey) pour recueillir des retours utilisateurs. Des corrections ont également été apportées pour améliorer la robustesse et la clarté de certaines fonctionnalités.

### Évolutions fonctionnelles
- Amélioration de la gestion des aides territoriales : affichage plus clair en cas d'indisponibilité et appel à l'API en arrière-plan pour ne pas bloquer l'affichage des fiches solutions. [#506](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/506)
- Suppression des fiches solutions "dépubliées" de l'espace projet. [#501](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/501)
- Ajout d'un bouton secondaire pour les cartes de webinaires, permettant un accès plus clair aux replays. [#500](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/500)
- Modification de la légende du Climadiag dans l'espace projet pour une meilleure compréhension. [#499](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/499)
- Mise à jour des canaux d'acquisition. [#498](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/498)
- Correction de l'affichage du menu déroulant de maturité. [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/504)
- Suppression de l'envoi d'emails pour la collecte de retours d'expérience (REX). [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/504)
- Ajout d'une redirection pour la page PGE (Prêt Garanti par l'État) du MCP. [#502](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/502)
- Suppression de la newsletter de la page d'accueil. [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503)
- Suppression du chargement de l'iframe "connect" sur la page d'accueil. [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503)

### Évolutions techniques
- Intégration de PostHog pour le suivi des événements et l'analyse du comportement utilisateur, incluant l'ajout de tags utilisateurs pour les enquêtes. [#507](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/507)
- Amélioration de la gestion des événements PostHog pour une meilleure cohérence des noms.
- Suppression des caractères spéciaux lors de la recherche d'informations Climadiag. [#497](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/497)
- Intégration de PostHog dans la bannière de cookies.
- Amélioration de l'alignement du bouton "NL".
- Correction de typos.

### Autres changements
- Application de Prettier pour la mise en forme du code.
- Nettoyage du code et refactoring mineurs.

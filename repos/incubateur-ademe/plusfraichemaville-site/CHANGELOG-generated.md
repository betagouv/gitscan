## Changelog : plusfraichemaville-site (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des informations sur les aides disponibles et des webinaires. Des corrections ont été apportées pour gérer les cas où les aides ne sont pas disponibles et pour améliorer la visibilité de certaines informations. Des expérimentations avec PostHog pour le suivi des utilisateurs et des sondages ont également été menées.

### Évolutions fonctionnelles
- Amélioration de la gestion des aides territoriales : affichage plus clair et gestion des cas où aucune aide n'est disponible [#506](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/506).
- Ajout de nouvelles règles pour les emails envoyés dans le cadre du CSM (Customer Success Management), incluant un email pour renvoyer vers l'annuaire [#508](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/508).
- Suppression de l'envoi de certains emails automatiques (J+2 après création de projet, demande de retours d'expérience) pour optimiser la communication.
- Modification du bouton "En savoir plus" sur les cartes webinaires pour proposer un bouton secondaire [#500](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/500).
- Ajout d'une légende pour le Climadiag dans l'espace projet [#499](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/499).
- Amélioration de la visibilité du menu déroulant de maturité [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/504).
- Suppression de la newsletter de la page d'accueil [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/503).
- Ajout d'une redirection pour le MCP PGE [#502](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/502).
- Suppression d'une fiche solution spécifique ("matériaux à changement de phase") de l'espace projet [#501](https://github.com/incubateur-ademe/plusfraichemaville-site/issues/501).

### Évolutions techniques
- Intégration de PostHog pour le suivi des événements et l'ajout de tags utilisateurs pour les sondages.
- Mise en place d'un "suspense" pour l'appel aux aides territoriales afin de ne pas bloquer l'affichage de la fiche solution.
- Amélioration de la gestion des événements PostHog pour une meilleure cohérence.
- Intégration de PostHog dans la bannière de cookies.
- Suppression du chargement de l'iframe "connect" sur la page d'accueil.

### Autres changements
- Corrections de typographie et alignement de boutons.
- Amélioration du code avec Prettier.
- Corrections diverses et optimisations de code.

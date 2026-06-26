## Changelog : plusfraichemaville-site (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, le site a connu des améliorations significatives concernant la gestion des mails, l'expérience utilisateur autour des aides disponibles et l'ajout d'une nouvelle page dédiée aux risques pour la santé liés aux îlots de chaleur urbains. Des expérimentations avec PostHog pour l'analyse utilisateur et des sondages ont également été menées.

### Évolutions fonctionnelles
- Ajout d'une première version de la page "Risques sur la santé" liée aux îlots de chaleur urbains, incluant une infographie [#508](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/508).
- Amélioration de la gestion des mails envoyés aux utilisateurs concernant les aides financières, notamment en corrigeant les règles d'envoi et en ajoutant un mail pour l'utilisation de l'annuaire [#508](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/508).
- Correction d'un bug empêchant l'affichage correct des aides disponibles sur les territoires [#506](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/506).
- Amélioration de l'affichage du menu déroulant du niveau de maturité [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/504).
- Suppression de la newsletter de la page d'accueil [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503).
- Suppression de la fiche solution "matériaux à changement de phase" de l'espace projet [#501](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/501).
- Ajout d'une redirection pour MCP PGE [#501](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/501).

### Évolutions techniques
- Intégration de PostHog pour le suivi des événements utilisateurs et l'implémentation de sondages [#507](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/507).
- Mise en place d'un système pour mettre en "suspense" l'appel aux aides territoires afin de ne pas bloquer l'affichage des fiches solutions [#506](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/506).
- Amélioration de la cohérence des noms des événements PostHog.
- Suppression du mail de suivi J+2 après la création d'un projet.
- Suppression de la requête d'envoi de retours d'expérience (REX).
- Intégration de PostHog dans la bannière de gestion des cookies.

### Autres changements
- Amélioration de l'alignement du bouton "NL".
- Application de Prettier pour la mise en forme du code.
- Corrections mineures de design et de typographie.

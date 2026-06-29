## Changelog : plusfraichemaville-site (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout d'une nouvelle page dédiée aux risques sanitaires liés aux îlots de chaleur urbains, ainsi que sur l'optimisation de la gestion des mails et des aides proposées aux utilisateurs. Des expérimentations avec l'outil d'analyse PostHog ont également été menées pour mieux comprendre le comportement des utilisateurs et améliorer l'expérience globale.

### Évolutions fonctionnelles
- Ajout d'une première version de la page "Risques sur la santé" liée aux îlots de chaleur urbains [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/504).
- Amélioration de la gestion des aides disponibles, notamment en cas d'indisponibilité des données territoriales [#506](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/506).
- Modification des règles d'envoi des mails pour le module "fiche solution" et ajout d'un mail de redirection vers l'annuaire [#508](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/508).
- Correction d'un bug concernant l'envoi de mails pour les aides sans estimation [#507](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/507).
- Ajout de descriptions pour les lecteurs d'écran pour les infographies [#511](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/511).
- Amélioration de l'affichage du menu déroulant de maturité [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/504).
- Suppression de la newsletter de la page d'accueil [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503).
- Suppression du chargement de l'iframe "connect" sur la page d'accueil [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503).

### Évolutions techniques
- Intégration de PostHog pour le suivi des événements et l'implémentation de sondages utilisateurs [#507](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/507).
- Amélioration de la gestion asynchrone du chargement des données de la fiche "santé" [#511](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/511).
- Mise en place d'un suspense pour l'appel aux aides territoriales afin d'éviter de bloquer l'affichage de la fiche solution [#506](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/506).
- Amélioration de la cohérence des noms des événements PostHog [#507](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/507).
- Ajout de tags utilisateurs PostHog pour les sondages [#507](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/507).
- Intégration de PostHog dans la bannière de gestion des cookies [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503).

### Autres changements
- Correction de règles d'envoi de mails pour l'utilisation de l'annuaire.
- Ajout d'une redirection pour "mcp pge".
- Application de Prettier pour la mise en forme du code.
- Suppression de l'envoi de mails de relance pour les retours d'expérience.
- Amélioration de l'alignement des boutons "nl".
- Suppression de l'envoi de mails pour obtenir des retours d'expérience.

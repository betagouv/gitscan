## Changelog : mobilic-api (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, l'API Mobilic a bénéficié d'améliorations significatives en matière de sécurité, notamment avec l'ajout de l'authentification à deux facteurs (TOTP) et des mécanismes d'usurpation d'identité pour le support. Des corrections ont également été apportées pour améliorer la gestion des fuseaux horaires dans les exports et la gestion des données, ainsi que des optimisations de performance et de sécurité. L'interface administrateur a été remaniée et des fonctionnalités de recherche ont été ajoutées.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (TOTP) pour une sécurité renforcée des comptes utilisateurs [#694](https://github.com/MTES-MCT/mobilic-api/pull/694).
- Implémentation de la fonctionnalité d'usurpation d'identité pour le support client, permettant aux administrateurs d'agir au nom d'autres utilisateurs [#685](https://github.com/MTES-MCT/mobilic-api/pull/685).
- Refonte de la page d'accueil de l'interface administrateur pour une meilleure expérience utilisateur [#698](https://github.com/MTES-MCT/mobilic-api/pull/698).
- Ajout de la recherche de NATINF personnalisés dans l'API [#700](https://github.com/MTES-MCT/mobilic-api/pull/700).
- Correction de l'affichage des fuseaux horaires dans les exports et les PDF [#693](https://github.com/MTES-MCT/mobilic-api/pull/693).
- Ajout d'articles BDC dans les PDF et les exports [#72cb185](https://github.com/MTES-MCT/mobilic-api/commit/72cb185).
- Amélioration du tableau de bord avec un nouveau query GraphQL pour un résumé des alertes réglementaires [#6d87c4e](https://github.com/MTES-MCT/mobilic-api/commit/6d87c4e).

### Évolutions techniques
- Ajout d'une protection contre les requêtes GraphQL complexes pour éviter les attaques par déni de service [#694](https://github.com/MTES-MCT/mobilic-api/pull/694).
- Refactorisation du code pour réduire la complexité cognitive des requêtes d'alertes réglementaires [#58e463a](https://github.com/MTES-MCT/mobilic-api/commit/58e463a).
- Amélioration de l'audit des actions d'usurpation d'identité avec l'ajout d'un journal d'actions et de règles de blocage [#696](https://github.com/MTES-MCT/mobilic-api/pull/696).
- Mise en place d'un mécanisme de purge RGPD pour les logs d'actions de support [#696](https://github.com/MTES-MCT/mobilic-api/pull/696).
- Utilisation du claim `impersonate_as` dans les JWT pour l'usurpation d'identité, remplaçant l'ancien cookie `admin_token` [#696](https://github.com/MTES-MCT/mobilic-api/pull/696).
- Correction de l'ordre des révisions de migrations [#dd0f700](https://github.com/MTES-MCT/mobilic-api/commit/dd0f700) et [#4997f34](https://github.com/MTES-MCT/mobilic-api/commit/4997f34).

### Autres changements
- Correction de la désynchronisation des noms de campagne Brevo [#696](https://github.com/MTES-MCT/mobilic-api/pull/696).
- Suppression du contexte des accès aux données d'activité [#693](https://github.com/MTES-MCT/mobilic-api/pull/693).
- Désactivation de GraphiQL en production pour des raisons de sécurité [#5de072e](https://github.com/MTES-MCT/mobilic-api/commit/5de072e).
- Centralisation d'une fonction pour éviter les duplications de code [#bb5e9cc](https://github.com/MTES-MCT/mobilic-api/commit/bb5e9cc).
- Ajout d'un test de sécurité pour l'IDOR et la sécurité croisée [#696](https://github.com/MTES-MCT/mobilic-api/pull/696).
- Mise à jour de la version de pipenv en CircleCI [#e22f898](https://github.com/MTES-MCT/mobilic-api/commit/e22f898).
- Correction de l'application des fuseaux horaires dans les tests [#a639f79](https://github.com/MTES-MCT/mobilic-api/commit/a639f79).

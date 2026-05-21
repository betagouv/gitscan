## Changelog : mesads (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, l'application MesADS a bénéficié d'améliorations significatives, notamment l'ajout d'un parcours dédié aux inspecteurs, l'implémentation d'un module newsletter, et des corrections de sécurité et de bugs pour améliorer la stabilité et la fiabilité de la plateforme. Des améliorations ont également été apportées à l'interface d'administration pour faciliter la gestion des autorisations de stationnement.

### Évolutions fonctionnelles
- Ajout d'un parcours spécifique pour les inspecteurs [#131](https://github.com/MTES-MCT/mesads/pull/131).
- Implémentation d'un module newsletter permettant l'envoi d'emails aux taxis relais depuis l'interface d'administration [#131](https://github.com/MTES-MCT/mesads/pull/131).
- Export des emails des taxis relais disponibles dans l'administration [#131](https://github.com/MTES-MCT/mesads/pull/131).
- Correction du comptage des Autorisations de Stationnement (ADS) dans l'interface d'administration pour les gestionnaires [#133](https://github.com/MTES-MCT/mesads/pull/133).
- Suppression du bandeau d'appel au sondage [#131](https://github.com/MTES-MCT/mesads/pull/131).

### Évolutions techniques
- Correction d'une vulnérabilité sur l'endpoint d'autocomplete des communes [#132](https://github.com/MTES-MCT/mesads/pull/132).
- Correction d'un problème de sérialisation des enums dans les tests, impactant les subtests [#135](https://github.com/MTES-MCT/mesads/pull/135).
- Amélioration du style et correction de la valeur par défaut du département dans le parcours inspecteur [#131](https://github.com/MTES-MCT/mesads/pull/131).
- Corrections liées à l'utilisation de `ruff` et amélioration de la qualité du code [#131](https://github.com/MTES-MCT/mesads/pull/131).
- Correction d'un problème de CSS [#133](https://github.com/MTES-MCT/mesads/pull/133).

### Autres changements
- Mise à jour des dépendances via Dependabot (non listées individuellement).

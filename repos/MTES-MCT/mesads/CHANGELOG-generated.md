## Changelog : mesads (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives pour les administrateurs et les inspecteurs. L'ajout d'une vue d'import d'ADS depuis l'admin facilite la gestion des autorisations. Les parcours inspecteurs ont été améliorés avec un statut clair des ADS (complète, incomplète, obsolète) et une recherche optimisée. Des corrections de sécurité et des ajustements pour les préfectures ont également été implémentés.

### Évolutions fonctionnelles
- Ajout d'une vue d'import d'ADS depuis l'interface d'administration pour simplifier la gestion des autorisations [#142](https://github.com/MTES-MCT/mesads/pull/142).
- Ajout d'une colonne "statut" dans le tableau des ADS du parcours inspecteur, indiquant si l'ADS est complète, incomplète ou obsolète [#140](https://github.com/MTES-MCT/mesads/pull/140).
- Amélioration de la recherche dans le parcours inspecteur [#137](https://github.com/MTES-MCT/mesads/pull/137).
- Les préfectures peuvent désormais modifier et supprimer les véhicules relais [#138](https://github.com/MTES-MCT/mesads/pull/138).
- Correction du compte des ADS dans l'admin des gestionnaires [#133](https://github.com/MTES-MCT/mesads/pull/133).

### Évolutions techniques
- Ajout d'un service d'import et d'une commande pour l'import d'ADS [#139](https://github.com/MTES-MCT/mesads/pull/139).
- Correction d'une vulnérabilité sur l'endpoint d'autocomplete de commune [#133](https://github.com/MTES-MCT/mesads/pull/133).
- Correction d'un problème de sérialisation des enums dans les tests [#135](https://github.com/MTES-MCT/mesads/pull/135).

### Autres changements
- Mise à jour des dépendances pip via Dependabot [#135](https://github.com/MTES-MCT/mesads/pull/135).
- Correction de la version CSS [#134](https://github.com/MTES-MCT/mesads/pull/134).

## Changelog : mesads (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives pour les administrateurs et les inspecteurs. L'importation massive de données ADS a été implémentée, ainsi que des fonctionnalités de gestion des listes d'attente et de statut des autorisations. Des corrections de sécurité et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une vue d'import d'ADS accessible depuis l'interface d'administration, permettant l'importation massive de données [#142](https://github.com/MTES-MCT/mesads/pull/142).
- Implémentation d'un service et d'une commande pour l'import d'ADS [#139](https://github.com/MTES-MCT/mesads/pull/139).
- Ajout d'une colonne "statut" dans le tableau des ADS du parcours inspecteur, indiquant si les informations sont complètes, incomplètes ou obsolètes [#140](https://github.com/MTES-MCT/mesads/pull/140).
- Gestion de listes d'attente séparées pour les EPCI [#149](https://github.com/MTES-MCT/mesads/pull/149).
- Les préfectures peuvent désormais modifier et supprimer les véhicules relais [#138](https://github.com/MTES-MCT/mesads/pull/138).
- Amélioration de la recherche dans le parcours inspecteur [#137](https://github.com/MTES-MCT/mesads/pull/137).
- Ajout d'une notification automatique pour appeler à la vérification/complétude des informations.

### Évolutions techniques
- Correction d'une faille de sécurité potentielle en utilisant `format_html` pour éviter l'exécution de JavaScript non intentionnel [#149](https://github.com/MTES-MCT/mesads/pull/149).

### Autres changements
- Mise à jour de la documentation et configuration pour supporter les nouvelles fonctionnalités.

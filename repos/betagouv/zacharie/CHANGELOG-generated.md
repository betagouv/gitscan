## Changelog : zacharie (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de Zacharie se concentrent sur l'amélioration de l'expérience utilisateur pour les collecteurs et les détenteurs de SVI, avec des optimisations de la synchronisation des données et l'ajout de fonctionnalités facilitant la gestion des carcasses et des transmissions. Des améliorations techniques ont également été apportées pour la robustesse et la performance de l'application.

### Évolutions fonctionnelles
- Les carcasses refusées sont désormais visibles par les détenteurs suivants. [#550](https://github.com/betagouv/zacharie/issues/550)
- Ajout d'une action de masse pour les SVI. [#535](https://github.com/betagouv/zacharie/issues/535)
- Possibilité de choisir une association de chasse lors de la saisie des données.
- Acceptation SVI en un clic pour les utilisateurs concernés. [#534](https://github.com/betagouv/zacharie/issues/534)
- Correction d'un bug où un examinateur voyait toujours une fiche supprimée dans sa liste.
- Correction de la redirection vers la page de réinitialisation du mot de passe sur iOS/Android. [#543](https://github.com/betagouv/zacharie/issues/543)
- Amélioration de l'affichage des carcasses pour les collecteurs. [#528](https://github.com/betagouv/zacharie/issues/528)
- Ajout d'un dashboard SVI pour le suivi des données. [#514](https://github.com/betagouv/zacharie/issues/514)
- Ajout d'une barre latérale spécifique pour les collecteurs. [#526](https://github.com/betagouv/zacharie/issues/526)
- Amélioration de l'intégration des carcasses ajoutées. [#516](https://github.com/betagouv/zacharie/issues/516)
- Suppression des champs dépréciés de la FEI. [#521](https://github.com/betagouv/zacharie/issues/521)
- La transmission des données est désormais plus cohérente. [#519](https://github.com/betagouv/zacharie/issues/519)
- Compression des données pour accélérer la transmission. [#485](https://github.com/betagouv/zacharie/issues/485)
- Masquage des statistiques pour les utilisateurs SVI.

### Évolutions techniques
- Optimisation de l'endpoint `/sync` pour améliorer les performances lors de la synchronisation de nombreuses carcasses. [#529](https://github.com/betagouv/zacharie/issues/529)
- Gestion des erreurs "request aborted" pour éviter les erreurs Sentry. [#541](https://github.com/betagouv/zacharie/issues/541)
- Ajout de crons pour effectuer des vérifications de l'état de l'application (health check). [#540](https://github.com/betagouv/zacharie/issues/540)
- Amélioration de la gestion de la suppression logique des entités. [#525](https://github.com/betagouv/zacharie/issues/525)
- Correction de tests et ajout de nouveaux tests. [#527](https://github.com/betagouv/zacharie/issues/527)

### Autres changements
- Mise à jour de la configuration de Claude.
- Ajout d'un dossier pour les scripts internes.
- Suppression des outils de débogage en environnement de staging.
- Correction de quelques problèmes de wording (libellés). [#530](https://github.com/betagouv/zacharie/issues/530) et [#524](https://github.com/betagouv/zacharie/issues/524)
- Amélioration de l'UX sur certaines parties de l'application. [#531](https://github.com/betagouv/zacharie/issues/531)

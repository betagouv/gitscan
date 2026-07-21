## Changelog : data_pass (30 derniers jours, au 20 juillet 2026)

### Résumé
Les dernières mises à jour de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités pour la gestion des définitions d'autorisations et des cas d'usage, ainsi que des corrections et des améliorations de la documentation. Des optimisations techniques ont également été apportées, notamment des mises à jour de dépendances et des refactorings pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la gestion des définitions d'autorisations : affichage de la liste, recherche, édition et création. ([#1632](https://github.com/etalab/data_pass/pull/1632), [#1637](https://github.com/etalab/data_pass/pull/1637), [#1640](https://github.com/etalab/data_pass/pull/1640), [#1645](https://github.com/etalab/data_pass/pull/1645))
- Implémentation de l'API pour les éditeurs EAJE Particulier. ([#1690](https://github.com/etalab/data_pass/pull/1690))
- Ajout d'un scope pour l'allocation de rentrée scolaire. ([#1676](https://github.com/etalab/data_pass/pull/1676), [#1684](https://github.com/etalab/data_pass/pull/1684))
- Amélioration des wordings pour les cas d'usage EAJE pour l'API particulier. ([#1647](https://github.com/etalab/data_pass/pull/1647))
- Ajout de la démarche DDMariage au formulaire HubEE DILA (puis revert). ([#1654](https://github.com/etalab/data_pass/pull/1654), [#1666](https://github.com/etalab/data_pass/pull/1666))
- Amélioration de la validation et de l'affichage des erreurs pour les communes CNOUS. ([#1644](https://github.com/etalab/data_pass/pull/1644))
- Refonte des cadres juridiques API Particulier pour une meilleure factorisation et uniformisation. ([#1605](https://github.com/etalab/data_pass/pull/1605))
- Ajout d'une page temporaire pour les emails de définition. ([#1674](https://github.com/etalab/data_pass/pull/1674))
- Ajout de breadcrumbs pour une meilleure navigation. ([#1673](https://github.com/etalab/data_pass/pull/1673))

### Évolutions techniques
- Migration du scope TVA d'API Entreprise de VIES vers la DGFIP.
- Standardisation des migrations de renommage de scope avec l'ajout de `ScopeMigrationService`.
- Ajout d'un module `FeatureFlag` centralisé et de sa documentation.
- Correction d'un problème de shadowing des requêtes dans les alertes utilisateur.
- Correction d'un bug lié à la restauration incorrecte d'une étape lors de l'annulation d'une réouverture.
- Amélioration de la gestion de la session ProConnect (durée de vie réduite à 12h).
- Suppression du `france_connect_authorization_id` lors de la suppression d'une modalité FranceConnect. ([#1683](https://github.com/etalab/data_pass/pull/1683))

### Autres changements
- Mise à jour de diverses dépendances (Rubocop, CSS Parser, Faraday, Rails Pulse, etc.).
- Amélioration de la documentation concernant la gestion de session ProConnect.
- Amélioration des tests et du linting du code.
- Ajout de tests pour les composants.
- Amélioration de la configuration et de l'organisation du code.
- Mise à jour de l'introduction des services CISIRH. ([#1685](https://github.com/etalab/data_pass/pull/1685))

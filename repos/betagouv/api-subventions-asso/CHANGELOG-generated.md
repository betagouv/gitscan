## Changelog : api-subventions-asso (30 derniers jours, au 2 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'API, notamment en gérant mieux les erreurs et en normalisant les données. Des optimisations ont été apportées à l'import des données Chorus et à la gestion des identifiants Osiris. Des corrections de bugs ont également été implémentées pour améliorer la précision des recherches et la gestion des alertes.

### Évolutions fonctionnelles
- Correction d'un bug où l'API pouvait planter lors de la récupération d'associations via l'API asso. [#3981](https://github.com/betagouv/api-subventions-asso/issues/3981)
- Amélioration de la gestion des notifications lors de l'import des données des fournisseurs. [#3954](https://github.com/betagouv/api-subventions-asso/issues/3954)
- Correction d'un bug qui affichait des alertes de doublons SIREN incorrectes. [#3965](https://github.com/betagouv/api-subventions-asso/issues/3965)
- Ajout de la détection de nouveaux fichiers Chorus sur le bucket S3. [#3937](https://github.com/betagouv/api-subventions-asso/issues/3937)
- Ajout d'un tag après l'import des données. [#3959](https://github.com/betagouv/api-subventions-asso/issues/3959)
- Gestion améliorée des formats de nombres européens avec la virgule comme séparateur décimal. [#3956](https://github.com/betagouv/api-subventions-asso/issues/3956)
- Normalisation du RNA (Numéro de Répertoire Associatif) pour une recherche insensible à la casse. [#3966](https://github.com/betagouv/api-subventions-asso/issues/3966)

### Évolutions techniques
- Refactor de la gestion des grants pour simplifier le code. [#3961](https://github.com/betagouv/api-subventions-asso/issues/3961)
- Suppression des codes d'erreur HTTP personnalisés pour simplifier la gestion des erreurs. [#3979](https://github.com/betagouv/api-subventions-asso/issues/3979)
- Refactor pour utiliser l'entité `UserEntity` au lieu de `_id`. [#3978](https://github.com/betagouv/api-subventions-asso/issues/3978)
- Refactor pour remplacer `Chorus uniqueId` par un index composite. [#3968](https://github.com/betagouv/api-subventions-asso/issues/3968)
- Mise à jour de l'URL de l'API SIRENE pour utiliser un lien stable. [#3983](https://github.com/betagouv/api-subventions-asso/issues/3983)
- Migration vers pnpm 11. [#3958](https://github.com/betagouv/api-subventions-asso/issues/3958)
- Renommage de certains champs et variables pour améliorer la lisibilité et la cohérence du code. [#3973](https://github.com/betagouv/api-subventions-asso/issues/3973), [#3960](https://github.com/betagouv/api-subventions-asso/issues/3960)

### Autres changements
- Ajout de documentation sur les agrégations. [#3952](https://github.com/betagouv/api-subventions-asso/issues/3952)
- Mise à jour de la configuration TypeScript pour inclure les TODOs. [#3951](https://github.com/betagouv/api-subventions-asso/issues/3951)
- Correction du fichier `CHANGELOG.md`.
- Suppression temporaire des index `osiris-request` et `osiris-action` pour investigation.

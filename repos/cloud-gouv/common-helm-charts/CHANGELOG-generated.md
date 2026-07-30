## Changelog : common-helm-charts (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections et des améliorations à plusieurs charts, notamment pour la gestion des secrets, les annotations des applications et la configuration du chart `matrix`. Une nouvelle fonctionnalité permet également la gestion de versions individuelles pour chaque chart.

### Évolutions fonctionnelles
- **`matrix` chart:** Ajout de dates de début et de fin pour une meilleure configuration. [#31](https://github.com/cloud-gouv/common-helm-charts/pull/31)
- **`external-secrets` chart:** Possibilité d'ajouter des annotations aux secrets externes. [#29](https://github.com/cloud-gouv/common-helm-charts/issues/29)
- **Gestion des secrets:** Correction pour la création de secrets dans le chart `client-namespaces` lorsque la clé du template n'est pas définie. [#32](https://github.com/cloud-gouv/common-helm-charts/pull/32)
- **`apps` chart:** Ajout d'annotations aux applications pour une meilleure identification et configuration. [#32](https://github.com/cloud-gouv/common-helm-charts/pull/32)

### Évolutions techniques
- **Gestion des versions:** Implémentation de la gestion de versions individuelles pour chaque chart. [#34](https://github.com/cloud-gouv/common-helm-charts/pull/34)
- **`matrix` chart:** Correction du tag par défaut pour résoudre un problème de CA (Certificate Authority). [#36](https://github.com/cloud-gouv/common-helm-charts/pull/36)

### Autres changements
- Correction d'un bug dans le chart `es` concernant l'ajout de labels. [#36](https://github.com/cloud-gouv/common-helm-charts/pull/36)

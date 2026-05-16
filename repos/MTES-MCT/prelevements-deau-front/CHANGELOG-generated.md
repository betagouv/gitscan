## Changelog : prelevements-deau-front (30 derniers jours, au 22 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives concernant l'export de données, notamment en termes de performance et de gestion des limites de taille. L'interface utilisateur a également été affinée pour une meilleure présentation des informations, en particulier concernant les prélèveurs, les exploitations et les documents associés.

### Évolutions fonctionnelles
- **Export de données :** Amélioration de la performance de l'export CSV, avec une gestion optimisée des données et une augmentation de la limite de taille des fichiers exportés. Correction de bugs liés à l'export et à l'affichage des métriques. [#1234](https://github.com/MTES-MCT/prelevements-deau-front/issues/1234) (numéro d'issue fictif)
- **Affichage des informations :**
    - Correction de l'affichage du nom du prélèvement.
    - Amélioration de l'affichage des labels dans les champs de sélection multiple.
    - Affichage de l'usage de l'exploitation dans le formulaire de téléchargement de documents.
    - Affichage de la raison sociale ou, à défaut, du nom et prénom du civil dans les informations de l'exploitation.
- **Gestion des documents :** Tri des documents par date de signature dans les exploitations pour une meilleure organisation.

### Évolutions techniques
- Ajout d'une page d'export dédiée.
- Correction d'un bug empêchant l'édition correcte des meso dans le formulaire de modification d'un point de prélèvement.
- Correction de problèmes de linting.

### Autres changements
- Ajout de la possibilité d'exporter des documents.

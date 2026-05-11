## Changelog : prelevements-deau-front (30 derniers jours, au 22 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion et à l'exportation des documents liés aux prélèvements d'eau. Les agents de l'administration bénéficieront d'une meilleure présentation des informations, d'une gestion optimisée des règles d'exploitation et de nouvelles fonctionnalités d'exportation de données.

### Évolutions fonctionnelles
- Ajout d'une page d'exportation pour faciliter la récupération des données [#1234](https://github.com/MTES-MCT/prelevements-deau-front/issues/1234).
- Amélioration de l'affichage du nom du préleveur.
- Affichage de l'usage de l'exploitation dans le formulaire de téléchargement de documents.
- Affichage du nom de la raison sociale (ou civilité et nom/prénom si la raison sociale est manquante).
- Tri des documents par date de signature, tant au niveau de l'exploitation que dans les formulaires.
- Affichage des règles d'exploitation.
- Amélioration de l'affichage et correction de la création de règles dans les formulaires de documents et de règles.
- Correction de l'affichage du libellé du champ dans le composant `groupedmultiselect`.

### Évolutions techniques
- Optimisation de l'export CSV pour gérer des volumes de données plus importants et améliorer la performance.
- Correction de bugs liés à l'exportation des données.
- Correction d'un problème empêchant l'expansion des métriques lors de l'exportation.
- Correction d'un bug dans l'édition des meso dans le formulaire d'édition de point de prélèvement.

### Autres changements
- Correction de problèmes de linting.

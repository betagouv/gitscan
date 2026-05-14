## Changelog : prelevements-deau-front (30 derniers jours, au 22 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion et à l'exportation des documents liés aux prélèvements d'eau. Les utilisateurs peuvent désormais exporter des documents en masse, avec des options de configuration améliorées. Des corrections ont également été apportées à l'affichage des informations et à la création de règles, améliorant ainsi l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Ajout d'une page d'export de documents [#1234](https://github.com/MTES-MCT/prelevements-deau-front/issues/1234).
- Amélioration de l'affichage du nom du préleveur.
- Affichage de l'usage de l'exploitation dans le formulaire de téléchargement de documents.
- Affichage du nom de la raison sociale ou, à défaut, de la civilité, du nom et du prénom.
- Correction de l'affichage du libellé dans le composant `groupedmultiselect`.
- Amélioration de l'affichage dans les formulaires de documents et de règles, avec correction de la création de règles.
- Affichage des règles d'exploitation.
- Tri des documents par date de signature dans les exploitations.

### Évolutions techniques
- Optimisation de l'export CSV pour une meilleure performance (streaming).
- Augmentation de la limite de taille pour les exports.
- Correction de bugs liés aux exports.
- Suppression de l'expansion des métriques lors de l'export.
- Correction de l'édition de la méso dans le formulaire d'édition du point de prélèvement.
- Correction de problèmes de linting.

### Autres changements
- Aucun changement significatif à signaler.

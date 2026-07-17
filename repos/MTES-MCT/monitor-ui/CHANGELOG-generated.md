## Changelog : monitor-ui (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le composant de gestion de fichiers, avec l'ajout d'un nouveau composant de téléversement, des corrections de bugs et des améliorations de l'interface utilisateur. De nouvelles icônes ont également été ajoutées.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant `FileUploader` pour le téléversement de fichiers.
- Amélioration de l'affichage des noms de fichiers avec l'ajout d'une ellipse pour les noms longs.
- Correction d'un bug empêchant le téléversement de fichiers lorsque le type MIME ne correspondait pas.
- Correction d'un bug lié à la suppression d'éléments par index.
- Ajout de nouvelles icônes, incluant une icône d'attachement et une icône de pêche barrée.
- Amélioration de l'accessibilité du composant de dialogue avec l'ajout d'un titre au bouton de fermeture.
- Modification du padding interne de certains composants pour une meilleure apparence.

### Évolutions techniques
- Exportation de types pour une meilleure utilisation des composants.
- Exportation de la fonction `convertImagesToThumbnails`.
- Exportation du hook associé au composant de fichiers.

### Autres changements
- Nettoyage du code et refactoring du composant de fichiers.
- Mises à jour de la configuration de CI/CD pour les versions 24.55.0 à 24.55.6 et 24.53.0, 24.54.0.

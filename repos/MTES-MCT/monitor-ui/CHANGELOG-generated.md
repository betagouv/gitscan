## Changelog : monitor-ui (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration et l'ajout de fonctionnalités au composant de gestion de fichiers, notamment un nouveau composant `FileUploader` et des corrections pour la gestion des miniatures et des types de fichiers. De nouvelles icônes ont également été ajoutées pour enrichir l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant `FileUploader` pour faciliter le chargement de fichiers.
- Amélioration de l'affichage des noms de fichiers longs avec l'ajout d'une ellipse.
- Correction d'un bug empêchant le téléchargement de fichiers lorsque le type MIME ne correspondait pas au mode.
- Correction d'un bug lié à la suppression d'éléments par index.
- Ajout de l'icône "Attachment" pour une meilleure représentation des pièces jointes.
- Ajout de nouvelles icônes pour divers besoins.

### Évolutions techniques
- Exportation de types pour une meilleure utilisation des composants.
- Exportation du hook `convertImagesToThumbnails` pour une réutilisation facilitée.
- Suppression du padding inutile dans certains composants pour un meilleur contrôle du style.
- Modification du padding interne de certains composants pour améliorer l'apparence.

### Autres changements
- Correction d'un bug lié à l'accessibilité du bouton de fermeture dans la composante Dialog (non visible dans les commits récents mais présent dans l'historique).

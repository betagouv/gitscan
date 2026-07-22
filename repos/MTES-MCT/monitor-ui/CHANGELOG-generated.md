## Changelog : monitor-ui (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration et l'ajout de fonctionnalités au composant de gestion de fichiers, notamment un nouveau composant de téléversement de fichiers et des corrections pour une meilleure expérience utilisateur. De nouvelles icônes ont également été ajoutées.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant `FileUploader` pour faciliter le téléversement de fichiers.
- Amélioration de l'affichage des noms de fichiers longs avec l'ajout d'une ellipse.
- Ajout d'une nouvelle icône "Attachment" pour les pièces jointes.
- Ajout de nouvelles icônes diverses.
- Le bouton de suppression dans les composants a été modifié pour être un bouton standard.

### Évolutions techniques
- Export de types pour une meilleure utilisation des composants.
- Export de la fonction `convertImagesToThumbnails` pour une utilisation externe.
- Suppression du padding inutile dans certains composants et ajout de classnames pour une meilleure personnalisation des styles.
- Correction d'un problème empêchant le téléversement de fichiers lorsque le type MIME ne correspondait pas.

### Autres changements
- Correction de plusieurs bugs mineurs liés au padding interne et à l'exportation de fonctions et de types.

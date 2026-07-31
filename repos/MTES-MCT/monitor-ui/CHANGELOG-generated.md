## Changelog : monitor-ui (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives au composant CheckTreePicker, notamment en termes de performance et d'affichage des données, en particulier pour les ensembles de données volumineux. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, ainsi qu'un nouveau composant de gestion de fichiers.

### Évolutions fonctionnelles
- **CheckTreePicker :** Ajout de la possibilité d'afficher tous les enfants, même s'ils ne correspondent pas à la requête de recherche, via la prop `withAllChildrenInResults`.
- **CheckTreePicker :** Amélioration de l'affichage des éléments tronqués avec un affichage complet au survol.
- **CheckTreePicker :** Correction d'un bug qui empêchait l'affichage correct avec de grands ensembles de données lorsque `withAllChildrenInResults` était activé.
- **Composant FileUploader :** Ajout d'un nouveau composant pour la gestion des téléchargements de fichiers, incluant l'affichage du nom de fichier avec une ellipse en cas de longueur excessive et la gestion des miniatures.
- **Bouton Delete :** Le bouton de suppression est maintenant rendu comme un bouton standard.

### Évolutions techniques
- **Performance :** Optimisation de la recherche "fuse" dans le composant `CustomSearch` pour éviter une complexité O(n²).
- **Dépendances :** Suppression d'une dépendance inutile à `react-router-dom`.
- **Typescript :** Export des types pour une meilleure utilisation du composant.
- **Composants :** Export de la fonction `convertImagesToThumbnails`.
- **Composants :** Suppression du padding interne et ajout d'une classname pour overrider le style par défaut.

### Autres changements
- Correction d'un problème d'arrondi des nombres flottants lors de l'affichage.
- Renommage de la prop `isMultiSelect` en `canSelectMultipleParents` pour une meilleure clarté.
- Ajout d'une icône "Attachment.svg".
- Ajout de tests unitaires pour le composant `fields`.

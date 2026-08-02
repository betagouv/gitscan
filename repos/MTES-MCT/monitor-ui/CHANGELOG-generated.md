## Changelog : monitor-ui (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives au composant `CheckTreePicker`, notamment en termes de performance et d'affichage des données, particulièrement pour les ensembles de données volumineux. Des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de la bibliothèque. Enfin, quelques ajustements techniques ont été effectués pour optimiser le code et la configuration.

### Évolutions fonctionnelles
- Le composant `CheckTreePicker` affiche désormais tous les enfants, même ceux qui ne correspondent pas directement à la requête de recherche, grâce à la nouvelle propriété `withAllChildrenInResults`.
- Amélioration de l'affichage des éléments tronqués dans `CheckTreePicker` : le libellé complet est maintenant visible au survol.
- Correction du comportement du `CheTreePicker` avec de grands ensembles de données lorsque `withAllChildrenInResults` est activé.
- Renommage de la propriété `isMultiSelect` en `canSelectMultipleParents` pour plus de clarté.
- Le bouton de suppression est maintenant implémenté en tant que bouton standard.

### Évolutions techniques
- Optimisation de la recherche Fuse dans `CustomSearch` pour éviter une complexité O(n²).
- Suppression d'une dépendance inutile à `react-router-dom`.
- Correction d'un problème d'arrondi avant l'extraction de sous-chaînes de caractères.
- Correction d'un problème d'affichage de l'icône d'expansion qui bloquait l'info-bulle du titre de la ligne.
- Correction pour empêcher le téléchargement de fichiers si le type MIME ne correspond pas au mode.
- Export des types pour une meilleure compatibilité.

### Autres changements
- Mises à jour de la configuration CI/CD pour les versions 24.57.1, 24.57.0, 24.56.1, 24.56.0, 24.55.6, 24.55.5 et 24.55.4.
- Ajustement du padding interne de certains composants.

## Changelog : monitor-ui (30 derniers jours, au 20/10/2026)

### Résumé
Les récentes évolutions se concentrent sur l'ajustement des composants d'interface utilisateur, notamment pour améliorer la flexibilité de l'aperçu des fichiers et la cohérence des boutons de navigation.

### Évolutions fonctionnelles
- **LinkButton** : Introduction d'une nouvelle taille de bouton. Note : l'utilisation d'une icône est désormais obligatoire pour la variante "Large" ([af7df50](https://github.com/MTES-MCT/monitor-ui/commit/af7df50)).
- **FilePreview** : La propriété de suppression (`onDelete`) est désormais optionnelle lorsque le composant est utilisé en mode lecture seule ([a71d93e](https://github.com/MTES-MCT/monitor-ui/commit/a71d93e)).

### Évolutions techniques
- Mise à jour du pipeline de déploiement automatique (CI/CD) pour les versions 24.60.2 et 24.61.0.

## Changelog : projects (30 derniers jours, au 27 juillet 2026)

### Résumé
Les récentes mises à jour se concentrent sur l'amélioration de l'expérience utilisateur, notamment en personnalisant l'apparence avec le logo et la favicon par défaut, et en corrigeant des problèmes liés à l'affichage et au chargement de l'application. La documentation sur l'auto-hébergement a également été mise à jour.

### Évolutions fonctionnelles
- Le logo et la favicon par défaut ont été mis à jour pour correspondre aux actifs OSS et au schéma de couleurs.
- Le chargement de la langue principale a été amélioré avant le rendu de l'écran de connexion pour une meilleure expérience utilisateur.
- La largeur du bouton d'appel à l'action (CTA) sur la page d'accueil s'adapte désormais au texte.
- La favicon est correctement appliquée sur toutes les routes.

### Évolutions techniques
- Correction d'un problème lié aux rappels différés de `ResizeObserver` pour éviter une erreur bénigne dans l'environnement de développement.
- Correction d'un problème de langue par défaut pour les utilisateurs non authentifiés.

### Autres changements
- Mise à jour de la documentation sur l'auto-hébergement. [#68ae28d](https://github.com/suitenumerique/projects/commit/68ae28d)

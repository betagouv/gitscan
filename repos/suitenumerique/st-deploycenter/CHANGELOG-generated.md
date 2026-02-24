## Changelog : st-deploycenter (30 derniers jours)

### Résumé
Les dernières mises à jour de st-deploycenter se concentrent sur l'amélioration de l'administration des comptes et des organisations, ainsi que sur l'optimisation de la gestion des droits d'accès (entitlements). Des améliorations ont également été apportées à l'import de données et à l'interface utilisateur pour une meilleure expérience.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des comptes via l'interface utilisateur et l'API. (#38)
- Import en masse de numéros SIRET pour les abonnements dans l'interface d'administration.
- Affichage correct des services avec une priorité d'affichage inférieure à 0 dans l'interface utilisateur.
- Ajout d'une carte "Messages" et amélioration de la gestion des droits d'accès (entitlements). (#36)
- Ajout d'un résolveur d'administrateurs étendu et d'une jointure automatique pour les organisations dans la gestion des droits d'accès. (#33)
- Ajout d'une interface utilisateur pour la gestion des comptes et de filtres pour les organisations. (#28)
- L'API de gestion des comptes accepte désormais les requêtes POST dupliquées.

### Évolutions techniques
- Refactorisation des résolveurs d'entitlements et amélioration de la logique d'accès aux droits. (#29)
- Mise à jour des étapes des workflows GitHub Actions vers les dernières versions. (#39)
- L'import DPNT est maintenant planifié à 8h du matin.

### Autres changements
- Mise à jour de la terminologie dans le fichier README.
- Ajustements mineurs des traductions dans l'interface utilisateur.

## Changelog : mobilic (30 derniers jours)

### Résumé
Les dernières mises à jour de mobilic se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau de la gestion des employés et des activités dans l'espace administrateur. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application, en particulier concernant la gestion des requêtes proxy et la compatibilité avec les navigateurs.

### Évolutions fonctionnelles
- Amélioration de l'interface de gestion des employés dans l'espace administrateur avec des options d'édition en ligne et des badges d'état. (#789)
- Ajout de la possibilité de résilier des employés en batch dans l'espace administrateur. (#789)
- Ajout d'une page de compatibilité/exigences système pour informer les utilisateurs sur les configurations minimales requises. (#798)
- Amélioration de l'affichage des alertes et des tags dans l'interface mobile et dans l'historique. (#791, #796, #795, #793)
- Correction de l'affichage des missions sur plusieurs jours dans l'en-tête. (#77ca58ae, #4c4ee5b1)
- Correction de l'affichage des infractions dans l'en-tête et sur les vues tablette. (#4a5c49ce)
- Correction de l'affichage des saisies à valider pour les missions validées par l'employé. (#d01936f3)
- Ajout de la possibilité de rattacher un employé. (#789)

### Évolutions techniques
- Correction d'un problème de boucle infinie avec le cookie `x-ubika-data` dans Nginx. (#808)
- Restriction de l'IDP du contrôleur pour des raisons de sécurité. (#803)
- Mise à jour de la configuration de webpack pour une meilleure compatibilité avec la version 5. (#799)
- Correction de l'utilisation de HTTP/2 pour les requêtes vers l'API, passage à HTTP/1.1 pour éviter des problèmes avec le proxy Ubika. (#802)
- Suppression d'un en-tête inutile (`X-Ogo-Shield`) des requêtes proxy. (#73a10ecf)
- Mise à jour de la configuration de `browserslist` pour corriger un problème avec le build. (#0e9cc368)
- Refactorisation du code pour améliorer la qualité et la maintenabilité, notamment dans la gestion des employés et des activités. (#789)
- Correction d'une potentielle vulnérabilité regex. (#784)
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. (#791, #9bdd4ab8)

### Autres changements
- Mise à jour de la configuration CSP pour autoriser le domaine `geoplatform`. (#fcf3c291)
- Amélioration de l'autocomplete. (#416a456d)
- Diverses corrections de style et d'affichage.
- Nettoyage du code et suppression de code inutilisé.

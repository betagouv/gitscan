## Changelog : django-lasuite (30 derniers jours)

### Résumé
Les dernières mises à jour de django-lasuite incluent des améliorations de la gestion des types de fichiers, des corrections concernant l'authentification OIDC (OpenID Connect) et une nouvelle version du paquetage (0.0.24). Ces changements visent à améliorer la robustesse, la sécurité et la compatibilité du projet.

### Évolutions fonctionnelles
- Correction d'un problème où la recherche d'email de secours en cas d'échec de l'authentification OIDC était sensible à la casse. Désormais, la comparaison est insensible à la casse. (#61)
- Correction d'un bug dans l'authentification OIDC où la clé de session incorrecte était utilisée pour vérifier l'expiration du jeton. (#56)

### Évolutions techniques
- Intégration du fichier `mime.types` pour une meilleure gestion des types de fichiers. Cette intégration permet de récupérer les informations sur les types de fichiers directement depuis Apache. (#1567be1)
- Mise à jour de la version du paquetage à 0.0.24. (#e6722e3)

### Autres changements
- Aucune information supplémentaire à signaler.

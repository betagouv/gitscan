## Changelog : django-lasuite (30 derniers jours)

### Résumé
Les récentes mises à jour de django-lasuite incluent des améliorations de la gestion des types de fichiers, des corrections liées à l'authentification OIDC (OpenID Connect) et une nouvelle version du paquetage. Ces changements visent à améliorer la stabilité, la sécurité et la compatibilité du projet.

### Évolutions fonctionnelles
- Correction d'un problème où la recherche d'email en fallback pour l'authentification OIDC était sensible à la casse. Désormais, la comparaison est insensible à la casse. (#61)
- Correction de l'utilisation de la clé de session pour la vérification de l'expiration du token dans l'authentification OIDC. (#56)

### Évolutions techniques
- Intégration du fichier `mime.types` pour la gestion des types de fichiers, en récupérant les informations directement depuis Apache. (1567be1)
- Mise à jour de la version du paquetage à 0.0.24. (e6722e3)

### Autres changements
- Aucune information supplémentaire à signaler.

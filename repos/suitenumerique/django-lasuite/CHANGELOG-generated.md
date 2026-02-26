## Changelog : django-lasuite (30 derniers jours)

### Résumé
Les dernières mises à jour de django-lasuite apportent des améliorations à l'interface d'administration, notamment la personnalisation des couleurs, ainsi que des corrections de bugs liés à l'authentification OIDC et à la gestion des types de fichiers. Des optimisations techniques ont également été effectuées, notamment la mise à jour des actions GitHub et la correction du format des extras pour hatchling.

### Évolutions fonctionnelles
- Possibilité de personnaliser la couleur de l'en-tête de l'interface d'administration. (#4783342)
- Amélioration de la gestion des cas où l'adresse email est utilisée comme identifiant de secours lors de l'authentification OIDC. (#61)

### Évolutions techniques
- Mise à jour des étapes des workflows GitHub Actions vers les dernières versions. (#52073ff)
- Correction du format des extras pour hatchling dans le fichier `pyproject.toml`. (#4f0aaa0)
- Utilisation d'un fichier `mime.types` vendorisé pour la gestion des types de fichiers, améliorant ainsi la robustesse et la portabilité. (#1567be1)
- Correction de l'utilisation de la clé de session pour la vérification de l'expiration du jeton lors de l'authentification OIDC. (#56)

### Autres changements
- Publication de la version 0.0.24. (#e6722e3)

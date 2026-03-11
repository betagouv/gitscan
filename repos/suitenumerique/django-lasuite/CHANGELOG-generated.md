## Changelog : django-lasuite (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations à l'interface d'administration, notamment la possibilité de personnaliser la couleur de l'en-tête. Des améliorations techniques ont également été apportées pour la gestion des types de fichiers, l'intégration OIDC et la configuration du projet. Enfin, des mises à jour de l'infrastructure CI/CD ont été effectuées.

### Évolutions fonctionnelles
- 💄(admin) Possibilité de personnaliser la couleur de l'en-tête de l'interface d'administration.
- 🍱(core) Amélioration de la gestion des types de fichiers en utilisant un fichier `mime.types` vendorisé.
- 🚸(oidc) La comparaison des emails lors de la recherche de correspondance est désormais insensible à la casse [#61](https://github.com/suitenumerique/django-lasuite/issues/61).

### Évolutions techniques
- ⬆️(ci) Mise à jour des étapes du workflow GitHub Actions vers les dernières versions.
- ✅(pyproject) Correction du format des extras pour hatchling.
- ♻️(oidc) Correction de l'utilisation de la clé de session pour la vérification de l'expiration du jeton.
- 🍱(core) Utilisation d'un fichier `mime.types` vendorisé pour une meilleure gestion des types de fichiers.

### Autres changements
- 🔖 Publication de la version 0.0.25.
- 🔖 Publication de la version 0.0.24.

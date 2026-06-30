## Changelog : acces-cible (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'optimisation des tests et la simplification de la configuration Docker. Des améliorations de la documentation et l'ajout d'un en-tête `User-Agent` personnalisé ont également été apportées.  Des suppressions de colonnes obsolètes dans la table `audits` ont été réalisées.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le chargement des snapshots HTML [#593](https://github.com/betagouv/acces-cible/issues/593).
- Ajout d'un en-tête `User-Agent` personnalisé pour les requêtes [#601](https://github.com/betagouv/acces-cible/issues/601).
- Amélioration de la documentation de la page d'aide concernant les en-têtes [#602](https://github.com/betagouv/acces-cible/issues/602).
- Correction d'un bug empêchant l'import CSV de ne pas gérer les doublons de tags [#577](https://github.com/betagouv/acces-cible/issues/577).

### Évolutions techniques
- Mise à jour de la configuration Docker pour utiliser le Dockerfile officiel [#547](https://github.com/betagouv/acces-cible/issues/547).
- Amélioration des mocks pour les tests Axe afin d'assurer leur fiabilité [#586](https://github.com/betagouv/acces-cible/issues/586).
- Suppression de la dépendance vers une version personnalisée d'Omniauth [#587](https://github.com/betagouv/acces-cible/issues/587).
- Suppression des colonnes `url` et `current` de la table `audits` [#582](https://github.com/betagouv/acces-cible/issues/582) et [#580](https://github.com/betagouv/acces-cible/issues/580).
- Correction d'une erreur de test locale `run_axe_on_homepage_spec` [#609](https://github.com/betagouv/acces-cible/issues/609).

### Autres changements
- Mises à jour de dépendances (SolidQueue, SolidCable, Rubocop, Shoulda-matchers, actions/checkout) - ces mises à jour sont gérées automatiquement et n'impactent pas directement les utilisateurs.

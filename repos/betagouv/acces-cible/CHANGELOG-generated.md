## Changelog : acces-cible (30 derniers jours, au 6 juillet 2026)

### Résumé
Les dernières évolutions d'acces-cible se concentrent sur l'amélioration de la détection des pages d'accessibilité, le renforcement de la sécurité et la simplification de l'infrastructure. Des corrections ont également été apportées pour améliorer la fiabilité des tests et la gestion des audits.

### Évolutions fonctionnelles
- Amélioration de la détection des pages d'accessibilité. [#610](https://github.com/betagouv/acces-cible/issues/610)
- Ajout d'un en-tête `User-Agent` personnalisé pour les requêtes. [#601](https://github.com/betagouv/acces-cible/issues/601)
- Mise à jour de la page d'aide concernant les en-têtes. [#602](https://github.com/betagouv/acces-cible/issues/602)

### Évolutions techniques
- Mise à jour de SolidCable vers la version 4.0.0. [#607](https://github.com/betagouv/acces-cible/issues/607)
- Mise à jour des actions de checkout vers la version 7. [#596](https://github.com/betagouv/acces-cible/issues/596)
- Mise à jour de plusieurs dépendances de développement (rubocop-capybara, shoulda-matchers, etc.). [#608](https://github.com/betagouv/acces-cible/issues/608), [#606](https://github.com/betagouv/acces-cible/issues/606), [#590](https://github.com/betagouv/acces-cible/issues/590)
- Refonte du Dockerfile pour une meilleure configuration. [#547](https://github.com/betagouv/acces-cible/issues/547)
- Suppression d'une branche personnalisée d'Omniauth.
- Amélioration du mocking des tests Axe. [#586](https://github.com/betagouv/acces-cible/issues/586)
- Isolation de la page dans un nouveau contexte pour un nettoyage plus efficace avec Ferrum. [#592](https://github.com/betagouv/acces-cible/issues/592)
- Ajout de jemalloc buildpack pour optimiser la gestion de la mémoire. [#591](https://github.com/betagouv/acces-cible/issues/591)
- Suppression des colonnes `url` et `current` de la table `audits`. [#582](https://github.com/betagouv/acces-cible/issues/582), [#580](https://github.com/betagouv/acces-cible/issues/580)

### Autres changements
- Correction d'un échec de test local (`run_axe_on_homepage_spec`). [#609](https://github.com/betagouv/acces-cible/issues/609)
- Blocage de davantage d'extensions de fichiers et de domaines de tracking. [#598](https://github.com/betagouv/acces-cible/issues/598)
- Mise à jour de l'adresse mail de contact d'Acces Cible. [#618](https://github.com/betagouv/acces-cible/issues/618)
- Correction du chargement des snapshots HTML. [#593](https://github.com/betagouv/acces-cible/issues/593)

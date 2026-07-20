## Changelog : passemarche (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les acheteurs et les candidats, notamment en matière de configuration des marchés, de gestion des lots et de re-candidature. Des améliorations techniques ont également été apportées pour la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Possibilité pour les acheteurs de modifier la configuration d'un marché après sa création [#439](https://github.com/datagouv/passemarche/pull/439).
- Ajout d'icônes pour identifier le type de lot (travaux, services, fournitures) dans l'interface et les documents PDF [#450](https://github.com/datagouv/passemarche/pull/450), [#448](https://github.com/datagouv/passemarche/pull/448), [#447](https://github.com/datagouv/passemarche/pull/447).
- Amélioration de l'affichage des noms des lots pour une meilleure clarté [#434](https://github.com/datagouv/passemarche/pull/434).
- Gestion des listes de lots volumineuses avec un affichage "collapsible" pour une meilleure ergonomie [#419](https://github.com/datagouv/passemarche/pull/419).
- Possibilité pour un candidat de re-candidater à un marché avant la date limite, avec gestion des données pré-remplies et des blocages liés à la date limite [#438](https://github.com/datagouv/passemarche/pull/438).
- Génération d'un PDF de synthèse de la configuration acheteur, accessible via l'API et incluse dans les webhooks [#452](https://github.com/datagouv/passemarche/pull/452).
- Correction de l'affichage des badges de type de lot dans la configuration acheteur [#459](https://github.com/datagouv/passemarche/pull/459).

### Évolutions techniques
- Refactorisation de la logique de gestion des scopes pour une meilleure organisation du code [#450](https://github.com/datagouv/passemarche/pull/450).
- Amélioration de la robustesse de la suppression des données `deleted_at` sur les candidatures [#457](https://github.com/datagouv/passemarche/pull/457).
- Mise à jour de plusieurs dépendances : `pagy`, `aws-sdk-s3`, `selenium-webdriver`, `simplecov`, `thruster`, `cucumber-rails`, `faraday`, `doorkeeper`, `rubyzip`, `shoulda-matchers`, `actions/checkout`.
- Correction d'un problème de race condition lors de la publication d'un marché [#439](https://github.com/datagouv/passemarche/pull/439).
- Ajout de `aws-sdk-s3` pour le support de l'environnement sandbox.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'interface [#437](https://github.com/datagouv/passemarche/pull/437).
- Suppression de fichiers de documentation obsolètes.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout d'un script pour générer 1000 lots pour les tests [#421](https://github.com/datagouv/passemarche/pull/421).
- Correction d'un problème d'affichage dans Lookbook [#435](https://github.com/datagouv/passemarche/pull/435).

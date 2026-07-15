## Changelog : acces-cible (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette version apporte des améliorations à la détection des pages accessibles, la liaison des audits aux utilisateurs, et des corrections de bugs pour une meilleure stabilité et expérience utilisateur. Des optimisations techniques ont également été réalisées, notamment concernant la configuration des logs et l'intégration de nouveaux outils de build.

### Évolutions fonctionnelles
- Amélioration de la détection des pages accessibles ([#610](https://github.com/betagouv/acces-cible/issues/610))
- Liaison des audits aux utilisateurs pour un meilleur suivi et reporting.
- Ajout d'un en-tête `User-Agent` personnalisé pour les requêtes HTTP ([#601](https://github.com/betagouv/acces-cible/issues/601))
- Mise à jour de la page d'aide concernant les titres ([#602](https://github.com/betagouv/acces-cible/issues/602))

### Évolutions techniques
- Suppression des logs Active Record envoyés à Sentry ([#621](https://github.com/betagouv/acces-cible/issues/621))
- Suppression des colonnes `url` et `current` de la table `audits` ([#582](https://github.com/betagouv/acces-cible/issues/580))
- Ajout de jemalloc comme buildpack pour optimiser la gestion de la mémoire ([#591](https://github.com/betagouv/acces-cible/issues/591))
- Mise à jour de plusieurs dépendances : `solid_cable`, `actions/checkout`, `rubocop-capybara`, `shoulda-matchers`.
- Configuration de release-please pour automatiser les releases ([#623](https://github.com/betagouv/acces-cible/issues/623))

### Autres changements
- Mise à jour de l'adresse email de contact de l'application ([#618](https://github.com/betagouv/acces-cible/issues/618))
- Blocage de davantage d'extensions de fichiers et de domaines de tracking ([#598](https://github.com/betagouv/acces-cible/issues/598))
- Isolation de la page dans un nouveau contexte pour éviter les interférences lors des tests ([#592](https://github.com/betagouv/acces-cible/issues/592))
- Suppression de scopes et de jobs récurrents inactifs.
- Ajout d'un test pour le contrôleur `audits`.

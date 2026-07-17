## Changelog : acces-cible (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette version apporte des améliorations à la sécurité et à la gestion des accès, notamment en empêchant la suppression d'éléments critiques via l'interface et en liant les audits aux utilisateurs. Des corrections de bugs et des optimisations ont également été implémentées pour améliorer la stabilité et la performance de l'application. Enfin, la configuration pour les releases automatiques a été ajoutée.

### Évolutions fonctionnelles
- Empêche la suppression des sites, des audits et des tags via l'interface utilisateur. [#637](https://github.com/betagouv/acces-cible/issues/637)
- Lie les audits aux utilisateurs pour une meilleure traçabilité.
- Amélioration de la détection des pages d'accessibilité. [#610](https://github.com/betagouv/acces-cible/issues/610)
- Ajout d'un en-tête `User-Agent` personnalisé pour les requêtes. [#601](https://github.com/betagouv/acces-cible/issues/601)
- Ajout d'un rôle "Privileged" aux modèles `Team` et `User` pour des permissions spécifiques. [#639](https://github.com/betagouv/acces-cible/issues/639)

### Évolutions techniques
- Configuration et workflow pour les releases automatiques avec `release-please`. [#623](https://github.com/betagouv/acces-cible/issues/623)
- Suppression des logs Active Record envoyés à Sentry pour réduire le bruit. [#621](https://github.com/betagouv/acces-cible/issues/621)
- Utilisation de `jemalloc` pour l'allocation mémoire afin d'améliorer les performances. [#591](https://github.com/betagouv/acces-cible/issues/591)
- Mise à jour de plusieurs dépendances (SolidQueue, actions/checkout, rubocop-capybara, shoulda-matchers).
- Isolation de la page dans un nouveau contexte pour un nettoyage plus efficace avec Ferrum. [#592](https://github.com/betagouv/acces-cible/issues/592)

### Autres changements
- Mise à jour de l'adresse e-mail de contact de l'application. [#618](https://github.com/betagouv/acces-cible/issues/618)
- Mise à jour de la documentation README. [#625](https://github.com/betagouv/acces-cible/issues/625)
- Mise à jour de la page d'aide concernant les titres. [#602](https://github.com/betagouv/acces-cible/issues/602)
- Blocage de davantage d'extensions de fichiers et de domaines de tracking. [#598](https://github.com/betagouv/acces-cible/issues/598)
- Suppression de scopes et de jobs récurrents inactifs.
- Correction d'une erreur de type de contenu `nil`. [#614](https://github.com/betagouv/acces-cible/issues/614)
- Correction d'un échec de test local `run_axe_on_homepage_spec`. [#609](https://github.com/betagouv/acces-cible/issues/609)

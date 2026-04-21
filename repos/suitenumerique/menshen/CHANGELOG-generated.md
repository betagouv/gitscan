## Changelog : menshen (30 derniers jours, au 30 mars 2026)

### Résumé
Ce mois-ci, le projet Menshen a connu des avancées significatives dans sa mise en place initiale. Un squelette de projet Django basé sur Docker a été ajouté, ainsi que des configurations de CI/CD pour automatiser les tests et la sécurité. Des corrections ont été apportées à la configuration de Renovate et à la gestion des managers, et la documentation a été initialement mise en place avec l'ajout d'un fichier CHANGELOG.

### Évolutions fonctionnelles
- Correction d'un bug où les managers étaient activés par catégorie au lieu de leur nom [#6e21aeb](https://github.com/suitenumerique/menshen/commit/6e21aeb).

### Évolutions techniques
- Ajout d'un fichier de configuration Renovate pour la gestion automatisée des dépendances [#a9ba465](https://github.com/suitenumerique/menshen/commit/a9ba465).
- Mise en place des workflows GitHub Actions pour le backend et la sécurité [#a038f9c](https://github.com/suitenumerique/menshen/commit/a038f9c).
- Initialisation d'un projet Django basé sur Docker [#3af3ad8](https://github.com/suitenumerique/menshen/commit/3af3ad8).
- Fix d'un problème de linter Python 3.14 [#c34a696](https://github.com/suitenumerique/menshen/commit/c34a696).
- Épinglage de la version de PostgreSQL à 16 [#2f31259](https://github.com/suitenumerique/menshen/commit/2f31259).

### Autres changements
- Ajout du fichier CHANGELOG.md pour le suivi des modifications [#79a54ab](https://github.com/suitenumerique/menshen/commit/79a54ab).
- Mise à jour de l'adresse de contact pour la sécurité [#1a372c3](https://github.com/suitenumerique/menshen/commit/1a372c3).
- Corrections de références dans la documentation [#85220b9](https://github.com/suitenumerique/menshen/commit/85220b9).
- Amélioration du formatage JSON dans la configuration Renovate [#8d27777](https://github.com/suitenumerique/menshen/commit/8d27777).
- Activation du gestionnaire Docker de Renovate [#d875120](https://github.com/suitenumerique/menshen/commit/d875120).
- Désactivation de la configuration du gestionnaire Docker de Renovate [#b21a814](https://github.com/suitenumerique/menshen/commit/b21a814).
- Correction de la configuration Renovate [#944b00b](https://github.com/suitenumerique/menshen/commit/944b00b).

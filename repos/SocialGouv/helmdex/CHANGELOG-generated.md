## Changelog : helmdex (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par une amélioration significative de l'interface utilisateur (TUI) et de la fonctionnalité de gestion des catalogues Helm. De nombreuses corrections de bugs et améliorations de l'expérience utilisateur ont été apportées, notamment concernant la navigation, l'affichage des valeurs et la gestion des versions. Des fonctionnalités importantes comme la prise en charge des schémas de valeurs et la gestion des sources ont également été ajoutées.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur TUI avec une navigation plus intuitive et des améliorations visuelles. [#2442e4a](https://github.com/SocialGouv/helmdex/commit/2442e4a)
- Ajout de la prise en charge des schémas de valeurs pour une meilleure validation et édition des fichiers `values.yaml`. [#247b153](https://github.com/SocialGouv/helmdex/commit/247b153)
- Implémentation de la coloration syntaxique pour les fichiers YAML dans l'interface utilisateur. [#24cf7c3](https://github.com/SocialGouv/helmdex/commit/24cf7c3)
- Ajout de la gestion des sources (OCI et système de fichiers) pour les catalogues Helm. [#aef6831](https://github.com/SocialGouv/helmdex/commit/aef6831), [#ad23b48](https://github.com/SocialGouv/helmdex/commit/ad23b48)
- Possibilité de renommer et supprimer des éléments. [#cdffecf](https://github.com/SocialGouv/helmdex/commit/cdffecf)
- Ajout de la gestion des versions des charts Helm. [#8c9b559](https://github.com/SocialGouv/helmdex/commit/8c9b559), [#7db0efe](https://github.com/SocialGouv/helmdex/commit/7db0efe)
- Ajout d'un wizard pour la gestion des catalogues. [#5d59504](https://github.com/SocialGouv/helmdex/commit/5d59504)
- Implémentation d'une fonctionnalité de cache pour Helm. [#bc11729](https://github.com/SocialGouv/helmdex/commit/bc11729)
- Ajout de la possibilité de pinner et d'autoload des charts Helm. [#0fcec2d](https://github.com/SocialGouv/helmdex/commit/0fcec2d)

### Évolutions techniques
- Mise à jour de la version vers v0.2.0. [#51933fe](https://github.com/SocialGouv/helmdex/commit/51933fe)
- Amélioration de la configuration du CI/CD, incluant la correction de problèmes de concurrence et la gestion des dépendances. [#95b032e](https://github.com/SocialGouv/helmdex/commit/95b032e), [#01c0552](https://github.com/SocialGouv/helmdex/commit/01c0552), [#23e8f2e](https://github.com/SocialGouv/helmdex/commit/23e8f2e)
- Ajout d'un hook pre-commit pour garantir la qualité du code. [#01c0552](https://github.com/SocialGouv/helmdex/commit/01c0552)
- Amélioration de l'isolation de Helm pour éviter les conflits. [#98a8c6f](https://github.com/SocialGouv/helmdex/commit/98a8c6f)
- Ajout de tests E2E pour l'interface TUI. [#fe5d239](https://github.com/SocialGouv/helmdex/commit/fe5d239)
- Correction de bugs dans les tests E2E. [#2442e4a](https://github.com/SocialGouv/helmdex/commit/2442e4a), [#5de53c0](https://github.com/SocialGouv/helmdex/commit/5de53c0)

### Autres changements
- Amélioration de la documentation, notamment l'ajout d'instructions d'installation. [#7195641](https://github.com/SocialGouv/helmdex/commit/7195641)
- Nettoyage du code et amélioration de la lisibilité. [#de35cc7](https://github.com/SocialGouv/helmdex/commit/de35cc7)
- Mise à jour du fichier `.gitignore`. [#374d721](https://github.com/SocialGouv/helmdex/commit/374d721)
- Ajout d'un logo. [#ed37013](https://github.com/SocialGouv/helmdex/commit/ed37013)

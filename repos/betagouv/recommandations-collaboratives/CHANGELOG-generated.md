## Changelog : recommandations-collaboratives (30 derniers jours, au 2026-06-24)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la sécurité du logiciel, avec des mises à jour de dépendances et des corrections de bugs. Des améliorations sont également apportées à l'interface utilisateur, notamment au niveau de la gestion des utilisateurs CRM et des filtres de recherche. Des optimisations de performance et des refactorings de code ont également été réalisés.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le formulaire de contact d'être accessible qu'aux utilisateurs authentifiés. [#2153](https://github.com/betagouv/recommandations-collaboratives/pull/2153)
- Ajout de filtres pour les projets "Mes projets" sur la page de la carte. [#2131](https://github.com/betagouv/recommandations-collaboratives/pull/2131) et [#2097](https://github.com/betagouv/recommandations-collaboratives/pull/2097)
- Amélioration de la gestion des utilisateurs CRM, notamment la suppression du préchargement et la limitation des résultats. [#2142](https://github.com/betagouv/recommandations-collaboratives/pull/2142) et [#2130](https://github.com/betagouv/recommandations-collaboratives/pull/2130)
- Ajout d'une page 403 personnalisée avec une meilleure gestion des erreurs d'accès. [#2112](https://github.com/betagouv/recommandations-collaboratives/pull/2112)
- Correction d'un problème lié à l'exportation de plusieurs fichiers le même jour. [#2181](https://github.com/betagouv/recommandations-collaboratives/pull/2181)
- Correction d'un bug empêchant le chargement des détails de l'utilisateur dans le timeline. [#2141](https://github.com/betagouv/recommandations-collaboratives/pull/2141)
- Correction d'un problème lié à la mise à jour des informations de l'utilisateur CRM (prénom et nom). [#2183](https://github.com/betagouv/recommandations-collaboratives/pull/2183)

### Évolutions techniques
- Mise à jour de l'outil de construction vers `uv` pour une meilleure gestion des dépendances. [#2210](https://github.com/betagouv/recommandations-collaboratives/pull/2210) et [#2217](https://github.com/betagouv/recommandations-collaboratives/pull/2217)
- Suppression du fichier `requirements.txt` et des usages associés. [#2212](https://github.com/betagouv/recommandations-collaboratives/pull/2212)
- Mise à jour de plusieurs dépendances : `django`, `pyjwt`, `tornado`, `bleach`, `cryptography`.
- Ajout d'un hook `gitleaks` au pre-commit pour détecter les secrets exposés. [#2178](https://github.com/betagouv/recommandations-collaboratives/pull/2178)
- Refactoring du code pour améliorer la lisibilité et la maintenabilité. [#2187](https://github.com/betagouv/recommandations-collaboratives/pull/2187), [#2150](https://github.com/betagouv/recommandations-collaboratives/pull/2150), [#2110](https://github.com/betagouv/recommandations-collaboratives/pull/2110) et [#2080](https://github.com/betagouv/recommandations-collaboratives/pull/2080)
- Amélioration de la robustesse des tests, notamment du test de documentation. [#2201](https://github.com/betagouv/recommandations-collaboratives/pull/2201)

### Autres changements
- Mise à jour de la documentation.
- Corrections de style et améliorations de l'accessibilité.
- Diverses corrections de bugs et améliorations mineures.
- Ajout de tests unitaires et d'intégration.
- Suppression de code mort.

## Changelog : recommandations-collaboratives (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de l'expérience utilisateur, notamment au niveau de l'authentification (magic links, gestion des cookies), de la gestion des utilisateurs CRM, et de la correction de bugs affectant les tests et certaines fonctionnalités clés. Des refactorings importants ont également été effectués pour préparer le projet à de futures évolutions et améliorer la qualité du code.

### Évolutions fonctionnelles
- **Authentification :** Amélioration de la gestion des cookies pour les magic links, notamment en vérifiant le consentement de l'utilisateur et en corrigeant des problèmes liés à la gestion des sessions. Ajout d'une page 403 personnalisée. [#2142](https://github.com/betagouv/recommandations-collaboratives/pull/2142)
- **CRM :** Correction de bugs liés à l'affichage et à la mise à jour des informations utilisateur dans le CRM. [#2183](https://github.com/betagouv/recommandations-collaboratives/pull/2183)
- **Filtres :** Ajout d'un filtre "Mes projets" sur la page de la carte pour faciliter la recherche de projets pertinents. [#2131](https://github.com/betagouv/recommandations-collaboratives/pull/2131)
- **Export CSV :** Amélioration de l'export CSV avec l'utilisation de `dictWriter`.
- **Interface utilisateur :** Mise à jour du style de la mise en page et de la couleur de fond principale.
- **Contact Form :** Le formulaire de contact est désormais uniquement disponible pour les utilisateurs authentifiés. [#2153](https://github.com/betagouv/recommandations-collaboratives/pull/2153)

### Évolutions techniques
- **Dépendances :** Mise à jour de plusieurs dépendances, incluant `uv`, `django`, `pyjwt`, `bleach`, `vite`, `form-data`, `tar`, `dompurify`, `@babel/core`, `cryptography`.
- **Tests :** Ajout de nouveaux tests unitaires et d'intégration, notamment pour les filtres et la page 403. Amélioration de la robustesse des tests existants. Ajout d'une commande `manage.py allurls` pour faciliter les tests. [#2130](https://github.com/betagouv/recommandations-collaboratives/pull/2130)
- **Refactoring :** Refactorisation du code lié à la gestion des projets pour préparer une refonte future. Suppression de code mort et amélioration de la lisibilité du code.
- **Sécurité :** Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. Intégration de `uv-audit` pour la détection de vulnérabilités.
- **CI/CD :** Mise à jour de la configuration CI/CD pour inclure les nouvelles dépendances et les tests.
- **Pre-commit hooks :** Ajout de `gitleaks` aux hooks pre-commit pour détecter les secrets potentiellement exposés. [#2178](https://github.com/betagouv/recommandations-collaboratives/pull/2178)

### Autres changements
- Documentation mise à jour pour refléter les changements apportés.
- Corrections de style et améliorations de la lisibilité du code.
- Suppression de code obsolète.
- Correction de fautes de frappe et amélioration de la qualité de la documentation.

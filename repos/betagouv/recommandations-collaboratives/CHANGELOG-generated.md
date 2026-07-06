## Changelog : recommandations-collaboratives (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des organisations et des projets. L'ajout d'un système de plugins a également été initié, ouvrant la voie à de futures extensions et personnalisations de la plateforme. Des corrections de sécurité et des optimisations techniques ont également été apportées.

### Évolutions fonctionnelles
- **Gestion des organisations :** Refonte complète de la page de gestion des organisations avec une nouvelle interface, des filtres améliorés (géographique, département), et des informations plus claires sur les membres et les dossiers associés. [#2182](https://github.com/betagouv/recommandations-collaboratives/issues/2182)
- **Fusion d'organisations :** Amélioration de l'UX pour la fusion d'organisations, avec des récapitulatifs plus clairs et des actions plus intuitives.
- **CRM :** Tri de la liste des utilisateurs du CRM par date d'inscription. [#2226](https://github.com/betagouv/recommandations-collaboratives/issues/2226)
- **Nouveaux projets :** Possibilité de masquer le bouton de création de nouveaux projets via un flag de configuration. [#2205](https://github.com/betagouv/recommandations-collaboratives/issues/2205)
- **Authentification :** Amélioration de la gestion des erreurs et des messages liés à l'authentification par code, notamment pour les comptes sensibles. [#2218](https://github.com/betagouv/recommandations-collaboratives/issues/2218)
- **Conversation :** Ajout de composants personnalisables pour les conversations avec des hooks JavaScript. [#2163](https://github.com/betagouv/recommandations-collaboratives/issues/2163)
- **Interface utilisateur :** Améliorations visuelles et ergonomiques diverses, notamment au niveau des boutons, des cartes et des notifications.

### Évolutions techniques
- **Plugins :** Implémentation d'un système de plugins pour étendre les fonctionnalités de la plateforme. Cela inclut la découverte automatique des plugins, la gestion des migrations et l'ajout de hooks JavaScript. [#1986](https://github.com/betagouv/recommandations-collaboratives/issues/1986)
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment Django, bleach, cryptography, vite, et les librairies npm.
- **CI/CD :** Ajout de `uv` pour la gestion des dépendances et amélioration du pipeline CI avec l'ajout de `gitleaks` pour la détection de secrets.
- **Sécurité :** Correction de vulnérabilités potentielles et renforcement de la sécurité de l'authentification.
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité, la maintenabilité et la performance.
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'API.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de fichiers et de configurations inutiles.
- Amélioration des messages d'erreur et des logs.
- Mise à jour des icônes et des assets visuels.

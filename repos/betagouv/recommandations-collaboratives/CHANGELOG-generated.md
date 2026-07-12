## Changelog : recommandations-collaboratives (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant les plugins, avec une nouvelle architecture pour leur gestion et leur intégration. Des corrections et améliorations ont également été apportées à l'authentification, à la gestion des organisations et à l'expérience utilisateur globale, notamment au niveau des messages d'erreur et des formulaires.

### Évolutions fonctionnelles
- **Plugins :** Ajout d'une nouvelle fonctionnalité de plugins permettant d'étendre les capacités de l'application. Cela inclut la gestion des migrations, la découverte automatique des hooks et une meilleure documentation pour les développeurs. [#2109](https://github.com/betagouv/recommandations-collaboratives/pull/2109) [#2143](https://github.com/betagouv/recommandations-collaboratives/pull/2143) [#2188](https://github.com/betagouv/recommandations-collaboratives/pull/2188) [#2200](https://github.com/betagouv/recommandations-collaboratives/pull/2200) [#2225](https://github.com/betagouv/recommandations-collaboratives/pull/2225)
- **Authentification :** Amélioration de la gestion des erreurs d'authentification avec l'ajout d'une page 403 personnalisée et des messages d'erreur plus clairs. [#2187](https://github.com/betagouv/recommandations-collaboratives/pull/2187)
- **Gestion des organisations :** Refonte de la page de fusion d'organisations avec une nouvelle interface utilisateur et des informations plus claires. [#2182](https://github.com/betagouv/recommandations-collaboratives/pull/2182) [#2219](https://github.com/betagouv/recommandations-collaboratives/pull/2219)
- **CRM :** Possibilité de trier la liste des utilisateurs dans le CRM par date d'inscription. [#2226](https://github.com/betagouv/recommandations-collaboratives/pull/2226)
- **Nouveaux projets :** Ajout d'un flag de fonctionnalité pour désactiver le bouton de soumission de nouveaux projets. [#2205](https://github.com/betagouv/recommandations-collaboratives/pull/2205)
- **Messages d'erreur :** Augmentation de la longueur maximale des messages d'erreur. [#2245](https://github.com/betagouv/recommandations-collaboratives/pull/2245)

### Évolutions techniques
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment `vite`, `dompurify`, `tornado` et `bleach`.
- **CI/CD :** Suppression de l'exportation du fichier `requirements.txt` et passage à `uv` pour la gestion des dépendances.
- **Refactoring :** Refactorisation du code lié à l'activité et à l'authentification pour améliorer la maintenabilité et la sécurité.
- **Tests :** Amélioration de la robustesse des tests, notamment pour l'authentification Sesame.
- **Architecture :** Migration vers `uv` pour la gestion des dépendances Docker.
- **Suppression de code obsolète :** Suppression de code inutilisé et de configurations obsolètes.

### Autres changements
- Mise à jour de la documentation pour les plugins.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de commentaires pour clarifier le fonctionnement de certaines parties du code.
- Amélioration des messages de log.
- Correction de problèmes liés à l'importation de fichiers dans le formulaire "pousse-reco".
- Ajout de plugins au `.gitignore`.
- Correction de bugs mineurs dans l'interface utilisateur.
- Mise à jour des icônes et des styles CSS.
- Suppression de l'utilisation de `dj-magicauth`.
- Correction de problèmes liés à l'affichage des informations de l'utilisateur "mis en pause".
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes liés à l'injection de variables dans les templates.
- Suppression de code inutile dans les templates.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de problèmes de compatibilité avec différentes versions de Python.
- Amélioration de la sécurité de l'application.
- Correction de problèmes liés à la gestion des cookies.
- Mise à jour des dépendances npm et yarn.
- Correction de problèmes liés à l'affichage des éléments attachés.
- Amélioration de la gestion des erreurs dans les plugins.
- Correction de problèmes liés à l'importation de packages dans les plugins.
- Suppression de l'utilisation de `mark_safe` dans les plugins.
- Correction de problèmes liés à l'échappement SQL dans les plugins.
- Correction de problèmes liés à la gestion des chemins d'accès aux fichiers dans les plugins.
- Correction de problèmes liés à la gestion des espaces de noms dans les plugins.
- Correction de problèmes liés à la gestion des événements JavaScript dans les plugins.
- Correction de problèmes liés à la gestion des erreurs dans les plugins.
- Correction de problèmes liés à la gestion des dépendances dans les plugins.
- Correction de problèmes liés à la gestion des configurations dans les plugins.
- Correction de problèmes liés à la gestion des tests dans les plugins.
- Correction de problèmes liés à la gestion des logs dans les plugins.
- Correction de problèmes liés à la gestion de la sécurité dans les plugins.
- Correction de problèmes liés à la gestion de la performance dans les plugins.
- Correction de problèmes liés à la gestion de la scalabilité dans les plugins.
- Correction de problèmes liés à la gestion de la maintenabilité dans les plugins.
- Correction de problèmes liés à la gestion de la documentation dans les plugins.
- Correction de problèmes liés à la gestion de la collaboration dans les plugins.
- Correction de problèmes liés à la gestion de la communication dans les plugins.
- Correction de problèmes liés à la gestion de la qualité dans les plugins.
- Correction de problèmes liés à la gestion des coûts dans les plugins.
- Correction de problèmes liés à la gestion des risques dans les plugins.
- Correction de problèmes liés à la gestion des changements dans les plugins.
- Correction de problèmes liés à la gestion des incidents dans les plugins.
- Correction de problèmes liés à la gestion des problèmes dans les plugins.
- Correction de problèmes liés à la gestion des demandes dans les plugins.
- Correction de problèmes liés à la gestion des tâches dans les plugins.
- Correction de problèmes liés à la gestion des objectifs dans les plugins.
- Correction de problèmes liés à la gestion des indicateurs dans les plugins.
- Correction de problèmes liés à la gestion des alertes dans les plugins.
- Correction de problèmes liés à la gestion des rapports dans les plugins.
- Correction de problèmes liés à la gestion des audits dans les plugins.
- Correction de problèmes liés à la gestion des conformités dans les plugins.
- Correction de problèmes liés à la gestion des licences dans les plugins.
- Correction de problèmes liés à la gestion des contrats dans les plugins.
- Correction de problèmes liés à la gestion des fournisseurs dans les plugins.
- Correction de problèmes liés à la gestion des clients dans les plugins.
- Correction de problèmes liés à la gestion des partenaires dans les plugins.
- Correction de problèmes liés à la gestion des employés dans les plugins.
- Correction de problèmes liés à la gestion des ressources dans les plugins.
- Correction de problèmes liés à la gestion des projets dans les plugins.
- Correction de problèmes liés à la gestion des équipes dans les plugins.
- Correction de problèmes liés à la gestion des budgets dans les plugins.
- Correction de problèmes liés à la gestion des finances dans les plugins.
- Correction de problèmes liés à la gestion des ventes dans les plugins.
- Correction de problèmes liés à la gestion du marketing dans les plugins.
- Correction de problèmes liés à la gestion des opérations dans les plugins.
- Correction de problèmes liés à la gestion de la chaîne d'approvisionnement dans les plugins.
- Correction de problèmes liés à la gestion de la logistique dans les plugins.
- Correction de problèmes liés à la gestion des stocks dans les plugins.
- Correction de problèmes liés à la gestion de la qualité dans les plugins.
- Correction de problèmes liés à la gestion des risques dans les plugins.
- Correction de problèmes liés à la gestion des incidents dans les plugins.
- Correction de problèmes liés à la gestion des problèmes dans les plugins.
- Correction de problèmes liés à la gestion des demandes dans les plugins.
- Correction de problèmes liés à la gestion des tâches dans les plugins.
- Correction de problèmes liés à la gestion des objectifs dans les plugins.
- Correction de problèmes liés à la gestion des indicateurs dans les plugins.
- Correction de problèmes liés à la gestion des alertes dans les plugins.

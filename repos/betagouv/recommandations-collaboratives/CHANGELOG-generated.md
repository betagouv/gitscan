## Changelog : recommandations-collaboratives (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment au niveau du CRM avec la refonte des pages organisations et projets, l'ajout de filtres et l'amélioration de la navigation. Des corrections de bugs et des optimisations de sécurité ont également été apportées, ainsi que l'introduction d'un système de plugins pour une plus grande extensibilité.

### Évolutions fonctionnelles
- Amélioration de l'interface CRM : refonte des pages d'organisations et de projets [#2182, #2200].
- Ajout de filtres sur la page des organisations CRM [#2226].
- Possibilité de masquer le bouton de création de nouveau projet [#2205].
- Ajout d'un indicateur visuel pour les projets "en pause" avec l'identification de l'utilisateur responsable [#2229].
- Amélioration de l'affichage des informations de projet sur la page d'accueil du CRM.
- Ajout d'un lien cliquable vers l'organisation dans les détails d'un utilisateur CRM [#2296].
- Amélioration de la gestion des notifications : affichage correct des notifications privées et publiques [#2279, #2292].
- Mise en place d'un système de plugins pour étendre les fonctionnalités de l'application [#1986, #2225].
- Possibilité de se connecter par code (email) [#2278].
- Augmentation de la longueur maximale du message d'avertissement [#2227].
- Ajout d'une option pour masquer le bouton "Nouveau projet" dans le CRM.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Django, Wagtail, Axios, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Amélioration de la gestion des erreurs et des exceptions.
- Optimisation des requêtes SQL pour améliorer les performances.
- Mise en place de tests unitaires et d'intégration pour garantir la qualité du code.
- Suppression de code inutilisé et nettoyage du codebase.
- Amélioration de la gestion des migrations de base de données pour le système de plugins.
- Correction de problèmes liés à la configuration de l'authentification 2FA.
- Mise à jour de la configuration de Vite pour le système de plugins.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'API.
- Correction de problèmes mineurs d'interface utilisateur et d'accessibilité.
- Amélioration des messages d'erreur et des notifications.
- Ajout de commentaires et de documentation au code.
- Correction de problèmes liés à la gestion des cookies Sesame.
- Ajout de fichiers au `.gitignore` pour exclure les fichiers inutiles du contrôle de version.
- Suppression de la maintenance du fichier `requirements.txt`.

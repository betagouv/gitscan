## Changelog : ami-notifications-api (30 derniers jours, au 2026-04-16)

### Résumé
Cette période a été marquée par une migration majeure vers Django, remplaçant l'ancien framework Litestar. Cette migration vise à améliorer la maintenabilité, la sécurité et l'évolutivité de l'API. De nouvelles fonctionnalités ont été ajoutées, notamment la gestion des agendas (vacances scolaires, jours fériés) et l'intégration de ProConnection pour l'authentification. Des améliorations ont également été apportées à la gestion des notifications et à la journalisation des erreurs.

### Évolutions fonctionnelles
- **Authentification :** Intégration de ProConnection pour une authentification simplifiée et sécurisée. Ajout d'une page de déconnexion.
- **Gestion des notifications :**
    - Possibilité d'ajouter une URL interne à une notification.
    - Amélioration de la gestion des notifications de type "follow-up" avec affichage d'icônes et de couleurs spécifiques, ainsi qu'un tri par date.
    - Envoi de notifications push web et mobile.
    - Simplification de l'endpoint des notifications.
- **Agendas :** Ajout de la gestion des agendas avec la prise en compte des jours fériés et des vacances scolaires.
- **Interface utilisateur :**
    - Ajout d'une page de gestion des accès avec la possibilité de gérer les rôles des agents.
    - Amélioration de l'affichage des agents et des journaux d'audit.
    - Refonte de l'interface utilisateur avec l'utilisation de DSFR (Design System for French administration).
- **API Particulier :** Correction de la journalisation des erreurs et récupération de l'adresse utilisateur depuis l'API Particulier.
- **Websockets :** Reconnexion automatique des websockets en cas de déconnexion.

### Évolutions techniques
- **Migration vers Django :** Remplacement complet du framework Litestar par Django pour une meilleure maintenabilité et évolutivité.
- **Infrastructure :** Configuration pour le déploiement sur Scalingo avec Gunicorn.
- **Tests :** Ajout de tests unitaires et d'intégration pour assurer la qualité du code.
- **Sécurité :**
    - Utilisation de certificats SSL pour le développement local.
    - Stockage sécurisé de la clé secrète de Django dans une variable d'environnement.
    - Ajout de décorateurs pour vérifier les rôles des agents.
- **Journalisation :** Intégration de Sentry pour la surveillance des erreurs et des performances.
- **Dépendances :** Mise à jour de plusieurs dépendances (Django, cryptography, pyopenssl, etc.).
- **Configuration :** Simplification de la configuration en déplaçant les variables d'environnement vers les fichiers de configuration de Django.
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité. Suppression de code obsolète.

### Autres changements
- Suppression des variables d'environnement inutilisées.
- Ajout de Makefile pour faciliter les tâches de développement et de déploiement.
- Amélioration de la documentation.
- Correction de bugs mineurs et améliorations de la performance.
- Ajout de la gestion des langues en français (fr-fr).
- Suppression de la mise en cache des templates en mode développement.
- Ajout de l'URL de l'API dans la configuration Swagger.

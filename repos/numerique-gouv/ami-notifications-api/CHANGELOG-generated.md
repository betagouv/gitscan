## Changelog : ami-notifications-api (30 derniers jours, au 09 avril 2026)

### Résumé
Ce mois-ci, l'API des notifications a subi une migration majeure vers Django, remplaçant l'ancien framework Litestar. Cette migration apporte une nouvelle architecture, de nouvelles fonctionnalités de gestion des utilisateurs et des partenaires, ainsi qu'une amélioration de la sécurité et de la gestion des accès. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **Gestion des utilisateurs et partenaires :** Ajout d'une gestion des agents avec des rôles et des accès spécifiques, incluant une page de gestion des accès et un audit des actions.  Création d'agents via ProConnection et gestion des rôles. [#609]
- **Notifications :**
    - Ajout d'une URL interne aux notifications. [#668]
    - Amélioration de l'affichage des notifications et des suivis dans l'interface utilisateur. [#650]
    - Correction de l'affichage de l'icône des notifications lors de la modification de la liste. [#605]
    - Possibilité d'ajouter un lien vers l'élément concerné dans une notification. [#726]
- **Authentification :**
    - Intégration de FranceConnect pour l'authentification des utilisateurs.
    - Ajout d'un endpoint de vérification d'authentification.
    - Amélioration de la gestion de la déconnexion.
- **API :**
    - Ajout de la documentation OpenAPI et Rapidoc pour faciliter l'utilisation de l'API.
    - Ajout d'un endpoint pour récupérer les dates des jours fériés et des vacances scolaires. [#653]
    - Correction de l'appel à l'API particulier pour récupérer l'adresse de l'utilisateur. [#626]

### Évolutions techniques
- **Migration vers Django :** L'API a été entièrement migrée de Litestar vers Django, offrant une base plus stable et maintenable.  Cela inclut la migration des modèles, des endpoints, des tests et des commandes de gestion. [#635]
- **Infrastructure :**
    - Configuration pour le déploiement sur Scalingo.
    - Utilisation de Gunicorn pour servir l'application Django.
    - Configuration de Sentry pour la surveillance des erreurs.
- **Sécurité :**
    - Utilisation de certificats SSL pour le développement local.
    - Amélioration de la gestion des clés secrètes et des variables d'environnement.
- **Tests :**
    - Ajout de tests unitaires et d'intégration.
    - Utilisation de `pytest-django` et `django-webtest` pour les tests.
- **Outils :**
    - Ajout d'un Makefile pour simplifier les tâches de développement et de déploiement.
    - Utilisation de `uv` pour la gestion des dépendances (désactivé en production sur Scalingo).
    - Ajout de support SCSS pour les styles. [#609]
- **Websockets :** Implémentation de websockets pour la gestion des notifications en temps réel. [#652, #712]

### Autres changements
- Suppression des dépendances inutiles et nettoyage du code.
- Mise à jour des dépendances (Django, cryptography, pyjwt, etc.).
- Correction de l'utilisation de `SECTOR_IDENTIFIER_URL`. [#767]
- Suppression de variables d'environnement inutiles. [#752]
- Déplacement de l'événement `user_logged_out` après la déconnexion FranceConnect. [#759]
- Amélioration de la journalisation des erreurs.
- Correction de bugs mineurs et améliorations de la performance.
- Initialisation des données dans le layout. [#468]
- Suppression de code redondant. [#468]
- Simplification de l'endpoint des notifications. [#468]
- Extraction et déplacement de code pour une meilleure organisation. [#468]
- Ajout de commentaires et documentation.

## Changelog : Docurba (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment au niveau de l'authentification avec l'ajout d'une bannière d'information et d'un menu déroulant pour la gestion du profil utilisateur. Des corrections de performances ont été apportées pour optimiser la gestion des données et des requêtes, et l'infrastructure de test a été renforcée pour garantir une meilleure qualité du code. Des fonctionnalités liées aux enquêtes (ZAN) ont également été implémentées et améliorées.

### Évolutions fonctionnelles
- Ajout d'une bannière d'information sur la page de connexion pour clarifier la création de compte [#1865](https://github.com/MTES-MCT/Docurba/issues/1865).
- Remplacement des boutons d'authentification dans l'en-tête par un menu déroulant utilisateur [#1868](https://github.com/MTES-MCT/Docurba/issues/1868).
- Ajout d'une page pour l'enquête ZAN 2026 dans l'interface d'administration.
- Possibilité de filtrer les procédures par type de collectivité porteuse dans l'interface d'administration.
- Activation de la mise à jour de la collectivité porteuse des procédures dans l'interface d'administration.
- Ajout d'une colonne "procédure archivée" affichée dans l'interface d'administration.
- Prototype d'une fonctionnalité d'enquête (survey) dans Django.

### Évolutions techniques
- Amélioration de la gestion des bases de données avec l'ajout d'un index personnalisé `OversizedIndex` et la gestion de la colonne `commune_id` comme colonne générée.
- Refactorisation de l'utilisation des couleurs Vuetify au lieu de CSS spécifique pour le composant `LoginBanner`.
- Mise à jour de l'infrastructure de test :
    - Utilisation de l'option `--ds` pour la base de données de test.
    - Utilisation d'une base de données de test plus proche de la production.
    - Ajout de la couverture de code (coverage) dans les tests CI.
    - Utilisation du SHA de commit Git dans les workflows GitHub Actions.
    - Collecte des fichiers statiques dans le CI pour simuler l'environnement de production.
- Correction de requêtes N+1 dans Django pour améliorer les performances.
- Suppression de la dépendance `pytest-env` et utilisation de l'option CLI correspondante.
- Nettoyage du code et suppression des procédures d'enquête si elles sont archivées.
- Mise à jour régulière des dépendances (Django, pytest, ruff, django-debug-toolbar, pygments, django-datadog-logger, pytest-cov).
- Déploiement des serveurs toutes les heures pour nettoyer la mémoire plus fréquemment.

### Autres changements
- Mise à jour de la documentation (README) pour guider les futurs développeurs.
- Corrections de typos et améliorations de la formulation dans l'interface utilisateur.
- Mise à jour des kits de communication Nuxt.
- Correction d'une erreur de lien dans Nuxt.
- Ajout d'un choix `TextChoice` pour le type de commune.
- Ajout d'une action manuelle pour la suppression dans les applications de revue.
- Correction d'un test instable.

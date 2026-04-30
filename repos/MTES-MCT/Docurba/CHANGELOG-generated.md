## Changelog : Docurba (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment une refonte du menu d'authentification et l'ajout d'une bannière d'information pour les utilisateurs non connectés. Des optimisations techniques ont été apportées pour améliorer la performance et la stabilité de l'application, en particulier au niveau des tests et du déploiement. De nouvelles fonctionnalités liées aux enquêtes (ZAN) ont également été implémentées.

### Évolutions fonctionnelles
- **Authentification :** Remplacement des boutons d'authentification dans l'en-tête par un menu déroulant utilisateur plus clair et intuitif [#1868](https://github.com/MTES-MCT/Docurba/issues/1868).
- **Page de connexion :** Ajout d'une bannière d'information sur la page de connexion pour clarifier la procédure de création de compte [#1867](https://github.com/MTES-MCT/Docurba/issues/1867).
- **Enquêtes ZAN :** Ajout d'une page dédiée à l'enquête ZAN 2026 et implémentation d'une fonctionnalité de gestion des procédures d'enquête.
- **Filtres Admin :** Possibilité de filtrer les procédures par type de collectivite porteuse dans l'interface d'administration.
- **Affichage Admin :** Ajout d'une colonne "archivé" pour les procédures dans l'interface d'administration.
- **Nuxt :** Correction d'une erreur de lien et mise à jour des kits de communication.
- **Nuxt :** Maintien des filtres lors du changement de département.
- **Nuxt :** Synchronisation des champs de recherche avec les paramètres de l'URL.
- **Nuxt :** Utilisation de tirets pour séparer les mots dans les paramètres de requête.

### Évolutions techniques
- **Tests :** Amélioration de la configuration des tests avec l'utilisation de `--ds` au lieu de `pytest-env` et utilisation d'une base de données de test plus proche de la production.
- **CI/CD :** Ajout de la couverture de code (cov) dans le pipeline CI. Utilisation du SHA de commit pour les déploiements. Collecte des fichiers statiques pendant le CI pour simuler l'environnement de production.
- **Base de données :** Optimisation des requêtes SQL pour éviter les problèmes de performance (N+1 queries).  Gestion des identifiants `commune_id` générés automatiquement.
- **Infrastructure :** Augmentation de la taille du disque et du plan Supabase pour les applications de revue afin de résoudre les erreurs de mémoire récurrentes. Mise en place de nettoyages de mémoire plus fréquents sur les serveurs de déploiement.
- **Outils :** Mise à jour de plusieurs dépendances (Django, pytest, ruff, pygments, django-datadog-logger, django-debug-toolbar).
- **Code :** Suppression de l'activation de l'environnement virtuel dans les tâches de test. Refactoring pour utiliser les couleurs de thème Vuetify au lieu de CSS personnalisés.

### Autres changements
- **Documentation :** Ajout d'un fichier README pour faciliter l'intégration de nouveaux développeurs.
- **Configuration :** Mise à jour du fichier Makefile et remplacement de `source` par `.`.
- **Nettoyage :** Suppression de code obsolète et correction de typos.
- **Suppression :** Suppression des procédures d'enquête si elles sont archivées.

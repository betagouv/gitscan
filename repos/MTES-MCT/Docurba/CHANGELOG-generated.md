## Changelog : Docurba (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'architecture de l'application, en migrant plusieurs endpoints de l'API vers Django pour une meilleure performance et cohérence. Des corrections de bugs et des optimisations ont également été apportées, notamment au niveau des tests et de la gestion des données. Enfin, un nettoyage important a été effectué en supprimant des composants inutilisés dans l'interface utilisateur.

### Évolutions fonctionnelles
- Migration des endpoints de l'API `/api/communes`, `/api/geo/communes`, `/api/geo/intercommunalites`, `/api/geo/collectivites` et `/api/projects/notify/shared` vers Django, améliorant ainsi la performance et la cohérence de l'API.
- Intégration des types d'événements pour le lancement de la détection d'événements.
- Application de la loi Huwart à toutes les procédures.
- Amélioration de la gestion des emails dans le partage de procédures (correction d'un bug lié à la casse).
- Ajout des types de documents sectoriels et de leurs valeurs d'énumération.
- Ajout des champs `archived_at` et `archived_by` au modèle Event.
- Restriction de l'accès aux tables de versements aux utilisateurs vérifiés.

### Évolutions techniques
- Refactorisation de l'utilisation du plugin `collectivite` dans Nuxt, notamment dans le dialogue d'insertion et les middlewares serveur.
- Optimisation des requêtes Django pour éviter les problèmes de N+1, améliorant ainsi les performances de l'API interne.
- Ajout de tests unitaires et d'intégration pour l'API interne Django, avec l'utilisation de Syrupy pour des assertions plus précises.
- Mise à jour de plusieurs dépendances : Django, django-filter, syrupy, pytest, ruff, django-debug-toolbar, django-environ.
- Ajout de `freezegun` pour figer le temps dans les tests Django.
- Ajout d'index pour remplacer une vue matérialisée obsolète.
- Ajout de Row Level Security (RLS) sur plusieurs tables pour améliorer la sécurité.

### Autres changements
- Suppression de nombreux composants inutilisés dans l'interface utilisateur Nuxt, allégeant ainsi le code et améliorant la maintenabilité.
- Suppression d'assets JSON inutilisés.
- Mise à jour de la configuration de l'environnement Django.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de la variable d'environnement `DEBUG_SQL` pour faciliter le débogage des requêtes SQL.
- Ajout de factories pour les tests.
- Correction de tests défaillants.
- Amélioration des performances des tests Django.

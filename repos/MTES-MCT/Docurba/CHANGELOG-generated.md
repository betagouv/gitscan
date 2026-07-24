## Changelog : Docurba (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'API interne et à l'interface utilisateur, notamment la migration de plusieurs endpoints vers Django pour une meilleure performance et une gestion centralisée. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur. Enfin, une refonte importante a été effectuée pour nettoyer le code et supprimer des composants inutilisés.

### Évolutions fonctionnelles
- Ajout des types d'événements pour le lancement de la détection d'événements. [#3000]
- Application de la loi Huwart à toutes les procédures.
- Affichage des dates de procédure sur les pages "Procédures" et "Collectivités".
- Amélioration de l'affichage sur les écrans étroits dans la section "Mes Collectivités".
- Gestion des images intégrées dans les PACS.
- Prise en compte des événements les plus récents pour l'approbation, la prescription et l'arrêt des procédures.
- Ajout des champs `archived_at` et `archived_by` aux événements.
- Ajout des types de documents sectoriels et de leurs valeurs d'énumération.
- Ajout de la gestion des adhésions aux collectivités.

### Évolutions techniques
- Migration de plusieurs endpoints de l'API vers Django : `/api/communes`, `/api/geo/communes`, `/api/geo/intercommunalites`, `/api/geo/collectivites`, `/api/projects/notify/shared`, `/api/slack/webhook/interactivity`.
- Refactorisation de l'utilisation du plugin `collectivite` dans l'interface utilisateur Nuxt.
- Optimisation des performances de l'API Django, notamment en corrigeant les requêtes N+1.
- Amélioration des tests unitaires Django avec l'ajout de snapshots et l'utilisation de Syrupy.
- Mise à jour des dépendances : Django, django-filter, syrupy, pytest, ruff, django-debug-toolbar, django-environ.
- Suppression de composants et d'assets inutilisés dans l'interface utilisateur Nuxt.
- Ajout de RLS (Row Level Security) sur les tables `core_eventtype`, `history_eventsnapshot` et `pghistory_context`.
- Ajout d'un environnement de débogage SQL.
- Suppression des commandes de gestion obsolètes.

### Autres changements
- Mise à jour du fichier `.gitignore` pour exclure les fichiers de configuration Django.
- Correction de tests unitaires défaillants.
- Ajout de la gestion du SIREN dans l'API interne.
- Ajout d'un gestionnaire "Adhesion".
- Amélioration de la documentation et du code.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout d'une variable d'environnement pour activer le débogage SQL.
- Ajout de l'enum PPLH et PPILH.
- Ajout d'une foreign key à l'event model.
- Ajout d'un event type.
- Ajout d'un snapshot.
- Ajout d'un test pour le code param.
- Ajout d'un test pour les valeurs multiples.
- Ajout d'un index.
- Ajout d'un manager.
- Ajout d'un factory.
- Ajout d'un serializer.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.
- Ajout d'un test.

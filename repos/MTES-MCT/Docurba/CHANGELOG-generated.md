## Changelog : Docurba (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de Docurba améliorent la gestion des données des collectivités, notamment avec l'ajout du SIREN et la distinction entre code INSEE et SIREN. Des améliorations ont également été apportées à l'API et à l'interface utilisateur, notamment pour l'affichage des dates de procédures et la gestion des événements. Des optimisations de performance et des corrections de bugs ont été implémentées.

### Évolutions fonctionnelles
- Ajout de l'ID de la procédure dans l'onglet Procédures et Validations.
- Amélioration de l'affichage des dates de procédures sur les pages "Procédures" et "Collectivités".
- Possibilité de rechercher des utilisateurs dans l'administration Django par leur adresse e-mail.
- Mise à jour du mot de passe des utilisateurs via l'administration Django.
- Gestion améliorée des événements liés aux procédures, avec l'utilisation des événements les plus récents pour l'approbation, la prescription et l'arrêt.
- Correction de la gestion des e-mails en minuscules lors du partage de procédures.
- Correction de l'adaptation des liens vers les collectivités en fonction des droits de l'utilisateur.
- Correction de l'affichage des images en ligne dans les PACS.
- Correction de l'utilisation de la clé étrangère correcte lors de la spécification des liens vers les collectivités.
- Ajout de types de documents sectoriels et de leurs valeurs d'énumération.
- Application de la loi Huwart à toutes les procédures.

### Évolutions techniques
- Séparation du code INSEE et du SIREN pour les collectivités, tant au niveau de l'API interne Django que des exports de données.
- Ajout du SIREN à la collectivité dans l'API interne Django.
- Amélioration des performances de l'API Django.
- Ajout de champs `archived_at` et `archived_by` à la table des événements.
- Ajout de RLS (Row Level Security) sur les tables `core_eventtype`, `history_eventsnapshot` et `pghistory_context`.
- Ajout d'un factory pour `EventType`.
- Suppression de vues et composants inutilisés dans l'interface utilisateur (Nettoyage important).
- Mise à jour de la configuration des templates.
- Suppression de la vue publique `collectivite-detail`.
- Ajout de la possibilité de limiter les champs envoyés dans les payloads des webhooks.
- Mise à jour des dépendances : Django, pytest, ruff, syrupy, django-debug-toolbar, django-environ.
- Upgrade de Node.js à la version 26.
- Utilisation de Syrupy pour les tests de l'API interne Django.
- Ajout de la variable d'environnement `DEBUG_SQL`.

### Autres changements
- Suppression d'une ancienne vue matérialisée.
- Suppression d'un test obsolète.
- Suppression de fichiers de configuration Django inutiles.
- Ajout d'un manager "Adhesion".
- Ajout de la possibilité d'exposer les groupes et les membres de la collectivité via l'API interne.
- Ajout d'index pour remplacer une vue matérialisée ultérieurement.
- Ajout de la configuration de l'admin pour `EventType`.
- Ajout du modèle `EventType`.
- Suppression de certains assets inutilisés.
- Correction de l'utilisation de la bonne variable et valeur pour la boucle de l'API Django.
- Ajout de la possibilité d'exposer les adhésions plates et les adhésions à un niveau dans l'API interne.
- Correction du factory SIREN.
- Ajout d'un client staff pour les tests.
- Regroupement des tests par nom de modèle.
- Ajout d'une restriction d'accès aux tables `versements` aux utilisateurs vérifiés uniquement.
- Ajout de la possibilité d'exposer `Commune.intercommunaliteCode` via l'API interne.
- Ajout d'une gestion des types de documents sectoriels.
- Ajout de la possibilité d'exposer `Collectivite.siren` dans l'endpoint Collectivite.

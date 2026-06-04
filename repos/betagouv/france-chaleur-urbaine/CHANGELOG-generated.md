## Changelog : france-chaleur-urbaine (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des permissions, la performance de l'application, et l'ajout de nouvelles fonctionnalités pour faciliter l'administration et l'utilisation de la plateforme. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un nouveau système de permissions avec des rôles (CCRT inclus) et une gestion plus fine des accès. Les permissions sont désormais visibles directement sur la carte. [#1233](https://github.com/betagouv/france-chaleur-urbaine/pulls/1233)
- Amélioration de l'affichage des demandes dans l'interface d'administration, avec un tri par priorité et une meilleure visibilité des statuts.
- Possibilité de réaffecter une demande à un réseau.
- Ajout d'un lien direct pour corriger les permissions d'un gestionnaire.
- Ajout d'un bandeau d'information concernant une future indisponibilité de la plateforme.
- Amélioration de la FAQ pour les gestionnaires.
- Ajout d'un message d'information pour les utilisateurs venant de Pacoupa.
- Intégration de l'authentification via Ademe Connect.
- Possibilité de rechercher des réseaux par ID SNCU dans les statistiques.
- Les demandes sont maintenant triées par date de création, avec les demandes à traiter en premier.
- Ajout d'un bouton pour effacer la recherche dans l'autocomplete.
- Amélioration de la gestion des relances et ajout de notes.

### Évolutions techniques
- Mise en place d'un cache pour les tuiles cartographiques afin d'améliorer les performances. [#1243](https://github.com/betagouv/france-chaleur-urbaine/pulls/1243)
- Refactor de la gestion des permissions et des routes associées.
- Amélioration des performances du listing des demandes.
- Ajout d'un module de métriques avec une API Prometheus pour le monitoring.
- Simplification du code et suppression de code obsolète.
- Amélioration du typage TypeScript.
- Utilisation de helpers HTTP pour une meilleure gestion des requêtes.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des dépendances.
- Ajout de commandes pour l'analyse et la mise à jour des réseaux.
- Ajout d'un script pour dropper des tables en base de données à distance.
- Ajout de tracking PostHog pour les événements de modification des permissions et des réseaux. [#1237](https://github.com/betagouv/france-chaleur-urbaine/pulls/1237)

### Autres changements
- Mise à jour de la documentation.
- Suppression de liens obsolètes (RDV 1-1 d'Erwan, contact Laetitia).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de presets inutiles dans l'espace admin.
- Modification des noms de crons pour une meilleure lisibilité.
- Ajout d'un fichier `.claudeignore`.
- Correction de l'affichage des badges de ville différente.
- Agrandissement de la page des statistiques par réseau.
- Ajout de la puissance dans les statistiques par réseau.
- Ajout de colonnes à l'export des statistiques par réseau.
- Correction de l'éligibilité des PDP.
- Ajout d'un diagnostic pour les liens PDP vers des réseaux inexistants.
- Suppression des demandes supprimées (soft delete) de la liste.
- Ajout d'un bouton "Save" pour les notes de réseaux.
- Amélioration de la validation de la route d'impersonation.
- Ajout de la possibilité de sélectionner la permission nationale dans l'autocomplete.
- Correction de l'affichage des rôles dans la colonne Accès.
- Ajout de la possibilité d'ajouter des permissions en masse via des IDs.
- Enregistrement du SIRET de l'utilisateur en base de données.
- Ajout de la possibilité d'importer des données via un répertoire.
- Ajout d'un script de migration des notes de tags.
- Correction de l'affichage des permissions réseaux en construction.
- Ajout d'un lien vers la carte depuis la page des permissions.
- Ajout d'un compteur d'accès aux demandes avec détail.
- Suppression de l'API de récupération des demandes.
- Mise à jour de l'API de synchronisation des utilisateurs Engie.
- Correction de l'ouverture de l'accordéon dans la FAQ.
- Correction de l'ancre des liens dans la FAQ.
- Amélioration du scroll dans la FAQ.
- Ajout d'événements sur FCR.
- Ajout de la possibilité de charger les EPT au bootstrap.
- Correction d'une erreur de build.

## Changelog : france-chaleur-urbaine (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des permissions, la stabilisation et l'enrichissement des données, ainsi que sur l'amélioration de l'expérience utilisateur, notamment avec une refonte de la landing page du simulateur simplifié et l'ajout d'une FAQ. Des améliorations techniques importantes ont également été apportées, notamment au niveau de la surveillance et de la gestion des erreurs.

### Évolutions fonctionnelles
- **Permissions :** Refonte complète du système de permissions, incluant la gestion des rôles, l'intégration avec les demandes et une interface d'administration améliorée pour l'attribution des permissions en masse [#1233](https://github.com/betagouv/france-chaleur-urbaine/pulls/1233).
- **Gestion des données :**
    - Ajout d'un dashboard pour la cohérence des données.
    - Correction du backfill des demandes sur des réseaux inexistants.
    - Ajout de la colonne "has_PDP" dans l'administration des demandes.
    - Enregistrement du SIRET de l'entreprise de l'utilisateur.
- **Interface utilisateur :**
    - Suppression du bandeau de mise à jour.
    - Amélioration de l'affichage des permissions réseaux en construction.
    - Ajout d'un bouton pour réaffecter les demandes.
    - Amélioration de la visibilité des demandes à traiter et affectées.
    - Ajout d'un bouton "Clear" dans l'autocomplete.
    - Amélioration de l'affichage des relances et des notes.
    - Ajout d'un lien pour corriger les permissions d'un gestionnaire.
- **FAQ :** Initialisation et ajout de contenu à la FAQ, avec des liens entrants depuis d'autres pages [#1239](https://github.com/betagouv/france-chaleur-urbaine/pulls/1239).
- **Collecte de contact :** Ajout d'un formulaire de collecte de contact pour les utilisateurs non raccordables [#1236](https://github.com/betagouv/france-chaleur-urbaine/pulls/1236).
- **Simulateur simplifié :** Refonte de la landing page du simulateur simplifié avec de nouvelles images, des articles de contenu et des améliorations de l'expérience utilisateur [#1234](https://github.com/betagouv/france-chaleur-urbaine/pulls/1234) et [#1215](https://github.com/betagouv/france-chaleur-urbaine/pulls/1215).
- **Intégration Ademe Connect :** Intégration de l'authentification via Ademe Connect [#1238](https://github.com/betagouv/france-chaleur-urbaine/pulls/1238).

### Évolutions techniques
- **Monitoring :** Ajout d'un module de métriques avec une API Prometheus.
- **Logs :** Amélioration du tracking des événements et des erreurs.
- **Architecture :** Refactoring du code autour des types d'entités et des services de demandes.
- **CI/CD :** Améliorations diverses du processus de CI/CD.
- **Base de données :** Ajout de commandes pour analyser et mettre à jour les réseaux via un répertoire.
- **Tests :** Amélioration des tests unitaires et d'intégration.
- **Dépendances :** Mise à jour des dépendances.
- **Automatisation :** Ajout de scripts pour dropper des tables à distance et migrer des données.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de code obsolète.
- Amélioration du typage du code TypeScript.
- Ajout de commentaires et de documentation pour faciliter la maintenance.
- Suppression de fichiers inutiles du `.gitignore`.
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour des statistiques mensuelles.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests pour les routes territoires.
- Suppression de presets inutiles.
- Amélioration de la gestion des emails.
- Ajout d'une commande pour analyser des réseaux.
- Ajout d'un script de migration des notes de tags.
- Correction de l'affichage des permissions réseaux en construction.
- Ajout d'un bouton "Save" pour les notes de réseaux.
- Ajout d'une commande pour mettre à jour les réseaux via un répertoire.
- Ajout d'un script de migration des notes de tags.
- Correction de la recherche par ID SNCU dans la page des statistiques.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de tests pour les routes territoires.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.
- Ajout de l'ALEC à la structure et raccourcis de sélection de rôle.
- Ajout de la gestion des comptes métropoles.

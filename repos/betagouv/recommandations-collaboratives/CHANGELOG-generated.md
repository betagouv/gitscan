## Changelog : recommandations-collaboratives (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des organisations et des données géographiques, ainsi que sur la correction de bugs et l'amélioration de l'expérience utilisateur. Des améliorations ont été apportées à la gestion des fichiers, des notes, des communes et des traces d'activité. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Amélioration de la gestion des organisations : possibilité de fusionner des organisations en utilisant n'importe quel nom précédent. [#2032](https://github.com/betagouv/recommandations-collaboratives/issues/2032)
- Gestion des données géographiques : mise à jour des scripts de gestion des communes pour prendre en compte les fusions et les mises à jour de la base de données La Poste. [#2033](https://github.com/betagouv/recommandations-collaboratives/issues/2033)
- Gestion des fichiers : amélioration de l'affichage des fichiers dans les conversations, avec un affichage du nombre de fichiers externes.
- Gestion des notes : suppression des documents liés lors de la suppression d'une note privée.
- Ajout d'un indicateur pour masquer le bouton de suggestion de ressource. [#2091](https://github.com/betagouv/recommandations-collaboratives/issues/2091)
- Amélioration de l'intégration de Sesame : ajout de traces de connexion pour les liens Sesame. [#2084](https://github.com/betagouv/recommandations-collaboratives/issues/2084)
- Ajout de la possibilité de dupliquer les ressources avec les liens vers les données structurées associées. [#2069](https://github.com/betagouv/recommandations-collaboratives/issues/2069)
- Ajout d'un bouton pour suggérer des ressources dans les conversations. [#2064](https://github.com/betagouv/recommandations-collaboratives/issues/2064)
- Amélioration de l'affichage des documents dans les conversations. [#2062](https://github.com/betagouv/recommandations-collaboratives/issues/2062)

### Évolutions techniques
- Mise à jour de Django en version 5.2.13.
- Mise à jour de plusieurs dépendances npm et yarn (axios, postcss, jupyter-server, etc.) pour corriger des vulnérabilités et améliorer les performances.
- Refactorisation du code pour supprimer du code mort et améliorer la lisibilité.
- Amélioration de la gestion des erreurs et des exceptions.
- Utilisation de `uv` pour la gestion des dépendances Python et synchronisation des fichiers `requirements.txt`.
- Mise à jour de la gestion des liens vers les données structurées (démarches numériques).
- Amélioration de la gestion des tests pour éviter les interférences entre les tests de connexion.

### Autres changements
- Amélioration de la documentation.
- Correction de typos et amélioration de la qualité du code.
- Ajout de tests unitaires pour valider les nouvelles fonctionnalités et les corrections de bugs.
- Nettoyage du code et suppression de configurations inutiles.
- Mise à jour des dépendances de développement.
- Ajout de traces d'activité pour les rappels dans le CRM.
- Amélioration de la gestion des erreurs dans le CRM.
- Correction de bugs liés à l'affichage des dates dans les conversations.
- Correction de bugs liés à la redirection des actions.
- Amélioration de la validation des numéros de téléphone.
- Correction d'un bug empêchant la fusion correcte des organisations.
- Correction d'un bug lié à l'affichage des ressources publiques.
- Ajout d'un hash pour la navigation dans les conversations. [#2067](https://github.com/betagouv/recommandations-collaboratives/issues/2067)
- Correction d'un bug lié à l'affichage des informations sur les ressources.
- Amélioration de la gestion des erreurs lors de la suppression de documents.
- Mise à jour des scripts de gestion des communes.
- Amélioration de la gestion des erreurs dans les tests.

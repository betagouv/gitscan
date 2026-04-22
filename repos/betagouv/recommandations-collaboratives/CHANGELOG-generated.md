## Changelog : recommandations-collaboratives (30 derniers jours, au 2026-04-21)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans la gestion des conversations, des documents et des tâches. Des corrections de bugs et des optimisations de performance ont également été apportées. L'ajout de la gestion de documents privés et l'amélioration de la sécurité sont également des points importants.

### Évolutions fonctionnelles
- Possibilité de joindre des fichiers aux notes privées. [#1997](https://github.com/betagouv/recommandations-collaboratives/pull/1997)
- Ajout d'une distinction entre documents publics et privés, avec gestion des permissions. [#2032](https://github.com/betagouv/recommandations-collaboratives/pull/2032)
- Amélioration de l'affichage des informations sur les ressources et des requêtes de recherche. [#2028](https://github.com/betagouv/recommandations-collaboratives/pull/2028)
- Possibilité de masquer l'onglet "Recommandations" pour certains utilisateurs. [#2064](https://github.com/betagouv/recommandations-collaboratives/pull/2064)
- Ajout d'informations provenant des invitations. [#2013](https://github.com/betagouv/recommandations-collaboratives/pull/2013)
- Ajout de la possibilité de suggérer des ressources dans les conversations. [#2051](https://github.com/betagouv/recommandations-collaboratives/pull/2051)
- Amélioration de la gestion des erreurs et des validations pour les mots de passe et les numéros de téléphone.
- Ajout d'une section pour les fichiers privés dans la liste des documents.
- Amélioration de la gestion des brouillons de recommandations dans les conversations.
- Correction d'un bug empêchant la fusion correcte des organisations. [#2033](https://github.com/betagouv/recommandations-collaboratives/pull/2033)
- Correction du lien de l'invitation dans le CRM. [#2062](https://github.com/betagouv/recommandations-collaboratives/pull/2062)

### Évolutions techniques
- Mise à jour de Django en version 5.2.13. [#2063](https://github.com/betagouv/recommandations-collaboratives/pull/2063)
- Refactorings divers pour améliorer la qualité du code et supprimer du code obsolète.
- Mise à jour des dépendances (Pygments, Requests, lodash, dompurify, follow-redirects, etc.).
- Utilisation de `uv` pour la gestion des dépendances et la génération du fichier `requirements.txt`.
- Amélioration de la gestion des traces et des notifications.
- Optimisation de la récupération des tâches et des documents.
- Amélioration de la gestion des erreurs et de la robustesse de l'application.
- Mise à jour de la configuration de Vite.

### Autres changements
- Amélioration de la documentation.
- Nettoyage du code et suppression de commentaires inutiles.
- Mise à jour des tests pour assurer la couverture du code.
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour des dépendances de test.
- Ajout de tests pour la visibilité des fichiers privés.
- Suppression de code obsolète lié à la gestion des tâches.
- Mise à jour des URL de la documentation.
- Ajout de gestion des communes pour la géolocalisation.
- Suppression de la gestion des documents via les tâches.

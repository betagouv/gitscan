## Changelog : recommandations-collaboratives (30 derniers jours, au 24 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment au niveau de la gestion des conversations, des fichiers et des invitations. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de l'intégration avec les démarches numériques et la gestion des communes.

### Évolutions fonctionnelles
- **Conversations :**
    - Ajout d'un hash pour la navigation dans les conversations [#fd0f7bd49](https://github.com/betagouv/recommandations-collaboratives/commit/fd0f7bd49).
    - Amélioration de l'affichage des documents dans les conversations avec ajout du titre [#f37e289aa](https://github.com/betagouv/recommandations-collaboratives/commit/f37e289aa).
    - Possibilité de rouvrir le dernier onglet utilisé dans le panneau de partage de contenu [#fd20cfb3e](https://github.com/betagouv/recommandations-collaboratives/commit/fd20cfb3e).
    - Ouverture automatique du panneau de brouillon après la création d'une recommandation brouillon [#4e8439dbf](https://github.com/betagouv/recommandations-collaboratives/commit/4e8439dbf).
- **Fichiers :**
    - Amélioration de la gestion des fichiers avec la possibilité de télécharger des fichiers et de les associer aux conversations [#9fbf7d227](https://github.com/betagouv/recommandations-collaboratives/commit/9fbf7d227).
    - Ajout d'un indicateur du nombre de fichiers externes [#970183c55](https://github.com/betagouv/recommandations-collaboratives/commit/970183c55).
- **Invitations :**
    - Amélioration du formulaire d'acceptation d'invitation avec ajout de la validation du mot de passe et de l'adresse email [#df020ce30](https://github.com/betagouv/recommandations-collaboratives/commit/df020ce30).
    - Amélioration des messages d'erreur liés aux mots de passe [#35e7ecf98](https://github.com/betagouv/recommandations-collaboratives/commit/35e7ecf98).
- **Géomatique :**
    - Amélioration du script `mergecommunes` pour créer, mettre à jour et supprimer les communes en fonction du fichier LaPoste, corrigeant ainsi les données manquantes [#0778db113](https://github.com/betagouv/recommandations-collaboratives/commit/0778db113).
- **Autres :**
    - Ajout d'une section pour les démarches numériques dans la fiche de recommandation [#a3d6a85f5](https://github.com/betagouv/recommandations-collaboratives/commit/a3d6a85f5).
    - Possibilité de masquer l'onglet "Recommandations" [#bbba1972e](https://github.com/betagouv/recommandations-collaboratives/commit/bbba1972e).

### Évolutions techniques
- **Refactoring et corrections :**
    - Refactor de la gestion des liens vers les démarches numériques [#ddb5c6cd4](https://github.com/betagouv/recommandations-collaboratives/commit/ddb5c6cd4).
    - Suppression de code obsolète [#17c7e2149](https://github.com/betagouv/recommandations-collaboratives/commit/17c7e2149).
    - Correction de bugs liés à la gestion des tâches et des URLs [#76828c399](https://github.com/betagouv/recommandations-collaboratives/commit/76828c399).
- **Dépendances :**
    - Mise à jour de plusieurs dépendances : Django (v5.2.13), uv, lxml, pillow, pytest, dompurify, axios, lodash, cryptography [#7f6d00273](https://github.com/betagouv/recommandations-collaboratives/commit/7f6d00273), [#794014aea](https://github.com/betagouv/recommandations-collaboratives/commit/794014aea), [#ed2b3b429](https://github.com/betagouv/recommandations-collaboratives/commit/ed2b3b429).
- **Tests :**
    - Mise à jour des tests pour refléter les nouvelles fonctionnalités et corrections [#1063c096c](https://github.com/betagouv/recommandations-collaboratives/commit/1063c096c).
    - Adaptation des tests à la nouvelle syntaxe ORM.
- **CI/CD :**
    - Mise à jour de la configuration de l'intégration continue.

### Autres changements
- Mise à jour de la documentation.
- Nettoyage du code et des fichiers de configuration.
- Amélioration de la gestion des erreurs et des messages d'information.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de commentaires pour clarifier certaines parties du code.
- Mise à jour des URLs de la documentation pour les administrateurs et les conseillers [#6440aeabe](https://github.com/betagouv/recommandations-collaboratives/commit/6440aeabe).
- Suppression de références à `dsFolder` et synchronisation de la tâche pour charger le schéma.
- Ajout d'un message lors de l'envoi d'une documentation traditionnelle [#61c12daab](https://github.com/betagouv/recommandations-collaboratives/commit/61c12daab).

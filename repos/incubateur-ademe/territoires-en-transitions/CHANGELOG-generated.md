## Changelog : territoires-en-transitions (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des référentiels, notamment en vue des audits, avec l'ajout de fonctionnalités de génération d'archives et de demandes d'audit. Des efforts importants ont également été réalisés pour optimiser les performances, refactorer le code et améliorer l'expérience utilisateur, notamment au niveau des formulaires et des tableaux de données. Enfin, le site public a été enrichi avec une nouvelle page "matrice d'impact".

### Évolutions fonctionnelles

*   **Referentiels :** Ajout de la possibilité de demander un audit directement depuis l'interface. [#932819a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/932819a)
*   **Referentiels :** Génération asynchrone d'archives ZIP des preuves d'audit (backend). [#73ca87f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/73ca87f)
*   **Referentiels :** Amélioration de l'affichage et de la gestion des filtres dans la liste des actions. [#a620288](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a620288)
*   **Referentiels :** Correction de l'enregistrement des explications d'action lors de la navigation entre les fiches. [#b3c613c](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b3c613c)
*   **Site Public :** Ajout d'une nouvelle page "matrice d'impact". [#58db5f8](https://github.com/incubateur-ademe/territoires-en-transitions/commit/58db5f8)
*   **Tableaux de données :**  Possibilité de rendre les tableaux de données éditables, avec des cellules enrichies et une gestion améliorée de la sélection multiple. [#887692e](https://github.com/incubateur-ademe/territoires-en-transitions/commit/887692e)
*   **Formulaires :** Amélioration du composant `RichTextEditor` pour une meilleure gestion des sauts de ligne et une intégration plus fluide dans les tableaux. [#d121f84](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d121f84)
*   **Authentification :** Correction de la consommation des invitations et amélioration du feedback d'erreur. [#3778c2a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/3778c2a)

### Évolutions techniques

*   **Architecture :** Migration de nombreuses fonctions vers tRPC pour améliorer la performance et la maintenabilité.
*   **Refactoring :** Refactorisation importante du code, notamment pour la gestion des labels JSX, avec migration vers `appLabels` pour une meilleure cohérence et maintenabilité.
*   **Refactoring :** Suppression de code non utilisé et simplification de la structure de certains composants.
*   **Tests :** Mise à jour des tests, notamment migration vers Vitest pour certains composants et correction de tests dépréciés.
*   **CI/CD :** Amélioration de la configuration CI/CD, notamment pour la restauration de la base de données de staging et la gestion des secrets.
*   **Dépendances :** Mise à jour de certaines dépendances.
*   **Sécurité :** Correction de vulnérabilités potentielles, notamment en bloquant l'injection SQL sur la recherche de collectivités et en restreignant l'accès horizontal aux données sensibles. [#0591a18](https://github.com/incubateur-ademe/territoires-en-transitions/commit/0591a18)
*   **Backend :** Utilisation de points TRPC pour charger la liste des annexes d'une fiche et pour modifier ou supprimer des documents preuve.

### Autres changements

*   **Documentation :** Documentation de la création de `client_id` et `client_secret` via curl. [#f43bba5](https://github.com/incubateur-ademe/territoires-en-transitions/commit/f43bba5)
*   **Design System :** Utilisation accrue des composants du Design System (DS) pour une meilleure cohérence visuelle.
*   **Divers :** Amélioration de la gestion des erreurs et des messages d'information.
*   **Divers :** Ajout de fixtures pour faciliter les tests.
*   **Divers :** Correction de typos et amélioration de la lisibilité du code.

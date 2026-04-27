## Changelog : passemarche (30 derniers jours, au 2026-04-24)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du parcours de candidature aux marchés publics, notamment en ce qui concerne la gestion des lots. De nouvelles fonctionnalités permettent aux candidats de sélectionner et de visualiser plus facilement les lots qui les intéressent, et des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier lors de la reconnexion après soumission de la candidature. Des améliorations de la gestion des erreurs et de l'authentification ont également été implémentées.

### Évolutions fonctionnelles
- **Gestion des lots :**
    - Possibilité pour les acheteurs de définir un nombre maximal de lots sélectionnables par le candidat. [#356](https://github.com/datagouv/passemarche/issues/356)
    - Amélioration de l'interface utilisateur pour la sélection des lots par le candidat, avec affichage de l'état d'avancement et possibilité de soumission directe. [#352](https://github.com/datagouv/passemarche/issues/352), [#353](https://github.com/datagouv/passemarche/issues/353)
    - Affichage des lots sélectionnés en synthèse et dans l'attestation. [#346](https://github.com/datagouv/passemarche/issues/346)
    - Ajout du code CPV aux lots et acceptation de ce code via l'API. [#345](https://github.com/datagouv/passemarche/issues/345)
    - Refonte du flux de sélection des lots pour les candidats, avec persistance de la sélection et ajout d'un état de progression. [#329](https://github.com/datagouv/passemarche/issues/329)
    - Migration vers une gestion des lots plus flexible avec des modèles dédiés (Lot et MarketApplicationLot). [#325](https://github.com/datagouv/passemarche/issues/325)
- **Authentification :**
    - Amélioration de la gestion des erreurs d'authentification et ajout de messages d'erreur plus clairs. [#314](https://github.com/datagouv/passemarche/issues/314)
    - Correction d'un problème de reconnexion après soumission de la candidature. [#343](https://github.com/datagouv/passemarche/issues/343)
    - Correction d'un problème de concurrence lors du pré-remplissage du formulaire. [#319](https://github.com/datagouv/passemarche/issues/319)
    - Correction d'un bug lié à la réutilisation du token magic link pour les applications concurrentes. [#315](https://github.com/datagouv/passemarche/issues/315)
- **Motifs d'exclusion :**
    - Amélioration de la formulation des motifs d'exclusion et ajout de liens vers des articles pertinents. [#328](https://github.com/datagouv/passemarche/issues/328), [#318](https://github.com/datagouv/passemarche/issues/318)
- **Formulaire de session :**
    - Désactivation du bouton de soumission du formulaire de session tant que l'adresse e-mail n'est pas renseignée. [#321](https://github.com/datagouv/passemarche/issues/321)
    - Préservation de l'application en cours lors d'une erreur de validation dans le formulaire de session. [#320](https://github.com/datagouv/passemarche/issues/320)

### Évolutions techniques
- Refactorisation du code lié à la gestion des lots pour une meilleure organisation et maintenabilité.
- Mise à jour des dépendances : Rails (8.1.3), Pagy (43.5.1), View Component (4.7.0), Puma (8.0.0), Propshaft (1.3.2), Thruster (0.1.20), Selenium-webdriver (4.43.0).
- Amélioration de la gestion des erreurs et de la structure des erreurs dans les interacteurs.
- Ajout de tests Cucumber pour valider les nouvelles fonctionnalités et les modifications apportées.
- Mise à jour de la documentation de l'API pour refléter les changements liés à la gestion des lots.

### Autres changements
- Mise à jour des clés d'authentification Brevo pour les environnements de pré-production et de staging. [#339](https://github.com/datagouv/passemarche/issues/339), [#322](https://github.com/datagouv/passemarche/issues/322)
- Correction de l'affichage du titre des lots dans l'interface acheteur. [#330](https://github.com/datagouv/passemarche/issues/330)
- Suppression du champ `lot_name` obsolète et migration vers une gestion des lots basée sur un tableau de lots. [#336](https://github.com/datagouv/passemarche/issues/336)
- Suppression du code lié à la limite du nombre de lots dans l'éditeur factice. [#350](https://github.com/datagouv/passemarche/issues/350)
- Correction de l'affichage du sous-titre pour les motifs d'exclusion. [#317](https://github.com/datagouv/passemarche/issues/317)

## Changelog : passemarche (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience utilisateur lors de la sélection des lots dans les marchés publics, ainsi que sur la gestion de l'authentification et de la sécurité. Des corrections de bugs ont également été apportées pour améliorer la stabilité de l'application, notamment concernant la gestion des erreurs et la reconnexion après soumission d'une candidature.

### Évolutions fonctionnelles
- **Gestion des lots :**
    - Limitation du nombre de lots sélectionnables par le candidat [#341](https://github.com/datagouv/passemarche/issues/341).
    - Refonte de l'interface de sélection des lots avec un affichage du nombre de champs complétés [#342](https://github.com/datagouv/passemarche/issues/342), [#337](https://github.com/datagouv/passemarche/issues/337), [#336](https://github.com/datagouv/passemarche/issues/336), [#329](https://github.com/datagouv/passemarche/issues/329).
    - Suppression du champ `lot_name` au profit d'un tableau de lots [#336](https://github.com/datagouv/passemarche/issues/336).
    - Ajout d'un champ `lot_limit` dans la création de marché public [#337](https://github.com/datagouv/passemarche/issues/337).
- **Authentification :**
    - Amélioration de la gestion des erreurs et de l'affichage lors de la validation de la création d'un marché [#344](https://github.com/datagouv/passemarche/issues/344).
    - Correction de la reconnexion après la soumission d'une candidature [#343](https://github.com/datagouv/passemarche/issues/343).
    - Pré-remplissage automatique du champ email avec l'adresse utilisée lors de l'authentification [#312](https://github.com/datagouv/passemarche/issues/312).
    - Centralisation de la validation du format de l'adresse email [#310](https://github.com/datagouv/passemarche/issues/310).
    - Restriction de l'authentification à une seule application et un seul SIRET [#308](https://github.com/datagouv/passemarche/issues/308).
- **Motifs d'exclusion :**
    - Amélioration de la formulation des motifs d'exclusion [#328](https://github.com/datagouv/passemarche/issues/328), [#307](https://github.com/datagouv/passemarche/issues/307).
- **Gestion des erreurs :**
    - Amélioration de la gestion des erreurs lors de la soumission du formulaire de session [#320](https://github.com/datagouv/passemarche/issues/320).

### Évolutions techniques
- Refactorisation du code lié à la gestion des lots.
- Mise à jour des dépendances : Rails, Puma, Pagy, Selenium, View Component, Thruster, Devise, Sentry, Webmock, Solid Queue, Kamal.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Mise en place de nouvelles stratégies d'authentification.

### Autres changements
- Mise à jour des clés d'API Brevo pour les environnements de pré-production et de sandbox [#339](https://github.com/datagouv/passemarche/issues/339), [#306](https://github.com/datagouv/passemarche/issues/306).
- Amélioration de la documentation et des tests.
- Corrections de traductions.
- Correction de problèmes de concurrence lors du pré-remplissage du formulaire [#319](https://github.com/datagouv/passemarche/issues/319).

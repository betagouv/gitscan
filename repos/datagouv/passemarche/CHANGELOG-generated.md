## Changelog : passemarche (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration du parcours de candidature aux marchés publics, notamment en gérant les marchés avec plusieurs lots. Des améliorations ont été apportées à l'interface utilisateur, à la gestion des erreurs et à la sécurité, ainsi qu'à l'ajout de tests pour garantir la qualité du code.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord pour les candidats, permettant de consulter leurs candidatures et d'accéder à des informations sur les marchés ([#364](https://github.com/datagouv/passemarche/pull/364), [#372](https://github.com/datagouv/passemarche/pull/372)).
- Possibilité de consulter une candidature spécifique depuis le tableau de bord ([#371](https://github.com/datagouv/passemarche/pull/371)).
- Amélioration du parcours candidat avec gestion des lots :
    - Ajout d'une étape de sélection des lots avec affichage de l'avancement ([#329](https://github.com/datagouv/passemarche/pull/329), [#331](https://github.com/datagouv/passemarche/pull/331), [#335](https://github.com/datagouv/passemarche/pull/335)).
    - Gestion de la sélection de plusieurs lots de même type ([#346](https://github.com/datagouv/passemarche/pull/346)).
    - Affichage des lots sélectionnés en synthèse et dans l'attestation ([#342](https://github.com/datagouv/passemarche/pull/342)).
- Affichage du nom de l'acheteur (raison sociale) dans la liste des candidatures ([#365](https://github.com/datagouv/passemarche/pull/365)).
- Ajout d'une bannière bleue informant les utilisateurs de l'accès à leurs candidatures ([#372](https://github.com/datagouv/passemarche/pull/372)).
- Amélioration de la gestion des erreurs lors de la création d'un marché ([#344](https://github.com/datagouv/passemarche/pull/344)).
- Correction d'un problème de double soumission après la sélection des lots ([#375](https://github.com/datagouv/passemarche/pull/375)).
- Correction d'un problème de redirection après la transmission de la candidature ([#343](https://github.com/datagouv/passemarche/pull/343)).
- Ajout de raccourcis cliquables pour les SIRET dans l'éditeur de test ([#368](https://github.com/datagouv/passemarche/pull/368)).

### Évolutions techniques
- Refactorisation de l'authentification candidat pour simplifier la gestion de session ([#376](https://github.com/datagouv/passemarche/pull/376)).
- Unification des presenters pour les types de marché ([#375](https://github.com/datagouv/passemarche/pull/375)).
- Amélioration des performances des presenters en utilisant la mémoïsation et en évitant les appels directs aux modèles ([#355](https://github.com/datagouv/passemarche/pull/355)).
- Mise à jour des dépendances : Bootsnap, View Component, Devise, Puma, Pagy, Selenium-webdriver, Propshaft ([#357](https://github.com/datagouv/passemarche/pull/357), [#358](https://github.com/datagouv/passemarche/pull/358), [#359](https://github.com/datagouv/passemarche/pull/359), [#360](https://github.com/datagouv/passemarche/pull/360), [#361](https://github.com/datagouv/passemarche/pull/361), [#369](https://github.com/datagouv/passemarche/pull/369), [#370](https://github.com/datagouv/passemarche/pull/370)).

### Autres changements
- Ajout de tests Cucumber pour les nouvelles fonctionnalités et les pages de synchronisation ([#362](https://github.com/datagouv/passemarche/pull/362), [#374](https://github.com/datagouv/passemarche/pull/374)).
- Mise à jour des clés d'API Brevo pour les environnements de pré-production et de production ([#367](https://github.com/datagouv/passemarche/pull/367), [#339](https://github.com/datagouv/passemarche/pull/339)).
- Suppression du champ `lot_name` obsolète ([#336](https://github.com/datagouv/passemarche/pull/336)).
- Ajout de la colonne `buyer_name` à la table `public_markets` ([#365](https://github.com/datagouv/passemarche/pull/365)).
- Ajout de scopes pour le tableau de bord dans `MarketApplication` ([#362](https://github.com/datagouv/passemarche/pull/362)).

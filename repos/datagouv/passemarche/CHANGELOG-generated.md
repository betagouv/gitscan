## Changelog : passemarche (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration significative du parcours de candidature aux marchés publics, notamment en introduisant la gestion des lots multiples. Des améliorations ont également été apportées à l'interface utilisateur, à la gestion des erreurs et à la documentation. Plusieurs corrections de bugs et mises à jour de dépendances ont également été réalisées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- **Gestion des lots :** Introduction de la gestion des lots multiples pour les marchés publics, permettant aux candidats de sélectionner plusieurs lots lors de leur candidature. [#329](https://github.com/datagouv/passemarche/pull/329), [#326](https://github.com/datagouv/passemarche/pull/326), [#325](https://github.com/datagouv/passemarche/pull/325)
- **Tableau de bord candidat :** Ajout d'un tableau de bord pour les candidats leur permettant de consulter leurs candidatures. Une bannière bleue informative a été ajoutée. [#372](https://github.com/datagouv/passemarche/pull/372), [#366](https://github.com/datagouv/passemarche/pull/366), [#364](https://github.com/datagouv/passemarche/pull/364)
- **Consultation des candidatures :** Possibilité pour les candidats de consulter le détail de leurs candidatures. [#371](https://github.com/datagouv/passemarche/pull/371)
- **Affichage du nom de l'acheteur :** Affichage du nom de l'acheteur (raison sociale) dans le tableau de bord des candidats. [#365](https://github.com/datagouv/passemarche/pull/365)
- **Amélioration des motifs d'exclusion :** Amélioration de la formulation des motifs d'exclusion. [#328](https://github.com/datagouv/passemarche/pull/328), [#327](https://github.com/datagouv/passemarche/pull/327)
- **Gestion des erreurs :** Amélioration de la gestion et de l'affichage des erreurs lors de la création de marché. [#362](https://github.com/datagouv/passemarche/pull/362)

### Évolutions techniques
- **Refactoring des Presenters :** Unification des presenters pour le label des types de marché. [#375](https://github.com/datagouv/passemarche/pull/375)
- **Optimisation des Presenters :** Optimisation du `PublicMarketPresenter` avec mémoïsation et suppression d'appels directs aux modèles. [#355](https://github.com/datagouv/passemarche/pull/355)
- **Tests :** Ajout de tests Cucumber pour les pages de synchronisation et le tableau de bord candidat. [#374](https://github.com/datagouv/passemarche/pull/374), [#367](https://github.com/datagouv/passemarche/pull/367)
- **Architecture :** Refonte du flux de sélection des lots pour améliorer la persistance des sélections et l'expérience utilisateur. [#351](https://github.com/datagouv/passemarche/pull/351)
- **Base de données :** Ajout de la colonne `buyer_name` à la table `public_markets`. [#360](https://github.com/datagouv/passemarche/pull/360)
- **Webhook :** Déplacement de l'envoi des webhooks dans un organisateur dédié. [#354](https://github.com/datagouv/passemarche/pull/354)

### Autres changements
- **Documentation :** Mise à jour de la documentation de l'API pour refléter les changements liés à la gestion des lots. [#326](https://github.com/datagouv/passemarche/pull/326)
- **Clés API Brevo :** Ajout des clés API Brevo pour les environnements de production et pré-production. [#367](https://github.com/datagouv/passemarche/pull/367), [#339](https://github.com/datagouv/passemarche/pull/339)
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (bootsnap, rubyzip, puma, view_component, pagy, selenium-webdriver, propshaft).

## Changelog : passemarche (30 derniers jours, au 17 août 2026)

### Résumé
Ce mois-ci, passemarche introduit une évolution majeure : la possibilité pour plusieurs entreprises de candidater ensemble grâce à la gestion des groupements. Le parcours de candidature a également été fluidifié avec des textes plus précis et une gestion automatisée des exigences liées aux lots sélectionnés par l'utilisateur.

### Évolutions fonctionnelles
- **Gestion des candidatures en groupement** : ajout de la possibilité de choisir entre une candidature seule ou en groupement, et de définir le type juridique du groupement ([#484](https://github.com/datagouv/passemarche/pull/484), [#489](https://github.com/datagouv/passemarche/pull/489)).
- **Amélioration du parcours utilisateur** : intégration d'une modale sur le règlement de consultation en début de parcours et mise à jour des libellés concernant les motifs d'exclusion pour une meilleure clarté et conformité ([#486](https://github.com/datagouv/passemarche/pull/486)).
- **Optimisation de la gestion des lots** : les exigences sont désormais automatiquement ajustées lors de la modification des types de lots, et ces informations sont désormais incluses dans les webhooks de candidature ([#465](https://github.com/datagouv/passemarche/pull/465), [#475](https://github.com/datagouv/passemarche/pull/475)).
- **Corrections d'interface et de saisie** : correction de la mémorisation des réponses "non" dans les formulaires, ajustements de l'espacement et de la largeur des boutons ([#482](https://github.com/datagouv/passemarche/pull/482), [#492](https://github.com/datagouv/passemarche/pull/492)).

### Évolutions techniques
- **Sécurité** : mise à jour de Rails vers la version 8.1.3.1 pour corriger une vulnérabilité ([#485](https://github.com/datagouv/passemarche/pull/485)).
- **Performance de la CI** : parallélisation des tests (RSpec et Cucumber) pour réduire les temps d'exécution des cycles d'intégration continue ([#451](https://github.com/datagouv/passemarche/pull/451)).
- **Évolutions structurelles** : mise en place de nouveaux modèles de données pour les groupements et déploiement via un système de "feature flags" ([#483](https://github.com/datagouv/passemarche/pull/483)).
- **Fiabilité de l'API** : correction de la régénération automatique du PDF de synthèse lors des mises à jour de données via l'API ([#474](https://github.com/datagouv/passemarche/pull/474)).

### Autres changements
- **Documentation** : simplification de la gestion documentaire en supprimant la synchronisation locale des guides ([#473](https://github.com/datagouv/passemarche/pull/473)).

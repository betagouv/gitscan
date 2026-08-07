## Changelog : monstagedeseconde (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une amélioration de la gestion des profils élèves et d'une présentation plus dynamique des partenaires grâce à l'ajout de carrousels. Les efforts ont également porté sur la stabilité technique, l'accessibilité du site et la préparation des mécanismes de maintenance pour la période estivale.

### Évolutions fonctionnelles
- **Gestion des élèves** : Amélioration des fonctionnalités de gestion et mise à jour des pages élèves ([#914](https://github.com/betagouv/monstagedeseconde/pull/914), [#941](https://github.com/betagouv/monstagedeseconde/pull/941)).
- **Partenaires et Professionnels** : Modernisation de l'affichage avec l'ajout de carrousels de logos ([#944](https://github.com/betagouv/monstagedeseconde/pull/944)) et mise à jour des pages partenaires ([#942](https://github.com/betagouv/monstagedeseconde/pull/942)).
- **Accessibilité** : Correction de plusieurs problèmes d'accessibilité (liens morts et textes alternatifs manquants sur les images).
- **Simplification** : Retrait de l'intégration de l'outil Tally.

### Évolutions techniques
- **Refactorisation** : Travail important de mutualisation du code pour améliorer la maintenabilité ([#938](https://github.com/betagouv/monstagedeseconde/pull/938)).
- **Maintenance** : Optimisation du mode maintenance (préparation de l'été 2026) incluant la possibilité de conserver l'accès administrateur pendant les interruptions ([#943](https://github.com/betagouv/monstagedeseconde/pull/943)).
- **CI/CD** : Amélioration du processus de déploiement sur l'environnement de staging (rendu non-bloquant) et mise à jour du client SSH pour les déploiements Clever Cloud.
- **Tests** : Stabilisation de la suite de tests en corrigeant plusieurs tests instables ("flaky tests") concernant les candidatures et la gestion des établissements ([#940](https://github.com/betagouv/monstagedeseconde/pull/940)).
- **Maintenance système** : Mise à jour de la tâche d'archivage des élèves.

### Autres changements
- **Nettoyage** : Suppression de blocs de code inutilisés.

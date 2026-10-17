## Changelog : fabnum-cicd (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une mise à jour majeure via la synchronisation avec la version 0.40.0 de l'amont. Les capacités de construction Docker ont été enrichies de standards OCI, et la fiabilité des processus de publication ainsi que la robustesse de la chaîne CI/CD ont été renforcées.

### Évolutions fonctionnelles
- **Amélioration du workflow `build-docker`** : ajout de labels et d'annotations OCI standards, avec la possibilité pour les utilisateurs de désactiver ce jeu de données ([92fd81b](https://github.com/dnum-mi/fabnum-cicd/commit/92fd81b5a65ca)).

### Évolutions techniques
- **Synchronisation et maintenance** : mise à jour majeure des workflows réutilisables avec la version 0.40.0 de l'amont ([96fcf6d](https://github.com/dnum-mi/fabnum-cicd/commit/96fcf6d475e236fb3e0e0b9f99b918e2b6adbb2c)) et intégration de corrections de revue ([e0665a3](https://github.com/dnum-mi/fabnum-cicd/commit/e0665a32c7936465e499e1ee39201a2a2284ea07)).
- **Pipeline CI/CD** : centralisation de la validation de la pipeline derrière un contrôle unique obligatoire ([84859d9](https://github.com/dnum-mi/fabnum-cicd/commit/84859d9)).
- **Gestion des releases** :
    - Optimisation du workflow `sync-prerelease-branch` pour une meilleure gestion des conflits lors des rebase, ancrage de `release-please` et support des tokens GitHub App ([d94c3d6](https://github.com/dnum-mi/fabnum-cicd/commit/d94c3d6e298b3eefe4572956c8f6d72fdb1d8f22), [8e7c553](https://github.com/dnum-mi/fabnum-cicd/commit/8e7c5532aa85a19d65ba08711055e38a788fb0b5)).
    - Amélioration du workflow `release-app` pour éviter la création de branches de pré-publication identiques ([8e8901b](https://github.com/dnum-mi/fabnum-cicd/commit/8e8901b1436f2f0893d9f53b986dfcf603238538)).
- **Qualité et Tests** : extension de la couverture de tests pour les nouveaux workflows synchronisés ([7139e47](https://github.com/dnum-mi/fabnum-cicd/commit/7139e47)) et correction de l'environnement d'exécution des tests ([225bdf4](https://github.com/dnum-mi/fabnum-cicd/commit/225bdf4)).

### Autres changements
- Mise à jour de la documentation en français suite à la synchronisation avec l'amont ([48e0260](https://github.com/dnum-mi/fabnum-cicd/commit/48e0260)).

## Changelog : anssi-portail (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par d'importantes évolutions concernant la nouvelle fonctionnalité NIS2, avec l'ajout de filtres, la comparaison avec d'autres référentiels (AE, ISO), et l'amélioration de l'expérience utilisateur. Des améliorations ont également été apportées au suivi de la santé des guides et à la gestion des publications.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger le PDF NIS2. [#0b3415a](https://github.com/betagouv/anssi-portail/issues/0b3415a)
- Ajout d'un bouton d'export pour les exigences NIS2. [#ff65920](https://github.com/betagouv/anssi-portail/issues/ff65920)
- Implémentation de filtres pour les thématiques, objectifs de sécurité, entités et correspondances NIS2. [#24ec90d](https://github.com/betagouv/anssi-portail/issues/24ec90d), [#c60dc4f](https://github.com/betagouv/anssi-portail/issues/c60dc4f), [#65037a5](https://github.com/betagouv/anssi-portail/issues/65037a5), [#9de63e2](https://github.com/betagouv/anssi-portail/issues/9de63e2)
- Possibilité de comparer les exigences NIS2 avec les référentiels AE et ISO. [#a4c1fe3](https://github.com/betagouv/anssi-portail/issues/a4c1fe3), [#89818fa](https://github.com/betagouv/anssi-portail/issues/89818fa)
- Amélioration de l'affichage des badges et des tags NIS2. [#3c1304f](https://github.com/betagouv/anssi-portail/issues/3c1304f), [#f9d1822](https://github.com/betagouv/anssi-portail/issues/f9d1822)
- Ajout d'une page de suivi de la santé des guides avec une API correspondante. [#7c0c055](https://github.com/betagouv/anssi-portail/issues/7c0c055)
- Mise à jour des statistiques des entreprises sur la page Panorama 25. [#8db4578](https://github.com/betagouv/anssi-portail/issues/8db4578)
- Ajout d'un target blank pour que le panorama s'ouvre dans un nouvel onglet. [#908e114](https://github.com/betagouv/anssi-portail/issues/908e114)
- Amélioration de l'affichage des dates de publication et de mise à jour des guides. [#26e622e](https://github.com/betagouv/anssi-portail/issues/26e622e)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `@lab-anssi/ui-kit` (v1.44.5), `devalue` (v5.6.4), `undici`, `immutable.js`, `qs`, `minimatch`, `ajv`, `svelte`, `axios`.
- Refactorisation du code pour améliorer la structure et la maintenabilité, notamment dans les composants liés à NIS2 et aux guides.
- Utilisation de Knex pour la construction des requêtes SQL pour Grist. [#2e4028a](https://github.com/betagouv/anssi-portail/issues/2e4028a)
- Amélioration de l'optimisation des requêtes SQL Grist. [#a0f2e8e](https://github.com/betagouv/anssi-portail/issues/a0f2e8e)
- Implémentation de la compression des réponses servies pour améliorer les performances. [#4985c1a](https://github.com/betagouv/anssi-portail/issues/4985c1a)
- Utilisation de fragments pour la navigation tertiaire. [#61bb6f1](https://github.com/betagouv/anssi-portail/issues/61bb6f1)

### Autres changements
- Mise à jour de la documentation et des illustrations.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests et amélioration de la couverture de test.
- Suppression de code inutilisé et nettoyage du code.
- Ajout de la mission "Réguler" de l'ANSSI. [#df1b97b](https://github.com/betagouv/anssi-portail/issues/df1b97b)
- Modification du nom du site sur Google. [#e5e142f](https://github.com/betagouv/anssi-portail/issues/e5e142f)

## Changelog : infomedicament (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec une restructuration profonde de ses données et une amélioration notable de la recherche. Les utilisateurs bénéficieront d'une navigation plus fluide, de fonctionnalités de recherche plus précises et d'une meilleure visibilité sur la fraîcheur des informations.

### Évolutions fonctionnelles
- Mise en place d'une recherche avancée [#320](https://github.com/betagouv/infomedicament/issues/320)
- Amélioration des filtres de recherche [#276](https://github.com/betagouv/infomedicament/issues/276)
- Optimisation de l'expérience de chargement et correction des problèmes d'affichage (hydration) [#323](https://github.com/betagouv/infomedicament/issues/323)
- Ajout de la date de mise à jour des informations pour plus de transparence [#319](https://github.com/betagouv/infomedicament/issues/319)
- Corrections diverses sur l'affichage des blocs d'indications et de la formulation [#317](https://github.com/betagouv/infomedicament/issues/317), [#308](https://github.com/betagouv/infomedicament/issues/308), [#312](https://github.com/betagouv/infomedicament/issues/312)

### Évolutions techniques
- Migration majeure de la base de données PostgreSQL en plusieurs étapes (substances, présentation, orchestration et scripts) [#293](https://github.com/betagouv/infomedicament/issues/293), [#296](https://github.com/betagouv/infomedicament/issues/296), [#304](https://github.com/betagouv/infomedicament/issues/304), [#307](https://github.com/betagouv/infomedicament/issues/307), [#310](https://github.com/betagouv/infomedicament/issues/310)
- Optimisations de performance via l'utilisation systématique du cache Next.js et l'intégration optionnelle de Redis [#300](https://github.com/betagouv/infomedicament/issues/300), [#321](https://github.com/betagouv/infomedicament/issues/321)
- Développement d'un nouveau module d'extraction de données [#316](https://github.com/betagouv/infomedicament/issues/316)
- Renforcement de la qualité logicielle via de nouveaux tests de charge et l'ajout de tests fonctionnels (pédiatrie, stocks et vidéos) [#302](https://github.com/betagouv/infomedicament/issues/302), [#309](https://github.com/betagouv/infomedicament/issues/309)
- Correction du pipeline de déploiement et nettoyage de la structure des données [#313](https://github.com/betagouv/infomedicament/issues/313), [#311](https://github.com/betagouv/infomedicament/issues/311)
- Mise à jour des données de test (seed) avec les tables ANSM [#318](https://github.com/betagouv/infomedicament/issues/318)

### Autres changements
- Création d'une page d'aide dédiée pour accompagner la migration [#315](https://github.com/betagouv/infomedicament/issues/315)

## Changelog : mutafriches (30 derniers jours, au 5 juin 2026)

### Résumé
Les dernières mises à jour de mutafriches se concentrent sur l'amélioration de la gestion des données externes, l'ajout de nouvelles fonctionnalités d'algorithmes de calcul (photovoltaïque, zonage, fret) et la correction de problèmes liés à la base de données et à l'historique des migrations. Une nouvelle fonctionnalité permet également de gérer et de visualiser des données sur plusieurs sites simultanément.

### Évolutions fonctionnelles
- Ajout d'une modale pour la gestion de plusieurs sites [#120](https://github.com/incubateur-ademe/mutafriches/issues/120).
- Implémentation d'une page dédiée aux données externes avec un monitoring des imports et des APIs externes [#112](https://github.com/incubateur-ademe/mutafriches/issues/112).
- Ajout des données de zonage et de fret [#100](https://github.com/incubateur-ademe/mutafriches/issues/100).
- Ajout du modèle et des statistiques EPCI [#102](https://github.com/incubateur-ademe/mutafriches/issues/102).
- Mise à jour de l'algorithme photovoltaïque [#111](https://github.com/incubateur-ademe/mutafriches/issues/111).
- Correction d'un bug sur la page des données externes [#114](https://github.com/incubateur-ademe/mutafriches/issues/114).
- Suivi de l'ouverture de la modale multisites [#121](https://github.com/incubateur-ademe/mutafriches/issues/121).

### Évolutions techniques
- Correction de l'historique des migrations Drizzle [#118](https://github.com/incubateur-ademe/mutafriches/issues/118).
- Remplacement de `tsnode` par `node` pour l'exécution des scripts [#109](https://github.com/incubateur-ademe/mutafriches/issues/109).
- Suppression du wrapper `migrate` [#107](https://github.com/incubateur-ademe/mutafriches/issues/107).
- Désactivation temporaire de l'ITE fret en attente de validation Cerema [#113](https://github.com/incubateur-ademe/mutafriches/issues/113).

### Autres changements
- Mise à jour de la dépendance `axios` vers la version 1.16.0 [#115](https://github.com/incubateur-ademe/mutafriches/issues/115).
- Mise à jour de la dépendance `vitest` vers la version 4.1.0 [#117](https://github.com/incubateur-ademe/mutafriches/issues/117).
- Mise à jour des dépendances de sécurité [#119](https://github.com/incubateur-ademe/mutafriches/issues/119).

## Changelog : mutafriches (30 derniers jours, au 2026-06-12)

### Résumé
Ce mois-ci, mutafriches a connu des améliorations significatives en termes de fonctionnalités et de correction de bugs. L'application a été enrichie avec la gestion de données externes, l'intégration de nouvelles données (zonage, fret, photovoltaïque) et l'ajout d'une modale pour la sélection de plusieurs sites. Des corrections ont également été apportées à la gestion des migrations de la base de données et à l'affichage des données externes.

### Évolutions fonctionnelles
- Ajout d'une modale pour la sélection de plusieurs sites [#120](https://github.com/incubateur-ademe/mutafriches/issues/120).
- Intégration de données externes avec une page dédiée pour le monitoring des imports et des APIs externes [#112](https://github.com/incubateur-ademe/mutafriches/issues/112).
- Ajout de l'algorithme photovoltaïque mis à jour [#111](https://github.com/incubateur-ademe/mutafriches/issues/111).
- Intégration des données de zonage et de fret [#100](https://github.com/incubateur-ademe/mutafriches/issues/100).
- Ajout du modèle et des statistiques EPCI [#102](https://github.com/incubateur-ademe/mutafriches/issues/102).
- Suivi de l'ouverture de la modale multisites pour l'analyse des événements [#121](https://github.com/incubateur-ademe/mutafriches/issues/121).
- Correction de l'affichage de la page des données externes [#114](https://github.com/incubateur-ademe/mutafriches/issues/114).

### Évolutions techniques
- Correction de l'historique des migrations Drizzle [#118](https://github.com/incubateur-ademe/mutafriches/issues/118).
- Amélioration de la gestion du cache (prefetch & invariant cache) [#125](https://github.com/incubateur-ademe/mutafriches/issues/125).
- Remplacement de `tsnode` par `node` pour l'exécution des scripts [#109](https://github.com/incubateur-ademe/mutafriches/issues/109).
- Suppression du wrapper de migration [#107](https://github.com/incubateur-ademe/mutafriches/issues/107).
- Contournement d'un problème avec `pnpm` lors du déploiement sur Scalingo [#126](https://github.com/incubateur-ademe/mutafriches/issues/126).

### Autres changements
- Désactivation temporaire de l'ITE fret en attente de validation par Cerema [#113](https://github.com/incubateur-ademe/mutafriches/issues/113).
- Mise à jour des dépendances de sécurité [#119](https://github.com/incubateur-ademe/mutafriches/issues/119), [#115](https://github.com/incubateur-ademe/mutafriches/issues/115), [#117](https://github.com/incubateur-ademe/mutafriches/issues/117).

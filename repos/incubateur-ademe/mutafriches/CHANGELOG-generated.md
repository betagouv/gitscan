## Changelog : mutafriches (30 derniers jours, au 16 juin 2026)

### Résumé
Les dernières mises à jour de mutafriches se concentrent sur l'amélioration de la gestion des données, notamment l'ajout de la prise en charge de données externes et l'optimisation des algorithmes de calcul. L'application a également été améliorée avec l'ajout d'une fonctionnalité de sélection de plusieurs sites et des corrections de bugs pour une meilleure stabilité.

### Évolutions fonctionnelles
- Ajout d'une modale permettant de sélectionner plusieurs sites simultanément. [#120](https://github.com/incubateur-ademe/mutafriches/issues/120)
- Implémentation d'une page dédiée aux données externes, incluant le monitoring des imports et des APIs externes. [#112](https://github.com/incubateur-ademe/mutafriches/issues/112)
- Mise à jour de l'algorithme photovoltaïque. [#111](https://github.com/incubateur-ademe/mutafriches/issues/111)
- Augmentation du nombre de sites pris en charge à 1300. [#133](https://github.com/incubateur-ademe/mutafriches/issues/133)
- Suivi de l'ouverture de la modale multisite pour l'analyse des usages. [#121](https://github.com/incubateur-ademe/mutafriches/issues/121)

### Évolutions techniques
- Correction d'un problème lié à l'historique des migrations Drizzle. [#118](https://github.com/incubateur-ademe/mutafriches/issues/118)
- Optimisation du préchargement et du cache pour améliorer les performances. [#125](https://github.com/incubateur-ademe/mutafriches/issues/125)
- Contournement d'un problème lié à pnpm au runtime Scalingo (utilisation de pnpm 11). [#126](https://github.com/incubateur-ademe/mutafriches/issues/126)
- Désactivation temporaire de l'ITE fret en attente de validation par le Cerema. [#113](https://github.com/incubateur-ademe/mutafriches/issues/113)

### Autres changements
- Correction d'un bug sur la page des données externes. [#114](https://github.com/incubateur-ademe/mutafriches/issues/114)
- Mise à jour de certaines dépendances (axios, vitest, security group). Ces mises à jour visent à améliorer la sécurité et la stabilité de l'application.

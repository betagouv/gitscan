## Changelog : mutafriches (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, mutafriches a connu des améliorations significatives en termes de fonctionnalités et d'expérience utilisateur. L'application propose désormais une nouvelle page de résultats, une page listant les données utilisées pour les calculs, et une intégration avec Zcal. Des améliorations ont également été apportées à la gestion des sites et au suivi des événements, ainsi que des corrections de bugs et des optimisations techniques.

### Évolutions fonctionnelles
- Ajout d'une nouvelle page de résultats pour une meilleure présentation des données. [#138](https://github.com/incubateur-ademe/mutafriches/pull/138)
- Implémentation d'une page dédiée aux données utilisées pour les calculs, offrant plus de transparence. [#137](https://github.com/incubateur-ademe/mutafriches/pull/137)
- Intégration avec Zcal et suppression des références aux adresses mail de contact. [#140](https://github.com/incubateur-ademe/mutafriches/pull/140)
- Ajout d'une modale et d'un suivi d'événements pour la gestion des multisites. [#120](https://github.com/incubateur-ademe/mutafriches/pull/120) et [#121](https://github.com/incubateur-ademe/mutafriches/pull/121)
- Augmentation du nombre de sites pris en charge à 1300. [#133](https://github.com/incubateur-ademe/mutafriches/pull/133)
- Ajout d'un identifiant visiteur anonyme persistant pour améliorer le suivi des utilisateurs récurrents. [#134](https://github.com/incubateur-ademe/mutafriches/pull/134)
- Ajout de pages juridiques. [#134](https://github.com/incubateur-ademe/mutafriches/pull/134)
- Ajout de la version de l'application dans le footer, non cliquable. [#143](https://github.com/incubateur-ademe/mutafriches/pull/143)
- Ajout de la version de l'application dans le footer. [#142](https://github.com/incubateur-ademe/mutafriches/pull/142)

### Évolutions techniques
- Refactorisation des pages "multisites" et "diagnostic" pour une meilleure maintenabilité. [#132](https://github.com/incubateur-ademe/mutafriches/pull/132)
- Correction d'un problème lié au préchargement et à la gestion du cache. [#125](https://github.com/incubateur-ademe/mutafriches/pull/125)
- Correction d'un problème lié à l'historique des migrations Drizzle. [#118](https://github.com/incubateur-ademe/mutafriches/pull/118)
- Contournement d'un problème avec pnpm au runtime Scalingo (utilisation de pnpm 11). [#126](https://github.com/incubateur-ademe/mutafriches/pull/126)
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité et améliorer la stabilité. [#128](https://github.com/incubateur-ademe/mutafriches/pull/128), [#119](https://github.com/incubateur-ademe/mutafriches/pull/119), [#115](https://github.com/incubateur-ademe/mutafriches/pull/115), [#117](https://github.com/incubateur-ademe/mutafriches/pull/117)

### Autres changements
- Suppression des fixtures Excel inutiles. [#141](https://github.com/incubateur-ademe/mutafriches/pull/141)

## Changelog : zero-logement-vacant (30 derniers jours, au 08 juillet 2026)

### Résumé
Les dernières mises à jour améliorent la performance et la fiabilité de l'application, notamment grâce à la mise en cache des données de référence. Des corrections ont été apportées pour améliorer la gestion des utilisateurs, des filtres et des données affichées. L'application bénéficie également d'une refactorisation technique importante pour moderniser son code et faciliter sa maintenance.

### Évolutions fonctionnelles
- Correction de l'affichage des libellés d'années de vacance (2022 remplacé par 2023) [#1875](https://github.com/MTES-MCT/zero-logement-vacant/issues/1875).
- Amélioration de la gestion des structures multi-établissements pour l'affichage des périmètres utilisateurs [#1870](https://github.com/MTES-MCT/zero-logement-vacant/issues/1870).
- Ajout d'un contrôle plein écran à la carte des logements [#1872](https://github.com/MTES-MCT/zero-logement-vacant/issues/1872).
- Correction de l'édition des propriétaires pour permettre la modification des adresses BAN avec un score nul [#1881](https://github.com/MTES-MCT/zero-logement-vacant/issues/1881).
- Correction de l'affichage des icônes de filtre pour utiliser la couleur "bleu-france" [#1876](https://github.com/MTES-MCT/zero-logement-vacant/issues/1876).
- Ajout d'une fonctionnalité permettant de lister les consommateurs LOVAC CEREMA non enregistrés [#1846](https://github.com/MTES-MCT/zero-logement-vacant/issues/1846).
- Amélioration de la gestion des filtres intercommunaux pour les DDT [#1867](https://github.com/MTES-MCT/zero-logement-vacant/issues/1867).
- Correction de la gestion des filtres de localité pour ignorer les filtres vides [#1865](https://github.com/MTES-MCT/zero-logement-vacant/issues/1865).
- Possibilité de rendre optionnel le champ "date de naissance" lors de la création/édition d'un propriétaire [#1861](https://github.com/MTES-MCT/zero-logement-vacant/issues/1861).

### Évolutions techniques
- Refactorisation majeure pour supprimer l'ancienne bibliothèque DSFR et migrer vers des composants MUI plus modernes [#1850](https://github.com/MTES-MCT/zero-logement-vacant/issues/1850).
- Mise en place d'un système de cache pour les données de référence afin d'améliorer les performances [#1852](https://github.com/MTES-MCT/zero-logement-vacant/issues/1852).
- Migration de la validation des données vers `validatorNext` pour une meilleure maintenabilité et performance [#1853](https://github.com/MTES-MCT/zero-logement-vacant/issues/1853).
- Utilisation de `oxlint` et `oxfmt` pour le linting et le formattage du code, remplaçant ESLint et Prettier [#1852](https://github.com/MTES-MCT/zero-logement-vacant/issues/1852).
- Amélioration des tests unitaires et d'intégration.
- Refactorisation de la gestion des factories pour une meilleure organisation et réutilisation.
- Déploiement du front avec Terraform via clevercloud_static_apache [#1882](https://github.com/MTES-MCT/zero-logement-vacant/issues/1882).

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'un script pour backfiller les adresses sur LOVAC 2026.
- Mise à jour des dépendances.
- Correction de la gestion des utilisateurs CEREMA LOVAC pour dédupliquer par email [#1888](https://github.com/MTES-MCT/zero-logement-vacant/issues/1888).
- Ajout d'un environnement de démonstration déployable en production [#1879](https://github.com/MTES-MCT/zero-logement-vacant/issues/1879).

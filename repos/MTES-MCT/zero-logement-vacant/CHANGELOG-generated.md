## Changelog : zero-logement-vacant (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité, de la cartographie et des outils de diagnostic et de réparation de données. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau des filtres et de l'édition des propriétaires. L'ajout d'un outil de réparation des données (ZLV repair harness) est une avancée majeure.

### Évolutions fonctionnelles
- Amélioration de la cartographie : possibilité de basculer l'affichage des périmètres, avec une option pour les garder visibles en rouge lorsqu'ils sont désactivés. [#1884](https://github.com/MTES-MCT/zero-logement-vacant/issues/1884)
- Amélioration de l'analyse du dashboard : mise à jour pour l'année 2026. [#1878](https://github.com/MTES-MCT/zero-logement-vacant/issues/1878)
- Correction de l'affichage des filtres : correction du libellé de l'année de vacance (passage de "inconsistancy2022" à 2023). [#1875](https://github.com/MTES-MCT/zero-logement-vacant/issues/1875)
- Correction des icônes de filtre : utilisation de la couleur "bleu-france" pour les icônes de filtre. [#1876](https://github.com/MTES-MCT/zero-logement-vacant/issues/1876)
- Date de naissance des propriétaires : le champ "date de naissance" est maintenant optionnel lors de l'édition des propriétaires. [#1861](https://github.com/MTES-MCT/zero-logement-vacant/issues/1861)
- Filtre intercommunalité DDT : correction pour permettre le filtre intercommunalité pour les structures DDT/départementales. [#1867](https://github.com/MTES-MCT/zero-logement-vacant/issues/1867)
- Liste des consommateurs LOVAC non enregistrés : ajout d'une fonctionnalité pour lister les consommateurs LOVAC non enregistrés. [#1846](https://github.com/MTES-MCT/zero-logement-vacant/issues/1846)

### Évolutions techniques
- **Nouvel outil de réparation des données (ZLV repair harness)** : développement complet d'un outil pour diagnostiquer et réparer les données, incluant une CLI, des types de données, des fonctions d'application et de statistiques, ainsi que des tests.
- Refactoring : amélioration de la structure du code et de la maintenabilité.
- Correction de bugs : résolution de problèmes liés à la gestion des images MapLibre et à la gestion des statuts des lots de logements.
- Déploiement : passage au déploiement via Terraform pour le frontend.
- Amélioration des tests : ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et corrections de bugs.
- Mise à jour des dépendances : mise à jour des dépendances npm et yarn.
- Amélioration de l'analyse : amélioration du rendu du dashboard d'analyse.
- Correction de la gestion des images MapLibre pour éviter les fuites de mémoire.

### Autres changements
- Documentation : ajout de la méthodologie de test RGAA complète comme référence à la demande.
- Documentation : intégration de la liste complète des 106 critères RGAA.
- Documentation : obligation de conformité RGAA pour le travail frontend.
- Amélioration de la documentation pour le repair harness.
- Mise à jour des compétences de l'équipe.
- Correction de la documentation pour la planification du repair harness.
- Ajout d'un plan d'implémentation pour le repair harness.
- Formatage du code.
- Corrections de typographie et de wording.

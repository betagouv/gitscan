## Changelog : ma-cantine (30 derniers jours, au 8 juin 2026)

### Résumé
Les dernières semaines ont été marquées par une forte activité sur le module Achats, avec l'ajout de nouvelles fonctionnalités comme la modification des achats, l'amélioration du formulaire et l'ajout de champs plus précis (caractéristiques, famille de produit). Des corrections et améliorations ont également été apportées aux diagnostics et aux exports de données.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier un achat via un nouveau formulaire. ([#6783](https://github.com/betagouv/ma-cantine/issues/6783))
- Début de la migration de la page de création d'achat vers Vue.js 3. ([#6759](https://github.com/betagouv/ma-cantine/issues/6759))
- Mise à jour de l'URL utilisée pour les achats, pointant vers la nouvelle adresse officielle. ([#6789](https://github.com/betagouv/ma-cantine/issues/6789))
- Ajout de l'autocomplétion dans les champs "Description" et "Fournisseurs" du module Achats. ([#6797](https://github.com/betagouv/ma-cantine/issues/6797))
- Ajout des champs "Caractéristiques" et "Famille de produit" au module Achats pour une meilleure catégorisation. ([#6782](https://github.com/betagouv/ma-cantine/issues/6782))
- Ajout de ressources (livrables GT sanitaire et médico-social). ([#6733](https://github.com/betagouv/ma-cantine/issues/6733))
- Correction de l'URL des CGU pour pointer vers le frontend. ([#6701](https://github.com/betagouv/ma-cantine/issues/6701))

### Évolutions techniques
- Refactor du module Achats : renommage des champs du modèle en français pour une meilleure lisibilité. ([#6765](https://github.com/betagouv/ma-cantine/issues/6765))
- Refactor du module Achats : séparation de la logique FRANCE, CIRCUIT_COURT et LOCAL dans les calculs d'agrégation. ([#6731](https://github.com/betagouv/ma-cantine/issues/6731))
- Suppression de l'utilisation de l'API Adresse dans la création de cantines, améliorant la stabilité et la performance. ([#6766](https://github.com/betagouv/ma-cantine/issues/6766))
- Suppression du code inutile lié à l'ancienne API Adresse. ([#6787](https://github.com/betagouv/ma-cantine/issues/6787))
- Refactor du module Diagnostics : simplification du calcul du coût repas et ajout d'un test. ([#6796](https://github.com/betagouv/ma-cantine/issues/6796))
- Amélioration de la commande pour remplir les champs calculés des diagnostics. ([#6754](https://github.com/betagouv/ma-cantine/issues/6754))
- Ajout de nouveaux querysets pour faciliter le filtrage et l'accès aux données.
- Amélioration de la gestion des exports de données (Open Data, Metabase).
- Diverses corrections et améliorations de la structure du code et des tests.

### Autres changements
- Ajout d'une page de documentation expliquant les commandes liées à une campagne de télédéclaration. ([#6738](https://github.com/betagouv/ma-cantine/issues/6738))
- Ajout de nouveaux champs `creation_user` aux modèles Cantines, Diagnostics et Achats pour suivre l'auteur de la création. ([#6750](https://github.com/betagouv/ma-cantine/issues/6750), [#6746](https://github.com/betagouv/ma-cantine/issues/6746), [#6745](https://github.com/betagouv/ma-cantine/issues/6745))
- Correction de la migration pour éviter les conflits. ([#6741](https://github.com/betagouv/ma-cantine/issues/6741), [#6732](https://github.com/betagouv/ma-cantine/issues/6732))

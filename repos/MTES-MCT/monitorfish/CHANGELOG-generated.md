## Changelog : monitorfish (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur pour les contrôles, notamment concernant la gestion des groupes de navires prioritaires, des signalements et des formulaires e-ISR. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi qu'une modernisation des outils de linting pour améliorer la qualité du code.

### Évolutions fonctionnelles
- Amélioration du suivi des contrôles sur les cibles prioritaires [#5306](https://github.com/MTES-MCT/monitorfish/issues/5306).
- Correction de l'affichage des groupes de navires prioritaires et ajout de tests unitaires.
- Correction de bugs liés à l'affichage de la profondeur des alertes dans les rapports et au débordement des jauges de profil de navire.
- Corrections sur les formulaires M1 et M3 (e-ISR) : affichage des champs, gestion des dates de mission, et ajout des champs armateur.
- Affichage des groupes partagés et des signalements de la marée sous la recherche navire dans le contexte des contrôles.
- Amélioration de l'affichage et de la gestion des groupes de navires, notamment pour l'export CSV et le style des groupes prioritaires.
- Ajout d'un filtre "navire sans fiche" dans la liste des signalements INN en Outre-mer OP [#5289](https://github.com/MTES-MCT/monitorfish/issues/5289).
- Correction du troncage du calendrier de fin de mission dans les rapports d'inspection.
- Mise à jour de la REG UE pour les avaries VMS.
- Amélioration du flux de gestion des navires.
- Ajout de colonnes dans l'interface.
- Mise à jour des PDF.

### Évolutions techniques
- Optimisation de la requête des dernières positions AIS pour améliorer les performances [#5300](https://github.com/MTES-MCT/monitorfish/issues/5300).
- Refonte du linter avec l'intégration d'OxLint (hybride ESLint) et application de règles de performance.
- Mise à jour des dépendances frontend (postcss).
- Amélioration de la configuration des hooks git et intégration de ktlint pour le backend.
- Utilisation de `updateMany` pour optimiser les mises à jour en base de données.
- Suppression de code obsolète et simplification de la logique.
- Correction de plusieurs avertissements et erreurs de linting.
- Migration vers ESLint 9 avec suppressions natives.

### Autres changements
- Ajout d'une section sur le `box-sizing` monitor-ui dans le fichier `CONTRIBUTING.md` [#5273](https://github.com/MTES-MCT/monitorfish/issues/5273).
- Mise à jour de la description des nouvelles fonctionnalités.
- Suppression de la baseline ktlint.
- Correction de commentaires obsolètes.
- Ajout d'un info icon.
- Suppression de la prop `vesselTargeted`.
- Ajout d'un message de progression dans le hook de pré-push pour les tests lents.
- Correction du scraper Legipeche pour gérer les pages non visitées [#5268](https://github.com/MTES-MCT/monitorfish/issues/5268).
- Mise à jour des dépendances Python.
- Suppression d'une réversion de la présentation/zone single-select pour les espèces et les discards.
- Suppression de règles de linting inutiles.
- Correction de la gestion des promesses flottantes dans le code frontend.
- Ajout de tests Cypress pour l'affichage des groupes de navires.
- Correction de bugs liés à la navigation au clavier dans les tableaux d'espèces.
- Amélioration de la gestion des états et des événements dans l'interface utilisateur.

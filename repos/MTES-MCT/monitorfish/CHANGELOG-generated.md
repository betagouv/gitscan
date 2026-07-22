## Changelog : monitorfish (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la performance de l'application, notamment pour l'affichage des positions AIS. Des corrections ont été apportées au scraper Legipeche et à la gestion des groupes prioritaires de navires. L'interface utilisateur a été améliorée avec des corrections et des ajustements pour les formulaires de contrôle (e-ISR) et l'affichage des informations sur les navires.

### Évolutions fonctionnelles
- Correction d'un problème de performance lors de la requête des dernières positions AIS [#5300](https://github.com/MTES-MCT/monitorfish/issues/5300).
- Amélioration de la gestion des groupes prioritaires : inclusion des navires sous charte, exclusion des segments habituels et correction de bugs [#5293](https://github.com/MTES-MCT/monitorfish/issues/5293).
- Correction du scraper Legipeche pour traiter les pages non visitées [#5268](https://github.com/MTES-MCT/monitorfish/issues/5268).
- Affichage du filtre "navire sans fiche" dans la liste des signalements INN pour les outre-mers [#5289](https://github.com/MTES-MCT/monitorfish/issues/5289).
- Correction du troncage de la date de fin de mission dans les signalements INN [#5269](https://github.com/MTES-MCT/monitorfish/issues/5269).
- Améliorations des formulaires M1 et M3 (e-ISR) suite aux retours du CNSP [#5283](https://github.com/MTES-MCT/monitorfish/issues/5283) et [#5268](https://github.com/MTES-MCT/monitorfish/issues/5268).
- Ajout de la description des groupes prioritaires.
- Affichage des groupes partagés et des signalements de la marée sous la recherche navire.
- Possibilité de sauvegarder une infraction en attente dans le rapport de contrôle.
- Amélioration de l'affichage des informations sur les groupes prioritaires dans la carte et la liste des navires.
- Affichage des messages manuels des préavis (PNO) dans le journal de bord du voyage [#5222](https://github.com/MTES-MCT/monitorfish/issues/5222).

### Évolutions techniques
- Mise à jour des dépendances Python (non-majeures) [#5277](https://github.com/MTES-MCT/monitorfish/issues/5277).
- Refonte du linter frontend avec l'intégration d'OxLint (hybride ESLint) [#5259](https://github.com/MTES-MCT/monitorfish/issues/5259) et [#5233](https://github.com/MTES-MCT/monitorfish/issues/5233).
- Amélioration des tests Cypress et Jest.
- Ajout de tests backend pour les groupes prioritaires.
- Optimisation de la requête SQL pour les positions AIS.
- Correction de violations de linting et amélioration de la qualité du code.
- Mise à jour des règles de linting et ajout de nouvelles règles.
- Amélioration des performances du backend avec l'utilisation de `updateMany`.

### Autres changements
- Correction de la logique de niveau de priorité de contrôle effectif.
- Suppression de règles de linting obsolètes.
- Mise à jour de la documentation.
- Corrections de typographie et d'affichage.
- Suppression de l'affichage de certains champs dans les formulaires e-ISR.
- Mise à jour de la REG UE pour les dysfonctionnements des balises.
- Ajout de l'opérateur à l'API publique.
- Corrections diverses et amélioration de la maintenance du code.

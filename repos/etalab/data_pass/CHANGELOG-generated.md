## Changelog : data_pass (30 derniers jours)

### Résumé
Les dernières mises à jour de data_pass se concentrent sur l'amélioration de l'administration des types d'habilitations, l'ajout de nouvelles intégrations API (APIPFC, GUNenv, Inser Jeunes Sup), et l'amélioration de la gestion des habilitations FranceConnect. Des corrections de bugs et des améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une interface d'administration pour la gestion des types d'habilitation (création, modification, suppression) [#1422](https://github.com/etalab/data_pass/pull/1422), [#1410](https://github.com/etalab/data_pass/pull/1410).
- Possibilité de choisir une habilitation FranceConnect existante lors de la liaison avec une demande APIPFC [#1407](https://github.com/etalab/data_pass/pull/1407).
- Ajout de la page Mentions Légales et de la Politique de Confidentialité [#1371](https://github.com/etalab/data_pass/pull/1371), [#1374](https://github.com/etalab/data_pass/pull/1374).
- Amélioration de l'affichage du motif d'annulation d'une réouverture d'habilitation [#1381](https://github.com/etalab/data_pass/pull/1381).
- Ajout de nouvelles API : GUNenv et Inser Jeunes Sup [#1417](https://github.com/etalab/data_pass/pull/1417), [#1370](https://github.com/etalab/data_pass/pull/1370).
- Possibilité de gérer les abonnements HubEE existants [#1372](https://github.com/etalab/data_pass/pull/1372).
- Ajout d'un badge "nouveau message" pour les demandes instructeur [#1411](https://github.com/etalab/data_pass/pull/1411).

### Évolutions techniques
- Mise en place de Papertrail pour le versioning des types d'habilitation dynamiques [#1440](https://github.com/etalab/data_pass/pull/1440).
- Refactoring de l'interface d'administration pour améliorer la lisibilité et l'accessibilité [#1436](https://github.com/etalab/data_pass/pull/1436), [#1421](https://github.com/etalab/data_pass/pull/1421).
- Amélioration de la gestion des scopes pour les types d'habilitation dynamiques [#1425](https://github.com/etalab/data_pass/pull/1425).
- Mise en place d'un système de feature flags pour l'APIPFC [#1427](https://github.com/etalab/data_pass/pull/1427).
- Suppression de code obsolète et nettoyage de la configuration [#1424](https://github.com/etalab/data_pass/pull/1424), [#1400](https://github.com/etalab/data_pass/pull/1397).
- Mise à jour des dépendances (RSpec, Rubocop, Rails Pulse, Docker) [#1450](https://github.com/etalab/data_pass/pull/1450), [#1451](https://github.com/etalab/data_pass/pull/1451), [#1449](https://github.com/etalab/data_pass/pull/1449), [#1452](https://github.com/etalab/data_pass/pull/1452), [#1428](https://github.com/etalab/data_pass/pull/1428), [#1367](https://github.com/etalab/data_pass/pull/1368).
- Ajout de tests pour améliorer la couverture et la stabilité du code [#1375](https://github.com/etalab/data_pass/pull/1375).
- Correction de tests flaky [#1404](https://github.com/etalab/data_pass/pull/1404).

### Autres changements
- Ajout d'un email de support [#1420](https://github.com/etalab/data_pass/pull/1420).
- Correction de typos et amélioration de la documentation [#1445](https://github.com/etalab/data_pass/pull/1445), [#1442](https://github.com/etalab/data_pass/pull/1442), [#1444](https://github.com/etalab/data_pass/pull/1444).
- Rotation annuelle du token webhook API Entreprise [#1439](https://github.com/etalab/data_pass/pull/1439).
- Suppression de la plateforme "Aides Etat" et du provider "DGE" [#1403](https://github.com/etalab/data_pass/pull/1403).
- Mise à jour des numéros de téléphone pour les contacts techniques des API [#1380](https://github.com/etalab/data_pass/pull/1380).

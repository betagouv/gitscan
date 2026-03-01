## Changelog : data_pass (30 derniers jours)

### Résumé
Les dernières mises à jour de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment en facilitant la gestion des habilitations et en ajoutant de nouvelles fonctionnalités pour les partenaires API. Des corrections de bugs et des améliorations de la stabilité ont également été apportées, ainsi que des ajustements pour l'intégration avec FranceConnect et d'autres services.

### Évolutions fonctionnelles
- Possibilité de révoquer une habilitation directement depuis la page d'habilitation. [#1394](https://github.com/etalab/data_pass/issues/1394)
- Possibilité de rouvrir une habilitation compatible APIP/APIPFC. [#1399](https://github.com/etalab/data_pass/issues/1399)
- Ajout d'un bouton de révocation sur la page d'une habilitation. [#1391](https://github.com/etalab/data_pass/issues/1391)
- Amélioration de l'historique des validations et des générations automatiques d'habilitation pour une meilleure lisibilité. [#1349](https://github.com/etalab/data_pass/issues/1349)
- Ajout de la possibilité de créer deux habilitations à partir d'une seule demande. [#1344](https://github.com/etalab/data_pass/issues/1344)
- Ajout de champs pré-remplis pour FranceConnect dans le formulaire API Particulier. [#1346](https://github.com/etalab/data_pass/issues/1346)
- Implémentation des vues pour les champs FranceConnect API Particulier unifiés. [#1332](https://github.com/etalab/data_pass/issues/1332)
- Ajout d'une page Politique de confidentialité. [#1374](https://github.com/etalab/data_pass/issues/1374)
- Ajout d'une page Mentions légales. [#1371](https://github.com/etalab/data_pass/issues/1371)
- Amélioration de la sélection de texte dans le champ email pour le transfert d'habilitation. [#1364](https://github.com/etalab/data_pass/issues/1364)
- Ajout de la possibilité de sélectionner le type d'habilitation dans la liste. [#1347](https://github.com/etalab/data_pass/issues/1347)
- Ajout de nouvelles scopes pour les API Particulier Extenso et Tarification cantine collège/lycée. [#1334](https://github.com/etalab/data_pass/issues/1334)

### Évolutions techniques
- Mise en place d'un nouveau dashboard de statistiques natif remplaçant l'iframe Metabase. [#1341](https://github.com/etalab/data_pass/issues/1341)
- Refactoring de l'affichage des onglets pour améliorer la performance et la maintenabilité.
- Amélioration de la gestion des erreurs lors de la récupération des données INSEE. [#1333](https://github.com/etalab/data_pass/issues/1333)
- Mise en place d'un système de feature flags pour l'APIPFC, permettant une activation progressive et contrôlée. [#1383](https://github.com/etalab/data_pass/issues/1383)
- Suppression de la configuration Rails Pulse obsolète.
- Amélioration de la robustesse des tests et correction de tests aléatoires. [#1404](https://github.com/etalab/data_pass/issues/1404)
- Mise à jour des dépendances Ruby et Rubocop.
- Ajout d'un cooldown de 7 jours à la configuration de Dependabot.
- Amélioration de la documentation pour l'utilisation de Docker. [#1338](https://github.com/etalab/data_pass/issues/1338)

### Autres changements
- Suppression de la plateforme "Aides Etat" et du provider "DGE". [#1397](https://github.com/etalab/data_pass/issues/1397)
- Suppression du provider "ministere_des_armees".
- Ajout des numéros de téléphone des contacts techniques pour les APIPFC. [#1379](https://github.com/etalab/data_pass/issues/1379)
- Ajout de l'identifiant du formulaire dans une habilitation. [#1396](https://github.com/etalab/data_pass/issues/1396)
- Correction de l'affichage du motif d'annulation de la réouverture. [#1381](https://github.com/etalab/data_pass/issues/1381)
- Ajout de factories pour les nouvelles APIs (api_gunenv et api_inser_jeunes_sup).
- Correction de l'accessibilité des liens externes sur la page Accessibilité.
- Suppression de l'ancien fichier CLAUSE.md.
- Mise à jour de la documentation pour les scopes FranceConnect.

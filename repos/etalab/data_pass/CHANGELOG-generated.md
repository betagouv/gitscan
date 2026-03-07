## Changelog : data_pass (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment autour de la gestion des habilitations FranceConnect et des demandes d'accès API. Des corrections de bugs et des ajustements ont également été apportés pour améliorer la stabilité et la clarté de l'application. De nouvelles fonctionnalités ont été implémentées pour faciliter la révocation et la réouverture des habilitations, ainsi que pour améliorer la gestion des demandes d'accès.

### Évolutions fonctionnelles
- Possibilité de sélectionner une habilitation FranceConnect existante lors d'une demande APIPFC. [#1375](https://github.com/etalab/data_pass/issues/1375)
- Ajout de la possibilité de révoquer une habilitation APIP (FC). [#1406](https://github.com/etalab/data_pass/issues/1406)
- Possibilité de rouvrir une habilitation APIP compatible APIPFC sans générer de nouvelle demande. [#1399](https://github.com/etalab/data_pass/issues/1399)
- Amélioration de l'historique des actions : consultation plus générique et affichage du type d'habilitation. [#1454](https://github.com/etalab/data_pass/issues/1454), [#1457](https://github.com/etalab/data_pass/issues/1457)
- Ajout d'une page Politique de confidentialité. [#1495](https://github.com/etalab/data_pass/issues/1495)
- Ajout de la page Mentions légales. [#1496](https://github.com/etalab/data_pass/issues/1496)
- Amélioration de la gestion des champs pré-remplis pour FranceConnect dans le formulaire API Particulier. [#1454](https://github.com/etalab/data_pass/issues/1454)
- Possibilité de créer deux habilitations à partir d'une demande. [#1439](https://github.com/etalab/data_pass/issues/1439)
- Amélioration de l'affichage des scopes FranceConnect en fonction de la modalité. [#1446](https://github.com/etalab/data_pass/issues/1446)
- Correction d'un bug empêchant d'annuler une demande de réouverture une fois lancée. [#1375](https://github.com/etalab/data_pass/issues/1375)
- Correction de l'affichage du lien vers l'infographie API TD CESU. [#1420](https://github.com/etalab/data_pass/issues/1420)
- Correction de l'affichage du motif d'annulation de la réouverture dans l'historique. [#1381](https://github.com/etalab/data_pass/issues/1381)

### Évolutions techniques
- Mise à jour des dépendances : `rails_pulse`, `rspec-rails`, `rubocop`.
- Suppression d'une gem en double.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la configuration des tests.
- Ajout de tests pour les CGU FranceConnect.
- Mise en place de rails_pulse pour le monitoring.
- Mise en place d'un système de feature flag pour l'APIPFC.
- Suppression de la plateforme "Aides Etat" et du provider "DGE".
- Correction de tests flaky.

### Autres changements
- Ajout des numéros de téléphone des contacts techniques pour les APIPFC. [#1379](https://github.com/etalab/data_pass/issues/1379)
- Mise à jour de la documentation.
- Nettoyage du code.
- Correction de l'affichage des CGU FranceConnect.
- Amélioration de la gestion des autorisations et des rôles.
- Mise à jour des scopes pour l'annuaire.
- Suppression de code obsolète.
- Ajout de statistiques publiques.

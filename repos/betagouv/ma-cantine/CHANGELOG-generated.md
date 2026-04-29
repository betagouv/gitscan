## Changelog : ma-cantine (30 derniers jours, au 2026-04-28)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités de télédéclaration, notamment avec l'ajout de nouveaux scripts pour faciliter la correction des bilans et la gestion des campagnes. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un script permettant de télédéclarer une liste de bilans hors campagne ([#6671](https://github.com/betagouv/ma-cantine/issues/6671)).
- Nouveau script pour télédéclarer tous les bilans en mode "CORRECTION" ([#6666](https://github.com/betagouv/ma-cantine/issues/6666)).
- Ajout d'un filtre "bilan télédéclaré" au tableau de bord ([#6655](https://github.com/betagouv/ma-cantine/issues/6655)).
- Amélioration de l'affichage de l'objectif viande et poisson dans les statistiques.
- Ajout d'un indicateur du nombre de filtres sélectionnés dans la liste déroulante.
- Ajout d'un nouveau filtre dans l'administration des diagnostics pour afficher les télédéclarations générées.
- Modification de l'affichage de la colonne "commune" dans le tableau de bord pour les groupes.
- Mise à jour du bandeau d'information pour refléter la prolongation de la campagne de correction.
- Ajout des dates de campagne dans l'interface.
- Ajout de ressources (clausier et protocole de pesée).

### Évolutions techniques
- Refactor de code lié aux télédéclarations pour simplifier et clarifier la logique métier ([#6656](https://github.com/betagouv/ma-cantine/issues/6656), [#6657](https://github.com/betagouv/ma-cantine/issues/6657)).
- Amélioration des performances de chargement des listes de cantines et d'utilisateurs dans l'administration.
- Optimisation de l'exportation des données pour l'observatoire.
- Correction d'un bug empêchant l'affichage de la police Marianne ([#6669](https://github.com/betagouv/ma-cantine/issues/6669)).
- Correction d'un bug lié à l'arrondi des décimales dans les totaux viandes et poissons des familles en télédéclaration ([#6605](https://github.com/betagouv/ma-cantine/issues/6605)).
- Suppression de code obsolète lié aux anciens imports de bilans ([#6642](https://github.com/betagouv/ma-cantine/issues/6642)).
- Amélioration de la commande de resubmit pour la télédéclaration.
- Ajout de tests pour les scripts de télédéclaration ([#6673](https://github.com/betagouv/ma-cantine/issues/6673)).
- Correction de l'API pour renvoyer uniquement les pourcentages d'approbation des diagnostics ([#6664](https://github.com/betagouv/ma-cantine/issues/6664)).
- Correction de l'affichage des valeurs brutes du bilan dans les cantines publiques ([#6663](https://github.com/betagouv/ma-cantine/issues/6663)).
- Mise à jour de la dépendance Django vers la version 5.2.13 ([#6623](https://github.com/betagouv/ma-cantine/issues/6623)).

### Autres changements
- Correction d'un lien dans le bandeau d'information ([#6675](https://github.com/betagouv/ma-cantine/issues/6675)).
- Correction d'une faute d'orthographe dans les mentions légales ([#6640](https://github.com/betagouv/ma-cantine/issues/6640)).
- Suppression d'un tiret superflu dans le texte "ma-cantine" ([#6633](https://github.com/betagouv/ma-cantine/issues/6633)).
- Modification du texte "supprimer" par "archiver" pour l'archivage des cantines ([#6604](https://github.com/betagouv/ma-cantine/issues/6604)).
- Modification de l'affichage des couverts jours par les couverts annuels dans la gestion des satellites ([#6624](https://github.com/betagouv/ma-cantine/issues/6624)).
- Ajout du status "CORRECTION" pour les bilans ([#6616](https://github.com/betagouv/ma-cantine/issues/6616)).
- Réorganisation des actions dans les cantines ([#6613](https://github.com/betagouv/ma-cantine/issues/6613)).
- Amélioration de l'interface utilisateur pour la modification des RSAT des satellites ([#6667](https://github.com/betagouv/ma-cantine/issues/6667)).
- Ajout du lien vers le communiqué de presse pour la prolongation de la campagne ([#6591](https://github.com/betagouv/ma-cantine/issues/6591)).
- Suppression du message d'alerte sur les données incorrectes pour l'année 2024 dans l'observatoire ([#6620](https://github.com/betagouv/ma-cantine/issues/6620)).
- Documentation de l'API Stats avec l'ajout des enums pour les filtres ([#6584](https://github.com/betagouv/ma-cantine/issues/6584)).

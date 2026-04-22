## Changelog : ma-cantine (30 derniers jours, au 2026-04-21)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la campagne de correction des télédéclarations, avec l'ajout de nouveaux statuts, des restrictions sur les modifications des bilans, et des améliorations de l'interface utilisateur pour faciliter le processus. Des optimisations et corrections ont également été apportées concernant l'extraction de données et l'administration.

### Évolutions fonctionnelles
- Ajout du filtre "bilan télédéclaré" au tableau de bord. ([#6655](https://github.com/betagouv/ma-cantine/issues/6655))
- Amélioration de l'affichage de la colonne "commune" dans le tableau de bord, masquant le message "Non renseignée" pour les groupes. ([#6653](https://github.com/betagouv/ma-cantine/issues/6653))
- Ajout d'un indicateur visuel pour le nombre de filtres sélectionnés dans les listes déroulantes. ([#6654](https://github.com/betagouv/ma-cantine/issues/6654))
- Ajout d'un nouveau filtre dans l'administration des diagnostics pour afficher les télédéclarations générées. ([#6582](https://github.com/betagouv/ma-cantine/issues/6582))
- Modification du bouton "Supprimer une cantine" pour afficher "Archiver une cantine". ([#6604](https://github.com/betagouv/ma-cantine/issues/6604))
- Ajout d'une page interne affichant les statistiques Metabase via iframe. ([#6590](https://github.com/betagouv/ma-cantine/issues/6590))
- Ajout des dates de campagne de correction dans l'interface. ([#6607](https://github.com/betagouv/ma-cantine/issues/6607))
- Remplacement du nombre de couverts jours par le nombre de couverts annuels dans la gestion des satellites. ([#6624](https://github.com/betagouv/ma-cantine/issues/6624))
- Ajout d'un lien vers le communiqué de presse concernant la prolongation de la campagne de correction. ([#6591](https://github.com/betagouv/ma-cantine/issues/6591))
- Mise à jour du bandeau d'information pour la campagne de correction. ([#6628](https://github.com/betagouv/ma-cantine/issues/6628))

### Évolutions techniques
- Refactorisation du code lié aux anciens imports de bilans. ([#6642](https://github.com/betagouv/ma-cantine/issues/6642))
- Amélioration de la commande de resubmit des télédéclarations pour accepter une liste d'IDs de diagnostics. ([#6644](https://github.com/betagouv/ma-cantine/issues/6644))
- Ajout de nouveaux querysets pour faciliter l'utilisation des données générées par 1TD1Site. ([#6468](https://github.com/betagouv/ma-cantine/issues/6468), [#6466](https://github.com/betagouv/ma-cantine/issues/6466), [#6455](https://github.com/betagouv/ma-cantine/issues/6455))
- Refactorisation de l'ETL pour inclure 1TD1Site dans les exports bruts. ([#6632](https://github.com/betagouv/ma-cantine/issues/6632))
- Amélioration de la gestion des arrondis dans le script de génération 1TD1Site. ([#6473](https://github.com/betagouv/ma-cantine/issues/6473))
- Amélioration de la performance du chargement des cantines et des utilisateurs dans l'administration. ([#6580](https://github.com/betagouv/ma-cantine/issues/6580), [#6579](https://github.com/betagouv/ma-cantine/issues/6579))
- Ajout d'un health check sur la base de données PostgreSQL pour les tâches asynchrones. ([#6547](https://github.com/betagouv/ma-cantine/issues/6547))
- Mise à jour de Django en 5.2.13.
- Amélioration de la récupération des données géographiques des SIREN en temps réel. ([#6556](https://github.com/betagouv/ma-cantine/issues/6556))

### Autres changements
- Correction d'une faute d'orthographe dans les mentions légales. ([#6640](https://github.com/betagouv/ma-cantine/issues/6640))
- Suppression du tiret dans le texte "ma-cantine". ([#6633](https://github.com/betagouv/ma-cantine/issues/6633))
- Ajout de fichiers dédiés pour la police Marianne. ([#6621](https://github.com/betagouv/ma-cantine/issues/6621))
- Documentation de l'API Stats avec les enums pour les filtres. ([#6584](https://github.com/betagouv/ma-cantine/issues/6584))
- Suppression de l'obligation de l'administration de tutelle pour le secteur "Autres structures d'enseignement". ([#6569](https://github.com/betagouv/ma-cantine/issues/6569))
- Correction de l'affichage du nom "ma-cantine" dans les statistiques. ([#6608](https://github.com/betagouv/ma-cantine/issues/6608))
- Suppression de l'icône du bouton "Archiver une cantine". ([#6606](https://github.com/betagouv/ma-cantine/issues/6606))
- Correction de l'arrondi des décimales pour les totaux viandes et poissons. ([#6605](https://github.com/betagouv/ma-cantine/issues/6605))
- Ajout de la mention "sites télédéclarés" pour 2025 dans l'observatoire. ([#6622](https://github.com/betagouv/ma-cantine/issues/6622))
- Suppression du message d'alerte sur les données incorrectes pour 2024 dans l'observatoire. ([#6620](https://github.com/betagouv/ma-cantine/issues/6620))
- Ajout des champs pourcentage et objectifs egalim dans les télédéclarations. ([#6549](https://github.com/betagouv/ma-cantine/issues/6549))

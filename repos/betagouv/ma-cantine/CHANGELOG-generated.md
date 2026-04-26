## Changelog : ma-cantine (30 derniers jours, au 23 avril 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives sur le tableau de bord et l'administration des diagnostics, notamment avec l'ajout de filtres et l'amélioration de l'affichage des données. Des corrections ont également été apportées concernant la télédéclaration et l'affichage des bilans, ainsi que des ajustements pour la campagne de correction en cours.

### Évolutions fonctionnelles
- Ajout d'un filtre sur le tableau de bord pour afficher uniquement les bilans télédéclarés. ([#6655](https://github.com/betagouv/ma-cantine/issues/6655))
- Amélioration de l'affichage du tableau de bord : la colonne 'commune' ne montre plus "Non renseignée" pour les groupes. ([#6653](https://github.com/betagouv/ma-cantine/issues/6653))
- Ajout d'un indicateur visuel du nombre de filtres sélectionnés dans les listes déroulantes. ([#6654](https://github.com/betagouv/ma-cantine/issues/6654))
- Ajout d'un nouveau filtre dans l'administration des diagnostics pour afficher les télédéclarations générées [1TD1Site]. ([#6582](https://github.com/betagouv/ma-cantine/issues/6582))
- Mise à jour du bandeau d'information concernant la campagne de correction. ([#6628](https://github.com/betagouv/ma-cantine/issues/6628))
- Ajout des dates de la campagne de correction. ([#6607](https://github.com/betagouv/ma-cantine/issues/6607))
- Remplacement de "supprimer" par "archiver" pour l'action d'archivage d'une cantine. ([#6604](https://github.com/betagouv/ma-cantine/issues/6604))
- Ajout d'une page interne affichant les statistiques Metabase via iframe. ([#6590](https://github.com/betagouv/ma-cantine/issues/6590))
- Ajout d'un lien vers le communiqué de presse concernant la prolongation de la campagne de correction. ([#6591](https://github.com/betagouv/ma-cantine/issues/6591))
- Modification de l'affichage des objectifs viande et poisson dans la synthèse de télédéclaration. ([#6619](https://github.com/betagouv/ma-cantine/issues/6619))
- Remplacement du nombre de couverts jours par le nombre de couverts annuels dans la gestion des satellites. ([#6624](https://github.com/betagouv/ma-cantine/issues/6624))
- Ajout du nouveau statut "CORRECTION" pour les bilans. ([#6616](https://github.com/betagouv/ma-cantine/issues/6616))
- Réorganisation des actions disponibles sur les cantines. ([#6613](https://github.com/betagouv/ma-cantine/issues/6613))

### Évolutions techniques
- Refactorisation du code lié aux anciens imports de bilans. ([#6642](https://github.com/betagouv/ma-cantine/issues/6642))
- Amélioration du script de resubmit pour la télédéclaration, permettant de traiter une liste d'ID de diagnostics. ([#6644](https://github.com/betagouv/ma-cantine/issues/6644))
- Optimisation des requêtes pour accélérer le chargement des cantines et des utilisateurs dans l'administration. ([#6579](https://github.com/betagouv/ma-cantine/issues/6579), [#6580](https://github.com/betagouv/ma-cantine/issues/6580))
- Ajout de la récupération des données géo en temps réel pour le SIRET et le SIREN des cantines. ([#6570](https://github.com/betagouv/ma-cantine/issues/6570))
- Amélioration de la gestion des transactions pour la commande de déclaration des données. ([#6589](https://github.com/betagouv/ma-cantine/issues/6589))
- Mise à jour de la configuration pour refléter la nouvelle date de fin de la campagne de correction. ([#6575](https://github.com/betagouv/ma-cantine/issues/6575))
- Amélioration du script de génération 1TD1Site pour gérer l'année 2025. ([#6618](https://github.com/betagouv/ma-cantine/issues/6618))
- Ajout de la librairie Marianne. ([#6621](https://github.com/betagouv/ma-cantine/issues/6621))

### Autres changements
- Correction d'une faute d'orthographe dans les mentions légales. ([#6640](https://github.com/betagouv/ma-cantine/issues/6640))
- Suppression d'un tiret superflu dans le texte "ma-cantine". ([#6633](https://github.com/betagouv/ma-cantine/issues/6633))
- Correction de l'affichage du nom "ma-cantine" dans les statistiques. ([#6608](https://github.com/betagouv/ma-cantine/issues/6608))
- Suppression de l'icône du bouton d'archivage d'une cantine. ([#6606](https://github.com/betagouv/ma-cantine/issues/6606))
- Documentation de l'API Stats avec l'ajout des enums pour les filtres. ([#6584](https://github.com/betagouv/ma-cantine/issues/6584))
- Suppression d'un message d'alerte sur les données incorrectes pour l'année 2024 dans l'observatoire. ([#6620](https://github.com/betagouv/ma-cantine/issues/6620))
- Modification du texte affiché pour les utilisateurs connectés concernant la prolongation de la campagne. ([#6567](https://github.com/betagouv/ma-cantine/issues/6567))
- Suppression de l'obligation de renseigner l'administration de tutelle pour le secteur "Autres structures d'enseignement". ([#6569](https://github.com/betagouv/ma-cantine/issues/6569))

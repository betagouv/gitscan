## Changelog : ma-cantine (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions de ma-cantine se concentrent sur l'amélioration des fonctionnalités de télédéclaration des bilans, notamment en préparation de la fin de la campagne de correction. Des corrections de bugs et des améliorations techniques ont également été apportées pour optimiser la plateforme et faciliter la gestion des données.

### Évolutions fonctionnelles
- **Télédéclarations :** Ajout d'un script permettant de télédéclarer une liste de bilans hors campagne.
- **Télédéclarations :** Amélioration de la commande de resubmit pour permettre la télédéclaration d'une liste de diagnostics par leur ID.
- **Campagne de correction :** Mise à jour du bandeau d'information concernant la campagne de correction.
- **Tableau de bord :** Ajout d'un filtre permettant d'afficher les bilans télédéclarés.
- **Gérer mes satellites :** Remplacement du nombre de couverts jours par le nombre de couverts annuels.
- **Campagne de correction :** Ajout du nouveau statut "CORRECTION" pour les bilans.
- **Cantines :** Réorganisation des actions disponibles dans l'interface.
- **Télédéclarations :** Suppression du bouton "Modifier mes données" si le bilan n'est pas télédéclaré.
- **Télédéclarations :** Déplacement du bloc de correction dans l'interface.

### Évolutions techniques
- **Données Géo :** Mise à jour du fichier de référence PAT (20250224 -> 20250710).
- **Cantines :** Suppression des tâches asynchrones liées à la récupération des données géographiques pour simplifier le code.
- **Télédéclarations :** Clarification et simplification du code des règles métiers encadrant la télédéclaration.
- **Diagnostics :** Modification de l'API pour renvoyer uniquement les pourcentages d'approbation des diagnostics.
- **ETL :** Ajout de 1TD1Site dans les exports bruts.
- **1TD1Site :** Amélioration du script de génération pour gérer les données de 2025.
- **1TD1Site :** Branchement pour supporter les données de 2025 dans l'observatoire.
- **Admin :** Ajout d'un filtre pour afficher les télédéclarations générées [1TD1Site] ([#6582](https://github.com/betagouv/ma-cantine/issues/6582)).
- **Dette Technique :** Suppression du code lié aux anciens imports de bilans.

### Autres changements
- **Corrections :** Correction de liens et de tests suite aux évolutions récentes.
- **Corrections :** Correction de l'affichage du pourcentage des valeurs durables et de qualité dans les télédéclarations.
- **Corrections :** Correction du non affichage de la police Marianne.
- **Corrections :** Correction d'une faute d'orthographe dans les mentions légales.
- **Corrections :** Exclusion des cantines supprimées des calculs de statistiques.
- **Améliorations :** Ajout d'un indicateur du nombre de filtres sélectionnés dans la liste déroulante.
- **Améliorations :** Clarification des messages d'erreur pour la modification des RSAT des satellites.
- **Améliorations :** Suppression du tiret dans le texte "ma-cantine".
- **Améliorations :** Masquage du message "Non renseignée" pour la colonne 'commune' dans le tableau de bord pour les groupes.
- **Refactoring :** Nettoyage de printemps du code.

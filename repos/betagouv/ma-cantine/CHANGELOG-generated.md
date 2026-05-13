## Changelog : ma-cantine (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des télédéclarations, notamment en vue de la fin de la campagne de correction. Des optimisations techniques ont également été apportées, notamment concernant les données géographiques et les exports de données. Enfin, quelques corrections de bugs et améliorations de l'interface utilisateur ont été réalisées.

### Évolutions fonctionnelles
- **Télédéclarations :** Ajout d'un script permettant de télédéclarer une liste de bilans en dehors de la campagne en cours.
- **Tableau de bord :** Ajout d'un filtre permettant d'afficher les bilans télédéclarés.
- **Campagne de correction :** Mise à jour du bandeau d'information concernant la campagne de correction.
- **Diagnostics :** Ajout d'un filtre dans l'interface d'administration pour afficher les télédéclarations générées.
- **Cantines publiques :** Affichage uniquement des pourcentages et badges de bilan, et non des valeurs brutes.

### Évolutions techniques
- **Données Géo :** Mise à jour du fichier de référence PAT (Passage à la version 20250710).
- **ETL :** Ajout des mesures de gaspillage (WasteMeasurements) dans les exports brutes (dbt).
- **Refactoring (Achats) :** Regroupement des statistiques d'agrégation dans une queryset dédiée et listage des groupes de caractéristiques pour faciliter leur réutilisation.
- **Refactoring (Diagnostics) :** Amélioration de la commande `diagnostic_fill_invalid_reason_list` (application et récapitulatif des statistiques).
- **Refactoring (Télédéclarations) :** Clarification et simplification du code des règles métiers encadrant les télédéclarations.
- **Refactoring (Cantines) :** Suppression des tâches asynchrones liées à la récupération des données géographiques et du code associé.
- **Refactoring (Scripts) :** Nettoyage général du code des scripts.
- **Refactoring (Dette Technique) :** Suppression du code lié aux anciens imports de bilans.
- **API :** L'API Diagnostics renvoie désormais uniquement les pourcentages d'approbation.

### Autres changements
- **CGU :** Correction de l'URL vers les conditions générales d'utilisation du frontend.
- **Mentions Légales :** Correction d'une faute d'orthographe.
- **UI :** Suppression du tiret dans le texte "ma-cantine".
- **Filtre :** Ajout d'un indicateur du nombre de filtres sélectionnés dans la liste déroulante.
- **Police Marianne :** Correction du problème d'affichage de la police.
- **Tests :** Correction des tests suite aux ajouts de règles métiers récents concernant les télédéclarations.

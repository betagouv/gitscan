## Changelog : ma-cantine (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des données, notamment la mise à jour des données géographiques et l'ajout de nouvelles données dans les exports. Des corrections de bugs et des améliorations techniques ont également été apportées, en particulier concernant la télédéclaration et les diagnostics.

### Évolutions fonctionnelles
- Mise à jour du fichier de référence PAT pour les données géographiques.
- Amélioration des messages d'erreur pour les satellites lors de la modification des RSAT en période de télédéclaration.
- Correction de l'affichage du pourcentage des valeurs durables et de qualité en télédéclaration.
- Correction de l'affichage de la police Marianne.
- Ajout d'un filtre "bilan télédéclaré" au tableau de bord.
- Ajout d'un indicateur du nombre de filtres sélectionnés dans la liste déroulante du tableau de bord.
- Correction de l'URL des CGU pour pointer vers le frontend.
- Amélioration du bandeau d'information de la campagne de correction.

### Évolutions techniques
- Ajout des mesures de gaspillage (WasteMeasurements) aux exports bruts (ETL).
- Refactor de l'API Validata pour vérifier la validité des fichiers avant l'export.
- Refactor de l'API Adresse pour rendre l'appel à la fonction indépendant de l'objet 'response'.
- Refactor de l'API Recherche Entreprises pour ne pas utiliser de camelCase dans les résultats.
- Regroupement des statistiques d'agrégation des achats dans une queryset dédiée.
- Liste des groupes de caractéristiques pour faciliter leur réutilisation dans les achats.
- Réorganisation des champs dans les modèles (Meta et timestamps en bas).
- Amélioration de la commande `diagnostic_fill_invalid_reason_list` pour l'application et le récapitulatif des statistiques.
- Suppression du code lié aux anciens imports de bilans.
- Simplification du code des règles métiers encadrant la télédéclaration.
- Homogénéisation des tests des scripts de télédéclaration récemment créés.
- Correction des tests suite aux ajouts de règles métiers récents et à la fin de la campagne de télédéclaration.
- Correction du script de resubmit pour éviter les plantages sur des cas particuliers.
- Clarification des méthodes pour récupérer les dates de fin de campagne de télédéclaration.
- Suppression des tâches asynchrones allant chercher les données géo.
- Exclusion des cantines supprimées des calculs de statistiques.
- Correction de l'API Diagnostics pour renvoyer uniquement les pourcentages d'approbation.

### Autres changements
- Petit nettoyage de code dans les scripts.
- Mise à jour des dépendances Django et Wagtail.

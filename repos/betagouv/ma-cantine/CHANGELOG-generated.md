## Changelog : ma-cantine (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des télédéclarations, notamment en vue de la fin de la campagne de correction. Des corrections ont été apportées pour assurer le bon fonctionnement des scripts et de l'interface utilisateur, ainsi que des optimisations techniques pour simplifier le code et améliorer les performances. La mise à jour des données géographiques PAT a également été effectuée.

### Évolutions fonctionnelles
- Ajout d'un script permettant de télédéclarer une liste de bilans hors campagne.
- Amélioration des messages d'erreur pour la modification des RSAT des satellites pendant la campagne de télédéclaration.
- Correction de l'affichage du pourcentage des valeurs durables et de qualité dans les télédéclarations.
- Correction de l'affichage de la police Marianne.
- Ajout d'un filtre "bilan télédéclaré" au tableau de bord.
- Ajout des dates de campagne dans l'interface.
- Remplacement du nombre de couverts jours par le nombre de couverts annuels dans la gestion des satellites.
- Ajout du statut "CORRECTION" pour les bilans.
- Réorganisation des actions dans la gestion des cantines.
- Suppression du message "Non renseignée" pour la colonne "commune" dans le tableau de bord pour les groupes.
- Amélioration de l'affichage de l'objectif viande et poisson dans la synthèse de télédéclaration.

### Évolutions techniques
- Suppression du code lié aux anciens imports de bilans.
- Refactorisation du code des règles métiers encadrant la télédéclaration.
- Suppression des tâches asynchrones pour la récupération des données géographiques.
- Amélioration du script de génération 1TD1Site pour gérer l'année 2025.
- Optimisation du queryset `with_satellites_snapshot_stats` pour pré-calculer certains champs.
- Simplification du code des méthodes de récupération des dates de fin de campagne.
- Homogénéisation des tests des scripts de télédéclaration.
- Nettoyage de code général (petit ménage de printemps).
- Correction de bugs et amélioration de la stabilité des scripts de télédéclaration.

### Autres changements
- Mise à jour du fichier de référence PAT (données géographiques) du 24 février 2025 au 10 juillet 2025.
- Correction de fautes d'orthographe dans les mentions légales.
- Mise à jour de la dépendance Django (5.2.11 -> 5.2.13).

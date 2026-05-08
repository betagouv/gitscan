## Changelog : ma-cantine (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la télédéclaration des bilans, notamment en vue de la fin de la campagne de correction. Des corrections ont été apportées pour assurer le bon fonctionnement des scripts et de l'interface utilisateur, ainsi que des optimisations techniques pour simplifier le code et améliorer la gestion des données. Des mises à jour des données géographiques ont également été intégrées.

### Évolutions fonctionnelles
- Ajout d'un script permettant de télédéclarer une liste de bilans hors campagne.
- Amélioration des messages d'erreur pour la modification des RSAT des satellites durant la campagne de télédéclaration.
- Correction de l'affichage du pourcentage des valeurs durables et de qualité en télédéclaration.
- Correction de l'affichage de la police Marianne.
- Ajout d'un filtre "bilan télédéclaré" au tableau de bord.
- Ajout des dates de campagne dans l'interface.
- Ajout du nouveau statut "CORRECTION" pour les bilans.
- Réorganisation des actions sur les fiches cantines.
- Remplacement du nombre de couverts jours par le nombre de couverts annuels dans la gestion des satellites.
- Suppression du message "Non renseignée" pour la colonne 'commune' du tableau de bord pour les groupes.
- Amélioration de l'affichage de l'objectif viande et poisson dans la synthèse de télédéclaration.

### Évolutions techniques
- Refactorisation du code lié aux données géographiques : suppression des tâches asynchrones et du code associé.
- Simplification du code des règles métiers encadrant la télédéclaration.
- Amélioration de la commande de resubmit pour la télédéclaration, permettant de traiter une liste d'ID de diagnostics.
- Optimisation de la récupération des dates de fin de campagne.
- Suppression du code lié aux anciens imports de bilans.
- Pré-calcul de certains champs pour le script de génération 1TD1Site.
- Mise à jour du fichier de référence PAT pour les données géographiques (20250224 -> 20250710).

### Autres changements
- Correction du lien dans le bandeau d'information de la campagne de correction.
- Correction des tests suite aux ajouts de règles métiers et à la fin de la campagne de correction.
- Exclusion des cantines supprimées des calculs de statistiques.
- Ajout de tests pour les scripts récemment créés.
- Nettoyage de code (petit ménage de printemps).
- Correction d'une faute d'orthographe dans les mentions légales.
- Suppression d'un tiret superflu dans le texte "ma-cantine".
- Mise à jour de la version de Django (5.2.11 -> 5.2.13).

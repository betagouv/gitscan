## Changelog : ma-cantine (30 derniers jours, au 16 avril 2026)

### Résumé
Les dernières mises à jour de ma-cantine se concentrent sur l'amélioration de la campagne de correction des bilans, notamment en ajustant l'interface utilisateur et en introduisant un nouveau statut pour les bilans en cours de correction. Des améliorations ont également été apportées à la gestion des données, en particulier concernant l'intégration des données 1TD1Site et la télédéclaration, ainsi que des corrections de bugs et des optimisations de performance.

### Évolutions fonctionnelles
- Ajout d'un nouveau statut "CORRECTION" pour les bilans en cours de correction.
- Modification de l'affichage du nombre de couverts, passant des couverts journaliers aux couverts annuels pour les satellites.
- Déplacement du bloc de correction dans l'interface de télédéclaration pour une meilleure organisation.
- Mise à jour du bandeau d'information concernant la campagne de correction.
- Suppression du bouton "Modifier mes données" si le bilan n'est pas télédéclaré.
- Amélioration de la commande de resubmit pour la télédéclaration, permettant de traiter une liste d'ID de diagnostics.
- Ajout des dates de campagne de correction dans l'interface.

### Évolutions techniques
- Intégration des données 1TD1Site dans les exports brutes pour l'ETL.
- Amélioration du script de génération 1TD1Site pour gérer l'année 2025.
- Refactor de certains querysets pour optimiser les performances, notamment pour les diagnostics et les télédéclarations.
- Mise à jour des dépendances Django (de 5.2.11 à 5.2.13).
- Amélioration de la gestion des arrondis dans le script de génération 1TD1Site.
- Ajout de health checks sur la base de données Postgres pour les tâches asynchrones.
- Utilisation de `django-dirtyfields` pour détecter les changements de champs.
- Augmentation de la fréquence des exports de données pour Metabase et l'Open Data.

### Autres changements
- Correction d'une faute d'orthographe dans les mentions légales.
- Suppression d'un tiret superflu dans le texte "ma-cantine".
- Ajout d'un fichier dédié pour la police Marianne et suppression de l'import en double.
- Modification du message d'alerte sur les données incorrectes pour l'année 2024 dans l'observatoire.
- Regroupement de l'affichage de l'objectif viande et poisson dans la synthèse de télédéclaration.
- Amélioration de l'affichage des actions dans l'interface Cantine.
- Ajout de documentation pour l'API Stats (enum pour les filtres secteurs, départements et régions).
- Ajout de ressources (clausier et protocole de pesée).
- Correction de l'affichage du nom "ma-cantine" dans les statistiques.
- Suppression de l'icône du bouton "Archiver une cantine".
- Remplacement de "supprimer" par "archiver" pour l'action d'archiver une cantine.
- Création d'une page interne pour afficher les statistiques Metabase via iframe.
- Ajout d'un lien vers le communiqué de presse concernant la prolongation de la campagne.
- Correction d'une erreur d'arrondi des décimales pour les totaux viandes et poissons.
- Correction d'un bug empêchant la modification d'une cantine via API si le SIRET était manquant.
- Amélioration de l'affichage des secteurs d'activités dans l'administration.
- Amélioration de l'affichage des utilisateurs et des cantines dans l'administration.
- Correction d'un bug dans le calcul des pourcentages et des objectifs Égalim.
- Amélioration de la gestion des données géo des cantines.
- Correction d'un bug dans les filtres de l'API Stats.
- Amélioration de la gestion des utilisateurs Brevo.
- Amélioration de la gestion des données géo des cantines lors de la modification du code INSEE.

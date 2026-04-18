## Changelog : ma-cantine (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions de ma-cantine se concentrent sur la campagne de correction des bilans, avec des améliorations de l'interface et de la gestion des statuts. Des optimisations ont également été apportées à l'ETL et aux données géographiques des cantines, ainsi qu'à l'administration de l'application.

### Évolutions fonctionnelles
- Ajout du nouveau statut "CORRECTION" pour les bilans dans le cadre de la campagne de correction.
- Modification de l'affichage du nombre de couverts, passant de "jours" à "annuels" dans la gestion des satellites.
- Déplacement du bloc de correction pour une meilleure organisation de l'interface.
- Réorganisation des actions disponibles sur la page "Cantine".
- Après la fin de la campagne, il n'est plus possible de modifier un bilan en mode brouillon.
- Suppression du bouton "Modifier mes données" si le bilan n'est pas télédéclaré.
- Correction de l'affichage du badge "À télédéclarer" pour les RSAT rejoignant un groupe après avoir soumis leur bilan.
- Correction du total de remplissage automatique pour la catégorie France dans les télédéclarations.
- Correction de l'affichage des montants incorrects dans la modale de prévisualisation des télédéclarations.
- Remplacement de "supprimer" par "archiver" pour l'action d'archivage d'une cantine.
- Ajout d'une page interne affichant les statistiques de Metabase via iframe.
- Ajout d'un lien vers le communiqué de presse concernant la prolongation de la campagne.
- Correction de l'affichage du nom "ma-cantine" dans les statistiques.
- Suppression de l'icône du bouton "Archiver une cantine".
- Correction d'un arrondi incorrect des décimales pour les totaux viandes et poissons dans les télédéclarations détaillées.

### Évolutions techniques
- Amélioration de la commande de resubmit des télédéclarations pour traiter une liste d'ID de diagnostics.
- Refactor de l'ETL pour inclure 1TD1Site dans les exports brutes.
- Optimisation des requêtes pour accélérer le chargement des cantines et des utilisateurs dans l'interface d'administration.
- Amélioration de la gestion des arrondis dans le script de génération 1TD1Site.
- Ajout d'un health check sur la base de données PostgreSQL pour les tâches asynchrones.
- Mise à jour de Django en version 5.2.13.
- Amélioration de la gestion des données géographiques des cantines, avec récupération en temps réel et script de réinitialisation.
- Ajout de logs pour le géobot.
- Refactor de la gestion des secteurs d'activités pour enlever l'obligation de l'administration de tutelle pour le secteur "Autres structures d'enseignement".
- Utilisation des TextChoices pour afficher les valeurs des champs dans l'interface d'administration.
- Amélioration de la gestion des données géo dans les télédéclarations.

### Autres changements
- Ajout de ressources (clausier et protocole de pesée).
- Ajout d'enum pour les filtres secteurs, départements et régions dans la documentation de l'API Stats.
- Correction d'une faute d'orthographe dans les mentions légales.
- Suppression d'un tiret superflu dans le texte "ma-cantine".
- Ajout de la date de fin de campagne dans le bandeau d'information.
- Modification du message d'alerte sur les données incorrectes pour l'année 2024 dans l'observatoire.
- Ajout de la mention "sites télédéclarés" pour 2024 dans l'observatoire.
- Suppression de l'import en double de la police Marianne.
- Ajout d'un fichier dédié à la police Marianne.

## Changelog : ma-cantine (30 derniers jours, au 23 avril 2026)

### Résumé
Les dernières mises à jour de ma-cantine se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du tableau de bord et des filtres, ainsi que sur la gestion de la campagne de correction des télédéclarations. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un filtre "bilan télédéclaré" au tableau de bord ([#6655](https://github.com/betagouv/ma-cantine/issues/6655)).
- Amélioration de l'affichage du nombre de filtres sélectionnés dans la liste déroulante des filtres.
- Masquage du message "Non renseignée" dans la colonne 'commune' du tableau de bord pour les groupes.
- Ajout d'un indicateur visuel pour les diagnostics télédéclarés dans l'administration.
- Mise à jour du bandeau d'information concernant la campagne de correction.
- Modification de l'affichage des objectifs viande et poisson dans la synthèse des télédéclarations.
- Remplacement de "supprimer" par "archiver" pour l'action d'archiver une cantine.
- Création d'une page interne pour afficher les statistiques Metabase via iframe.
- Ajout d'un lien vers le communiqué de presse concernant la campagne de prolongation.
- Modification de l'affichage des secteurs d'activités dans l'administration.
- Ajout des dates de campagne de correction.
- Modification de l'affichage du nom "ma-cantine" dans les statistiques.
- Suppression de l'icône du bouton d'archivage d'une cantine.

### Évolutions techniques
- Refactorisation du code lié aux anciens imports de bilans.
- Amélioration de la performance du chargement des cantines et des utilisateurs dans l'administration.
- Correction de bugs liés aux tests suite aux ajouts de règles métiers pour les télédéclarations.
- Correction d'un bug empêchant le script de resubmit de télédéclarations de fonctionner correctement.
- Empêche la modification d'un bilan en SUBMITTED ou CORRECTION après la fin de la campagne de correction.
- Ajout de nouveaux querysets pour faciliter l'utilisation des données de télédéclaration générées par 1TD1Site.
- Amélioration du script de génération des bilans 1TD1Site pour gérer l'année 2025.
- Utilisation des informations satellites pour récupérer les données géographiques.
- Correction d'un bug d'arrondi des décimales pour les totaux viandes et poissons.
- Amélioration de la gestion des arrondis dans le script de génération 1TD1Site.
- Ajout d'enum pour les filtres secteurs, départements et régions dans la documentation de l'API.
- Mise à jour de la documentation pour refléter les modifications apportées.

### Autres changements
- Correction d'une faute d'orthographe dans les mentions légales.
- Suppression d'un tiret superflu dans un texte contenant "ma-cantine".
- Création d'un fichier dédié pour la police Marianne et suppression de l'import en double.
- Mise à jour de la police Marianne.
- Mise à jour de la dépendance Django vers la version 5.2.13.

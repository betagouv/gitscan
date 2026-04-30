## Changelog : monlogementetudiant (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'administration des logements et des gestionnaires, avec l'ajout de nouvelles fonctionnalités d'import CSV, d'export de données et de gestion des utilisateurs. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment la refonte de la page de détails des logements et l'ajout de filtres et de widgets pour faciliter la recherche. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- **Import CSV:** Ajout d'une fonctionnalité d'import CSV pour les logements, avec une prévisualisation, un résumé du propriétaire et une gestion des erreurs améliorée [#1234](https://github.com/betagouv/monlogementetudiant/issues/1234).
- **Export CSV:** Possibilité d'exporter la liste des comptes gestionnaires en format CSV.
- **Gestion des utilisateurs:** Amélioration de la gestion des propriétaires et des gestionnaires, avec la possibilité de lier un propriétaire à un compte administrateur.
- **Page de détails des logements:** Refonte complète de la page de détails des logements avec un affichage en onglets pour une meilleure organisation des informations.
- **Filtres et Widgets:** Ajout de nouveaux filtres et widgets pour affiner la recherche de logements (superficie, besoin de logement social, etc.).
- **Visite virtuelle:** Intégration de la possibilité d'ajouter un lien vers une visite virtuelle (3D) pour les logements.
- **Affichage des documents:** Possibilité d'afficher tous les documents associés à un logement.
- **Statistiques d'administration:** Ajout de statistiques pour l'administration, permettant de suivre l'activité et les données clés.
- **Demande sociale:** Ajout de la gestion des demandes de logement social.
- **Nouvelles options de recherche:** Ajout de filtres pour les logements avec des équipements spécifiques (wifi, cuisine, salle de bain).
- **Affichage des aides:** Ajout de widgets pour simuler les aides possibles.
- **Informations sur les logements:** Ajout de l'affichage de la superficie et du type de logement.
- **Politique d'administration des gestionnaires:** Ajout d'une politique d'administration pour les gestionnaires.

### Évolutions techniques
- **Mise à jour Drizzle ORM:** Mise à jour de Drizzle ORM vers la version 0.45.2.
- **Optimisation des migrations:** Optimisation des migrations de la base de données.
- **Indexation PostGIS:** Amélioration de l'indexation PostGIS pour optimiser les requêtes géospatiales.
- **Refonte de l'architecture:** Refonte de certaines parties de l'architecture pour améliorer la maintenabilité et la performance.
- **Amélioration des tests:** Ajout de tests d'intégration et correction de tests existants.
- **Mise à jour Next.js:** Mise à jour de Next.js vers la version 16.2.
- **S3 Upload:** Implémentation de l'upload d'images vers S3.
- **Healthcheck:** Ajout d'un healthcheck pour les villes.
- **Canonical URLs & Metadata:** Ajout de canonical URLs et de metadata pour améliorer le SEO.

### Autres changements
- **Documentation:** Mise à jour de la documentation.
- **Nettoyage du code:** Suppression de code inutile et amélioration de la lisibilité du code.
- **Wording:** Corrections et améliorations du wording dans l'interface utilisateur.
- **Configuration:** Mise à jour de la configuration de l'environnement de développement et de production.
- **Correction de bugs:** Correction de divers bugs et améliorations de la stabilité de l'application.
- **Amélioration des logs:** Ajout de logs plus détaillés pour faciliter le débogage.
- **Suppression des sitemaps:** Suppression des liens vers les sitemaps, car ils sont maintenant gérés par le CMS.

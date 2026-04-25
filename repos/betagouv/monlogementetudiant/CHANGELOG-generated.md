## Changelog : monlogementetudiant (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration significative de l'administration des logements et des résidences, notamment avec l'ajout d'un outil d'import CSV avancé avec suivi de progression.  Des améliorations ont également été apportées à l'interface utilisateur, à la recherche et à la gestion des partenaires. Plusieurs corrections de bugs et optimisations ont été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Import CSV Amélioré :** Ajout d'un outil d'import CSV pour les résidences avec suivi de progression via SSE, aperçu des données et résumé du propriétaire. [#1234](https://github.com/betagouv/monlogementetudiant/issues/1234)
- **Filtres de recherche :** Possibilité de filtrer les actualités disponibles.
- **Widgets Calculatrice/Simulateur Aides :** Intégration de nouveaux widgets pour aider les étudiants à calculer les aides auxquelles ils peuvent prétendre.
- **Affichage des logements :** Amélioration de l'affichage des logements, incluant un badge pour les disponibilités inconnues.
- **Partenaires :** Importation et normalisation des noms des partenaires.
- **Visite Virtuelle :** Ajout de la possibilité d'intégrer des visites virtuelles via un lien YouTube.
- **Demande Sociale :** Intégration de la gestion des demandes sociales.
- **Informations Résidences :** Possibilité d'éditer la superficie et le prix des logements lors de la modification.
- **Page Détails Logement :** Refonte de la page de détails des logements avec un système d'onglets.
- **Gestion des propriétaires :** Possibilité de lier un propriétaire à un logement depuis l'administration.
- **Statistiques Administration :** Ajout de statistiques pour l'administration.
- **Documents :** Affichage de tous les documents associés à un logement.
- **Fac Habitat :** Ajout de la gestion de Fac Habitat, incluant la validation des données importées.

### Évolutions techniques
- **Optimisation des migrations :** Amélioration de l'application des migrations de base de données.
- **Mise à jour Next.js :** Mise à jour vers la version 16.2 de Next.js.
- **S3 Upload :** Implémentation de l'upload d'images vers Amazon S3.
- **Indexation PostGIS :** Ajout d'indexation PostGIS pour améliorer les performances des requêtes géospatiales.
- **Suppression de liens Sitemaps :** Suppression des liens vers les sitemaps, désormais gérés sur le CMS.
- **Métadonnées :** Création de métadonnées pour chaque page afin d'éviter la duplication et d'améliorer le SEO.
- **Healthcheck Villes :** Ajout d'un healthcheck pour les données des villes.
- **Refactoring :** Plusieurs refactorings de code ont été effectués pour améliorer la maintenabilité.

### Autres changements
- **Documentation :** Mise à jour de la documentation et du fichier README.
- **Tests :** Ajout et amélioration des tests unitaires et E2E.
- **Wording :** Corrections et améliorations du wording sur plusieurs parties de l'application.
- **Correction de bugs :** Correction de nombreux bugs mineurs et améliorations de la stabilité.
- **Amélioration de l'UX/UI :** Diverses améliorations de l'expérience utilisateur et de l'interface utilisateur.
- **Sentry :** Réactivation de Sentry pour le suivi des erreurs.
- **robots.txt :** Ajout d'un fichier robots.txt pour contrôler l'indexation par les moteurs de recherche.

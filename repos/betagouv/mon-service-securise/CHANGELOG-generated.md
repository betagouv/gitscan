## Changelog : mon-service-securise (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la migration vers une nouvelle architecture SPA (Single Page Application) pour améliorer l'expérience utilisateur et la performance de l'application.  De nombreuses pages ont été converties, notamment la page service, décrire V2, les mesures, et les contacts utiles. Des améliorations ont également été apportées à la gestion des administrateurs et des entités, ainsi qu'à l'interface utilisateur générale.

### Évolutions fonctionnelles
- Ajout de la gestion des administrateurs :
    - Possibilité d'ajouter des entités administrées via la console d'administration.
    - Récupération des utilisateurs administrés et supervisés.
    - Ajout d'une page listant les utilisateurs pour un administrateur d'organisation.
- Amélioration de la gestion des entités :
    - Ajout d'une route API pour lister les entités d'un administrateur ou superviseur.
    - Spécialisation du dépôt de données pour l'administration.
- Nouvelle fonctionnalité : Ajout d'une méthode pour lister les entités d'un administrateur ou superviseur.
- Amélioration de l'export CSV des mesures : correction du traitement du département vide et navigation hors de la SPA pour l'export.
- Ajout de la page "Communauté" sur la page d'accueil.
- Ajout de landing pages pour "Sécurisez votre service numérique" et "Industrialisez vos homologations".
- Ajout de la navigation au sein du parcours d'homologation.
- Ajout de la page "Indice Cyber" dans la SPA.
- Ajout des risques V1 à la SPA et à l'API du service complet.
- Ajout de la possibilité de reprendre une homologation via une nouvelle route d'API.
- Ajout de la page "Récapitulatif" au parcours d'homologation.
- Ajout de la page "Avis" au parcours d'homologation.
- Ajout de la page "Documents" au parcours d'homologation.
- Ajout de la page "Téléchargement du dossier" au parcours d'homologation.

### Évolutions techniques
- Migration vers une architecture SPA pour plusieurs pages (Page Service, Décrire V2, Mesures, Contacts Utiles).
- Conversion de nombreux composants et modèles en TypeScript pour une meilleure typage et maintenabilité.
- Refonte de la navigation principale avec le composant `dsfr-navigation`.
- Utilisation du `dsfr-header` pour l'en-tête de l'application.
- Amélioration de la structure du code et extraction de méthodes privées.
- Mise à jour de nombreuses dépendances (eslint, axios, basic-ftp, etc.).
- Suppression de code obsolète (anciennes vues pug).
- Utilisation du nouveau header dans la page service.
- Suppression des fichiers d'entête.
- Utilisation du dépôt de données dans la route /api/admin/entites.
- Chiffrement des données des tables superviseur et admin_organisations.

### Autres changements
- Mise en avant de la formation sur l'interface.
- Correction de typos et amélioration de la lisibilité du code.
- Amélioration des styles et de la structure de certains blocs de la page d'accueil.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs et améliorations de la performance.
- Ajout de commentaires et documentation pour faciliter la compréhension du code.
- Correction de problèmes de CSS et d'affichage.
- Correction de problèmes liés à la gestion des états et des données.
- Amélioration de la gestion des erreurs et des exceptions.

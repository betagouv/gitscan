## Changelog : monlogementetudiant (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'import de données (CSV, CLI), l'ajout de fonctionnalités pour les administrateurs (gestion des typologies, suivi des jobs, statistiques), et l'optimisation de l'expérience utilisateur, notamment sur la page de recherche et la gestion des logements. Des corrections de bugs et des améliorations techniques ont également été apportées pour stabiliser la plateforme.

### Évolutions fonctionnelles
- **Import de données :**
    - Amélioration de l'import CSV avec affichage de la progression via SSE, prévisualisation et résumé pour les propriétaires. [#2345](lien vers PR)
    - Synchronisation du formulaire d'import CSV avec l'interface CLI.
    - Validation du payload lors de l'import CSV.
- **Interface administrateur :**
    - Ajout de la possibilité pour les administrateurs d'ajouter des typologies aux logements importés.
    - Création d'un écran d'administration pour suivre les jobs planifiés.
    - Ajout de statistiques pour les propriétaires.
- **Recherche et affichage des logements :**
    - Ajout de filtres sur la page de recherche.
    - Amélioration de la réactivité du widget de recherche.
    - Ajout d'un widget affichant les logements à proximité avec des informations supplémentaires.
    - Affichage d'un badge pour les disponibilités inconnues.
- **Gestion des logements :**
    - Amélioration du formulaire de mise à jour et de création des logements.
    - Possibilité de gérer plusieurs adresses pour un logement.
    - Ajout de champs pour la superficie et les besoins en logement social lors de l'import CSV.
- **Authentification :**
    - Amélioration de la gestion des erreurs d'authentification et des cookies.
- **Autres :**
    - Ajout d'une politique d'administration pour les gestionnaires.
    - Ajout d'un bandeau NPS (Net Promoter Score).
    - Ajout d'une fonctionnalité de calculatrice de budget et de simulateur d'aides.

### Évolutions techniques
- **Infrastructure :**
    - Mise à jour de pnpm vers une version LTS.
    - Mise à jour de Next.js.
- **Base de données :**
    - Optimisation de requêtes SQL.
    - Ajout de contraintes `ON DELETE CASCADE` pour améliorer l'intégrité des données.
- **Code :**
    - Refactoring du code pour améliorer la lisibilité et la maintenabilité.
    - Nettoyage du code (suppression de code inutile).
    - Utilisation de Zod pour la validation des variables d'environnement (Brevo, autres).
    - Suppression des liens vers les sitemaps, désormais gérés par le CMS.
    - Ajout de tests d'intégration.
    - Mise à jour de la librairie Drizzle ORM.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et amélioration des wordings.
- Correction de problèmes liés aux tests et à la construction du projet.
- Mise à jour des dépendances.
- Amélioration de la gestion des métadonnées pour le SEO.
- Ajout de tests E2E.
- Correction de problèmes de rendu sur mobile.

## Changelog : monlogementetudiant (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'import de données (CSV, CLI), l'ajout de nouvelles fonctionnalités pour les gestionnaires et les propriétaires (statistiques, export de comptes), ainsi que sur des corrections de bugs et des optimisations de l'interface utilisateur, notamment au niveau de la calculatrice de budget et des filtres de recherche. Des améliorations ont également été apportées à l'authentification et à la gestion des adresses.

### Évolutions fonctionnelles
- Ajout d'aides à la mobilité CROUS ([#87edc53](https://github.com/betagouv/monlogementetudiant/pull/87edc53)).
- Les administrateurs peuvent maintenant ajouter des typologies de logements lors de l'import de données ([#5cedac2](https://github.com/betagouv/monlogementetudiant/pull/5cedac2)).
- Amélioration de l'import CSV avec une barre de progression, un aperçu et un résumé pour les propriétaires ([#00057f6](https://github.com/betagouv/monlogementetudiant/pull/00057f6)).
- Ajout de statistiques pour les propriétaires.
- Possibilité d'exporter la liste des comptes gestionnaires.
- Ajout d'un filtre pour afficher les logements avec des actualités disponibles.
- Ajout de la fréquence de calcul de budget dans la calculatrice.
- Ajout d'une politique d'administration pour les gestionnaires.
- Amélioration de la gestion des adresses multiples.
- Ajout d'une bannière NPS (Net Promoter Score).
- Ajout de métadonnées pour les pages génériques et souveraines, améliorant le SEO.
- Envoi d'un email aux propriétaires lors de la création de leur compte.
- Ajout d'un widget logement avec des logements à proximité.
- Amélioration du formulaire de création/modification de résidences.

### Évolutions techniques
- Mise à jour de Drizzle ORM vers la version 0.45.2.
- Amélioration de l'architecture pour gérer les métadonnées des pages.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Optimisation des requêtes SQL.
- Mise à jour de la version de Next.js.
- Passage à une version LTS de pnpm.
- Amélioration de la gestion des variables d'environnement avec Zod.
- Correction de problèmes liés aux cookies d'authentification.
- Amélioration de la gestion des erreurs d'authentification.
- Ajout de tests d'intégration.

### Autres changements
- Correction de bugs mineurs liés à l'interface utilisateur (calculatrice, filtres, etc.).
- Amélioration de la réactivité du widget.
- Correction de problèmes liés aux littéraux romains.
- Amélioration de la gestion des erreurs dans le CI/CD.
- Suppression des liens vers les sitemaps (maintenus sur le CMS).
- Correction de typos et amélioration de la documentation.
- Suppression de colonnes inutilisées dans la base de données.
- Correction de problèmes liés aux breadcrumbs.
- Correction de problèmes liés à la vérification de la signature.
- Amélioration de la gestion des images.
- Correction de problèmes liés à la redirection après connexion.

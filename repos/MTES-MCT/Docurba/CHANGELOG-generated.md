## Changelog : Docurba (30 derniers jours, au 11 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur Nuxt3, notamment concernant la gestion des procédures, des événements et des PLU. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de l'application. Des optimisations techniques ont également été réalisées, notamment au niveau de l'infrastructure et de la sécurité, avec l'ajout de l'authentification Supabase et la configuration de Nginx.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la gestion des événements liés aux procédures, avec la distinction des événements antérieurs et postérieurs à la loi Huwart.
- Correction d'un bug empêchant la création de PLU avec plusieurs communes [#issue](https://github.com/MTES-MCT/Docurba/issues/).
- Possibilité de filtrer les types de procédures par date de début.
- Affichage du statut des procédures dans la liste des événements.
- Amélioration de la recherche et de l'affichage des collectivités et communes via une API interne.
- Publication de la page de lecture des PAC (Plans d'Action Concertés).
- Ajout d'une indication visuelle pour les procédures antérieures à la loi Huwart.
- Amélioration de la sélection des types de procédures.
- Correction d'un bug qui affichait des projets automatiques dans la liste des PACs.
- Correction d'un bug qui empêchait la détection de tous les événements de prescription.
- Correction d'un bug qui empêchait de filtrer correctement les événements de prescription.
- Ajout de la possibilité de récupérer les collectivités via l'API Django.

### Évolutions techniques
- Mise en place de l'authentification Supabase avec gestion des sessions et des utilisateurs.
- Configuration de Nginx pour la gestion du reverse proxy, la limitation du débit et la diffusion des fichiers statiques.
- Ajout d'alertes Slack lors des déploiements.
- Utilisation de `curl` à la place de `wget` pour les requêtes HTTP.
- Amélioration des tests API Django.
- Ajout de nouvelles catégories de PAC et d'une catégorie d'événement.
- Mise à jour des dépendances : `supabase`, `ruff`, `django-filter`, `djangorestframework`, `cryptography`.
- Amélioration des performances des tests Django.
- Ajout de tests pour l'API Django.
- Correction de problèmes de CORS en environnement local.
- Ajout de commentaires dans le code.
- Suppression de dépendances inutiles (whitenoise, django-revproxy).
- Utilisation explicite de l'URL de l'API Docurba dans Nuxt.
- Refactorisation du code Nuxt pour améliorer la lisibilité et la maintenabilité.
- Ajout de la gestion des variables d'environnement pour l'URL Nuxt3.

### Autres changements
- Documentation : mise à jour de la documentation interne.
- Configuration : ajout d'une tâche quotidienne pour vérifier les mises à jour des dépendances.
- Nettoyage du code et suppression de code commenté.
- Ajout d'un champ `last_updated_at` aux procédures.
- Mise à jour des types d'événements dans la base de données.
- Correction de conflits de migration Django.
- Suppression des événements de fin d'échéance pour se conformer à la loi Huwart.
- Modification du nom des procédures lors de la mise à jour du type de document.
- Ajout d'un champ `last_sign_in_at` au modèle User.
- Ajout d'un header `Supabase-Authorization` pour les requêtes Supabase.
- Ajout d'une table Session en test dans le docker-compose.
- Ajout de l'email au ProfileFactory.
- Ajout de la dépendance Supabase.
- Correction de conflits de migration.
- Suppression d'un index et d'une fonction inutiles dans la base de données.
- Ajout d'un dossier `exports` ignoré par Git.
- Mise à jour du type de collectivité pour distinguer les EPCI.
- Correction d'un bug lié à la manipulation de variables indéfinies dans Nuxt.
- Correction d'un bug lié à l'affichage du statut des procédures.
- Correction d'un bug qui empêchait la récupération du dernier événement.
- Ajout de la gestion des erreurs lors de la récupération des procédures.
- Ajout d'un trigger pour l'événement de première vue de page dans Nuxt.

## Changelog : docs (30 derniers jours, au 24 juin 2026)

### Résumé
Ce changelog résume les améliorations apportées au projet Docs au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration de l'accessibilité, l'ajout de nouvelles fonctionnalités comme le mode présentateur et la possibilité de quitter un document, ainsi que des corrections de bugs et des optimisations de performance.

### Évolutions fonctionnelles
- Ajout de la possibilité de quitter un document.
- Implémentation du mode présentateur pour les documents.
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches.
- Ajout d'un bouton pour créer des sous-documents.
- Support des liens `mailto:` dans le menu d'aide.
- Ajout d'un badge DPG au README.
- Possibilité d'ajouter un sous-menu "Légal" configurable dans le menu d'aide.
- Amélioration de la gestion des réactions sur les commentaires avec une limite.
- Ajout d'un support pour les liens d'ancrage dans la table des matières.
- Ajout d'un bouton pour laisser un document.

### Évolutions techniques
- Refactorisation de la gestion des événements PostHog côté backend.
- Amélioration des performances de l'arbre de navigation.
- Correction d'un bug lié au service worker causant un rechargement de l'onglet.
- Mise à jour de BlockNote à la version 0.51.4.
- Correction d'un problème de chargement de l'élément "left panel" dans certaines conditions.
- Optimisation de la récupération des commentaires pour éviter les requêtes N+1.
- Correction de problèmes liés à la gestion des threads orphelins.
- Suppression de Crisp (outil de chat).
- Suppression du code de masquage des documents.
- Amélioration de la gestion des erreurs de connexion à la base de données lors des tests.
- Suppression d'un paramètre de tri inutile dans la classe Paginator.
- Mise à jour des dépendances JavaScript.
- Correction d'une vulnérabilité de sécurité.
- Suppression d'une tâche CI inutile.
- Amélioration de la gestion des événements lors de la création, suppression et modification de documents.

### Autres changements
- Corrections de typos dans le guide de contribution.
- Améliorations de l'accessibilité de divers composants (champs de recherche, modales, titres, etc.).
- Mise à jour des chaînes de traduction.
- Ajout d'un badge Snyk au README.
- Amélioration de la gestion du focus dans les modales.
- Correction de problèmes d'affichage de titres longs dans la table des matières.
- Amélioration de l'affichage des icônes dans l'en-tête du panneau gauche.
- Correction de bugs liés à la conversion HTML/Markdown (préservation des éléments formatés).
- Ajout de tests unitaires pour le mode présentateur.
- Correction de bugs liés à l'exportation de documents.
- Ajout de la configuration de PostHog.
- Mise à jour de la documentation pour inclure le nouveau paramètre de configuration.
- Correction de problèmes liés à l'affichage des emojis.
- Amélioration de la gestion des erreurs lors de l'importation de documents.
- Correction de bugs liés au chargement des documents.
- Correction de bugs liés à la gestion des accès aux documents.
- Mise à jour de la documentation pour inclure le nouveau paramètre CONVERSION_UPLOAD_ENABLED.

## Changelog : conseillers-entreprises (30 derniers jours)

### Résumé
Cette période a été marquée par des améliorations de performance, notamment au niveau des requêtes et du chargement des pages, ainsi que par des corrections de bugs impactant l'expérience utilisateur, comme la gestion des erreurs et l'affichage des informations. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour la gestion des antennes et des optimisations, et à la sécurité avec la suppression de fonctionnalités obsolètes.

### Évolutions fonctionnelles
- Amélioration de l'affichage de l'URL du partenaire, affichant désormais l'URL complète et non plus seulement un indicateur.
- Ajout d'une section "Optimisation" unifiée, remplaçant l'ancienne section "Veille".
- Ajout d'une nouvelle fonctionnalité permettant de suivre les antennes et leurs performances.
- Ajout d'un bandeau d'information configurable pour afficher des messages importants aux utilisateurs.
- Amélioration de la gestion des erreurs lors de la suppression d'experts.
- Possibilité de supprimer des experts individuels lors de la suppression d'un utilisateur.
- Ajout d'un avertissement de confidentialité dans le modal de présentation des personnes.
- Correction de l'affichage des URL de sollicitation pour utiliser des paramètres basés sur le slug.
- Correction d'un bug empêchant la navigation correcte dans le processus de création de sollicitation en mode localisation.
- Correction d'un bug qui pouvait transformer une erreur 404 en erreur 500.

### Évolutions techniques
- Ajout de l'intégration avec AppSignal pour le monitoring et le suivi des erreurs.
- Optimisation des requêtes SQL pour améliorer les performances, notamment au niveau de la récupération des sollicitations.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment au niveau des filtres de recherche de besoins.
- Mise à jour de plusieurs dépendances, incluant `nokogiri`, `rack` et `webpack`.
- Amélioration de la couverture des tests unitaires.
- Suppression de code obsolète et de configurations inutiles.
- Simplification de la gestion des formulaires et suppression de paramètres inutiles.
- Utilisation de classes CSS plus modernes pour le style des éléments d'interface.

### Autres changements
- Documentation de l'utilisation d'AppSignal dans le guide d'architecture.
- Mise à jour de la documentation README avec une mention de l'intégration AppSignal.
- Suppression du dossier `.vscode` du suivi Git.
- Correction de typos et amélioration de la qualité du code.
- Amélioration des messages d'internationalisation (i18n).
- Désactivation de robots d'indexation sur l'environnement de staging.
- Suppression de l'option `local: true` dans les formulaires.
- Normalisation du format du code INSEE dans le modèle Solicitation.
- Ajout de tests pour les nouvelles fonctionnalités.

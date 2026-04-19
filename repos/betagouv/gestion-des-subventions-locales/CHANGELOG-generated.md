## Changelog : gestion-des-subventions-locales (30 derniers jours, au 2026-04-17)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment en ajoutant de nouvelles fonctionnalités de filtrage et de tri dans les tableaux, et en améliorant la présentation des données. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de l'infrastructure. L'intégration avec l'API DS a été améliorée avec un proxy GraphQL.

### Évolutions fonctionnelles
- Ajout de filtres par catégorie DETR/DSIL sur les listes de projets.
- Ajout de filtres par budget vert, dotation sollicitée et dossier complet.
- Ajout de filtres par cofinancement, zonage et contractualisation.
- Ajout de colonnes "Zonage" et "Contractualisation" dans les tableaux de projets.
- Ajout de l'affichage des cofinancements.
- Ajout d'une colonne "Taux sollicité" dans l'export des données.
- Possibilité de modifier le taux même si le montant est supérieur à l'assiette.
- Affichage du nom de l'EPCI dans les tableaux de projets.
- Amélioration de la mise en page des arrêtés et lettres.
- Ajout d'un badge "Notifié" pour indiquer les projets notifiés.
- Ajout du lien vers le dossier dans les pages de documents (pour les administrateurs).
- Ajout de la civilité du porteur de projet.
- Amélioration de la performance de la page projet (back-office).
- Filtres et barre d'outils pleine largeur comme le tableau.
- Ajout de filtres par date sur les listes projets, simulations et programmation.
- Correction de la réouverture des modales de statut avec contenu obsolète.
- Changement des titres des pages (Gestion des Subventions Locales -> Turgot).

### Évolutions techniques
- Refactorisation des FilterSets et de la pagination de SimulationDetailView.
- Remplacement des agrégats ProjetService par ProjetQuerySet.totals() pour améliorer les performances.
- Optimisation des requêtes et des prefetch/select_related dans les vues.
- Ajout d'un proxy GraphQL pour l'API DS filtré par instructeurs.
- Configuration du schéma GraphQL DS avec autorisation.
- Stockage du hash du token proxy au lieu du texte brut pour améliorer la sécurité.
- Utilisation de SQLite en mémoire pour les tests CI.
- Amélioration de la configuration des tests CI (permissions, jobs parallèles).
- Ajout d'un workflow de déploiement en production via GitHub Actions.
- Centralisation des événements Matomo dans un fichier de constantes.
- Correction de problèmes de CSP (Content Security Policy) liés à Matomo.
- Refactorisation du système de mentions de publipostage.
- Ajout d'une tâche de nettoyage des projets programmés sur des enveloppes antérieures.
- Empêcher les requêtes HTTP non mockées dans les tests.
- Rendre la variable `dotation_not_treated` déterministe pour stabiliser les tests.
- Validation de l'assiette avant acceptation d'une dotation.
- Correction de l'exécution des tests en parallèle avec pytest-xdist.
- Correction d'un bug empêchant de ne pas sélectionner les projets programmés sur des enveloppes antérieures dans les simulations.
- Correction d'un bug empêchant de ne pas re-basculer un projet sur une enveloppe plus récente lors d'une mise à jour de dossier accepté.

### Autres changements
- Ajout du déploiement de l'environnement de démo.
- Documentation ajoutée pour les instructions de publication en production.
- Nettoyage de code et suppression de code obsolète.
- Mise à jour des templates DGCL.
- Ajout d'une action pour programmer les projets acceptés 2026 vers l'enveloppe 2025.
- Correction de l'affichage des cofinancements sur la page projet.
- Correction de la synchronisation du montant lorsqu'un projet est accepté sur Turgot.
- Correction de l'affichage de l'enveloppe dans les simulations.
- Correction du header CSS pour les lettres et arrêtés.
- Correction de la toolbar Tiptap.
- Correction de la barre de recherche sur la page enveloppe du BO.
- Backport de la branche `main` vers `develop`.
- Mise en place d'un backup régulier du code source chiffré.

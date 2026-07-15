## Changelog : sylvasan (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette période a été marquée par une forte activité de développement, notamment sur l'application mobile (iOS et Android) et l'interface web. Les améliorations incluent la gestion des follow-ups (suivis), l'ajout de fonctionnalités de suppression de données, l'amélioration de la gestion des images et des vocabulaires, ainsi que des corrections de bugs et des optimisations de performance. De nombreuses mises à jour de dépendances ont également été intégrées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- **Follow-ups :** Ajout de la gestion des follow-ups (suivis) avec la possibilité de les créer, modifier, supprimer et visualiser sur le web et le mobile.  Possibilité d'ajouter des observations à des réponses d'autres personnes et d'afficher les données des followups.
- **Suppression de données :** Implémentation d'une fonctionnalité de suppression de réponses et d'enquêtes avec confirmation.
- **Gestion des images :** Amélioration de la gestion des images, notamment lors de la sauvegarde de brouillons et de l'affichage dans les résumés.
- **Vocabulaires :** Ajout du chargement des vocabulaires pour l'affichage des réponses.
- **Authentification :** Ajout de messages d'erreur pour l'authentification et d'un renvoi d'email de confirmation.
- **Géolocalisation :** Amélioration de la gestion de la géolocalisation avec la possibilité de choisir une position en touchant la carte et d'afficher les coordonnées.
- **Interface utilisateur :** Améliorations de l'interface utilisateur sur le web et le mobile, incluant des ajustements de layout, l'ajout de spinners de chargement et l'amélioration de l'affichage des champs.
- **Synchronisation des données :** Ajout d'un mécanisme automatique de mise à jour des données et d'un indicateur visuel de synchronisation.

### Évolutions techniques
- **Refactoring :** Refactoring de code pour améliorer la lisibilité et la maintenabilité, notamment concernant la validation et la sélection d'organisations/pôles.
- **Typescript :** Ajout de types Typescript pour améliorer la robustesse du code.
- **PostGIS :** Intégration de PostGIS pour la gestion des données géographiques.
- **Tests :** Ajout de tests unitaires pour les follow-ups et les enquêtes.
- **CI/CD :** Mises à jour de la configuration CI/CD.
- **Dépendances :** Mises à jour de nombreuses dépendances (Django, React, Node.js, PostgreSQL, ruff, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- **Architecture Mobile :** Amélioration de l'architecture de l'application mobile (iOS et Android) avec des mises à jour des versions et des librairies utilisées.

### Autres changements
- **Documentation :** Ajout d'un ADR (Architecture Decision Record) concernant le prop-drilling.
- **Configuration :** Ajout d'un document de permissions pour les rôles.
- **Nettoyage de code :** Suppression de code mort et de variables inutilisées.
- **Corrections de bugs :** Correction de plusieurs bugs, notamment concernant la navigation post-followup, la modification des suivis, le stockage des brouillons et le positionnement des éléments d'interface.
- **Mises à jour de version :** Mises à jour des versions Android et iOS.

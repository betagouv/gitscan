## Changelog : monitorenv (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'interface utilisateur et la gestion des données réglementaires. Des corrections ont été apportées pour améliorer l'expérience utilisateur, notamment au niveau de la visualisation des zones de vigilance et de la gestion des missions. Des efforts importants ont été déployés pour optimiser le flux de mise à jour des données réglementaires provenant du CACEM, avec suppression de code obsolète et amélioration de la robustesse.

### Évolutions fonctionnelles
- Amélioration de l'affichage du planning dans la liste des zones de vigilance, avec ajout d'un infobulle pour la période. [#issue_lien_si_disponible]
- Ajout d'un cercle indiquant la période directement dans le nom des zones de vigilance et correction de l'interface utilisateur pour l'affichage étendu.
- Correction de l'affichage des notes sur la timeline des missions.
- Amélioration de la recherche de couches cartographiques avec correction des filtres de tags.
- Ajout de la possibilité d'ajouter des tags liés aux actions environnementales et à la période aux missions.
- Refonte de la table des missions pour la rendre extensible, améliorant ainsi la présentation des informations.
- Ajout de boutons de réinitialisation sur les modales de mission, de rapports et du tableau de bord.
- Ajout de nouvelles tags.
- Correction de l'affichage des identifiants de mission (suppression des ellipses).
- Ajout de colonnes liées à la plongée lors d'opérations de contrôles conchylicoles.
- Correction de tests unitaires et E2E.

### Évolutions techniques
- Refactorisation du code, notamment pour MonthBox et la gestion des zones de vigilance.
- Suppression de code obsolète lié aux zones réglementaires.
- Amélioration du flux de mise à jour des zones réglementaires provenant du CACEM.
- Correction de requêtes SQL pour les identifiants CACEM.
- Suppression de triggers inutiles pour la mise à jour des zones réglementaires.
- Mise à jour de dépendances : Cypress (14.5.3 -> 15.14.2), @sentry/browser (8.54.0 -> 10.51.0), ol-mapbox-style (12.3.3 -> 13.4.1), python-dotenv (1.2.1 -> 1.2.2), pytest (9.0.2 -> 9.0.3), cryptography (46.0.5 -> 46.0.7), black (26.1.0 -> 26.3.1).
- Correction de type errors.
- Remplacement de `Cypress.env` par `Cypress.expose`.
- Exclusion de `package.lock` de la surveillance de Dependabot.
- Ajout de validation sur les cas d'utilisation de patch.
- Correction de l'import d'un module.

### Autres changements
- Correction d'une faute de frappe dans le README.
- Mise à jour de l'icône de l'interface utilisateur.
- Mise à jour du label "Drone" pour les unités de contrôle.
- Correction de la favicon en production.
- Désactivation du rebase automatique pour Dependabot.
- Ajout d'un message d'avertissement pour les tags incomplets.
- Correction de tests pour les champs patch plongée.
- Suppression du mot "New" pour les zones réglementaires.

## Changelog : resorption-bidonvilles (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment en termes d'accessibilité et de conformité aux standards de design (DSFR). Des corrections de bugs et des optimisations ont été apportées, ainsi que des évolutions concernant la gestion des droits d'accès aux informations et l'ajout de nouvelles fonctionnalités comme la gestion des sites favoris et l'intégration d'une nouvelle phase de diagnostic technique.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité en corrigeant le clic sur les intervenants et le rendu visuel à la navigation au clavier.
- Ajout de la possibilité de marquer des sites comme favoris, avec une gestion des droits d'accès et un affichage dédié dans une nouvelle section "Mes sites".
- Intégration d'une nouvelle phase "Diagnostic technique" dans le processus de résorption, incluant des modifications de la base de données, de l'API et de l'interface utilisateur.
- Amélioration de l'affichage des informations sur les sites, notamment l'ajout du nombre total de mineurs et la possibilité de filtrer par conditions de vie.
- Correction de l'affichage de la date de la phase "official_opening".
- Ajout de la colonne "Financée par la DIHAL" et gestion de sa visibilité selon les droits de l'utilisateur.
- Modification de l'ordre des onglets dans les statistiques, avec activation par défaut de l'onglet "Situation à date".

### Évolutions techniques
- Refactoring important du code lié à la gestion des commentaires, avec création de services et de contrôleurs dédiés, amélioration de la gestion des erreurs et des tests unitaires.
- Amélioration de la gestion des droits d'accès aux informations, notamment pour l'affichage du numéro de téléphone des utilisateurs.
- Optimisation de la recherche de la phase associée dans l'item de phase.
- Utilisation de `Set` pour améliorer la performance de la vérification du type de localisation.
- Mise à jour des dépendances et correction de typages.
- Amélioration de la structure du code et suppression de code obsolète.

### Autres changements
- Suppression de commentaires inutiles.
- Mise à jour de la documentation.
- Ajout d'une popup d'information concernant un futur changement de noms d'actions.
- Correction de liens et de libellés.
- Amélioration de la présentation des données dans l'export Word.
- Ajout de tests unitaires pour la nouvelle fonctionnalité de gestion des sites favoris.

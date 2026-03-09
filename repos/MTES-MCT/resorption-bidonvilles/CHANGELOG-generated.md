## Changelog : resorption-bidonvilles (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité, de la gestion des utilisateurs et de l'expérience utilisateur globale de la plateforme. Des corrections de bugs ont été apportées, notamment concernant l'affichage des données, la gestion des erreurs et la validation des entrées. Des améliorations de l'interface utilisateur ont été implémentées, en particulier pour l'alignement avec le Design System de la République Française (DSFR).

### Évolutions fonctionnelles
- Correction d'un bug d'affichage des lieux [#1436](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1436).
- Simplification de la condition d'affichage d'un élément.
- Correction de l'affichage du bouton "Modifier les options".
- Passage à 6 sites affichés par page.
- Amélioration de l'accessibilité de la liste des sites paginée.
- Ajout d'un onglet de taux par département si plusieurs départements sont représentés.
- Gestion des options de permissions dans la fiche utilisateur.
- Ajout d'une route pour la liste des logs de connexion.
- Possibilité de filtrer les valeurs `undefined`/`null` pour l'export des données.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Correction de l'alerte "Empty label text".
- Amélioration de l'icône et de l'alignement des champs de formulaire.
- Ajout d'icônes pour le mot de passe.
- Correction de l'affichage de l'ID d'action.
- Ajout de la gestion des erreurs SQL pour sécuriser les requêtes.

### Évolutions techniques
- Refactoring et nettoyage des logs de debug.
- Correction de fautes de frappe.
- Simplification du code et regroupement de la gestion de copie de parcelle.
- DSFRisation de plusieurs composants (boutons, tags, etc.).
- Ajout de tests unitaires.
- Création d'une migration pour ajouter le champ de l'ID d'action calculé.
- Transmission de l'ID depuis la base de données avec backup calculé.
- Utilisation de `lodash` pour certaines opérations.
- Amélioration du système de copie.
- Utilisation de `Set` pour optimiser la vérification d'existence.
- Utilisation d'un objet `Error` pour une meilleure gestion des erreurs.
- Utilisation de `formatTimestamp()` pour uniformiser le formatage des dates.

### Autres changements
- Mise à jour de la documentation.
- Suppression de commentaires inutiles.
- Correction de la mention de désabonnement aux courriels automatiques.
- Mise à jour des dépendances.
- Suppression de fichiers inutilisés.
- Correction de problèmes de style et d'accessibilité.

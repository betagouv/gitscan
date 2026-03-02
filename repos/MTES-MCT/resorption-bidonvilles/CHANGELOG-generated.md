## Changelog : resorption-bidonvilles (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment en termes de gestion des logs de connexion, de recherche et d'interface utilisateur. Des corrections de bugs et des optimisations de performance ont également été réalisées. L'application continue d'évoluer pour offrir une meilleure expérience aux agents de l'administration dans leur travail de résorption des bidonvilles.

### Évolutions fonctionnelles
- Ajout de la gestion des options de permissions dans la fiche utilisateur.
- Implémentation de la gestion des logs de connexion : ajout d'une route, d'un modèle, d'un service et d'un composant d'affichage avec filtres, recherche et pagination.
- Amélioration de la recherche : ajout de la possibilité de rechercher des actions par ID, des localisations géographiques et des structures "opérateurs".
- Possibilité de filtrer les actions par structure "opérateur".
- Ajout du taux de MAJ des actions à l'affichage.
- Amélioration de l'affichage des erreurs et des messages d'information avec l'utilisation de composants DSFR (DsfrAlert).
- Ajout d'un onglet affichant les taux par département lorsque plusieurs départements sont représentés.
- Correction de l'alerte "Empty label text".
- Amélioration de l'icône d'erreur pour une meilleure cohérence chromatique.
- Correction du problème d'interprétation du code HTML dans les messages d'erreur.
- Mise à jour du bouton pour l'harmonisation avec le DSFR.
- Ajout de l'export du tri utilisateur.
- Application du tri SQL pour l'export des données.

### Évolutions techniques
- Migration de `isPlural` vers des utilitaires.
- Refactoring du code pour utiliser des composants DSFR (DsfrInput, DsfrButton, DsfrAlert, DsfrTable).
- Amélioration du typage du code.
- Optimisation de la performance de l'affichage des marqueurs sur la carte.
- Sécurisation de la requête SQL lors de l'export des données.
- Ajout de tests unitaires.
- Mise à jour des dépendances.
- Correction de vulnérabilités de sécurité via Snyk.

### Autres changements
- Modification du wording pour l'affichage d'informations.
- Suppression de commentaires inutiles.
- Correction de la police utilisée dans le PDF.
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la lisibilité du code.
- Suppression de code mort.
- Ajout de commentaires pour clarifier certaines parties du code.
- Suppression de console.log inutiles.
- Amélioration de la structure du code.

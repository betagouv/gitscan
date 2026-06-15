## Changelog : proconnect-identite (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la maintenabilité du système, notamment en préparation de la migration vers PostgreSQL 17. Des améliorations ont également été apportées à la gestion des organisations et des certifications, ainsi qu'à l'intégration avec des outils de supervision comme Metabase. Des corrections de bugs et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- Amélioration de la validation automatique des utilisateurs lors de l'inscription, notamment pour les organisations disposant d'un domaine de contact officiel [#1934](https://github.com/proconnect-gouv/proconnect-identite/issues/1934).
- Ajout de la possibilité de spécifier une raison pour le refus d'une certification, stockée en base de données [#1931](https://github.com/proconnect-gouv/proconnect-identite/issues/1931).
- Simplification du processus d'inscription pour les petites organisations civiles ou agricoles disposant d'une adresse email gratuite [#1972](https://github.com/proconnect-gouv/proconnect-identite/issues/1972).
- Ajout de la catégorie juridique "Pôle d'équilibre territorial et rural" [#1982](https://github.com/proconnect-gouv/proconnect-identite/issues/1982).
- Mise en place d'un nouveau mécanisme de calcul pour déterminer si une entité est un service public [#1946](https://github.com/proconnect-gouv/proconnect-identite/issues/1946).

### Évolutions techniques
- Préparation de la base de données pour la compatibilité avec PostgreSQL 17 [#1983](https://github.com/proconnect-gouv/proconnect-identite/issues/1983).
- Ajout d'un index sur la table `users_oidc_clients` pour améliorer les performances des requêtes [#1989](https://github.com/proconnect-gouv/proconnect-identite/issues/1989).
- Refonte de l'import de types PostgreSQL pour une meilleure compatibilité avec les bundlers de navigateurs [#1947](https://github.com/proconnect-gouv/proconnect-identite/issues/1947).
- Mise à jour de plusieurs dépendances, incluant `axios`, `moment-timezone`, `uuid`, `cypress`, et d'autres, pour bénéficier des dernières corrections et améliorations de sécurité.
- Ajout d'un client dédié pour l'environnement de préproduction de la fédération d'identité [#1937](https://github.com/proconnect-gouv/proconnect-identite/issues/1937).
- Amélioration de la gestion des emails et migration progressive hors de l'utilisation des emails MonComptePro [#1930](https://github.com/proconnect-gouv/proconnect-identite/issues/1930).
- Ajout d'authenticators pour les statistiques Metabase [#1967](https://github.com/proconnect-gouv/proconnect-identite/issues/1967).

### Autres changements
- Ajout de scripts pour la mise à jour de la liste des administrations dans Grist [#1943](https://github.com/proconnect-gouv/proconnect-identite/issues/1943), [#1945](https://github.com/proconnect-gouv/proconnect-identite/issues/1945), [#1946](https://github.com/proconnect-gouv/proconnect-identite/issues/1946).
- Correction d'un bug lié à l'apostrophe dans la recherche [#1966](https://github.com/proconnect-gouv/proconnect-identite/issues/1966).
- Amélioration de la configuration et de la gestion des workflows CI/CD.
- Mise à jour de la documentation et des configurations internes.

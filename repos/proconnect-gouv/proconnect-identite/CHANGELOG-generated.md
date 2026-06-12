## Changelog : proconnect-identite (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, de la performance et de la maintenabilité de la plateforme. Des optimisations de la base de données, des mises à jour de dépendances et des corrections de bugs ont été implémentées. Des améliorations significatives ont également été apportées à la gestion des organisations et des certifications, ainsi qu'à la compatibilité avec les annuaires d'entreprises.

### Évolutions fonctionnelles
- Ajout d'une raison pour les rejets de modération, permettant aux utilisateurs de mieux comprendre les motifs de refus. [#1931](https://github.com/proconnect-gouv/proconnect-identite/pulls/1931)
- Amélioration de la validation automatique des utilisateurs lors de l'inscription, notamment pour les organisations disposant d'un domaine de contact officiel. [#1934](https://github.com/proconnect-gouv/proconnect-identite/pulls/1934)
- Possibilité de sauter la modération pour les petites organisations civiles ou agricoles utilisant une adresse email gratuite. [#1972](https://github.com/proconnect-gouv/proconnect-identite/pulls/1972)
- Ajout d'un champ "raison de la fin d'utilisation" dans la base de données pour les modérations. [#1954](https://github.com/proconnect-gouv/proconnect-identite/pulls/1954)
- Ajout de la catégorie juridique "Pôle d'équilibre territorial et rural". [#1982](https://github.com/proconnect-gouv/proconnect-identite/pulls/1982)
- Mise en place d'un nouveau mécanisme pour calculer si une entité est un service public. [#1945](https://github.com/proconnect-gouv/proconnect-identite/pulls/1945)
- Début de la migration des emails MonComptePro vers un nouveau système. [#1930](https://github.com/proconnect-gouv/proconnect-identite/pulls/1930)

### Évolutions techniques
- Optimisation des performances de la base de données en ajoutant un index sur la table `users_oidc_clients`. [#1989](https://github.com/proconnect-gouv/proconnect-identite/pulls/1989)
- Mise à jour de la base de données pour assurer la compatibilité avec PostgreSQL 17. [#1983](https://github.com/proconnect-gouv/proconnect-identite/pulls/1983)
- Refactorisation du hook `seed` pour une meilleure organisation et maintenabilité. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pulls/1926)
- Correction d'un problème d'importation de types pour PostgreSQL dans les contextes. [#1947](https://github.com/proconnect-gouv/proconnect-identite/pulls/1947)
- Ajout d'un client dédié pour l'environnement de préproduction. [#1937](https://github.com/proconnect-gouv/proconnect-identite/pulls/1937)
- Mise à jour de plusieurs dépendances, incluant `axios`, `uuid`, `systeminformation`, `brace-expansion`, `moment-timezone` et `cypress`.
- Amélioration de la gestion des erreurs OIDC en ajoutant une description. [#1914](https://github.com/proconnect-gouv/proconnect-identite/pulls/1914)

### Autres changements
- Ajout d'un authentificateur pour Metabase pour un meilleur suivi des statistiques. [#1967](https://github.com/proconnect-gouv/proconnect-identite/pulls/1967)
- Mise en place de workflows pour faciliter l'exécution locale des scripts de mise à jour des annuaires d'entreprises. [#1943](https://github.com/proconnect-gouv/proconnect-identite/pulls/1943)
- Ajout de scripts et de workflows pour la gestion et la mise à jour des données des administrations dans Grist. [#1946](https://github.com/proconnect-gouv/proconnect-identite/pulls/1946) et [#1952](https://github.com/proconnect-gouv/proconnect-identite/pulls/1952)
- Correction d'un bug lié à l'encodage des URL. [#1966](https://github.com/proconnect-gouv/proconnect-identite/pulls/1966)
- Amélioration du ratio de l'expéditeur alternatif des emails. [#1951](https://github.com/proconnect-gouv/proconnect-identite/pulls/1951)
- Suppression du motif de rejet "autre" et remplacement par un message informant l'utilisateur de consulter son email. [#1927](https://github.com/proconnect-gouv/proconnect-identite/pulls/1927)

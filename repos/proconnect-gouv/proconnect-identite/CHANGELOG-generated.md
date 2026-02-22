## Changelog : proconnect-identite (30 derniers jours)

### Résumé
Les dernières mises à jour de ProConnect Identité se concentrent sur l'amélioration de l'expérience utilisateur, notamment lors de l'authentification via FranceConnect et de la gestion des organisations. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la robustesse et de la maintenance du code.

### Évolutions fonctionnelles
- Possibilité de choisir le nom à afficher après l'authentification via FranceConnect. (#1792)
- Amélioration de la réactivité de l'interface utilisateur. (#1777)
- Les sessions utilisateurs ne sont plus perdues lors du rechargement de l'application. (#1778)
- Possibilité de choisir parmi plusieurs mairies lors de l'authentification. (#1728)
- Ajout d'un champ "statut" aux modérations. (#1740)
- Migration des fichiers de migration vers TypeScript. (#1712)
- Amélioration de l'algorithme pour déterminer si une entreprise est unipersonnelle. (#1746)
- Suppression du flag de fonctionnalité pour l'affichage du bouton FranceConnect. (#1705)
- Collecte de données supplémentaires lors de la connexion (nom du fournisseur de service et adresse IP de l'utilisateur). (#1703)

### Évolutions techniques
- Optimisation de la requête de suggestion d'organisation pour améliorer les performances. (#1786)
- Correction d'une exportation incorrecte dans l'API entreprise. (#1783)
- Mise à jour de la configuration du package entreprise. (#1783)
- Ajout d'une contrainte "not null" pour le type de vérification. (#1784)
- Refactorisation de la gestion des types de vérification (suppression de types obsolètes et migration vers des types plus précis). (#1762, #1760, #1701, #1711)
- Migration de la vérification de domaine vers un type plus précis. (#1761)
- Ajout de tests unitaires pour les types de vérification. (#1759)
- Refactorisation de la logique de gestion des statuts de modération. (#1702)
- Simplification du logger de débogage. (#1747)
- Suppression d'une variable d'environnement FranceConnect obsolète. (#1718)
- Mise à jour des dépendances : `qs`, `axios`, `sentry`, `hono`, `ejs`, `cypress-io/github-action`.

### Autres changements
- Mise à jour de l'icône de la section d'aide. (#1773)
- Ajout d'un avertissement pour l'environnement de test. (#1754)
- Ajout d'un test E2E pour la certification de dirigeant avec un flux de suggestion. (#1775)
- Ajout d'un test E2E pour la vérification de domaine. (#1753)
- Mise à jour des fichiers de verrouillage des dépendances. (#1772, #1750, #1730, #1691)
- Amélioration de la documentation et du code.
- Corrections de bugs mineurs et améliorations de la qualité du code.

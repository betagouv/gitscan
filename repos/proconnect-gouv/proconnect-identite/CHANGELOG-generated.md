## Changelog : proconnect-identite (30 derniers jours)

### Résumé
Les dernières mises à jour de ProConnect Identité améliorent la gestion des organisations, la vérification des identités et l'expérience utilisateur globale. Des corrections de bugs et des optimisations ont été apportées, notamment concernant la gestion des associations, des modérations et des types de vérification. L'interface utilisateur a également été modernisée.

### Évolutions fonctionnelles
- Possibilité pour les mairies de choisir l'adresse email utilisée pour l'authentification (#1728).
- Amélioration de l'algorithme pour déterminer si une entité est une entreprise unipersonnelle (#1746).
- Ajout d'un statut "réouvert" aux modérations (#1701).
- Amélioration de la gestion des types de vérification, avec suppression de types obsolètes (#1711, #1702).
- Collecte de données supplémentaires (sp\_name et user\_ip\_address) pour le suivi (#1724).
- Mise à jour de la page FranceConnect (#1723).
- Affichage d'un avertissement en cas d'utilisation de l'environnement de test (#1754).
- Nouvelle interface utilisateur plus moderne (#1753).

### Évolutions techniques
- Migration de fichiers de migration vers TypeScript (#1712).
- Refactorisation majeure de la gestion des "guards" (sécurité) (#1716).
- Migration de la vérification des petites associations vers le domaine lorsque l'email est vérifié (#1760).
- Ajout de tests unitaires pour la vérification des types d'assignation d'utilisateur (#1759).
- Suppression de la variable d'environnement dépréciée pour les certificats (#1705).
- Suppression d'un timeout inutile dans les tests Cypress (#1704).
- Amélioration de la gestion des erreurs et des alertes, notamment en cas d'indisponibilité de l'API Sirene (#1724).
- Ajout de types pour les modérations dans le package `shared-identite` (#1693).
- Correction d'un bug empêchant la réécriture des liens de domaine non vérifiés après modération (#1761).
- Simplification du logger de débogage (#1747).

### Autres changements
- Mise à jour des dépendances : `qs`, `axios`, `sentry`, `hono`, `ejs`, `lodash` (#1763, #1756, #1735, #1699, #1698, #1708).
- Mise à jour des actions GitHub (Cypress) (#1749, #1730).
- Ajout de commentaires et documentation pour améliorer la lisibilité du code.
- Corrections mineures et améliorations de la qualité du code.
- Ajout d'un fichier barrel dans le dossier adapter (#1766).
- Ajout de la possibilité de choisir entre plusieurs mairies (#1722).
- Ajout du champ `verified_by_coop_mediation_numerique` aux liens organisation-utilisateur (#1736).
- Ajout du champ `ordre_professionnel_domain` aux liens organisation-utilisateur (#1720).
- Ajout de la gestion du statut "en attente" pour les modérations (#1740).
- Correction d'un problème d'écrasement des liens de domaine non vérifiés (#1761).
- Suppression de la possibilité d'avoir un type de vérification vide dans la table `users_organizations` (#1702).
- Ajout d'une commande Cypress pour la connexion via magic link (#1747).
- Amélioration de la gestion des erreurs lors de la copie des données pour l'anonymisation (#1757).
- Ajout du champ `status` à la table `franceconnect_userinfo` pour l'anonymisation (#1757).
- Mise à jour de l'icône de l'aide (#1773).
- Publication des versions v1.6.1 et v1.6.0 du package identité (#1767, #1764).

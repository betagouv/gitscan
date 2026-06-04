## Changelog : proconnect-identite (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se concentrent sur l'amélioration de la gestion des services publics, la migration vers de nouvelles méthodes d'envoi d'emails, et l'amélioration de la robustesse et de la maintenance du système. Des corrections et des mises à jour ont également été apportées pour améliorer la compatibilité et la sécurité.

### Évolutions fonctionnelles
- **Gestion des services publics :** Nouvelle fonction `computeIsServicePublic` pour déterminer si un organisme est un service public, utilisant un nouvel algorithme. [#1968](https://github.com/proconnect-gouv/proconnect-identite/pull/1968)
- **Emails :** Début de la migration de l'envoi d'emails depuis MonComptePro, avec l'ajout du nom de l'expéditeur. [#1930](https://github.com/proconnect-gouv/proconnect-identite/pull/1930)
- **Modération :** Ajout des champs `end_user_reason` et `allow_editing` à la table des modérations pour une meilleure gestion des rejets et une plus grande flexibilité. [#1954](https://github.com/proconnect-gouv/proconnect-identite/pull/1954)
- **Erreurs OIDC :** Ajout d'une description d'erreur OIDC pour améliorer l'information renvoyée à PCF en cas de problème. [#1914](https://github.com/proconnect-gouv/proconnect-identite/pull/1914)
- **Validation des utilisateurs :** Amélioration de la validation automatique des utilisateurs rejoignant la plateforme avec un domaine de contact officiel. [#1934](https://github.com/proconnect-gouv/proconnect-identite/pull/1934)

### Évolutions techniques
- **Publication du package RNE :** Le package `rne` est maintenant public. [#1963](https://github.com/proconnect-gouv/proconnect-identite/pull/1963)
- **Refactoring :** Refactorisation du hook `seed` avant les tests E2E pour une meilleure organisation et maintenabilité. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pull/1926)
- **Typescript :** Correction de l'importation du type `pg` pour une meilleure compatibilité avec les bundlers. [#1947](https://github.com/proconnect-gouv/proconnect-identite/pull/1947)
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances, incluant `axios`, `moment-timezone`, `prettier`, `systeminformation`, `uuid`, `cypress-io/github-action`, `actions/labeler`, `hono`, `brace-expansion`, et `redis`.
- **Docker :** Mise à jour de l'image Node.js utilisée dans Docker. (Annulée puis rétablie) [#1921](https://github.com/proconnect-gouv/proconnect-identite/pull/1921)
- **CI/CD :** Ajout d'un workflow dispatch pour faciliter l'exécution manuelle des tâches CI/CD. [#1945](https://github.com/proconnect-gouv/proconnect-identite/pull/1945)

### Autres changements
- **Documentation :** Amélioration de la documentation et ajout de commentaires.
- **Scripts d'administration :** Ajout et amélioration de scripts pour l'administration et la mise à jour des données, notamment pour la liste des administrations. [#1946](https://github.com/proconnect-gouv/proconnect-identite/pull/1946)
- **Nettoyage de code :** Suppression du motif de rejet de modération et homogénéisation de la syntaxe.
- **Correction de bug :** Correction d'un bug empêchant l'exécution du script d'administration localement. [#1949](https://github.com/proconnect-gouv/proconnect-identite/issues/1949)
- **Mise à jour des fixtures :** Mise à jour des identifiants client et secret pour l'environnement de pré-production PCF. [#1938](https://github.com/proconnect-gouv/proconnect-identite/pull/1938) et [#1939](https://github.com/proconnect-gouv/proconnect-identite/pull/1939)

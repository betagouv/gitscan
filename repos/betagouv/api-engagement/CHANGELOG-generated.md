## Changelog : api-engagement (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance et la sécurité de l'API, avec des optimisations de recherche et l'ajout de limitations de débit. L'application (back office) bénéficie également de corrections d'affichage et d'améliorations de l'expérience utilisateur, notamment en matière de responsive design. Des travaux ont été réalisés pour faciliter l'intégration avec de nouveaux partenaires comme le SDIS.

### Évolutions fonctionnelles
- Ajout de la gestion des missions de Service Civique via GRIMPIO. [#977](https://github.com/betagouv/api-engagement/issues/977)
- Amélioration de l'affichage de l'URL de l'API Sandbox dans l'exemple de commande cURL du broadcaster. [#1012](https://github.com/betagouv/api-engagement/issues/1012)
- Correction de l'affichage et de la disposition du sélecteur de date dans l'application (back office). [#975](https://github.com/betagouv/api-engagement/issues/975)
- Correction du problème de déconnexion lors d'erreurs réseau dans l'application (back office). [#976](https://github.com/betagouv/api-engagement/issues/976)
- Amélioration du responsive design de l'application (back office) pour les petits écrans, en respectant les normes RGAA 10.11. [#930](https://github.com/betagouv/api-engagement/issues/930)

### Évolutions techniques
- Refactorisation du middleware de contrôle d'accès de l'API avec ajout de tests. [#1013](https://github.com/betagouv/api-engagement/issues/1013)
- Optimisation de la recherche d'organisations dans l'API en utilisant `tsvector`. [#950](https://github.com/betagouv/api-engagement/issues/950)
- Ajout de limitations de débit (rate limiting) pour l'API, avec des limites basées sur l'adresse IP et l'éditeur (publisher). [#932](https://github.com/betagouv/api-engagement/issues/932)
- Suppression du magasin partagé pour les limites de débit (rate limit). [#959](https://github.com/betagouv/api-engagement/issues/959)
- Refactorisation du traitement des missions avec exclusion des organisations publiantes. [#965](https://github.com/betagouv/api-engagement/issues/965)
- Exécution séquentielle de l'agrégation des widgets pour améliorer la stabilité. [#966](https://github.com/betagouv/api-engagement/issues/966)
- Ajout de jobs de sauvegarde de la base de données RDB. [#955](https://github.com/betagouv/api-engagement/issues/955)
- Correction d'un bug empêchant le job de sauvegarde RDB de s'exécuter. [#957](https://github.com/betagouv/api-engagement/issues/957)
- Suppression de la colonne `mission_id` dans la table `stat_events`. [#933](https://github.com/betagouv/api-engagement/issues/933)
- Correction de l'échelle maximale de l'API. [#949](https://github.com/betagouv/api-engagement/issues/949)

### Autres changements
- Ajout d'une configuration Mockoon pour les tests. [#978](https://github.com/betagouv/api-engagement/issues/978)
- Amélioration du script de vérification des champs orphelins de `stat_event` pour les missions.
- Correction d'un bug dans la page des organisations désactivées.
- Publication des versions v1.4.0 et v1.4.1.

## Changelog : api-engagement (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de performance et de sécurité, notamment grâce à l'optimisation des recherches d'organisations et à l'ajout de limitations de débit. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des améliorations de l'interface utilisateur dans l'application web.

### Évolutions fonctionnelles
- Ajout de scripts pour les missions SDIS [#942](https://github.com/betagouv/api-engagement/issues/942).
- Amélioration de la liste des utilisateurs et des formulaires utilisateurs dans l'application web [#922](https://github.com/betagouv/api-engagement/issues/922).
- Amélioration du sélecteur de plage de dates dans l'application web, avec une accessibilité accrue [#928](https://github.com/betagouv/api-engagement/issues/928).
- Correction d'un bug empêchant la déconnexion de l'utilisateur en cas d'erreur réseau dans l'application web [#930](https://github.com/betagouv/api-engagement/issues/930).
- Ajout de limites de débit pour les requêtes API (publisherRateLimiter et ipRateLimiter) [#932](https://github.com/betagouv/api-engagement/issues/932).
- Correction d'un problème de redirection après la création d'une mission [#926](https://github.com/betagouv/api-engagement/issues/926).
- Amélioration des filtres de modération avec une recherche facettée [#902](https://github.com/betagouv/api-engagement/issues/902).

### Évolutions techniques
- Refactorisation de la recherche d'organisations pour utiliser `tsvector`, améliorant ainsi les performances [#950](https://github.com/betagouv/api-engagement/issues/950).
- Suppression du magasin partagé pour les limites de débit, simplifiant ainsi l'architecture [#959](https://github.com/betagouv/api-engagement/issues/959).
- Refactorisation du traitement des missions avec exclusion de l'organisation publiant [#965](https://github.com/betagouv/api-engagement/issues/965).
- Refactorisation de l'exécution des agrégations du widget en mode séquentiel [#966](https://github.com/betagouv/api-engagement/issues/966).
- Ajout de jobs de sauvegarde de la base de données RDB [#955](https://github.com/betagouv/api-engagement/issues/955) et activation du job [#957](https://github.com/betagouv/api-engagement/issues/957).
- Suppression de colonnes inutiles et amélioration des requêtes pour optimiser les performances de l'API [#917](https://github.com/betagouv/api-engagement/issues/917), [#918](https://github.com/betagouv/api-engagement/issues/918), [#919](https://github.com/betagouv/api-engagement/issues/919), [#921](https://github.com/betagouv/api-engagement/issues/921).
- Mise à jour de la documentation OpenAPI [#915](https://github.com/betagouv/api-engagement/issues/915).
- Ajout d'une politique de sécurité [#920](https://github.com/betagouv/api-engagement/issues/920).
- Amélioration de la configuration du proxy Metabase [#916](https://github.com/betagouv/api-engagement/issues/916).

### Autres changements
- Publication des versions v1.3.0 et v1.4.0 [#956](https://github.com/betagouv/api-engagement/issues/956), [#959](https://github.com/betagouv/api-engagement/issues/959).
- Amélioration du script de vérification des champs orphelins de `stat_event` [#428515e](https://github.com/betagouv/api-engagement/commit/428515e).
- Correction de l'affichage de la page organisation désactivée [#18512e0](https://github.com/betagouv/api-engagement/commit/18512e0).
- Amélioration des règles CLAUDE [#4e75f5d](https://github.com/betagouv/api-engagement/commit/4e75f5d).
- Diverses mises à jour de dépendances.

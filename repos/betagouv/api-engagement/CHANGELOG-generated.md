## Changelog : api-engagement (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de performance, notamment au niveau de la recherche d'organisations et de la gestion des sauvegardes de la base de données. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des améliorations d'accessibilité et de l'expérience utilisateur sur l'interface web.

### Évolutions fonctionnelles
- Ajout de scripts pour les missions SDIS via l'API. [#942](https://github.com/betagouv/api-engagement/pull/942)
- Amélioration de la recherche d'organisations grâce à l'utilisation de `tsvector`. [#950](https://github.com/betagouv/api-engagement/pull/950)
- Correction d'un bug empêchant la déconnexion en cas d'erreur réseau dans l'application. [#930](https://github.com/betagouv/api-engagement/pull/930)
- Amélioration de la conception réactive pour les petites vues (RGAA 10.11). [#930](https://github.com/betagouv/api-engagement/pull/930)
- Amélioration de la liste des utilisateurs et des formulaires utilisateurs dans l'application. [#922](https://github.com/betagouv/api-engagement/pull/922)
- Correction du blocage de la sélection du jour courant dans le sélecteur de date. [#924](https://github.com/betagouv/api-engagement/pull/924)
- Amélioration des filtres de modération avec la recherche facetée. [#902](https://github.com/betagouv/api-engagement/pull/902)
- Correction d'un problème de redirection lorsque la mission n'est pas trouvée. [#926](https://github.com/betagouv/api-engagement/pull/926)
- Correction d'un problème d'affichage de la page organisation. [#925](https://github.com/betagouv/api-engagement/pull/925)
- Amélioration de l'accessibilité du sélecteur de date. [#928](https://github.com/betagouv/api-engagement/pull/928)

### Évolutions techniques
- Mise en place de sauvegardes régulières de la base de données (RDB). [#955](https://github.com/betagouv/api-engagement/pull/955) et [#957](https://github.com/betagouv/api-engagement/pull/957)
- Suppression du magasin partagé de limitation de débit de l'API. [#959](https://github.com/betagouv/api-engagement/pull/959)
- Ajout de limiteurs de débit basés sur l'éditeur et l'adresse IP. [#932](https://github.com/betagouv/api-engagement/pull/932)
- Optimisation de la mise à l'échelle de l'API (max_scale). [#949](https://github.com/betagouv/api-engagement/pull/949)
- Suppression de la clé étrangère `mission` dans la table `stat_events`. [#933](https://github.com/betagouv/api-engagement/pull/933) et [#921](https://github.com/betagouv/api-engagement/pull/921)
- Suppression des champs d'organisation hérités de la table `stat_event`. [#918](https://github.com/betagouv/api-engagement/pull/918)
- Suppression des champs d'organisation hérités du schéma de mission. [#917](https://github.com/betagouv/api-engagement/pull/917)
- Amélioration des règles CLAUDE. [#935](https://github.com/betagouv/api-engagement/pull/935)
- Mise à jour de la documentation OpenAPI. [#915](https://github.com/betagouv/api-engagement/pull/915)
- Ajout d'une politique de sécurité. [#920](https://github.com/betagouv/api-engagement/pull/920)

### Autres changements
- Publication des versions v1.4.1 et v1.3.1.
- Amélioration du script de vérification des champs orphelins de mission dans `stat_event`. [#930](https://github.com/betagouv/api-engagement/pull/930)
- Correction de la configuration du proxy Metabase. [#916](https://github.com/betagouv/api-engagement/pull/916)
- Correction de la configuration du déploiement sandbox de l'application. [#914](https://github.com/betagouv/api-engagement/pull/914)
- Suppression de la dépendance `letudiant` des jobs.
- Mise à jour des dépendances.

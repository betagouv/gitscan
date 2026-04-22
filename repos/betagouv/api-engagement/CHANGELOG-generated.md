## Changelog : api-engagement (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la sécurité de l'API, ainsi que sur des corrections d'accessibilité et des ajustements de l'interface utilisateur de l'application. Des optimisations ont été apportées aux requêtes et à la gestion des données, et des mesures de limitation de débit ont été implémentées pour protéger l'API contre les abus.

### Évolutions fonctionnelles
- Ajout d'un nouveau type de mission : "reserve_operationnelle" [#901](https://github.com/betagouv/api-engagement/issues/901).
- Amélioration du filtre d'organisation dans l'application pour se baser sur l'ID, corrigeant un problème de fonctionnement [#867](https://github.com/betagouv/api-engagement/issues/867).
- Correction d'un bug empêchant la déconnexion en cas d'erreur réseau dans l'application [#930](https://github.com/betagouv/api-engagement/issues/930).
- Amélioration de l'accessibilité du sélecteur de date dans l'application (RGAA 10.11) [#928](https://github.com/betagouv/api-engagement/issues/928).
- Amélioration de l'accessibilité de la liste des utilisateurs et des formulaires utilisateurs dans l'application [#922](https://github.com/betagouv/api-engagement/issues/922).
- Correction du blocage de la sélection du jour courant dans le sélecteur de date de l'application [#924](https://github.com/betagouv/api-engagement/issues/924).
- Correction d'un problème de redirection lorsque la mission n'est pas trouvée [#926](https://github.com/betagouv/api-engagement/issues/926).
- Amélioration du formulaire d'édition de widget dans l'application [#925](https://github.com/betagouv/api-engagement/issues/925).

### Évolutions techniques
- Implémentation de la limitation de débit (rate limiting) pour les requêtes à l'API, basée sur l'éditeur et l'adresse IP [#932](https://github.com/betagouv/api-engagement/issues/932).
- Mise à l'échelle de l'API pour gérer un volume de requêtes plus important [#949](https://github.com/betagouv/api-engagement/issues/949).
- Suppression de la clé étrangère `mission_id` dans la table `stat_events` pour améliorer la performance et la flexibilité [#933](https://github.com/betagouv/api-engagement/issues/933).
- Refactorisation du code pour supprimer les champs de mission dénormalisés de la table `stat_event` [#921](https://github.com/betagouv/api-engagement/issues/921).
- Suppression des champs d'organisation hérités dans l'API et l'analytics [#917](https://github.com/betagouv/api-engagement/issues/917) et [#918](https://github.com/betagouv/api-engagement/issues/918).
- Amélioration des règles CLAUDE pour une meilleure analyse du contenu [#935](https://github.com/betagouv/api-engagement/issues/935).
- Mise à jour de la documentation OpenAPI de l'API [#915](https://github.com/betagouv/api-engagement/issues/915).
- Ajout d'une politique de sécurité [#920](https://github.com/betagouv/api-engagement/issues/920).
- Mise à jour des dépendances (Vite, ESLint, etc.).

### Autres changements
- Amélioration du script de vérification des champs orphelins `stat_event` [#936](https://github.com/betagouv/api-engagement/issues/936).
- Correction du proxy Metabase pour restreindre l'accès à une carte spécifique [#916](https://github.com/betagouv/api-engagement/issues/916).
- Amélioration des statistiques d'administration pour les types de missions [#892](https://github.com/betagouv/api-engagement/issues/892).
- Corrections et améliorations de la configuration CI/CD.
- Mises à jour de la configuration de déploiement pour l'environnement sandbox.
- Publication des versions v1.2.0, v1.2.1 et v1.3.0.

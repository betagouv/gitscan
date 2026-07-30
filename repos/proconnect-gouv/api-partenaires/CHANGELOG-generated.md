## Changelog : api-partenaires (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce changelog couvre les 30 derniers jours et met en évidence la mise en place initiale de l'API, incluant la configuration de l'environnement de développement, l'implémentation de la gestion des clients OIDC et des améliorations de sécurité. L'API permet désormais aux fournisseurs OIDC de gérer une partie de leur configuration.

### Évolutions fonctionnelles
- Ajout des routes `/api/oidc_clients*` pour la gestion des clients OIDC, migrées de pcdbapi. [#7](https://github.com/proconnect-gouv/api-partenaires/pulls/7)
- Exposition des champs `createdAt` et `updatedAt` dans les réponses de l'API pour les clients OIDC. [#20](https://github.com/proconnect-gouv/api-partenaires/pulls/20)
- Implémentation de la gestion de la configuration des partenaires basée sur MongoDB. [#8417678](https://github.com/proconnect-gouv/api-partenaires/commit/8417678)

### Évolutions techniques
- Refonte de la gestion des secrets OIDC, simplifiant la cryptographie et renforçant la sécurité. [#10](https://github.com/proconnect-gouv/api-partenaires/pulls/10), [#11](https://github.com/proconnect-gouv/api-partenaires/pulls/11), [#12](https://github.com/proconnect-gouv/api-partenaires/pulls/12)
- Configuration des fournisseurs OIDC chargée via un pipeline Zod pour une validation robuste. [#14](https://github.com/proconnect-gouv/api-partenaires/pulls/14)
- Ajout du middleware `hono/logger` pour améliorer la journalisation. [#15](https://github.com/proconnect-gouv/api-partenaires/pulls/15)
- Simplification et renforcement de la sécurité des clients OIDC, incluant la suppression de champs inutiles. [#9](https://github.com/proconnect-gouv/api-partenaires/pulls/9), [#13](https://github.com/proconnect-gouv/api-partenaires/pulls/13)
- Mise en place d'un environnement de CI/CD avec Docker, des tests d'intégration et dependabot pour la gestion des dépendances. [#1](https://github.com/proconnect-gouv/api-partenaires/pulls/1), [#4](https://github.com/proconnect-gouv/api-partenaires/pulls/4), [#5](https://github.com/proconnect-gouv/api-partenaires/pulls/5), [#6](https://github.com/proconnect-gouv/api-partenaires/pulls/6)
- Utilisation de Bun pour l'exécution des tests.
- Configuration de l'environnement de test avec Docker Compose.

### Autres changements
- Documentation de la configuration, des routes et des tests d'intégration.
- Ajout de tests de régression pour les résultats d'un audit de sécurité. [#8](https://github.com/proconnect-gouv/api-partenaires/pulls/8)
- Renommage de la variable d'environnement `SANDBOX_API_SECRET` en `OIDC_CLIENTS_API_SECRET`. [#18](https://github.com/proconnect-gouv/api-partenaires/pulls/18)
- Correction d'un bug permettant la valeur `null` pour le champ `signed_response_alg` des clients OIDC. [#17](https://github.com/proconnect-gouv/api-partenaires/pulls/17)
- Restauration de la clé dans la réponse formatée des clients OIDC. [#16](https://github.com/proconnect-gouv/api-partenaires/pulls/16)
- Séparation de la configuration `oidc_providers.yaml` par environnement. [#19](https://github.com/proconnect-gouv/api-partenaires/pulls/19)

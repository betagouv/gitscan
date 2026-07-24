## Changelog : api-partenaires (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce changelog présente les premiers développements de l'API Partenaires, une API permettant aux partenaires de ProConnect de gérer une partie de leur configuration. Les travaux initiaux se sont concentrés sur la mise en place de l'infrastructure de base, l'implémentation de la gestion des fournisseurs OIDC, et l'ajout de tests d'intégration pour renforcer la sécurité et la fiabilité.

### Évolutions fonctionnelles
- Ajout des routes `/api/oidc_clients*` permettant de gérer les clients OIDC, migrées de pcdbapi. [#7](https://github.com/proconnect-gouv/api-partenaires/pulls/7)
- Implémentation de la configuration des partenaires stockée en base de données MongoDB.
- Possibilité de configurer les noms de domaine complets (FQDN) des fournisseurs OIDC.
- Amélioration de la gestion des algorithmes de signature des réponses OIDC, permettant les valeurs nulles. [#17](https://github.com/proconnect-gouv/api-partenaires/issues/17)
- Restauration de la clé dans la réponse `format_oidc_client`. [#16](https://github.com/proconnect-gouv/api-partenaires/issues/16)

### Évolutions techniques
- Refonte de la sécurité des clients OIDC, simplification du chiffrement et renforcement de la protection. [#8](https://github.com/proconnect-gouv/api-partenaires/issues/8), [#9](https://github.com/proconnect-gouv/api-partenaires/issues/9), [#10](https://github.com/proconnect-gouv/api-partenaires/issues/10), [#11](https://github.com/proconnect-gouv/api-partenaires/issues/11), [#12](https://github.com/proconnect-gouv/api-partenaires/issues/12)
- Suppression de la protection au niveau de l'application basée sur les adresses IP autorisées.
- Simplification de la configuration et chargement via un pipeline Zod. [#14](https://github.com/proconnect-gouv/api-partenaires/issues/14)
- Ajout du middleware `hono/logger` pour la journalisation des requêtes. [#15](https://github.com/proconnect-gouv/api-partenaires/issues/15)
- Mise en place d'une infrastructure CI/CD complète avec Docker, tests d'intégration et dépendabot.
- Utilisation d'images Docker épinglées pour garantir la reproductibilité.
- Compilation en binaire statique avec Docker multi-étapes.
- Ajout de tests d'intégration pour valider le fonctionnement de l'API.
- Documentation de la configuration, des routes et des tests d'intégration.

### Autres changements
- Renommage de la variable d'environnement `SANDBOX_API_SECRET` en `OIDC_CLIENTS_API_SECRET`. [#18](https://github.com/proconnect-gouv/api-partenaires/issues/18)
- Mise à jour des dépendances `prettier`, `actions/checkout` et `hono`.
- Initialisation du projet avec Bun et création du squelette initial.
- Suppression de certaines actions et configurations inutiles dans le CI.
- Ajout d'exemples de configuration pour l'autorisation par adresse IP.

## Changelog : api-partenaires (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, l'API Partenaires a connu une refonte significative, passant d'une base de code initiale à une architecture plus robuste et sécurisée. L'ajout de routes pour la gestion des clients OIDC et la configuration des partenaires, ainsi que l'implémentation de tests d'intégration, marquent une avancée importante pour le projet.

### Évolutions fonctionnelles
- Ajout des routes `/api/oidc_clients*` pour la gestion des clients OIDC, migrées depuis pcdbapi [#7](https://github.com/proconnect-gouv/api-partenaires/issues/7).
- Implémentation d'une configuration des partenaires stockée en base de données MongoDB.
- Ajout d'un exemple d'intégration pour la modification des FQDN des fournisseurs (edit_provider_fqdns).
- Amélioration de la gestion des algorithmes de signature des réponses OIDC, autorisant maintenant les valeurs nulles [#17](https://github.com/proconnect-gouv/api-partenaires/issues/17).
- Restauration de la clé au bon format dans la réponse `format_oidc_client` [#16](https://github.com/proconnect-gouv/api-partenaires/issues/16).

### Évolutions techniques
- Refonte de la sécurité des clients OIDC, simplifiant le chiffrement et renforçant la protection [#8](https://github.com/proconnect-gouv/api-partenaires/issues/8), [#9](https://github.com/proconnect-gouv/api-partenaires/issues/9), [#10](https://github.com/proconnect-gouv/api-partenaires/issues/10), [#11](https://github.com/proconnect-gouv/api-partenaires/issues/11), [#12](https://github.com/proconnect-gouv/api-partenaires/issues/12).
- Configuration des fournisseurs OIDC chargée via un pipeline Zod pour une meilleure validation [#14](https://github.com/proconnect-gouv/api-partenaires/issues/14).
- Suppression des champs `email`, `editable` et `collaborators` pour simplifier la gestion des secrets [#13](https://github.com/proconnect-gouv/api-partenaires/issues/13).
- Ajout du middleware `hono/logger` pour une meilleure journalisation des requêtes [#15](https://github.com/proconnect-gouv/api-partenaires/issues/15).
- Mise en place d'une infrastructure CI/CD complète avec des workflows pour les tests, la construction Docker et la gestion des dépendances.
- Utilisation de Docker pour la compilation en binaire statique.
- Ajout de tests d'intégration pour valider le bon fonctionnement de l'API.
- Suppression de la protection par liste blanche d'adresses IP au niveau de l'application.
- Configuration des environnements ANCT OIDC séparément.
- Renommage de la variable `SANDBOX_API_SECRET` en `OIDC_CLIENTS_API_SECRET`.

### Autres changements
- Documentation de la configuration, des routes et des tests d'intégration.
- Documentation de l'exemple de contrat `AUTHORIZED_IPS`.
- Mise à jour des dépendances Prettier et actions/checkout.
- Mise à jour de la version de Hono.

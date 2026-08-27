## Changelog : api-partenaires (30 derniers jours, au 26 août 2026)

### Résumé
Les récentes évolutions améliorent la traçabilité des données en exposant les dates de création et de modification des clients OIDC. Le projet a également bénéficié d'une clarification de la nomenclature concernant la gestion des domaines de messagerie et d'une extension du support matériel pour les conteneurs Docker.

### Évolutions fonctionnelles
- Ajout des champs de date de création (`createdAt`) et de mise à jour (`updatedAt`) dans les réponses de l'API pour les clients OIDC [#20](https://github.com/proconnect-gouv/api-partenaires/pull/20)

### Évolutions techniques
- Refactorisation de la gestion des domaines : renommage de `fqdns` en `attached_email_domains` dans le modèle MongoDB et l'implémentation pour une meilleure cohérence du code [#31](https://github.com/proconnect-gouv/api-partenaires/pull/31) [#36](https://github.com/proconnect-gouv/api-partenaires/pull/36)
- Extension de l'infrastructure Docker pour inclure le support de l'architecture `arm64` [#25](https://github.com/proconnect-gouv/api-partenaires/pull/25)

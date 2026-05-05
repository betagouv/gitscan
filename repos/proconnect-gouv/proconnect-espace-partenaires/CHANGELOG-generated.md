## Changelog : proconnect-espace-partenaires (30 derniers jours, au 20 avril 2026)

### Résumé
Ce changelog présente les récentes évolutions de l'espace partenaires ProConnect. Les principales améliorations concernent l'ajout d'un mode maintenance pour bloquer les modifications de l'espace partenaire, ainsi que des améliorations de la documentation pour faciliter la configuration et la résolution des erreurs. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance permettant de désactiver les modifications de l'espace partenaire. [#312](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/312)

### Évolutions techniques
- Mise à jour de la dépendance `proconnect-gouv/federation/api-partner` vers la version `4f05153`. [#315](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/315)
- Mises à jour des dépendances de développement :
    - `typescript` dans `/e2e` [#296](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/296)
    - `lodash` dans `/e2e` et globalement [#302](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/302), [#304](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/304)
    - `@playwright/test` dans `/e2e` [#310](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/310)
    - `follow-redirects` [#313](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/313)
    - `defu` [#295](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/295)

### Autres changements
- Amélioration de la documentation concernant les erreurs Y020032 et la configuration. [#294](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/294)
- Restructuration de la documentation `configuration.md` et correction de la numérotation dans `index.mdx`. [#311](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/311)
- Tests IDP. [#299](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/299)

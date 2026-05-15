## Changelog : proconnect-espace-partenaires (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'espace partenaires a bénéficié d'améliorations axées sur la documentation, la gestion des rôles et des organisations, ainsi que l'ajout d'un mode maintenance pour faciliter les opérations. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une mention de l'organisation et de son numéro SIRET pour les professionnels. [#330](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/330)
- Implémentation d'un mode maintenance permettant de désactiver les modifications de l'espace partenaire. [#312](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/312)
- Précision de la gestion des ACrs EIDAS1 lorsque ceux-ci ne sont pas gérés. [#323](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/323)

### Évolutions techniques
- Mise à jour de la dépendance `proconnect-gouv/federation/api-partner` vers les versions `3af5769` et `4f05153`. [#315](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/315) et [#327](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/327)
- Mises à jour de plusieurs dépendances de développement : `axios`, `fast-xml-builder`, `fast-uri`, `postcss`, `typescript`, `next`, `lodash`, `@playwright/test` et `follow-redirects`. (Ces mises à jour sont automatiques et visent à maintenir la sécurité et la stabilité du projet).

### Autres changements
- Amélioration de la documentation concernant les claims utilisateurs retournés par `/user-info`. [#322](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/322)
- Ajout d'une section sur la configuration MFA (Multi-Factor Authentication) dans le guide LemonLDAP::NG. [#316](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/316)
- Ajout de documentation sur les scopes des rôles. [#331](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/331)

## Changelog : proconnect-espace-partenaires (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la documentation pour faciliter l'intégration des partenaires, ainsi que sur l'ajout d'un mode maintenance pour bloquer les modifications de l'espace partenaire. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance permettant de désactiver les modifications de l'espace partenaire. [#312](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/312)

### Évolutions techniques
- Mise à jour de la documentation concernant la configuration de l'authentification avec LemonLDAP::NG, incluant une section sur l'authentification multi-facteurs (MFA). [#316](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/316)
- Clarification dans la documentation concernant le retour des informations utilisateur via l'endpoint `/user-info`. [#322](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/322)
- Restructuration et amélioration de la documentation de configuration. [#311](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/311)
- Ajout d'informations sur l'erreur Y020032 et sa configuration dans la documentation. [#294](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/294)

### Autres changements
- Mises à jour de diverses dépendances (TypeScript, Lodash, Playwright, follow-redirects, proconnect-gouv/federation/api-partner) pour assurer la sécurité et la stabilité de l'application.

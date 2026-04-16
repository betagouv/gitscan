## Changelog : proconnect-espace-partenaires (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation pour les partenaires, notamment concernant la configuration et l'intégration avec les Identity Providers (IDP). Des optimisations techniques ont également été apportées pour améliorer les performances et la stabilité de l'application, notamment via la mise à jour de la version de PostgreSQL et l'ajout d'un cache de build Next.js.

### Évolutions fonctionnelles
- **Documentation Fédération d'Identité (FI):** Ajout de sections sur les erreurs Y020032 et la configuration des numéros d'erreur. [#294](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/294)
- **Documentation FI:** Restructuration de la page de configuration et amélioration de la navigation dans la documentation IDP avec l'ajout d'une table des matières. [#311](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/311), [#277](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/277)
- **Documentation FI:** Clarification des niveaux EIDAS et amélioration de la découverte des informations. [#290](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/290)
- **Documentation FI:** Ajout d'une page pour la résolution d'URL RIE Discovery et une page pour le référentiel IP des fournisseurs de services. [#291](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/291), [#292](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/292)
- **Documentation FI:** Documentation de l'authentification multi-facteurs (MFA) pour les fournisseurs d'identité. [#264](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/264)
- **Documentation:** Ajout d'une fonctionnalité de recherche dans la documentation. [#256](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/256)

### Évolutions techniques
- **Cache de Build Next.js:** Ajout d'un cache de build pour accélérer les déploiements. [#276](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/276)
- **Mise à jour PostgreSQL:** Mise à jour vers PostgreSQL 17.9 et 16.13. [#275](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/275), [#274](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/274)
- **Mise à jour des dépendances:** Mises à jour de plusieurs dépendances, notamment `next`, `@gouvfr-lasuite/proconnect.debounce`, `proconnect-gouv/federation/api-partner`, `flatted`, `glob` et `defu`.

### Autres changements
- Tests d'intégration de l'IDP. [#299](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/299)
- Tests de configuration FI. [#278](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/278)
- Tests.proco. [#293](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/293)

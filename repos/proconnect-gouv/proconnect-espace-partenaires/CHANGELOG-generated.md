## Changelog : proconnect-espace-partenaires (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation, notamment concernant l'intégration eIDAS et l'authentification forte. Des corrections et clarifications ont été apportées pour faciliter la compréhension des partenaires et améliorer l'expérience d'intégration. Des mises à jour techniques ont également été effectuées pour maintenir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Clarification de la distinction entre eIDAS1-MFA et eIDAS2 dans la documentation. [#349](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/349)
- Amélioration de la documentation concernant les niveaux eIDAS pour les fournisseurs de service. [#352](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/352)
- Suppression de la distinction "géré par l'organisation" pour eIDAS2/eIDAS3 dans la documentation. [#367](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/367)
- Ajout d'une documentation pour le paramètre `organization_label`. [#348](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/348)
- Mise à jour de la documentation concernant l'authentification à double facteur. [#375](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/375)

### Évolutions techniques
- Mise à jour de la dépendance `proconnect-gouv/federation/api-partner` dans plusieurs commits.
- Mise à jour des dépendances de développement : `@babel/core`, `js-yaml`, `esbuild`, `@playwright/test`, `@uuv/playwright`, `tsx`, `form-data`, `actions/checkout`.
- Suppression d'anciennes adresses IP. [#360](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/360)
- Suppression d'une note de prudence concernant la définition du niveau ACR. [#369](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/369)
- Suppression d'une exigence d'autorisation obsolète pour le scope `roles`. [#353](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/353)

### Autres changements
- Restructuration de la documentation concernant les données fournies par les fournisseurs de service pour une meilleure clarté. [#317](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/317)
- Regroupement des données additionnelles et complémentaires dans la documentation. [#347](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/347)
- Ajout d'une table des matières pour l'organisation-label dans la documentation. [#351](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/351)
- Ajout d'une ressource partagée `norme_eidas` à la documentation FS et FI. [#350](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/350)
- Intégration du guide ANSSI sur les distinctions eIDAS dans la documentation. [#362](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/362)
- Linter : corrections et améliorations de la qualité du code.

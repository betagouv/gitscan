## Changelog : sill-deploy (30 derniers jours, au 19 mars 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur une refonte majeure de la gestion des types de logiciels dans Catalogi, visant à unifier et simplifier le schéma de données. Des améliorations ont également été apportées à l'infrastructure de déploiement et à l'environnement de développement.

### Évolutions fonctionnelles

*   Ajout d'un endpoint `/v2/catalogi.json` qui retourne la liste de tous les logiciels [#491](https://github.com/codegouvfr/sill-deploy/issues/491).
*   Possibilité d'accéder à la base de données PostgreSQL via un tunnel SSH pour faciliter le débogage et l'inspection des données [#74792b0](https://github.com/codegouvfr/sill-deploy/commit/74792b0).
*   Ajout de champs personnalisables pour les logiciels dans la table `softwares` [#f952712](https://github.com/codegouvfr/sill-deploy/commit/f952712).

### Évolutions techniques

*   **Refonte des types de logiciels :** Une refonte complète de la gestion des types de logiciels a été entreprise (issue [#491](https://github.com/codegouvfr/sill-deploy/issues/491)) avec :
    *   Définition de nouveaux types de logiciels canoniques.
    *   Renommage des colonnes de la table `softwares` pour correspondre au nouveau schéma.
    *   Suppression des données externes obsolètes.
    *   Alignement des types API et web avec le nouveau schéma canonique.
*   **Infrastructure :**
    *   Mise en place de workflows de déploiement spécifiques au SILL et synchronisation avec le projet principal [#a01ac44](https://github.com/codegouvfr/sill-deploy/commit/a01ac44).
    *   Passage de Yarn à pnpm pour la gestion des dépendances [#774d5e5](https://github.com/codegouvfr/sill-deploy/commit/774d5e5).
    *   Mise à jour de Node.js vers la version 24 et de pnpm vers la version 10.32.1 [#02b1d8e](https://github.com/codegouvfr/sill-deploy/commit/02b1d8e).
    *   Utilisation de `tsx` pour le développement de l'API avec rechargement à chaud [#e63d1d5](https://github.com/codegouvfr/sill-deploy/commit/e63d1d5).
*   **Architecture :**
    *   Utilisation d'un modèle de packages internes pour le partage de types entre l'API et l'interface web [#d4ca4e6](https://github.com/codegouvfr/sill-deploy/commit/d4ca4e6).

### Autres changements

*   Ajout d'une feuille de route pour l'unification des types de logiciels [#fe94aa5](https://github.com/codegouvfr/sill-deploy/commit/fe94aa5).
*   Documentation ajoutée concernant la migration de Yarn vers pnpm, l'utilisation de `tsx` en développement et le partage de packages [#68c1a26](https://github.com/codegouvfr/sill-deploy/commit/68c1a26).
*   Mise à jour de l'outil d'analyse IOC pour utiliser `pnpm-lock.yaml` [#4a8c1a7](https://github.com/codegouvfr/sill-deploy/commit/4a8c1a7).
*   Plusieurs corrections et ajustements liés à la refonte des types de logiciels (renommage de champs, correction de données, etc.) [#af95e5c](https://github.com/codegouvfr/sill-deploy/commit/af95e5c), [#be9ab74](https://github.com/codegouvfr/sill-deploy/commit/be9ab74), [#b322515](https://github.com/codegouvfr/sill-deploy/commit/b322515), [#b25d1fa](https://github.com/codegouvfr/sill-deploy/commit/b25d1fa), [#7e3f7e7](https://github.com/codegouvfr/sill-deploy/commit/7e3f7e7), [#51ad6b9](https://github.com/codegouvfr/sill-deploy/commit/51ad6b9), [#4fe147a](https://github.com/codegouvfr/sill-deploy/commit/4fe147a), [#2cc2ee4](https://github.com/codegouvfr/sill-deploy/commit/2cc2ee4), [#24aaabf](https://github.com/codegouvfr/sill-deploy/commit/24aaabf), [#0100fa5](https://github.com/codegouvfr/sill-deploy/commit/0100fa5).

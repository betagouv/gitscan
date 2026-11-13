## Changelog : potentiel (30 derniers jours, au 12 novembre 2026)

### Résumé
Le projet a connu une phase d'activité intense marquée par l'intégration de plusieurs versions majeures (de la 3.92 à la 3.97). Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur (design responsive, nouveaux tableaux de bord), le renforcement de la sécurité (généralisation de ProConnect et de la 2FA) et une montée en version importante de l'infrastructure technique (PostgreSQL 18, Node 26, TypeScript 7).

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités et améliorations :**
    - Mise en place d'une page vitrine pour Potentiel et les appels d'offres [#4740](https://github.com/MTES-MCT/potentiel/issues/4740).
    - Amélioration du tableau de bord avec l'ajout d'une section "nouveautés" et l'affichage du nombre de demandes [#4691](https://github.com/MTES-MCT/potentiel/issues/4691), [#4698](https://github.com/MTES-MCT/potentiel/issues/4698).
    - Évolutions de l'API EDF OA [#4706](https://github.com/MTES-MCT/potentiel/issues/4706) et intégration de données de raccordement sur la page Candidature [#4697](https://github.com/MTES-MCT/potentiel/issues/4697).
    - Meilleure visibilité des autorités instructrices dans les listes et les détails des dossiers [#4791](https://github.com/MTES-MCT/potentiel/issues/4791), [#4762](https://github.com/MTES-MCT/potentiel/issues/4762).
    - Affichage de la carte et ajout de sections de détails (CDC) pour les dossiers éliminés [#4708](https://github.com/MTES-MCT/potentiel/issues/4708), [#4707](https://github.com/MTES-MCT/potentiel/issues/4707).
- **Gestion des processus et sécurité :**
    - Généralisation de l'authentification ProConnect pour tous les partenaires, incluant l'obligation de la double authentification (2FA) [#4705](https://github.com/MTES-MCT/potentiel/issues/4705), [#4744](https://github.com/MTES-MCT/potentiel/issues/4744).
    - Affinement des règles métier concernant les recours, les attestations de désignation et les mainlevées [#4774](https://github.com/MTES-MCT/potentiel/issues/4774), [#4716](https://github.com/MTES-MCT/potentiel/issues/4716), [#4719](https://github.com/MTES-MCT/potentiel/issues/4719).
    - Gestion des délais pour la prolongation des phases d'essai [#4699](https://github.com/MTES-MCT/potentiel/issues/4699).
- **Expérience utilisateur et corrections :**
    - Optimisation de l'interface pour les mobiles et tablettes (responsive) [#4785](https://github.com/MTES-MCT/potentiel/issues/4785), [#4761](https://github.com/MTES-MCT/potentiel/issues/4761).
    - Corrections sur l'affichage des listes (utilisateurs, GRD), des tâches et des événements en doublon [#4748](https://github.com/MTES-MCT/potentiel/issues/4748), [#4694](https://github.com/MTES-MCT/potentiel/issues/4694), [#4742](https://github.com/MTES-MCT/potentiel/issues/4742).

### Évolutions techniques
- **Infrastructure et Environnement :**
    - Migration de la base de données vers PostgreSQL 18 [#4760](https://github.com/MTES-MCT/potentiel/issues/4760).
    - Mise à jour majeure des runtimes : passage à Node 26 [#4787](https://github.com/MTES-MCT/potentiel/issues/4787) et TypeScript 7 [#4789](https://github.com/MTES-MCT/potentiel/issues/4789).
- **CI/CD et Sécurité :**
    - Renforcement de la sécurité de la CI et mises à jour de sécurité Next.js [#4764](https://github.com/MTES-MCT/potentiel/issues/4764), [#4727](https://github.com/MTES-MCT/potentiel/issues/4727).
    - Amélioration de la gestion des logs et de la surveillance (Sentry) [#4730](https://github.com/MTES-MCT/potentiel/issues/4730), [#4710](https://github.com/MTES-MCT/potentiel/issues/4710).
- **Outils :**
    - Amélioration de la CLI (gestion des stages, logging, suppression de subscriber) [#4776](https://github.com/MTES-MCT/potentiel/issues/4776), [#4778](https://github.com/MTES-MCT/potentiel/issues/4778).

### Autres changements
- Documentation de l'authentification [#4717](https://github.com/MTES-MCT/potentiel/issues/4717).
- Nettoyage du code (renommage de variables, suppression de typologies obsolètes et de feature flags) [#4777](https://github.com/MTES-MCT/potentiel/issues/4777), [#4763](https://github.com/MTES-MCT/potentiel/issues/4763), [#4734](https://github.com/MTES-MCT/potentiel/issues/4734).

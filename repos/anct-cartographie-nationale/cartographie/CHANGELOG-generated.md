## Changelog : cartographie (30 derniers jours, au 31 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte significative de son infrastructure technique, avec l'adoption de nouvelles bibliothèques et composants de l'écosystème Arckit. Ces changements visent à améliorer la maintenabilité, la performance et la cohérence du code. Une nouvelle fonctionnalité de formulaire de contact avec envoi d'emails a été ajoutée, permettant aux utilisateurs de contacter directement l'équipe. Des améliorations ont également été apportées aux filtres de recherche de lieux, notamment avec l'ajout de filtres de disponibilité.

### Évolutions fonctionnelles
- Ajout d'un formulaire de contact avec envoi d'emails via SMTP ([fca7f7d](https://github.com/anct-cartographie-nationale/cartographie/commit/fca7f7d15e4b6be20ece4a2b7c6fe384047f2752)).
- Amélioration des filtres de recherche de lieux avec l'ajout de filtres "ouvert maintenant" et "ouvert le week-end" ([5e43199](https://github.com/anct-cartographie-nationale/cartographie/commit/5e431994984addc366348f60659427490696295f)).
- Modification de l'étiquette affichée pour l'URL d'un lieu, passant de "Site internet" à "Site internet" ([2ae2aff](https://github.com/anct-cartographie-nationale/cartographie/commit/2ae2aff22b8f3846f821f316996f749b6a604d6b)).

### Évolutions techniques
- Migration de l'outil de suivi d'analytics Matomo vers `@arckit/telemetry` ([118f113](https://github.com/anct-cartographie-nationale/cartographie/commit/118f113dec9391048a863303c11e63fca1e2b112)).
- Refonte de la gestion des formulaires avec l'adoption de la bibliothèque `@arckit/form` ([52943dc](https://github.com/anct-cartographie-nationale/cartographie/commit/52943dc2b47841b2583619913437f7251469712d)).
- Adoption de composants d'interface utilisateur standardisés de `@arckit/daisyui` ([efb60f8](https://github.com/anct-cartographie-nationale/cartographie/commit/efb60f85a5c49868c41498c161957096476a6969)).
- Refonte de la gestion des routes Next.js avec l'adoption de `@arckit/nextjs` ([7af3a5d](https://github.com/anct-cartographie-nationale/cartographie/commit/7af3a5d6236f8f9327523a54276f117142688152)).
- Optimisation du chargement et du filtrage des horaires d'ouverture des lieux ([4f7f332](https://github.com/anct-cartographie-nationale/cartographie/commit/4f7f3324b31170f6f42588166163431f6247a831)).
- Mise à jour de l'infrastructure CI/CD avec l'utilisation de pnpm 11 et l'amélioration de la configuration des workflows ([2672b3e](https://github.com/anct-cartographie-nationale/cartographie/commit/2672b3e4f97f62486f9f6566940139141298966c)).
- Ajout de la détection de secrets avec Gitleaks dans les hooks pré-commit et CI ([f24c364](https://github.com/anct-cartographie-nationale/cartographie/commit/f24c3642468229f1780f07c4d35f299b96f56802)).

### Autres changements
- Mise à jour des dépendances `@arckit/nextjs` et `@arckit/resultset` vers la version 2.0.0 ([9f4f664](https://github.com/anct-cartographie-nationale/cartographie/commit/9f4f664792026f761974c61891b87996162f0955)).
- Configuration de l'envoi d'emails via Brevo (anciennement Sendinblue) en utilisant Secret Manager ([63bdff7](https://github.com/anct-cartographie-nationale/cartographie/commit/63bdff7819c977981143348468f58304a2134f05)).
- Mise à jour du domaine TEM pour l'envoi d'emails vers `inclusion-numerique.anct.gouv.fr` (reverté puis corrigé) ([705ded9](https://github.com/anct-cartographie-nationale/cartographie/commit/705ded95479a119642c777116251980b0227f467), [cba4497](https://github.com/anct-cartographie-nationale/cartographie/commit/cba449745064b3441148798226f6304f7476364e)).

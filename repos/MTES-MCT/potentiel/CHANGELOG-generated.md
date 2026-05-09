## Changelog : potentiel (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'import de données (notamment depuis le DN), la gestion des rôles et permissions, la correction de bugs liés à l'interface utilisateur et aux workflows, ainsi que des optimisations techniques pour la sécurité et la performance. Des améliorations ont également été apportées à la gestion des garanties financières et des documents.

### Évolutions fonctionnelles
- Import des renouvellements et de la puissance initiale avec le DN, incluant la mise à jour des exports correspondants. [#4200](https://github.com/MTES-MCT/potentiel/issues/4200)
- Possibilité de demander une mainlevée suite à un abandon de projet. [#4209](https://github.com/MTES-MCT/potentiel/issues/4209)
- Ajout des coordonnées géodésiques aux projets. [#4191](https://github.com/MTES-MCT/potentiel/issues/4191)
- Intégration des valeurs par défaut pour le coefficient K. [#4160](https://github.com/MTES-MCT/potentiel/issues/4160)
- Modification de l'attestation de conformité. [#4159](https://github.com/MTES-MCT/potentiel/issues/4159)
- Refonte des pages "Garanties financières" pour une meilleure expérience utilisateur. [#4175](https://github.com/MTES-MCT/potentiel/issues/4175)
- Ajout de la possibilité de signaler les PPA (DREAL/DGEC). [#4192](https://github.com/MTES-MCT/potentiel/issues/4192)
- Ajout d'un nouveau rôle "admin" (anciennement "admin" devient "dgec"). [#4183](https://github.com/MTES-MCT/potentiel/issues/4183)
- Import des références de raccordement depuis le DN. [#4103](https://github.com/MTES-MCT/potentiel/issues/4103)
- Amélioration de l'import des données du DN concernant la date d'échéance de la Garantie Financière. [#4197](https://github.com/MTES-MCT/potentiel/issues/4197) et [#4202](https://github.com/MTES-MCT/potentiel/issues/4202)

### Évolutions techniques
- Mise à jour des dépendances Next.js, React et React-DSFR pour corriger des failles de sécurité. [#4195](https://github.com/MTES-MCT/potentiel/issues/4195)
- Intégration des modifications de la release 3.77. [#4210](https://github.com/MTES-MCT/potentiel/issues/4210) et [#4199](https://github.com/MTES-MCT/potentiel/issues/4199)
- Refactoring de la projection détail fournisseur candidature. [#4203](https://github.com/MTES-MCT/potentiel/issues/4203)
- Refactoring des tests GRD, des requêtes et ajout d'un nouveau test. [#4201](https://github.com/MTES-MCT/potentiel/issues/4201)
- Ajout de la permission spécifique pour exporter les dossiers de raccordement. [#4169](https://github.com/MTES-MCT/potentiel/issues/4169)
- Ajout de `AWS_REGION` dans les variables d'environnement nécessaires pour le s3Schema de la partie CLI. [#4188](https://github.com/MTES-MCT/potentiel/issues/4188)
- Ajout des types de node au tsconfig de base. [#4166](https://github.com/MTES-MCT/potentiel/issues/4166)
- Simplification de la modélisation AO. [#4114](https://github.com/MTES-MCT/potentiel/issues/4114)
- Optimisation de la récupération des gestionnaires dans la DCR.
- Amélioration de la gestion du cache GraphQL.

### Autres changements
- Correction de bugs liés à la séparation des rôles admin/dgec. [#4208](https://github.com/MTES-MCT/potentiel/issues/4208)
- Amélioration de l'accessibilité : titre des pages, liens ARIA. [#4205](https://github.com/MTES-MCT/potentiel/issues/4205) et [#4186](https://github.com/MTES-MCT/potentiel/issues/4186)
- Correction d'un bug empêchant la soumission du formulaire lors du retour en arrière. [#4176](https://github.com/MTES-MCT/potentiel/issues/4176)
- Correction d'un bug lié à la suppression des raccordements pour les projets abandonnés.
- Corrections de typos et améliorations du design. [#4198](https://github.com/MTES-MCT/potentiel/issues/4198)
- Correction d'un bug empêchant la réception des notifications pour les cocontractants hors de leur zone. [#4178](https://github.com/MTES-MCT/potentiel/issues/4178)
- Correction d'erreurs de suppression et de simplification de code.
- Mise à jour des données de test. [#4181](https://github.com/MTES-MCT/potentiel/issues/4181)
- Suppression des notifications des étapes du projet en cas de recours. [#4179](https://github.com/MTES-MCT/potentiel/issues/4179)

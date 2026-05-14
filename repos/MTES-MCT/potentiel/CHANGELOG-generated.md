## Changelog : potentiel (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'import de données, la gestion des rôles utilisateurs et des signalements, ainsi que des corrections de bugs et des améliorations de l'expérience utilisateur, notamment sur les pages de garanties financières et d'attestation de conformité. Des mises à jour de sécurité des dépendances ont également été intégrées.

### Évolutions fonctionnelles
- Possibilité pour l'administration d'annuler un signalement PPA. [#4204](https://github.com/MTES-MCT/potentiel/issues/4204)
- Ajout du SIREN/SIRET dans le formulaire. [#4193](https://github.com/MTES-MCT/potentiel/issues/4193)
- Import des renouvellements et de la puissance initiale avec les DN (Données Normalisées) et mise à jour des exports. [#4200](https://github.com/MTES-MCT/potentiel/issues/4200)
- Intégration des valeurs par défaut pour le coefficient K. [#4160](https://github.com/MTES-MCT/potentiel/issues/4160)
- Refonte des pages "Garanties financières" pour une meilleure expérience utilisateur. [#4175](https://github.com/MTES-MCT/potentiel/issues/4175)
- Modification de l'attestation de conformité. [#4159](https://github.com/MTES-MCT/potentiel/issues/4159)
- Ajout de la possibilité de demander une mainlevée suite à un abandon. [#4209](https://github.com/MTES-MCT/potentiel/issues/4209)
- Ajout des coordonnées géodésiques. [#4191](https://github.com/MTES-MCT/potentiel/issues/4191)
- Implémentation du signalement PPA (DREAL/DGEC). [#4192](https://github.com/MTES-MCT/potentiel/issues/4192)

### Évolutions techniques
- Mise à jour des dépendances Next.js, React et React-DSFR pour corriger des failles de sécurité. [#4195](https://github.com/MTES-MCT/potentiel/issues/4195)
- Ajout d'un nouveau rôle "admin" et transformation de l'ancien rôle "admin" en "dgec". [#4183](https://github.com/MTES-MCT/potentiel/issues/4183)
- Suppression des utilisations de `getContext` du package `@potentiel-applications/request-context` dans le SSR (Server Side Rendering). [#4224](https://github.com/MTES-MCT/potentiel/issues/4224)
- Utilisation d'un helper server only pour gérer les feature flags côté SSR. [#4218](https://github.com/MTES-MCT/potentiel/issues/4218)
- Ajout de vérifications de variables d'environnement sur les différents scripts `@potentiel/cli`. [#4211](https://github.com/MTES-MCT/potentiel/issues/4211)
- Correction d'un problème de flaky test. [#4213](https://github.com/MTES-MCT/potentiel/issues/4213)
- Utilisation du type helper `IdentifiantParameter` aux endroits oubliés. [#4214](https://github.com/MTES-MCT/potentiel/issues/4214)
- Ajout de AWS_REGION dans les variables d'environnement nécessaires pour le s3Schema de la partie CLI. [#4188](https://github.com/MTES-MCT/potentiel/issues/4188)
- Ajout des types de node au tsconfig de base. [#4166](https://github.com/MTES-MCT/potentiel/issues/4166)

### Autres changements
- Correction de bugs liés à l'export du lauréat et ajout des coordonnées à NomEtLocalitéLauréatImportés-V1. [#4232](https://github.com/MTES-MCT/potentiel/issues/4232)
- Correction d'un bug où la modification d'un GRD sans email de contact échouait si aucun changement n'était effectué dans le formulaire. [#4229](https://github.com/MTES-MCT/potentiel/issues/4229)
- Correction des cdc disponibles pour CRE4 ZNI. [#4221](https://github.com/MTES-MCT/potentiel/issues/4221)
- Ajout de titres manquants et uniformisation. [#4228](https://github.com/MTES-MCT/potentiel/issues/4228)
- Ajout des coordonnées au dump. [#4219](https://github.com/MTES-MCT/potentiel/issues/4219)
- Correction des oublis liés à la séparation des rôles admin/dgec. [#4208](https://github.com/MTES-MCT/potentiel/issues/4208)
- Ajout de liens ARIA aux listes réclamer, documents, utilisateurs pour l'accessibilité. [#4186](https://github.com/MTES-MCT/potentiel/issues/4186)
- Correction du bouton retour qui soumettait le formulaire. [#4176](https://github.com/MTES-MCT/potentiel/issues/4176)
- Mise à jour des CSP pour Crisp. [#4212](https://github.com/MTES-MCT/potentiel/issues/4212)
- Refacto des domaines champs supplémentaires. [#4147](https://github.com/MTES-MCT/potentiel/issues/4147)
- Suppression de la notification des étapes du projet en cas de recours. [#4179](https://github.com/MTES-MCT/potentiel/issues/4179)
- Correction d'un bug lié à l'import DN : date échéance GF. [#4197](https://github.com/MTES-MCT/potentiel/issues/4197) et [#4222](https://github.com/MTES-MCT/potentiel/issues/4222)
- Correction d'une erreur lors de la suppression.
- Diverses corrections et simplifications de code.
- Intégration des modifications de la release 3.78 et 3.77. [#4233](https://github.com/MTES-MCT/potentiel/issues/4233) et [#4210](https://github.com/MTES-MCT/potentiel/issues/4210)

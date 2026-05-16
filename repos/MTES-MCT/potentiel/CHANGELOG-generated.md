## Changelog : potentiel (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des signalements PPA, l'intégration de nouvelles données (DN, JOUE), et l'amélioration de l'expérience utilisateur, notamment en matière de gestion des garanties financières et de l'accessibilité. Des corrections de bugs et des optimisations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Possibilité pour l'administration d'annuler un signalement PPA. [#4204](https://github.com/MTES-MCT/potentiel/issues/4204)
- Ajout de la possibilité de modifier uniquement le SIRET d'un site. [#4225](https://github.com/MTES-MCT/potentiel/issues/4225)
- Import des données de renouvellement et de la puissance initiale avec les DN, incluant la date d'échéance de la garantie financière. [#4200](https://github.com/MTES-MCT/potentiel/issues/4200) et [#4197](https://github.com/MTES-MCT/potentiel/issues/4197)
- Ajout des coordonnées géodésiques. [#4191](https://github.com/MTES-MCT/potentiel/issues/4191)
- Intégration des valeurs par défaut pour le coefficient K. [#4160](https://github.com/MTES-MCT/potentiel/issues/4160)
- Ajout de la possibilité de demander une mainlevée suite à un abandon. [#4209](https://github.com/MTES-MCT/potentiel/issues/4209)
- Refonte des pages "Garanties financières" pour une meilleure expérience utilisateur. [#4175](https://github.com/MTES-MCT/potentiel/issues/4175)
- Ajout de la possibilité de signaler un PPA (DREAL/DGEC). [#4192](https://github.com/MTES-MCT/potentiel/issues/4192)
- Ajout du SIREN / SIRET. [#4193](https://github.com/MTES-MCT/potentiel/issues/4193)

### Évolutions techniques
- Mise à jour des dépendances Next.js, React et React-DSFR pour corriger des failles de sécurité. [#4195](https://github.com/MTES-MCT/potentiel/issues/4195)
- Ajout d'un nouveau rôle "admin" et modification du rôle "ancien admin" en "dgec". [#4183](https://github.com/MTES-MCT/potentiel/issues/4183)
- Suppression des utilisations de `getContext` du package `@potentiel-applications/request-context` dans le SSR. [#4224](https://github.com/MTES-MCT/potentiel/issues/4224)
- Ajout d'un helper server only pour gérer les feature flags côté SSR. [#4218](https://github.com/MTES-MCT/potentiel/issues/4218)
- Utilisation du type helper `IdentifiantParameter` aux endroits oubliés. [#4214](https://github.com/MTES-MCT/potentiel/issues/4214)
- Force l'utilisation de pg16 dans l'environnement de test de restauration. [#4217](https://github.com/MTES-MCT/potentiel/issues/4217)
- Mise à jour des CSP pour Crisp. [#4212](https://github.com/MTES-MCT/potentiel/issues/4212)
- Utilisation de vérifications de variable d'environnement sur les différents scripts `@potentiel/cli`. [#4211](https://github.com/MTES-MCT/potentiel/issues/4211)

### Autres changements
- Correction d'erreurs d'affichage de la raison dans l'historique. [#4238](https://github.com/MTES-MCT/potentiel/issues/4238)
- Correction de redirections d'emails vers les bonnes URLs. [#4239](https://github.com/MTES-MCT/potentiel/issues/4239)
- Correction d'un test flaky lié à la modification du site de production. [#4240](https://github.com/MTES-MCT/potentiel/issues/4240)
- Ajout de titres manquants et uniformisation de l'interface. [#4228](https://github.com/MTES-MCT/potentiel/issues/4228)
- Correction de l'export lauréat et ajout des coordonnées à NomEtLocalitéLauréatImportés-V1. [#4232](https://github.com/MTES-MCT/potentiel/issues/4232)
- Correction d'un problème de GRD sans email de contact lors de modifications du formulaire. [#4229](https://github.com/MTES-MCT/potentiel/issues/4229)
- Ajout de liens ARIA aux listes réclamer, documents et utilisateurs pour améliorer l'accessibilité. [#4186](https://github.com/MTES-MCT/potentiel/issues/4186)
- Suppression de la notification des étapes du projet en cas de recours. [#4179](https://github.com/MTES-MCT/potentiel/issues/4179)
- Correction d'une erreur lors de la suppression de raccordements pour les projets abandonnés.
- Correction d'erreurs liées à la séparation des rôles admin/dgec. [#4208](https://github.com/MTES-MCT/potentiel/issues/4208)
- Diverses corrections de bugs et améliorations de la qualité du code.

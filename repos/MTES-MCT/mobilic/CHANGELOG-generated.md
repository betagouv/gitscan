## Changelog : mobilic (30 derniers jours, au 22 mai 2026)

### Résumé
Les dernières mises à jour de Mobilic se concentrent sur l'amélioration de l'interface d'administration, notamment avec une refonte de la page d'accueil, l'ajout de fonctionnalités d'importation massive de véhicules et l'amélioration de la gestion des missions et des activités. Des corrections de bugs et des améliorations de sécurité ont également été apportées. L'application contrôle a bénéficié d'améliorations de l'interface et de la recherche d'infractions.

### Évolutions fonctionnelles
- Ajout d'un logo partenaire Chaventon Express sur l'interface [#848](https://github.com/MTES-MCT/mobilic/pull/848).
- Amélioration de la page d'accueil de l'administration avec une refonte complète [#836](https://github.com/MTES-MCT/mobilic/pull/836).
- Possibilité d'importer massivement des véhicules via une nouvelle modale [#837](https://github.com/MTES-MCT/mobilic/pull/837).
- Ajout de la possibilité de rechercher des informations NATINF dans l'application contrôle [#842](https://github.com/MTES-MCT/mobilic/pull/842).
- Amélioration de l'affichage des activités passées dans l'administration [#841](https://github.com/MTES-MCT/mobilic/pull/841) et [#839](https://github.com/MTES-MCT/mobilic/pull/839).
- Ajout du support de l'authentification à deux facteurs (TOTP) pour une sécurité renforcée [#2e2d935e](https://github.com/MTES-MCT/mobilic/commit/2e2d935e).
- Ajout de la fonctionnalité d'usurpation d'identité (impersonation) d'utilisateur pour l'administration [#826](https://github.com/MTES-MCT/mobilic/pull/826).
- Amélioration de la recherche d'infractions personnalisées dans l'application contrôle [#4c0112ef](https://github.com/MTES-MCT/mobilic/commit/4c0112ef).

### Évolutions techniques
- Refactorisation du code pour améliorer la réutilisation et la maintenabilité, notamment dans la gestion des dates et des composants d'interface utilisateur.
- Utilisation de constantes pour les couleurs et les configurations afin d'améliorer la cohérence et la facilité de modification.
- Amélioration de la validation des numéros d'immatriculation des véhicules.
- Utilisation des composants DSFR (Design Système Français Républicain) pour l'interface utilisateur, notamment dans l'application contrôle.
- Optimisation de la gestion des données et des requêtes GraphQL.

### Autres changements
- Mise à jour de la documentation et des textes de l'application, notamment concernant la page de sécurité [#850](https://github.com/MTES-MCT/mobilic/pull/850).
- Corrections de bugs mineurs et améliorations de l'expérience utilisateur.
- Suppression de code inutilisé et nettoyage du code source.
- Ajout de suivi des assets DSFR dans le build.
- Correction de problèmes de duplication de code détectés par SonarCloud.

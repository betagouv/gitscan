## Changelog : mobilic (30 derniers jours, au 18 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface administrateur, notamment avec la refonte de la page d'accueil et l'ajout de fonctionnalités d'importation massive de véhicules. Des corrections ont également été apportées pour améliorer la gestion des activités passées et la validation des données, ainsi que l'ajout de l'authentification à deux facteurs (TOTP) et de la possibilité d'impersonner des utilisateurs.

### Évolutions fonctionnelles
- Ajout de la recherche d'articles natinf dans le module de contrôle [#842](https://github.com/MTES-MCT/mobilic/issues/842).
- Amélioration de la gestion des dates dans le module de contrôle, notamment pour la sélection avec un QR code [#837](https://github.com/MTES-MCT/mobilic/issues/837).
- Implémentation de l'authentification à deux facteurs (TOTP) avec interface utilisateur complète et gestion de l'impersonation d'utilisateurs.
- Refonte de la page d'accueil de l'interface administrateur [#836](https://github.com/MTES-MCT/mobilic/issues/836).
- Ajout de la possibilité d'importer massivement des véhicules via un modal dédié [#837](https://github.com/MTES-MCT/mobilic/issues/837) et [#849](https://github.com/MTES-MCT/mobilic/issues/849).
- Affichage des activités même si la mission est antérieure à 31 jours [#841](https://github.com/MTES-MCT/mobilic/issues/841).
- Possibilité d'ajouter des infractions personnalisées dans le module de contrôle.
- Amélioration de l'affichage des erreurs frontend dans le module de contrôle.

### Évolutions techniques
- Refactorisation du code pour améliorer la réutilisation de composants et la lisibilité.
- Utilisation d'icônes DSFR dans les actions d'édition des tableaux de l'interface administrateur.
- Optimisation de la gestion des dates dans le panneau d'activités de l'interface administrateur.
- Amélioration de la validation du numéro d'immatriculation des véhicules.
- Utilisation de `replaceAll` au lieu de `replace` avec une expression régulière pour une meilleure performance.
- Extraction de la logique de configuration du date picker et de rafraîchissement dans des constantes partagées.
- Utilisation de chaînage optionnel pour accéder aux données des missions dans le reducer `workDays`.

### Autres changements
- Ajout de suivi Matomo spécifique aux véhicules.
- Correction de typos et amélioration de la documentation.
- Suppression de code inutilisé.
- Mise à jour des assets DSFR.
- Correction de problèmes de duplication de code détectés par SonarCloud.
- Correction de problèmes liés à la réassignation de paramètres dans le module de contrôle.
- Correction d'un bug lié à la déconnexion lors de l'impersonation.
- Correction d'un bug lié à l'affichage des informations de l'utilisateur dans la configuration TOTP.
- Correction d'un bug lié à la soumission du code TOTP en cas d'erreur GraphQL.
- Correction d'un bug lié à l'affichage des missions dans l'interface administrateur.

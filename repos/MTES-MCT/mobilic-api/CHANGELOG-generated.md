## Changelog : mobilic-api (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API Mobilic se concentrent sur l'amélioration de l'expérience utilisateur, notamment en simplifiant l'invitation et l'activation des utilisateurs, en ajoutant des informations sur le poids des véhicules aux bulletins de contrôle, et en optimisant la gestion des alertes réglementaires. Des améliorations techniques ont également été apportées pour la qualité du code, la gestion des erreurs et l'intégration avec des services tiers.

### Évolutions fonctionnelles
- Possibilité d'inviter des utilisateurs par leur ID lors d'invitations groupées. [#675](https://github.com/MTES-MCT/mobilic-api/pull/675)
- Simplification de l'inscription des utilisateurs invités par un employeur : activation automatique si l'email correspond, sinon envoi d'un email d'activation. [#395138a](https://github.com/MTES-MCT/mobilic-api/commit/395138a)
- Ajout du poids du véhicule (PTAC ou poids réel) sur les bulletins de contrôle (BDC). [#674](https://github.com/MTES-MCT/mobilic-api/pull/674), [#660](https://github.com/MTES-MCT/mobilic-api/pull/660), [#56c8378](https://github.com/MTES-MCT/mobilic-api/commit/56c8378)
- Amélioration de la gestion des alertes réglementaires pour les employés. [#665](https://github.com/MTES-MCT/mobilic-api/pull/665)
- Gestion des cas où il n'y a pas d'activité lors d'un contrôle. [#657](https://github.com/MTES-MCT/mobilic-api/pull/657)
- Nouvelle interface pour les bulletins de contrôle (BDC) avec correction des informations sur les entreprises. [#667](https://github.com/MTES-MCT/mobilic-api/pull/667)

### Évolutions techniques
- Ajout d'un hook `commitlint` pour assurer la conformité des messages de commit aux conventions. [#680](https://github.com/MTES-MCT/mobilic-api/pull/680)
- Optimisation de la gestion des erreurs et des alertes pour Scalingo. [#663](https://github.com/MTES-MCT/mobilic-api/pull/663)
- Restriction des fournisseurs d'identité (IdP) autorisés pour les contrôleurs. [#662](https://github.com/MTES-MCT/mobilic-api/pull/662)
- Amélioration de la gestion des emails pour les consentements tiers et l'activation des utilisateurs. [#676](https://github.com/MTES-MCT/mobilic-api/pull/676), [#664](https://github.com/MTES-MCT/mobilic-api/pull/664)
- Correction d'un crash lié au flush automatique lors de la validation d'un employé. [#682](https://github.com/MTES-MCT/mobilic-api/pull/682)
- Refactorisation de la logique d'affichage du poids du véhicule dans le bulletin de contrôle. [#5cc6251](https://github.com/MTES-MCT/mobilic-api/commit/5cc6251)

### Autres changements
- Mise à jour de la documentation et des tests pour les nouvelles fonctionnalités.
- Suppression de la dépendance `pypdf3`. [#662](https://github.com/MTES-MCT/mobilic-api/pull/662)
- Correction du nom du pipeline d'acquisition Brevo. [#668](https://github.com/MTES-MCT/mobilic-api/pull/668)
- Ajout d'index sur la table `employment`. [#74af1b7](https://github.com/MTES-MCT/mobilic-api/commit/74af1b7)

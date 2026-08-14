## Changelog : vao (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur la gestion complète du cycle de vie du "premier agrément", permettant aux administrations de demander des compléments, de modifier ou de refuser des dossiers de manière plus fluide. Le projet a également bénéficié d'améliorations significatives en matière d'accessibilité (RGAA) et de performances de la base de données.

### Évolutions fonctionnelles

**Gestion du premier agrément**
- Mise en place du processus complet de demande de compléments, de modification et de validation du premier agrément [#1492](https://github.com/SocialGouv/vao/issues/1492), [#1493](https://github.com/SocialGouv/vao/issues/1493), [#1504](https://github.com/SocialGouv/vao/issues/1504), [#1506](https://github.com/SocialGouv/vao/issues/1506).
- Gestion des refus de premier agrément côté DREETS, incluant la mise à jour des modèles d'emails de notification [#1495](https://github.com/SocialGouv/vao/issues/1495), [#1497](https://github.com/SocialGouv/vao/issues/1497).
- Création d'une page dédiée au premier agrément [#1501](https://github.com/SocialGouv/vao/issues/1501).
- Prise en charge globale des premiers agréments dans le back-office [#1487](https://github.com/SocialGouv/vao/issues/1487), [#1503](https://github.com/SocialGouv/vao/issues/1503).

**Administration et gestion des comptes**
- Amélioration de la visibilité des validations de comptes dans la liste du back-office [#1513](https://github.com/SocialGouv/vao/issues/1513).
- Possibilité de supprimer un agrément directement depuis le formulaire organisme [#1507](https://github.com/SocialGouv/vao/issues/1507).
- Correction d'erreurs de permissions et de dysfonctionnements sur les boutons de refus de compte [#1511](https://github.com/SocialGouv/vao/issues/1511), [#1500](https://github.com/SocialGouv/vao/issues/1500).

**Expérience utilisateur et accessibilité**
- Améliorations de l'accessibilité (RGAA) sur la hiérarchie des éléments et la page de récupération de mot de passe [#1486](https://github.com/SocialGouv/vao/issues/1486), [#1488](https://github.com/SocialGouv/vao/issues/1488).
- Corrections de formulaires (validation des dates de visite d'hébergement, onglet documents) et ajustements de libellés (mention casier judiciaire) [#1502](https://github.com/SocialGouv/vao/issues/1502), [#1499](https://github.com/SocialGouv/vao/issues/1499), [#1490](https://github.com/SocialGouv/vao/issues/1490).
- Masquage de certains éléments RGAA et bilans dans le back-office [#1491](https://github.com/SocialGouv/vao/issues/1491).

### Évolutions techniques

**Infrastructure et Performance**
- Migration de la construction des images vers `buildkit-operator` pour l'amélioration du CI [#1464](https://github.com/SocialGouv/vao/issues/1464).
- Optimisation de la base de données via l'indexation de requêtes pour résoudre des problèmes de lenteur (timeouts) en production [#1489](https://github.com/SocialGouv/vao/issues/1489).

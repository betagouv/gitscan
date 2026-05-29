## Changelog : karfur (30 derniers jours, au 27 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la détection et à la gestion des doublons, notamment au niveau des agents et des lieux. Des corrections de bugs ont été implémentées pour améliorer la stabilité de l'application, en particulier concernant les erreurs 500 observées en production et les problèmes d'affichage sur mobile. Des ajustements d'interface et des corrections de coquilles ont également été effectués pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un endpoint pour la recherche de doublons d'agents [#3754](https://github.com/refugies-info/karfur/pull/3754).
- Amélioration du classement des candidats potentiels en cas de doublons [#3758](https://github.com/refugies-info/karfur/pull/3758).
- Correction d'une coquille sur la page "mission" [#3746](https://github.com/refugies-info/karfur/pull/3746).
- Correction de l'affichage du compteur de bénévoles sur la page de traduction [#3736](https://github.com/refugies-info/karfur/pull/3736).
- Correction du padding sur le dernier accordéon de la fiche RCO [#3742](https://github.com/refugies-info/karfur/pull/3742).

### Évolutions techniques
- Amélioration de la gestion des erreurs et des valeurs nulles pour le prénom des utilisateurs SSO [#3751](https://github.com/refugies-info/karfur/pull/3751).
- Stabilisation de la configuration de Jest pour les tests mobiles [#3753](https://github.com/refugies-info/karfur/pull/3753).
- Ajout de tests Jest pour la configuration mobile [#3753](https://github.com/refugies-info/karfur/pull/3753).
- Correction de problèmes de scoring des doublons [#3760](https://github.com/refugies-info/karfur/pull/3760).
- Mise à jour des dépendances pnpm et des actions GitHub [#3715](https://github.com/refugies-info/karfur/pull/3715), [#3741](https://github.com/refugies-info/karfur/pull/3741), [#3734](https://github.com/refugies-info/karfur/pull/3734).
- Correction de problèmes liés à la reconstruction des traductions pour les démarches.
- Ajout de GitLeaks pour la détection de secrets dans le code.

### Autres changements
- Correction de problèmes de validation des traductions [#3735](https://github.com/refugies-info/karfur/pull/3735).
- Amélioration de la gestion des erreurs 500 en production [#3745](https://github.com/refugies-info/karfur/pull/3745).
- Correction de problèmes de formatage des nombres en français.
- Mise à jour des dépendances de sécurité.

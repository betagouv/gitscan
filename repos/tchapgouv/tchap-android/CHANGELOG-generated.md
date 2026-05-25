## Changelog : tchap-android (30 derniers jours, au 4 mai 2026)

### Résumé
Cette version apporte des améliorations à la sécurité, notamment concernant la réinitialisation de l'identité et la gestion des exceptions de sécurité pour les tuiles OpenMapTiles. Des corrections de bugs ont été implémentées pour résoudre des erreurs lors de la réinitialisation de l'application et des problèmes liés à l'analyse statique du code (linting). Enfin, la vérification des appareils a été réactivée.

### Évolutions fonctionnelles
- Correction d'une erreur "Cannot find secrets in storage" qui survenait lors de la réinitialisation complète de l'application.
- Réactivation de la bannière de vérification des appareils [#3aa4b16069].
- Amélioration de la réinitialisation de l'identité, corrigeant des problèmes liés aux signatures croisées et à la clé de récupération [#c405759740].

### Évolutions techniques
- Mise à jour vers la version 1.6.58 d'Element Android [#3d90260e1c, #29f7544612].
- Ajout d'une exception de sécurité pour les tuiles OpenMapTiles [#42a823b63b].
- Corrections de problèmes identifiés par l'analyse statique du code (linting) [#4851eb84ed, #43ca5ca1d6].
- Corrections liées au flux MAS [#ccd6d2f463].

### Autres changements
- Ajout de changelogs pour certaines fonctionnalités [#8ba0442b37, #b7c129f3ae].
- Mise à jour des textes de l'application [#617f5b2f87].
- Correction d'un problème de linting concernant une constante incorrecte [#776f24c1c1].
- Correction d'un problème lié à la localisation [#42afd38bbe].

## Changelog : mon-indemnisation-justice (30 derniers jours, au 25 juin 2026)

### Résumé
Ce changelog fait état d'une période riche en améliorations et corrections, touchant à la fois l'expérience utilisateur et les fondations techniques de l'application. Les efforts se sont concentrés sur l'amélioration de la gestion des dossiers, la correction de bugs, l'intégration de nouvelles fonctionnalités (comme la frise temporelle et le test d'éligibilité), et le renforcement de la sécurité et de la robustesse de l'application.

### Évolutions fonctionnelles
- Ajout d'une frise temporelle pour visualiser l'historique des dossiers [#86e0f75](https://github.com/betagouv/mon-indemnisation-justice/commit/86e0f75).
- Mise en place du test d'éligibilité dans l'espace public [#be88cc6](https://github.com/betagouv/mon-indemnisation-justice/commit/be88cc6).
- Possibilité de modifier les critères de recherche de dossiers [#b3785de](https://github.com/betagouv/mon-indemnisation-justice/commit/b3785de).
- Affichage des pièces jointes au format PDF via `react-pdf` [#216a13f](https://github.com/betagouv/mon-indemnisation-justice/commit/216a13f).
- Création d'une page "Mes dossiers" permettant de lister les dossiers associés à un utilisateur [#c54ef5c](https://github.com/betagouv/mon-indemnisation-justice/commit/c54ef5c).
- Amélioration du navigateur de pages pour une meilleure expérience utilisateur [#aae1bba](https://github.com/betagouv/mon-indemnisation-justice/commit/aae1bba).
- Fluidification de l'affichage des champs et possibilité de masquer les outils Tanstack [#e8aeaf1](https://github.com/betagouv/mon-indemnisation-justice/commit/e8aeaf1).
- Correction du fonctionnement de la modale de mot de passe oublié [#f120742](https://github.com/betagouv/mon-indemnisation-justice/commit/f120742).
- Ajout d'une gestion des erreurs FIP6 et FDO avec affichage et remontée des erreurs [#8272609](https://github.com/betagouv/mon-indemnisation-justice/commit/8272609) et [#4d0b818](https://github.com/betagouv/mon-indemnisation-justice/commit/4d0b818).
- Mise en place d'un tourniquet avec message de chargement au démarrage de l'application [#7655272](https://github.com/betagouv/mon-indemnisation-justice/commit/7655272).

### Évolutions techniques
- Injection de l'URL de déconnexion dans le contexte agent pour une meilleure gestion de l'authentification [#78a286f](https://github.com/betagouv/mon-indemnisation-justice/commit/78a286f).
- Utilisation de la version legacy de `react-pdf` pour résoudre des problèmes de compatibilité [#f6e7923](https://github.com/betagouv/mon-indemnisation-justice/commit/f6e7923).
- Mise en place de headers CSP (Content Security Policy) pour renforcer la sécurité de l'application [#2d7460c](https://github.com/betagouv/mon-indemnisation-justice/commit/2d7460c) et corrections successives [#6c29178](https://github.com/betagouv/mon-indemnisation-justice/commit/6c29178), [#739a1ac](https://github.com/betagouv/mon-indemnisation-justice/commit/739a1ac).
- Intégration de Sentry pour la gestion des erreurs et le suivi des performances [#9a526f7](https://github.com/betagouv/mon-indemnisation-justice/commit/9a526f7).
- Refactoring de l'espace public avec amélioration de la qualité et de la cohérence du code [#820530a](https://github.com/betagouv/mon-indemnisation-justice/commit/820530a) et [#1d06713](https://github.com/betagouv/mon-indemnisation-justice/commit/1d06713).
- Conversion de la page "Mon compte" vers React [#55e0da8](https://github.com/betagouv/mon-indemnisation-justice/commit/55e0da8).
- Mise en place de tests unitaires et end-to-end pour garantir la qualité du code [#47ad9ec](https://github.com/betagouv/mon-indemnisation-justice/commit/47ad9ec).

### Autres changements
- Mise à jour du guide de déclaration PN [#b673eb7](https://github.com/betagouv/mon-indemnisation-justice/commit/b673eb7).
- Corrections diverses et amélioration de la documentation.
- Suppression de dépendances inutiles et nettoyage du code.
- Correction de liens morts et amélioration de l'accessibilité.

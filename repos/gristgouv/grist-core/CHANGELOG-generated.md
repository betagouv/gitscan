## Changelog : grist-core (30 derniers jours, au 31 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment en matière d'accessibilité avec l'ajout de raccourcis clavier et une meilleure compatibilité avec les lecteurs d'écran. Des efforts importants ont également été consacrés à la sécurité, avec l'implémentation d'un flux OAuth et la gestion des consentements. Enfin, des corrections et des améliorations ont été apportées au processus d'installation rapide et à la gestion des documents.

### Évolutions fonctionnelles
- Ajout de raccourcis clavier pour ouvrir les menus de ligne et de colonne dans les vues de grille. [#2230](https://github.com/gristlabs/grist-core/issues/2230)
- Amélioration du support des lecteurs d'écran dans les vues de grille. [#2114](https://github.com/gristlabs/grist-core/issues/2114)
- Ajout de nouveaux formats de date. [#2347](https://github.com/gristlabs/grist-core/issues/2347)
- Implémentation d'un flux OAuth avec gestion des consentements et des autorisations. [#150](https://github.com/gristlabs/grist-core/issues/150)
- Amélioration du processus d'installation rapide, notamment pour les utilisateurs venant de getgrist.com. [#2310](https://github.com/gristlabs/grist-core/issues/2310)
- Possibilité d'utiliser du CSS personnalisé dans les widgets. [#2089](https://github.com/gristlabs/grist-core/issues/2089)
- Ajout d'un point de terminaison MCP (pour les instances SaaS). [#2363](https://github.com/gristlabs/grist-core/issues/2363)
- Amélioration de la détection de la langue et des mécanismes de repli pour la localisation. [#2313](https://github.com/gristlabs/grist-core/issues/2313)

### Évolutions techniques
- Ajout d'un backend de stockage externe basé sur le système de fichiers pour les tests.
- Refonte de la structure OIDC en préparation de l'implémentation du flux de consentement et de gestion des autorisations.
- Mise à jour de plusieurs dépendances : `webpack-dev-server`, `ws`, `multiparty`, `axios`, `file-type`, `node-forge`, `postcss`, `lodash`.
- Amélioration de la gestion des erreurs et de la robustesse du serveur.
- Ajout d'un mécanisme pour forker un document lors de sa modification depuis la popup d'assistance.
- Ajout d'un backend filesystem pour le stockage externe.

### Autres changements
- Mise à jour de la documentation et du README pour couvrir le processus d'installation rapide. [#2366](https://github.com/gristlabs/grist-core/issues/2366)
- Corrections de tests pour assurer la stabilité de la suite de tests.
- Traductions mises à jour pour plusieurs langues : Hongrois, Italien, Portugais, Allemand, Indonésien, Basque, Chinois simplifié, Français.
- Signature des CLA (Contributor License Agreement) par plusieurs contributeurs.
- Nettoyage et refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Réservation du sous-domaine "forum". [#2351](https://github.com/gristlabs/grist-core/issues/2351)
- Correction d'une erreur de console lors de l'utilisation de `ctrl+alt+o` sur la page d'accueil. [#2343](https://github.com/gristlabs/grist-core/issues/2343)
- Prévention de la création de forks anonymes. [#2319](https://github.com/gristlabs/grist-core/issues/2319)

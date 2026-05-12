## Changelog : drive (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la prévisualisation des fichiers, notamment des PDF, et sur l'ajout de nouvelles fonctionnalités liées aux droits d'accès et à la gestion des fichiers. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité.

### Évolutions fonctionnelles
- Ajout d'une modal d'avertissement concernant les droits d'accès pour certains fichiers. [#aa09906](https://github.com/suitenumerique/drive/commit/aa09906123456789abcdef0123456789)
- Amélioration de la prévisualisation des fichiers PDF avec affichage des miniatures, zoom et navigation par page.
- Possibilité de configurer la durée de validité des invitations via une variable d'environnement. [#352e195](https://github.com/suitenumerique/drive/commit/352e195123456789abcdef0123456789)
- Amélioration de la gestion des téléchargements avec affichage de la progression, des erreurs et possibilité d'annulation.
- Ajout de métriques d'organisation à l'API d'utilisation. [#aa09906](https://github.com/suitenumerique/drive/commit/aa09906123456789abcdef0123456789)
- Possibilité de configurer l'utilisation de PKCE pour l'authentification SSO. [#e355497](https://github.com/suitenumerique/drive/commit/e355497123456789abcdef0123456789)
- Ajout d'un menu d'actions sur mobile pour la page "Mes fichiers".
- Amélioration de la gestion des colonnes personnalisées avec tri et internationalisation.

### Évolutions techniques
- Refactorisation des composants de prévisualisation de fichiers pour utiliser les composants de la librairie `ui-kit`.
- Migration des imports MIME vers la librairie `ui-kit`.
- Amélioration de la gestion des transactions lors de la duplication de fichiers. [#68abb54](https://github.com/suitenumerique/drive/commit/68abb54123456789abcdef0123456789)
- Refactorisation des entitlements dans un package backend dédié.
- Amélioration de la gestion des erreurs et de la journalisation pour l'action `get_file_content` dans WOPI. [#d6e27ba](https://github.com/suitenumerique/drive/commit/d6e27ba123456789abcdef0123456789)
- Mise à jour de plusieurs dépendances (React, Next.js, Pytest, Vite).
- Suppression de la fonctionnalité de mirroring. [#805ef77](https://github.com/suitenumerique/drive/commit/805ef77123456789abcdef0123456789)
- Amélioration de la gestion des uploads lors de la suppression du dossier parent.
- Amélioration de la performance et de la stabilité des tests E2E.
- Refactorisation du code de prévisualisation pour une meilleure maintenabilité.

### Autres changements
- Mise à jour de la documentation (changelog).
- Ajout de tests E2E pour les nouvelles fonctionnalités et corrections de bugs.
- Correction de problèmes de SonarCloud.
- Suppression de code inutilisé.
- Mise à jour de la version de release à 0.18.0 [#9add475](https://github.com/suitenumerique/drive/commit/9add475123456789abcdef0123456789) et 0.17.0 [#3ca5b0e](https://github.com/suitenumerique/drive/commit/3ca5b0e123456789abcdef0123456789)

## Changelog : drive (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout de la duplication d'éléments, l'amélioration du gestionnaire d'upload, et l'intégration d'un visualiseur PDF. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment concernant la gestion des fichiers dans la corbeille et la gestion des tests E2E.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de duplication d'éléments (fichiers et dossiers) avec un préfixe "Copie de" pour le nouvel élément. [#238d6eb](https://github.com/suitenumerique/drive/commit/238d6eb)
- Amélioration du gestionnaire d'upload avec affichage de la progression, gestion des erreurs et possibilité d'annulation. [#399c1a7](https://github.com/suitenumerique/drive/commit/399c1a7)
- Intégration d'un visualiseur PDF avec navigation par pages, zoom et aperçu en vignette. [#62df235](https://github.com/suitenumerique/drive/commit/62df235)
- Ajout de la possibilité de trier les éléments par date de création et par nom du créateur. [#1441b4f](https://github.com/suitenumerique/drive/commit/1441b4f)
- Ajout de la possibilité de définir des colonnes personnalisées dans l'explorateur de fichiers. [#a4569a3](https://github.com/suitenumerique/drive/commit/a4569a3)
- Ajout d'une commande pour purger les éléments supprimés après une période définie. [#ea811ca](https://github.com/suitenumerique/drive/commit/ea811ca)
- Possibilité de supprimer définitivement les éléments de la corbeille. [#81fcb98](https://github.com/suitenumerique/drive/commit/81fcb98)

### Évolutions techniques
- Mise à jour de Django en version 5.2.13 (correction de sécurité). [#d4a83b6](https://github.com/suitenumerique/drive/commit/d4a83b6)
- Mise à jour de Pillow en version 12.2.0 (correction de sécurité). [#832725d](https://github.com/suitenumerique/drive/commit/832725d)
- Amélioration de la configuration CI/CD : pré-construction du frontend et service via Nginx pour les tests E2E. [#bdfade5](https://github.com/suitenumerique/drive/commit/bdfade5)
- Optimisation des tests E2E : parallélisation et mise en cache des navigateurs Playwright. [#2099179](https://github.com/suitenumerique/drive/commit/2099179)
- Restriction du token du workflow drive-frontend pour une meilleure sécurité. [#768f616](https://github.com/suitenumerique/drive/commit/768f616)
- Utilisation de react-query pour la gestion asynchrone des fichiers PDF. [#ee10b7b](https://github.com/suitenumerique/drive/commit/ee10b7b)
- Mise à jour de ds-proxy en version 2.0.0-alpha.4. [#2fc865e](https://github.com/suitenumerique/drive/commit/2fc865e)

### Autres changements
- Mise à jour de la documentation pour l'installation en réseau local. [#2a419c9](https://github.com/suitenumerique/drive/commit/2a419c9)
- Ajout de tests E2E pour les nouvelles fonctionnalités (duplication, colonnes personnalisées, PDF viewer).
- Correction de divers problèmes de style et de compatibilité dans le frontend.
- Amélioration de la gestion des erreurs et des messages d'information.
- Mise à jour des traductions.
- Nettoyage du code et suppression de code inutilisé.

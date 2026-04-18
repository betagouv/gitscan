## Changelog : drive (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à l'expérience utilisateur, notamment l'ajout de la duplication d'éléments, l'intégration d'un visualiseur PDF, et des améliorations de l'interface utilisateur pour les actions mobiles et les colonnes personnalisables. Des corrections de bugs et des optimisations de performance ont également été réalisées, ainsi qu'une amélioration de la sécurité.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de duplication d'éléments (fichiers et dossiers) avec un préfixe "Copie de" [#238d6eb](https://github.com/suitenumerique/drive/commit/238d6eb).
- Intégration d'un visualiseur PDF complet avec navigation par pages, zoom et barre de miniatures [#62df235](https://github.com/suitenumerique/drive/commit/62df235).
- Amélioration de l'expérience d'upload de fichiers avec affichage de la progression, gestion des erreurs et possibilité d'annulation [#399c1a7](https://github.com/suitenumerique/drive/commit/399c1a7).
- Ajout d'un menu d'actions sur mobile pour la page "Mes fichiers" [#0cc97d6](https://github.com/suitenumerique/drive/commit/0cc97d6).
- Implémentation de colonnes personnalisables dans l'explorateur de fichiers, avec tri et configuration [#0686605](https://github.com/suitenumerique/drive/commit/0686605).
- Possibilité de trier les éléments par date de création, nom du créateur et taille [#1441b4f](https://github.com/suitenumerique/drive/commit/1441b4f).
- Ajout d'une commande pour purger les éléments supprimés définitivement [#ea811ca](https://github.com/suitenumerique/drive/commit/ea811ca).

### Évolutions techniques
- Mise à jour de Django en version 5.2.13 (correction de sécurité) [#d4a83b6](https://github.com/suitenumerique/drive/commit/d4a83b6).
- Mise à jour de Pillow en version 12.2.0 (correction de sécurité) [#832725d](https://github.com/suitenumerique/drive/commit/832725d).
- Amélioration de la configuration du workflow CI/CD pour pré-construire l'interface utilisateur et la servir via Nginx [#bdfade5](https://github.com/suitenumerique/drive/commit/bdfade5).
- Optimisation des tests E2E avec parallélisation et mise en cache des navigateurs Playwright [#2099179](https://github.com/suitenumerique/drive/commit/2099179).
- Refonte de l'architecture de l'upload de fichiers pour permettre l'annulation et une meilleure gestion des erreurs [#bdb5fcd](https://github.com/suitenumerique/drive/commit/bdb5fcd).
- Utilisation de React Query pour la gestion des données du visualiseur PDF [#ee10b7b](https://github.com/suitenumerique/drive/commit/ee10b7b).
- Amélioration de la configuration du serveur Nginx pour servir correctement les fichiers .mjs [#aca3adf](https://github.com/suitenumerique/drive/commit/aca3adf).

### Autres changements
- Mise à jour de la documentation pour inclure la configuration réseau locale [#622fb81](https://github.com/suitenumerique/drive/commit/622fb81).
- Ajout de tests E2E pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la couverture de code et correction de problèmes signalés par SonarCloud [#51552ac](https://github.com/suitenumerique/drive/commit/51552ac).
- Mise à jour des traductions pour les nouvelles fonctionnalités.
- Nettoyage du code et suppression de code inutilisé.
- Ajout de variables d'environnement pour configurer le comportement de PostHog en développement [#e132107](https://github.com/suitenumerique/drive/commit/e132107).

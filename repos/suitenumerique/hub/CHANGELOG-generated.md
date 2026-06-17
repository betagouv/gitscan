## Changelog : hub (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration significative de la fonctionnalité de chat. Les utilisateurs peuvent désormais profiter de réactions aux messages, de fils de discussion, d'une composition de messages améliorée et d'une intégration avec Matrix. L'interface utilisateur a également été enrichie avec un panneau d'outils pour accéder aux documents et d'autres fonctionnalités.

### Évolutions fonctionnelles
- Ajout de notifications toast pour une meilleure expérience utilisateur [#fbda3fa](https://github.com/suitenumerique/hub/commit/fbda3fa).
- Implémentation des réactions aux messages avec un sélecteur d'emojis et l'affichage des réactions sur les messages [#fddef9e](https://github.com/suitenumerique/hub/commit/fddef9e).
- Introduction des fils de discussion pour organiser les conversations et permettre des réponses structurées [#928eecf](https://github.com/suitenumerique/hub/commit/928eecf).
- Ajout d'un panneau d'outils pour le chat, incluant l'accès aux documents [#6604bf1](https://github.com/suitenumerique/hub/commit/6604bf1).
- Prévisualisation des fichiers (PDF, images, vidéos, audio) dans le panneau d'outils documents [#c3a9df4](https://github.com/suitenumerique/hub/commit/c3a9df4).
- Intégration du client Matrix pour la messagerie [#004883d](https://github.com/suitenumerique/hub/commit/004883d).
- Nouvelle interface de composition de messages [#be7ecac](https://github.com/suitenumerique/hub/commit/be7ecac).
- Ajout d'une bannière indiquant les fils de discussion non lus [#2ef00e8](https://github.com/suitenumerique/hub/commit/2ef00e8).
- Ajout d'une barre d'outils au survol des messages [#195a26d](https://github.com/suitenumerique/hub/commit/195a26d).

### Évolutions techniques
- Refactorisation de l'architecture du chat pour supporter plusieurs comptes [#cfbd7b0](https://github.com/suitenumerique/hub/commit/cfbd7b0).
- Généralisation du contrat des drivers de chat pour supporter plusieurs comptes [#8271178](https://github.com/suitenumerique/hub/commit/8271178).
- Séparation de l'API Hub des drivers de chat [#02b7f6d](https://github.com/suitenumerique/hub/commit/02b7f6d).
- Introduction de `MockDriver` et `StandardDriver` pour simplifier les tests et le développement [#38f9904](https://github.com/suitenumerique/hub/commit/38f9904).
- Amélioration de la gestion des layouts pour persister l'état de l'interface utilisateur [#aacd11b](https://github.com/suitenumerique/hub/commit/aacd11b).
- Utilisation de hooks pour gérer les requêtes et actions liées au chat [#1f344b8](https://github.com/suitenumerique/hub/commit/1f344b8).
- Amélioration de la couverture des tests E2E pour les nouvelles fonctionnalités de chat [#ca95bc3](https://github.com/suitenumerique/hub/commit/ca95bc3) et [#bd2f5c0](https://github.com/suitenumerique/hub/commit/bd2f5c0).
- Ajout de formatage Prettier pour l'ensemble du workspace [#d9bcde5](https://github.com/suitenumerique/hub/commit/d9bcde5).

### Autres changements
- Documentation de l'architecture multi-comptes du chat [#d28d6dd](https://github.com/suitenumerique/hub/commit/d28d6dd).
- Suppression des logs de débogage de la couche chat [#9e28901](https://github.com/suitenumerique/hub/commit/9e28901).
- Suppression du suivi du fichier `.env.development` [#064aa7e](https://github.com/suitenumerique/hub/commit/064aa7e).
- Réactivation du linting sur les builds [#b7124fa](https://github.com/suitenumerique/hub/commit/b7124fa).
- Ajout de couleurs de fond contextuelles pour l'interface utilisateur [#4058a28](https://github.com/suitenumerique/hub/commit/4058a28).
- Ajout des dépendances Matrix et OIDC [#1a35fa2](https://github.com/suitenumerique/hub/commit/1a35fa2).

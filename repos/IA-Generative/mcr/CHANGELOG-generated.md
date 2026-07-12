## Changelog : mcr (30 derniers jours, au 2026-07-09)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la performance et de la robustesse de la transcription, ainsi que sur la refactorisation de l'architecture pour une meilleure maintenabilité et scalabilité. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment pour l'importation de fichiers et la gestion des retours utilisateurs.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs lors de l'envoi de retours utilisateurs, avec validation de la longueur des commentaires et gestion des erreurs de base de données. [#831](https://github.com/IA-Generative/mcr/pulls/831)
- Ajout d'une fonctionnalité d'importation de fichiers en un clic, simplifiant le processus pour les utilisateurs. [#896](https://github.com/IA-Generative/mcr/pulls/896)
- Possibilité de télécharger les scripts des réunions. [#843](https://github.com/IA-Generative/mcr/pulls/843)
- Amélioration de la détection des échecs d'upload et signalement à Sentry. [#831](https://github.com/IA-Generative/mcr/pulls/831)
- Ajout d'une nouvelle compétence "testing-standard" pour faciliter la création et la revue des tests. [#925](https://github.com/IA-Generative/mcr/pulls/925)
- Amélioration de la gestion des URLs de webinaires. [#863](https://github.com/IA-Generative/mcr/pulls/863)

### Évolutions techniques
- Refactorisation majeure de l'architecture de la transcription, avec séparation des préoccupations en use cases et infrastructure. [#901](https://github.com/IA-Generative/mcr/pulls/901), [#866](https://github.com/IA-Generative/mcr/pulls/866), [#870](https://github.com/IA-Generative/mcr/pulls/870), [#822](https://github.com/IA-Generative/mcr/pulls/822), [#824](https://github.com/IA-Generative/mcr/pulls/824), [#825](https://github.com/IA-Generative/mcr/pulls/825)
- Implémentation de la transcription asynchrone pour améliorer la réactivité. [#866](https://github.com/IA-Generative/mcr/pulls/866)
- Optimisation du chargement des modèles de reconnaissance vocale (lazy loading) pour réduire le temps de démarrage et la consommation de ressources. [#923](https://github.com/IA-Generative/mcr/pulls/923)
- Parallélisation du traitement des chunks de transcription pour une meilleure performance. [#919](https://github.com/IA-Generative/mcr/pulls/919)
- Amélioration de l'observabilité avec l'intégration de Sentry et la gestion des erreurs HTTP. [#837](https://github.com/IA-Generative/mcr/pulls/837)
- Mise en place de hooks Git pour améliorer la qualité du code (linting, formatage, vérification des secrets). [#911](https://github.com/IA-Generative/mcr/pulls/911), [#844](https://github.com/IA-Generative/mcr/pulls/844)
- Utilisation de `httpx` au lieu de `fastapi` pour les requêtes HTTP. [#854](https://github.com/IA-Generative/mcr/pulls/854)
- Amélioration de la configuration de l'environnement local et CI/CD. [#917](https://github.com/IA-Generative/mcr/pulls/917), [#932](https://github.com/IA-Generative/mcr/pulls/932)

### Autres changements
- Documentation de la configuration de Sentry via 1Password. [#909](https://github.com/IA-Generative/mcr/pulls/909)
- Mise à jour des templates de rapport de bug et de feedback utilisateur. [#913](https://github.com/IA-Generative/mcr/pulls/913)
- Ajout d'une commande `make install` pour simplifier l'installation des dépendances locales. [#834](https://github.com/IA-Generative/mcr/pulls/834)
- Nettoyage du code et suppression de code obsolète.
- Indexation de nouvelles tables dans la base de données pour améliorer les performances des requêtes. [#918](https://github.com/IA-Generative/mcr/pulls/918)
- Backfill des données pour les réunions historiques. [#918](https://github.com/IA-Generative/mcr/pulls/918)

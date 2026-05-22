## Changelog : template-proto (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration avec Coolify pour un déploiement simplifié, l'utilisation de l'IA via Claude, et l'amélioration de l'expérience de développement avec des ajustements de configuration et de l'infrastructure. Des corrections ont également été apportées pour assurer la compatibilité avec les dernières versions du Design System Fr et pour améliorer la robustesse du processus de déploiement.

### Évolutions fonctionnelles
- Intégration de l'auto-provisionnement de Coolify lors du premier déploiement, simplifiant la mise en production et rapportant l'état dans l'interface `/save`. [#4](https://github.com/betagouv-experimentations/template-proto/issues/4)
- Ajout d'une étape `/cadrer` en amont de `/build` pour préparer l'utilisation des skills d'IA d'Etalab. [#1](https://github.com/betagouv-experimentations/template-proto/issues/1)
- Amélioration de la gestion des migrations de la base de données : elles sont désormais exécutées automatiquement au démarrage du conteneur si le journal Drizzle n'existe pas.
- Ajout d'un test de fumée avant de rendre le contrôle, assurant un minimum de fonctionnalité après le déploiement.

### Évolutions techniques
- Utilisation explicite de l'invocation des skills de Claude dans les phases `/build` et `/build` pour une meilleure gestion de l'IA. [#2](https://github.com/betagouv-experimentations/template-proto/issues/2)
- Mise à jour de l'URL Coolify pour refléter les changements récents. [#4](https://github.com/betagouv-experimentations/template-proto/issues/4)
- Refonte de la configuration de l'environnement de développement avec l'utilisation de variables d'environnement pour les ressources de la machine virtuelle d'agent.
- Suppression des installations npm globales dans le script de runtime de la machine virtuelle d'agent.
- Passage à la version 1.32 du Design System Fr et adaptation du code en conséquence. [#11a6b3c](https://github.com/betagouv-experimentations/template-proto/commit/11a6b3c)
- Ajout d'un fichier `package-lock.json` pour garantir des builds reproductibles.
- Correction du nom du script de runtime de la machine virtuelle d'agent.

### Autres changements
- Documentation mise à jour pour aligner le fichier `CLAUDE.md` sur le modèle Etalab IA beta.gouv. [#3](https://github.com/betagouv-experimentations/template-proto/issues/3)
- Ajout d'un fichier README orienté PM avec une personnalisation automatique lors du bootstrap.
- Amélioration de la capture de l'URL de la base de données interne depuis la réponse de création de Coolify.
- Renommage de la variable d'environnement `COOLIFY_TOKEN` en `COOLIFY_TOKEN_WRITE`.
- Ajustement de la taille de la machine virtuelle d'agent (RAM, disque, CPU) pour optimiser les performances.
- Service des assets statiques du Design System Fr depuis le dossier `public/`.
- Corrections diverses et améliorations de la configuration de l'environnement de développement.

## Changelog : st-ansible (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois a été marqué par une accélération importante du projet avec la publication des versions 0.5.0, 0.6.0 et 0.7.0. Les évolutions majeures incluent l'ajout du composant "Conversations", une refonte de la gestion des tâches de fond via Dramatiq, et des améliorations significatives de la sécurité, notamment sur la gestion des secrets et la confiance envers les autorités de certification.

### Évolutions fonctionnelles
- **Nouveaux services** : Introduction du rôle "Conversations", incluant son processus de déploiement (bootstrap) et sa documentation.
- **Intégration applicative** : Mise en place de la liaison entre les applications "Transfers" et "File-Scanner", intégrant nativement la détection antivirus.
- **Gestion des configurations et secrets** :
    - Possibilité de déployer les secrets des applications sous forme de fichiers via Podman.
    - Ajout d'une option pour restreindre l'exécution du processus "beat" à un seul hôte de workers.
    - Flexibilité accrue pour l'application "Messages" permettant d'utiliser Exav en remplacement de ClamAV.
- **Sécurité** : Mise à jour du CLI pour rejeter les autorités de certification (CA) eMudhra compromises.

### Évolutions techniques
- **Refonte de l'architecture des workers** : Migration des unités de workers vers Dramatiq [#123](https://github.com/suitenumerique/st-ansible/pull/123).
- **Fiabilité et monitoring** :
    - Amélioration de la surveillance des workers grâce à l'utilisation des healthchecks natifs de Dramatiq.
    - Optimisation des healthchecks Podman pour une exécution plus légère (sans recours à un shell).
- **Optimisation du CLI** : Amélioration de la logique de mise à jour (replay du socks-proxy) et découplage des tests de réparation du proxy.
- **Intelligence et filtrage** : Déploiement de la configuration du classificateur Bayes avec apprentissage automatique (autolearn) pour l'application "Messages".
- **Infrastructure** : Mise à jour des workflows GitHub Actions.

### Autres changements
- Ajout de la documentation pour le nouveau composant "Conversations".

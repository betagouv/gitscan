## Changelog : infra-apps (30 derniers jours, au 16/09/2026)

### Résumé
Ce mois a été marqué par une phase importante de stabilisation et de sécurisation de la plateforme Iterion. Les efforts se sont concentrés sur la fiabilisation des exécutions (runners), l'optimisation de la gestion des ressources Kubernetes pour éviter les interruptions de tâches, et le renforcement de la sécurité des accès et de la visibilité opérationnelle.

### Évolutions fonctionnelles
- **Nouvelle identité réseau** : `iterion.cloud` devient l'URL publique canonique de la plateforme, avec redirection automatique des anciens hôtes.
- **Observabilité accrue** : Intégration de l'envoi d'alertes opérationnelles vers Mattermost et activation du suivi d'erreurs via Sentry.
- **Amélioration des services** : Les déploiements sont désormais capables d'envoyer des emails.

### Évolutions techniques
- **Stabilisation du cœur Iterion** :
    - Mises à jour successives du runner et du serveur pour supporter de nouveaux schémas de file d'attente et corriger des régressions de configuration (notamment sur `kubectl`).
    - Fixation des images (runner et serveur) par *digest* pour garantir l'immuabilité des déploiements et empêcher la rupture des exécutions en cours lors des mises à jour.
- **Gestion des ressources et Scaling** :
    - Optimisation de la taille du pool de runners pour équilibrer la capacité de traitement et la stabilité des tâches de longue durée.
    - Mise en place de `PriorityClass` pour garantir que les composants critiques de la plateforme soient prioritaires sur les pods d'exécution [#732](https://github.com/SocialGouv/iterion#732).
    - Application de limites de mémoire (8Gi) sur les pods d'exécution et ajustement des politiques Kyverno pour une meilleure répartition des charges sur les nœuds.
- **Sécurité et Réseau** :
    - Sécurisation des instances Metabase via l'ajout d'un proxy `oauth2-proxy` et correction de la gestion des certificats SSL.
    - Correction des scopes OAuth2 pour GitHub afin de rétablir les permissions nécessaires.
- **Infrastructure et Données** :
    - Activation de la réplication de flux JetStream (R3) pour assurer la haute disponibilité des données en production.
    - Activation du tracing pour améliorer le diagnostic des performances.

### Autres changements
- **Nettoyage** : Déclassement (decommission) des composants `charon-carnets` et `metabase` (environnement recosante).
- **Documentation** : Mise à jour des notes techniques concernant le couplage entre les images du runner et du serveur.

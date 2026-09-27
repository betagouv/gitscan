## Changelog : infra-apps (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a été marqué par une phase importante de stabilisation et de montée en charge de la plateforme Iterion. Les efforts se sont concentrés sur l'amélioration de la disponibilité (réplication des données, gestion des files d'attente), l'augmentation des capacités de calcul et la sécurisation des accès. L'adresse publique officielle de la plateforme est désormais consolidée autour du domaine `iterion.cloud`.

### Évolutions fonctionnelles
- **Nouvelle identité web** : Migration vers `iterion.cloud` comme URL publique canonique pour la plateforme.
- **Nouveaux modèles d'IA** : Déploiement des runtimes Opus 5.5 et GPT-6 pour les utilisateurs.
- **Amélioration de l'expérience utilisateur** : Mise en place de redirections automatiques vers l'hôte canonique et activation de l'envoi d'e-mails par les déploiements.

### Évolutions techniques
- **Capacité et Performance (Iterion)** :
    - Augmentation de la taille du pool de runners (passage de 8 à 12 slots) pour mieux gérer la concurrence des tâches.
    - Optimisation de la gestion de la mémoire des pods de calcul (limite de 8Gi).
    - Mise en place de la réplication de flux JetStream (R3) sur la production pour garantir une haute disponibilité des données.
- **Fiabilité du CI/CD (ARC)** :
    - Amélioration de la résilience des runners avec l'ajout d'alertes en cas d'interruption pour éviter le blocage des files d'attente de fusion [#54].
    - Stabilisation du démarrage des runners et gestion des dépendances API (dind) [#55, #56].
    - Ancrage des images par digest pour éviter les interruptions de tâches en cours lors des mises à jour.
- **Sécurité et Conformité** :
    - Déploiement de l'antivirus ClamAV sur l'environnement `ovh-prod` pour le projet Domifa.
    - Sécurisation des instances Metabase via l'ajout d'un proxy OAuth2 et de certificats dédiés.
    - Renforcement de la sécurité des cookies de session et des scopes GitHub sur le proxy d'authentification.
    - Injection sécurisée de jetons "forge" dans les namespaces de CI.

### Autres changements
- **Nettoyage de l'infrastructure** : Déclassement des composants `charon-carnets` et de l'instance Metabase de l'environnement `recosante`.
- **Documentation** : Mise à jour des notes techniques concernant le couplage entre les images de runners et les serveurs.

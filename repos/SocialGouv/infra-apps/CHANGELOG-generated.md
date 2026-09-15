## Changelog : infra-apps (30 derniers jours, au 13/09/2026)

### Résumé
Ce mois a été principalement consacré à la stabilisation et à la professionnalisation de la plateforme Iterion. Les évolutions majeures incluent l'adoption d'une URL publique officielle, le renforcement de la haute disponibilité des données et une amélioration significative de la gestion des ressources de calcul pour éviter l'interruption des tâches de longue durée.

### Évolutions fonctionnelles
- **Nouvelle identité web** : `iterion.cloud` devient l'URL publique canonique de la plateforme.
- **Communications** : Le déploiement est désormais capable d'envoyer des emails.
- **Expérience utilisateur** : Correction du flux de retour après la connexion (sign-in) dans l'interface Studio.

### Évolutions techniques
- **Stabilité et mise à l'échelle d'Iterion** :
    - Optimisation du pool de runners (passage de 8 à 12 instances) pour absorber la charge des campagnes et des revues de PR.
    - Correction des problèmes de mise à l'échelle (KEDA) qui interrompaient les processus de calcul de longue durée.
    - Verrouillage des images de runners par digest pour éviter les ruptures de service lors des déploiements.
    - Ajustement de la gestion des ressources (mémoire et `PriorityClass`) pour garantir la priorité des pods de la plateforme sur les pods de calcul.
- **Fiabilité et Observabilité** :
    - Mise en place de la réplication de flux JetStream pour assurer la haute disponibilité des données (Data-HA).
    - Activation du traçage et intégration du suivi d'erreurs via Sentry pour une meilleure réactivité opérationnelle.
- **Sécurité et Authentification** :
    - Sécurisation des instances Metabase par l'ajout d'un proxy OAuth2 et correction de la gestion des certificats.
    - Nettoyage des secrets obsolètes (clés API OpenAI et Claude) et des secrets de forfait au niveau des pods.
    - Amélioration de la sécurité des pipelines CI/CD via l'isolation des tokens de forge dans les namespaces dédiés.
- **Maintenance des composants** :
    - Série de mises à jour critiques du runner de production pour corriger diverses régressions (notamment sur `kubectl`, la gestion des timeouts et les politiques de ressources) [[#822](https://github.com/SocialGouv/infra-apps/issues/822)], [[#846](https://github.com/SocialGouv/infra-apps/issues/846)], [[#850](https://github.com/SocialGouv/infra-apps/issues/850)].

### Autres changements
- **Nettoyage de l'infrastructure** : Déclassement et suppression des composants obsolètes `charon-carnets` et `metabase`.
- **Documentation** : Mise à jour de la documentation concernant la configuration des runners.

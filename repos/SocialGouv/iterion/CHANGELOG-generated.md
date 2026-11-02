## Changelog : iterion (30 derniers jours, au 02/11/2026)

### Résumé
Ce mois a été marqué par une montée en puissance de la sécurité et de la robustesse de la plateforme. Les efforts se sont concentrés sur l'isolation stricte des environnements d'exécution (sandboxing), la sécurisation de la gestion des secrets et des variables d'environnement, ainsi que sur la conformité de l'interface Studio aux normes d'accessibilité (RGAA). La plateforme gagne également en prévisibilité grâce à une gestion plus fine des budgets d'exécution et des capacités des agents IA.

### Évolutions fonctionnelles
- **Accessibilité (RGAA) :** Amélioration significative de l'interface Studio pour respecter les normes d'accessibilité, incluant la correction des contrastes, la gestion des rôles d'icônes, la navigation au clavier et la visibilité du focus [#2527, #2558, #2556, #2590].
- **Interface Studio :**
    - Ajout d'un éditeur pour les overrides de credentials des webhooks [#72c1ac4b].
    - Amélioration de la gestion des connexions via un nouvel écran d'administration des intégrations [#4abbad80].
    - Affichage des livrables (Markdown) directement dans le tiroir des artefacts du résumé de run [#2700].
    - Amélioration de la navigation : le passage entre les équipes est facilité et les menus d'organisation sont plus lisibles [#2560, #9a468].
- **Gestion des Agents et Bots :**
    - **Capacités explicites :** Le DSL permet désormais de déclarer explicitement les capacités (capabilities) d'un nœud, évitant des erreurs d'exécution imprévues [#1801, cc4cbeb].
    - **Mode de surveillance :** Introduction de "prod-watch" pour recevoir des digestes et des alertes de session via Mattermost [#2764, #1701].
    - **Sous-agents :** Support de la résolution de sous-agents nommés directement depuis le workspace [#7dd35049].
- **Connectivité :** Support du remplacement de tokens pour les connexions PAT et gestion améliorée des webhooks depuis le Studio [#318d9867, #2479].

### Évolutions techniques
- **Sécurité et Isolation (Sandboxing) :**
    - **Protection des environnements :** Renforcement massif de l'isolation des variables d'environnement (`.env`) pour empêcher les fuites de secrets entre le projet et l'hôte [#2310, #2321, #2339].
    - **Gestion des secrets :** Implémentation d'une gestion des secrets par "sinks" (destinations) et sécurisation des processus de rotation des credentials [#875c5922, #56c74126].
    - **Infrastructure Souveraine :** Mise en place de "Sovereign Runner Pools", permettant d'isoler physiquement les ressources (pods) par équipe ou par client pour garantir une séparation totale [#2273, #2236].
- **Runtime et DSL :**
    - **Gestion des budgets :** Amélioration de la précision du suivi des budgets, avec une proratisation automatique lors du franchissement de seuils et une gestion des signaux de travail pour les boucles [#d65f0a84, d50e711].
    - **Optimisation du Parser :** Amélioration de la résilience du parser lors de la lecture de listes corrompues et optimisation des performances de scan [#c2c34a83, c2c34a83].
    - **Routage adaptatif :** Implémentation d'une politique de routage (adaptive-routing) permettant de définir des règles de redirection au niveau de l'organisation ou de l'équipe [#2210, #2159].
- **Infrastructure et Backend :**
    - **Observabilité :** Exposition d'une surface `/metrics` pour permettre un monitoring complet via Prometheus [#9174dd9].
    - **Fiabilité des files d'attente :** Amélioration de la gestion des erreurs et des délais d'attente sur NATS, notamment lors des redémarrages de brokers [#1ad0c1d9, 7698d727].
    - **Stockage :** Optimisation des interactions avec MongoDB et S3 pour la gestion des pièces jointes et la persistance des runs [#ed8f8931, 0f49e66b].

### Autres changements
- **Documentation :**
    - Mise à jour majeure de la documentation incluant de nouveaux diagrammes de base de données (ERD), des schémas de flux de fonctionnalités et des guides de démarrage rapide [#2582, #2561, #2577, #2878].
    - Publication de plusieurs nouveaux ADR (Architecture Decision Records) concernant la sécurité des secrets et la gestion des dépendances de bundles [#144, #145, #146, #148].
- **CI/CD et Tests :**
    - Intégration de la suite de tests E2E Playwright directement dans le pipeline de CI [#9c0d139c].
    - Optimisation des jobs de tests pour réduire la consommation de ressources et améliorer la détection de comportements instables (flakiness) [#2213, #2568].

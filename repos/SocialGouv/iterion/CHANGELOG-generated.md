## Changelog : iterion (30 derniers jours, au 17 août 2026)

### Résumé
Ce mois a été marqué par une montée en puissance majeure de la plateforme, notamment avec l'introduction du nouveau backend d'exécution "Pi" et d'une architecture optimisée pour les interactions asynchrones entre l'IA et l'humain. L'expérience utilisateur a été considérablement enrichie par de nouveaux outils d'automatisation (triage d'issues, génération de wiki) et une interface de pilotage (Studio) plus intuitive et visuelle. La fiabilité globale a été renforcée par la mise en place de tests de non-régression comportementale ("Golden Master") et d'un système de gestion de la persistance des tâches.

### Évolutions fonctionnelles
- **Gestion des ressources et coûts** : Ajout de limites d'usage personnalisables pour prévenir les dépassements de quotas auprès des fournisseurs d'IA [#438](https://github.com/SocialGouv/iterion/pull/438).
- **Améliorations du Studio** : 
    - Prévisualisation directe des contenus (JSON, Markdown, texte) lors des étapes de validation humaine [#425](https://github.com/SocialGouv/iterion/pull/425).
    - Nouvel éditeur multi-fichiers pour la configuration des bots dans le cloud [#344](https://github.com/SocialGouv/iterion/pull/344).
    - Refonte du tableau de bord des pipelines avec un système de colonnes et de glisser-déposer [#243](https://github.com/SocialGouv/iterion/pull/243).
    - Interface de recherche et d'exploration de configuration par arbre rétractable.
- **Nouveaux agents spécialisés** :
    - **Triagy** : Automatisation du triage des issues via un système de routage intelligent [#22](https://github.com/SocialGouv/iterion/pull/22).
    - **Wikky** : Générateur de documentation (wiki) pour maintenir la connaissance du projet.
- **Accessibilité et Notifications** : 
    - Intégration d'un auditeur d'accessibilité (Ultra11y) pour garantir la conformité des interfaces [#409](https://github.com/SocialGouv/iterion/pull/409).
    - Système de notifications par Web Push pour alerter les opérateurs lors des pauses nécessitant une intervention [#266](https://github.com/SocialGouv/iterion/pull/266).

### Évolutions techniques
- **Architecture et Backends** :
    - Introduction de **Pi** comme backend d'exécution de premier rang [#308](https://github.com/SocialGouv/iterion/pull/308).
    - Implémentation de l'architecture asynchrone (ADR-081) permettant des interactions fluides et des points de suspension (await_answers) entre les nœuds et l'opérateur.
    - Déploiement d'un serveur **MCP** (Model Context Protocol) pour l'opérateur.
- **Fiabilité et Qualité** :
    - Mise en place de **Golden Master (Goldy)** : un réseau de non-régression comportementale pour valider les sorties des agents face à des scénarios de test complexes.
    - Renforcement de l'isolation via un système de **sandbox** amélioré (support Devbox) et une gestion plus stricte des identités Git et des credentials.
    - Amélioration de la résilience des exécutions : gestion du "keepalive" pour les tâches de longue durée et mécanisme de reprise (resume) plus robuste pour les sous-agents.
- **Infrastructure et CI/CD** :
    - Optimisation des pipelines d'images et découplage des flux de déploiement pour accélérer les cycles de release.
    - Amélioration de la gestion des budgets de tokens et de la détection des dérives de dépendances.

### Autres changements
- **Documentation** : Mise à jour massive et alignement de l'ensemble de la documentation technique (guides d'architecture, procédures de déploiement cloud, et bilans de runs de bots).
- **Nettoyage** : Refactorisation de la gestion des bundles et optimisation de la gestion des ressources de l'engine.

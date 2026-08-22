## Changelog : iterion (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois a été marqué par une consolidation majeure de la fiabilité et de la sécurité du système. L'introduction du framework "Golden Master" permet désormais de garantir la non-régression comportementale des agents par des audits automatisés. Parallèlement, le projet a renforcé l'isolation de ses environnements d'exécution (sandbox) et a considérablement enrichi l'interface de pilotage (Studio) pour offrir une meilleure visibilité sur les changements et les processus de validation humaine.

### Évolutions fonctionnelles
- **Nouveau juge d'arbitrage** : Introduction de *Themis*, un juge spécialisé pour résoudre les cas de divergence bloqués dans les workflows.
- **Améliorations du Studio** :
    - Prévisualisation directe des contenus (JSON, Markdown, texte) lors des étapes de validation humaine [#425].
    - Affichage des changements de fichiers directement dans la console de suivi des exécutions.
    - Interface de gestion des pipelines et des cartes Kanban améliorée pour un meilleur suivi des tâches.
    - Éditeur multi-fichiers pour la configuration des bots dans le cloud.
- **Nouveau serveur MCP** : Mise à disposition d'un serveur *Model Context Protocol* permettant d'exposer les capacités d'Iterion (locales et distantes) à d'autres outils d'IA.
- **Gestion des budgets et ressources** :
    - Amélioration de la détection et de la prévention des dépassements de budget lors des boucles d'exécution (loop budget guard).
    - Possibilité de mutualiser les quotas de souscription LLM entre les contributeurs.
- **Nouveautés DSL** : Ajout de la fonctionnalité `auto_memory` pour permettre une gestion automatique du contexte par nœud.

### Évolutions techniques
- **Framework Golden Master (Goldy)** : Déploiement d'un système complet de non-régression comportementale incluant l'audit de mutantes, la gestion de sceaux de validation (seal) et des rapports de verdict structurés pour garantir la stabilité des agents.
- **Sécurité et Isolation (Sandbox/Pi)** :
    - Renforcement massif du confinement (containment) pour protéger les credentials et les données sensibles.
    - Intégration du backend "pi" comme moteur d'exécution de premier rang.
    - Sécurisation des échanges de tokens et des accès aux secrets.
- **Résilience du Runtime** :
    - Implémentation d'une procédure de "lame-duck drain" permettant de terminer gracieusement les exécutions en cours lors d'un déploiement.
    - Amélioration de la reprise de session (StateRef) pour permettre de reprendre un nœud après une interruption.
- **Observabilité** : Intégration de Sentry et GlitchTip pour le suivi des erreurs et standardisation des logs pour une meilleure traçabilité des appels LLM [#463, #459].
- **Gestion des identités et credentials** : Possibilité de faire pivoter les credentials LLM de la plateforme via la base de données sans nécessiter de redéploiement [#466].

### Autres changements
- **Documentation** : Migration complète de la documentation vers **VitePress** et mise à jour massive des guides (MCP, DSL, architectures, et guides de déploiement).
- **Automatisation de la doc** : Mise en place d'un système de rafraîchissement automatique de la documentation via des bots dédiés, avec support des modes incrémentaux et des amendements de PR [#289].
- **Maintenance** : Nettoyage automatique des répertoires temporaires de projet (`PROJECT_SCRATCH_DIR`) pour optimiser l'espace disque [#469].

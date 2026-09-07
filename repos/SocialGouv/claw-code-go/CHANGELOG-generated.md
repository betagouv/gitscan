## Changelog : claw-code-go (30 derniers jours, au 5 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision des agents et l'intégration de la nouvelle génération de modèles Claude 5. Le système est désormais capable de produire des résultats structurés et validés, tout en offrant une gestion plus robuste et automatisée des modèles d'intelligence artificielle.

### Évolutions fonctionnelles
- **Amélioration du workflow d'agent** : L'outil `agent` peut désormais retourner des résultats structurés et validés selon un schéma défini, permettant une meilleure intégration des données produites par les sous-agents.
- **Correction du runtime** : Résolution d'un problème où des sorties structurées étaient sollicitées avant que l'agent n'ait effectué le travail nécessaire [#1](https://github.com/SocialGouv/claw-code-go/issues/1).

### Évolutions techniques
- **Mise à jour du registre de modèles** : 
    - Intégration de la famille de modèles Claude 5.
    - Les alias de modèles pointent désormais automatiquement vers la version la plus récente de leur lignée.
- **Optimisation de la gestion des modèles** : Implémentation d'une stratégie "copy-then-swap" pour les entrées de modèles rafraîchies en direct, évitant ainsi les mutations d'objets en place et garantissant une meilleure stabilité.
- **Tests et Fixtures** : Mise à jour des tests de l'API et des "golden fixtures" pour assurer la compatibilité avec les modèles Claude 5 (Opus et Sonnet).

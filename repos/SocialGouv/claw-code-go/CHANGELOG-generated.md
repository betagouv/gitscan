## Changelog : claw-code-go (30 derniers jours, au 22 mai 2024)

### Résumé
Les récentes évolutions renforcent la capacité du système à orchestrer des agents intelligents en améliorant la gestion des nouveaux modèles d'IA (notamment la famille Claude 5) et en permettant des interactions plus précises. Les utilisateurs peuvent désormais compter sur des agents capables de fournir des résultats structurés et validés, rendant les automatisations plus fiables.

### Évolutions fonctionnelles
- **Amélioration des workflows d'agents** : Les agents peuvent désormais retourner des résultats structurés et validés via un schéma lors de l'exécution de tâches, garantissant une meilleure intégration des données produites.

### Évolutions techniques
- **Gestion des modèles d'IA** :
    - Intégration de la famille de modèles Claude 5 dans le registre de modèles, avec une résolution automatique des alias vers les versions les plus récentes.
    - Amélioration de la gestion des versions pour ChatGPT-Codex, permettant une configuration spécifique par modèle.
    - Optimisation de la compatibilité avec les nouveaux modèles via le backend OpenAI.
- **API et Runtime** :
    - Extension du support des schémas JSON pour accepter des types définis sous forme de tableaux.
    - Optimisation de la gestion de la concurrence dans le registre de modèles via une stratégie de remplacement sécurisée ("copy-then-swap") pour éviter les mutations en place.
    - Correction d'un problème de logique exigeant un travail préalable avant de générer une sortie structurée [#1](https://github.com/SocialGouv/claw-code-go/issues/1).
- **Tests** :
    - Mise à jour des tests de l'API et des fixtures de référence pour s'aligner sur les dernières versions des modèles Claude (Opus et Sonnet).

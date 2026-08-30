## Changelog : iterion (30 derniers jours, au 29 août 2026)

### Résumé
Ce mois a été marqué par une montée en puissance de l'automatisation via l'introduction de nouveaux agents spécialisés (bots) et un renforcement massif de la fiabilité du système. Iterion améliore sa capacité à surveiller les vulnérabilités, à générer de la documentation et à tester ses propres fonctionnalités de manière autonome. L'expérience utilisateur est également enrichie par une interface de contrôle plus riche et une gestion plus fine des coûts et des ressources d'intelligence artificielle.

### Évolutions fonctionnelles
- **Nouveaux agents spécialisés (Bots) :**
    - Introduction de **Senti**, un agent de surveillance des vulnérabilités basé sur l'inventaire, fonctionnant sans LLM pour plus d'efficacité ([#515](https://github.com/SocialGouv/iterion/issues/515)).
    - Déploiement de **Prody**, un agent capable de générer de la documentation fonctionnelle à partir de catalogues de produits multi-dépôts ([#524](https://github.com/SocialGouv/iterion/issues/524)).
    - Ajout de **Endy**, un bot dédié à la couverture et à l'audit des tests de bout en bout (e2e) ([#fa20fe0](https://github.com/SocialGouv/iterion/commit/fa20fe0)).
- **Améliorations de l'interface Studio & CLI :**
    - Aperçu direct du contenu (JSON, Markdown, texte) sur les portes de validation humaines pour faciliter la prise de décision ([#425](https://github.com/SocialGouv/iterion/issues/425)).
    - Interface Studio plus ergonomique : tiroirs de cartes de pipeline redimensionnables et valeurs d'entrée/sortie extensibles ([#335](https://github.com/SocialGouv/iterion/issues/335)).
    - Affichage des changements de fichiers d'un nœud directement dans la console d'exécution ([#352](https://github.com/SocialGouv/iterion/issues/352)).
- **Gestion des modèles et des coûts :**
    - Exposition des tarifs des modèles et de la limite de sortie maximale via `ModelCapabilities` ([#575](https://github.com/SocialGouv/iterion/issues/575)).
    - Mise en place de mécanismes de repli (fallback) entre différents modèles via le langage DSL ([#365](https://github.com/SocialGouv/iterion/issues/365)).
    - Contrôle granulaire des budgets d'utilisation (usage-caps) avec une API d'administration en temps réel ([#9d4659c](https://github.com/SocialGouv/iterion/commit/9d4659c)).
- **Nouvelles capacités du moteur (Runtime & DSL) :**
    - Possibilité de "rembobiner" (rewind) une exécution à un nœud précédent pour corriger un chemin ([#348](https://github.com/SocialGouv/iterion/issues/348)).
    - Ajout de l'option `auto_memory` pour activer la gestion de la mémoire par nœud dans le DSL ([#450](https://github.com/SocialGouv/iterion/issues/450)).
    - Support du protocole MCP (Model Context Protocol) pour exposer Iterion localement et à distance ([#421](https://github.com/SocialGouv/iterion/issues/421)).

### Évolutions techniques
- **Observabilité et Monitoring :**
    - Intégration de **Sentry/GlitchTip** pour le suivi des erreurs et standardisation des formats de logs ([#459](https://github.com/SocialGouv/iterion/issues/459)).
    - Traçabilité améliorée en enregistrant précisément le modèle utilisé lors de chaque exécution ([#501](https://github.com/SocialGouv/iterion/issues/501)).
- **Sécurité et Isolation :**
    - Renforcement de l'isolation des bacs à sable (sandboxes) et amélioration de la gestion des certificats de confiance (JVM truststore) ([#4ad6768](https://github.com/SocialGouv/iterion/commit/4ad6768)).
    - Amélioration de la gestion des secrets et de l'identité des agents dans les environnements isolés.
- **Infrastructure et Résilience :**
    - Implémentation d'un mode "lame-duck" pour permettre un drainage gracieux des exécutions en cours lors des déploiements ([#3ec777f](https://github.com/SocialGouv/iterion/commit/3ec777f)).
    - Optimisation de la gestion des ressources LLM via un système de mutualisation des quotas d'abonnement ([#350](https://github.com/SocialGouv/iterion/issues/350)).
    - Fusion des exécutions ciblées sur les dépôts directement côté serveur pour plus de fiabilité ([#7787036](https://github.com/SocialGouv/iterion/commit/7787036)).
- **Qualité logicielle :**
    - Campagne massive de renforcement de la couverture de tests de bout en bout (e2e) via une approche matricielle pour garantir la stabilité des fonctionnalités critiques ([#fa20fe0](https://github.com/SocialGouv/iterion/commit/fa20fe0)).

### Autres changements
- Mise à jour exhaustive de la documentation pour aligner les guides utilisateurs sur les nouvelles architectures de bots et les processus de révision.
- Nettoyage de diverses parties du moteur de runtime et refactorisation pour améliorer la clarté du code.

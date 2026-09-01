## Changelog : iterion (30 derniers jours, au 31 août 2026)

### Résumé
Ce mois a été marqué par une montée en puissance de la fiabilité et de la sécurité de la plateforme. Les évolutions majeures concernent l'amélioration de la résilience des agents (capacité à basculer automatiquement d'un modèle d'IA à un autre en cas de besoin), un renforcement massif de la couverture de tests pour garantir la stabilité, et une gestion plus fine des budgets et des permissions. L'expérience utilisateur dans l'interface Studio a également été enrichie pour offrir une meilleure visibilité sur les changements et les coûts.

### Évolutions fonctionnelles
- **Intelligence Artificielle & Modèles** :
    - Introduction de mécanismes de repli (fallback) entre différents modèles d'IA pour assurer la continuité des tâches ([#365](https://github.com/SocialGouv/iterion/issues/365)).
    - Affichage des capacités des modèles, incluant les tarifs et les limites de sortie maximum ([#575](https://github.com/SocialGouv/iterion/issues/575)).
    - Extension de la phase de planification des bots pour inclure la détection de lacunes de fonctionnalités et la couverture de tests ([#578](https://github.com/SocialGouv/iterion/issues/578)).
    - Mise en place de "Senti", un sentinelle de vulnérabilités capable d'inventorier les risques sans recours systématique aux LLM ([#515](https://github.com/SocialGouv/iterion/issues/515)).
    - Introduction de "Themis", un juge basé sur des doctrines pour arbitrer les cas de divergence bloquants ([#371](https://github.com/SocialGouv/iterion/issues/371)).
- **Interface Studio & CLI** :
    - Amélioration de la visibilité lors des étapes de validation humaine avec la prévisualisation du JSON, du Markdown et du texte ([#425](https://github.com/SocialGouv/iterion/issues/425)).
    - Affichage des changements de fichiers effectués par un nœud directement dans la console d'exécution ([#352](https://github.com/SocialGouv/iterion/issues/352)).
    - Les portes de revue affichent désormais l'intégralité des changements depuis la revue précédente ([#351](https://github.com/SocialGouv/iterion/issues/351)).
- **Gestion des exécutions** :
    - Possibilité de "rembobiner" (rewind) une exécution à un nœud antérieur pour reprendre le travail ([#348](https://github.com/SocialGouv/iterion/issues/348)).
    - Ajout de l'option `auto_memory` pour permettre à un nœud de gérer son propre fichier de mémoire ([#450](https://github.com/SocialGouv/iterion/issues/450)).

### Évolutions techniques
- **Infrastructure & Résilience** :
    - Configuration de la réplication des flux JetStream pour garantir la haute disponibilité des données (data-HA) ([#592](https://github.com/SocialGouv/iterion/issues/592)).
    - Migration des configurations critiques (identifiants LLM, rôles de bots, overrides) vers une base de données pour permettre des mises à jour sans redéploiement ([#466](https://github.com/SocialGouv/iterion/issues/466), [#535](https://github.com/SocialGouv/iterion/issues/535)).
    - Renforcement de la gestion des budgets : les exécutions respectent désormais plus strictement les limites de consommation et gèrent mieux les dépassements ([#529](https://github.com/SocialGouv/iterion/issues/529), [#532](https://github.com/SocialGouv/iterion/issues/532)).
- **Sécurité & Sandbox** :
    - Durcissement des politiques de sécurité dans les environnements isolés (sandbox), notamment sur les règles réseau et la gestion des secrets ([#566](https://github.com/SocialGouv/iterion/issues/566), [#531](https://github.com/SocialGouv/iterion/issues/531)).
    - Correction de la propagation des politiques de permission à travers l'IPC ([#589](https://github.com/SocialGouv/iterion/issues/589)).
- **Observabilité** :
    - Intégration de Sentry/GlitchTip pour le suivi des erreurs et standardisation des logs au format JSON ([#459](https://github.com/SocialGouv/iterion/issues/459), [#458](https://github.com/SocialGouv/iterion/issues/458)).
    - Meilleure traçabilité en enregistrant précisément le modèle utilisé lors de chaque appel ([#501](https://github.com/SocialGouv/iterion/issues/501)).
- **Qualité & Tests** :
    - Campagne massive d'augmentation de la couverture de tests de bout en bout (e2e) via le bot "Endy" ([#506](https://github.com/SocialGouv/iterion/issues/506)).
    - Avancement des frameworks "Golden Master" et "Modernize" pour automatiser les tests adverses et la validation des standards ([#528](https://github.com/SocialGouv/iterion/issues/528), [#524](https://github.com/SocialGouv/iterion/issues/524)).

### Autres changements
- Mise à jour importante de la documentation technique (ADR, guides d'utilisation, bilans d'incidents et de campagnes) ([#591](https://github.com/SocialGouv/iterion/issues/591), [#582](https://github.com/SocialGouv/iterion/issues/582)).
- Automatisation de la génération du changelog pour plus de cohérence ([#579](https://github.com/SocialGouv/iterion/issues/579), [#584](https://github.com/SocialGouv/iterion/issues/584)).
- Nettoyage des répertoires temporaires du projet ([#469](https://github.com/SocialGouv/iterion/issues/469)).

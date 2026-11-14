## Changelog : agent-skills (30 derniers jours, au 03/11/2026)

### Résumé
Ce mois a été marqué par une restructuration profonde du projet pour améliorer l'organisation des compétences (skills) et simplifier leur déploiement. L'installation est désormais unifiée et simplifiée sur Windows, macOS et Linux, et de nouvelles capacités d'audit et de sécurité ont été intégrées pour renforcer l'accompagnement des agents de codage.

### Évolutions fonctionnelles
- **Nouvelles compétences (skills) :** Ajout de `/repo-perimetre` pour vérifier la cohérence des diffs par rapport à l'intention d'une PR [#12](https://github.com/IA-Generative/agent-skills/issues/12), ainsi que des modules `audit-rag` et `repo-impact` [#11](https://github.com/IA-Generative/agent-skills/issues/11).
- **Sécurité :** Introduction d'un hook `destructive-guard` pour protéger les actions critiques de l'agent [#11](https://github.com/IA-Generative/agent-skills/issues/11).
- **Compatibilité agents :** Extension du support pour Kimi Code CLI, Deep Code et d'autres modèles (DeepSeek, GLM) via un agent hôte [#13](https://github.com/IA-Generative/agent-skills/issues/13).
- **Ajustements de nommage :** Mise à jour des noms des plugins et de la marketplace pour assurer la compatibilité avec les standards des fournisseurs (notamment Anthropic).

### Évolutions techniques
- **Refonte de l'architecture :** Organisation des compétences par groupes et exposition via les plugins OpenCode/Claude [#14](https://github.com/IA-Generative/agent-skills/issues/14) [#19](https://github.com/IA-Generative/agent-skills/issues/19).
- **Installation simplifiée :** Mise en place d'un processus d'installation en une ligne via `gh api` ou scripts natifs (`install.ps1`, `install.sh`) compatible macOS, Windows et Linux [#16](https://github.com/IA-Generative/agent-skills/issues/16).
- **Optimisation CI/CD :** Automatisation de la génération et de la vérification des catalogues `index.json` en CI et amélioration de la compatibilité de la CI sur Windows.
- **Structure du projet :** Déplacement du `package.json` à la racine pour permettre l'installation du plugin OpenCode via URL git [#15](https://github.com/IA-Generative/agent-skills/issues/15).

### Autres changements
- Mise à jour de la documentation concernant le renommage des compétences, les procédures d'installation et l'utilisation de la marketplace.
- Nettoyage du code : suppression du hook `SessionStart` et des instructions de groupe obsolètes.

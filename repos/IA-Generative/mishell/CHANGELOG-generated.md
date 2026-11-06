## Changelog : mishell (30 derniers jours, au 04 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans sa stabilisation et son ergonomie. L'accent a été mis sur l'amélioration de l'expérience utilisateur grâce à une documentation entièrement repensée et une installation plus flexible, tout en renforçant la fiabilité technique via une couverture de tests étendue et une sécurisation accrue des composants de la marketplace.

### Évolutions fonctionnelles
- **Optimisation d'OpenCode** : Intégration par défaut de `mishell-base` et possibilité d'une installation "à la carte" pour plus de flexibilité.
- **Nouveau composant** : Introduction du plugin `mishell-agent-skills`.
- **Simplification de la configuration** : Réduction de la complexité du fichier `opencode.jsonc` grâce à l'utilisation de permissions génériques.

### Évolutions techniques
- **Sécurisation de la marketplace** : Les bundles sont désormais épinglés par SHA pour garantir l'intégrité des versions utilisées.
- **Renforcement de la qualité (Tests)** : Mise en place d'une suite de tests robuste pour valider la structure de la marketplace, l'installation isolée de Claude Code et le chargement correct des configurations OpenCode [#3](https://github.com/IA-Generative/mishell/pull/3).
- **Validation des compétences** : Ajout de tests garantissant que les compétences `mishell-base` sont correctement sollicitées lors des appels d'intention.

### Autres changements
- **Refonte de la documentation** : Restructuration complète du README (utilisation de tableaux, de listes et d'accordéons) et passage de la documentation technique et des commentaires en anglais.
- **Guides utilisateurs** : Ajout de sections dédiées à la mise à jour, à la désinstallation (Claude Code et OpenCode) et à la transition vers les nouveaux plugins remplaçant les anciens.
- **Documentation métier** : Configuration et documentation des compétences d'ingénierie (suivi des tickets, étiquetage et documentation de domaine).

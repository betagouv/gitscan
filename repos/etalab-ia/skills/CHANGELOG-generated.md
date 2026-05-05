## Changelog : skills (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, le projet skills a connu des améliorations significatives, notamment l'ajout de nouvelles "skills" RAG (Retrieval-Augmented Generation) issues du dépôt Dragster, une meilleure gestion des secrets grâce à l'intégration de Gitleaks, et des corrections pour assurer la conformité avec les standards de l'État français. La documentation a également été mise à jour pour refléter ces changements.

### Évolutions fonctionnelles
- Ajout de nouvelles "skills" RAG provenant du dépôt Dragster, enrichissant les capacités des assistants de code IA. [#12](https://github.com/etalab-ia/skills/pull/12)
- Ajout des règles de comportement de l'IA dans les templates, pour une utilisation plus responsable et alignée avec les principes de l'État. [#15](https://github.com/etalab-ia/skills/pull/15)
- Amélioration de la gestion des descriptions dans les fichiers YAML des skills RGAA, corrigeant des problèmes de formatage. [#9](https://github.com/etalab-ia/skills/pull/9)
- Simplification de la portée des templates pour une meilleure clarté et facilité d'utilisation.

### Évolutions techniques
- Refactorisation du code pour isoler les skills RAG dans le répertoire `skills/.experimental/`. [#16](https://github.com/etalab-ia/skills/pull/16)
- Intégration de `gitleaks` au pre-commit pour détecter et prévenir la présence de secrets sensibles dans le code. [#10](https://github.com/etalab-ia/skills/pull/10)
- Déplacement des skills sous le répertoire `skills/` et mise en conformité avec la spécification Agent Skills. [#7](https://github.com/etalab-ia/skills/pull/7)
- Correction d'un problème de branche obsolète dans le workflow de synchronisation avec Datagouv.
- Correction d'une erreur de nommage dans le workflow de synchronisation avec Datagouv.

### Autres changements
- Ajout d'un fichier README pour chaque skill, améliorant la documentation et la compréhension de chaque fonctionnalité. [#11](https://github.com/etalab-ia/skills/pull/11)
- Mise à jour du README principal avec les dernières fonctionnalités et suppression de la section "skill-creator" non implémentée. [#8](https://github.com/etalab-ia/skills/pull/8)
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Synchronisation des changements depuis le dépôt Datagouv. [#14](https://github.com/etalab-ia/skills/pull/14)

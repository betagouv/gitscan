## Changelog : skills (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, le projet skills a connu une évolution significative avec l'ajout de nouvelles "skills" pour les assistants de code IA, notamment celles issues de Dragster. Des améliorations ont été apportées à la documentation, à la conformité du code et à la sécurité, avec l'intégration d'outils de détection de secrets. L'accent a également été mis sur l'amélioration de l'expérience développeur grâce à des templates plus complets et des corrections de configuration.

### Évolutions fonctionnelles
- Ajout de nouvelles skills RAG (Retrieval-Augmented Generation) issues du dépôt Dragster [#12](https://github.com/etalab-ia/skills/pull/12).
- La skill `datagouv` a été ajoutée, permettant de synchroniser les données avec data.gouv.fr [#34841b7](https://github.com/etalab-ia/skills/commit/34841b7).
- La skill `lasuite-ui-kit` a été ajoutée pour le développement avec LaSuite React [#65b8dc2](https://github.com/etalab-ia/skills/commit/65b8dc2).
- La skill `rgaa` permet désormais d'exporter le rapport d'audit au format Markdown [#b53dc4a](https://github.com/etalab-ia/skills/commit/b53dc4a).
- La skill `react-dsfr` a été améliorée avec la prise en charge du mode sombre, des composants Display et l'intégration d'ESLint [#162de7c](https://github.com/etalab-ia/skills/commit/162de7c).

### Évolutions techniques
- Refactorisation de la structure du projet pour déplacer les skills sous le répertoire `skills/` et assurer la conformité avec la spécification Agent Skills [#ad047dd](https://github.com/etalab-ia/skills/commit/ad047dd).
- Ajout de `gitleaks` au pre-commit pour la détection de secrets dans le code [#0d7f292](https://github.com/etalab-ia/skills/commit/0d7f292).
- Mise à jour de l'action `actions/checkout` en v5 pour supporter Node.js 24 [#27eb93f](https://github.com/etalab-ia/skills/commit/27eb93f).
- Correction des imports Next.js App Router et du chargement des icônes pour la skill `react-dsfr` [#274acdb](https://github.com/etalab-ia/skills/commit/274acdb).
- La skill `rgaa` a été transformée en un outil d'audit de conformité a posteriori [#98cb5c7](https://github.com/etalab-ia/skills/commit/98cb5c7).
- Correction d'un problème de copie des assets DSFR pour la configuration Vite [#9ed61d5](https://github.com/etalab-ia/skills/commit/9ed61d5).

### Autres changements
- Ajout de README pour chaque skill [#7fe599f](https://github.com/etalab-ia/skills/pull/11).
- Mise à jour de la documentation README avec les dernières fonctionnalités et suppression de la section "skill-creator" non implémentée [#5845655](https://github.com/etalab-ia/skills/pull/7).
- Ajout de sections "Expected Behavior" et guides de personnalisation aux templates [#676d442](https://github.com/etalab-ia/skills/commit/676d442).
- Amélioration du template beta.gouv avec l'ajout de "Definition of Done", CI et documentation de l'architecture [#bac59af](https://github.com/etalab-ia/skills/commit/bac59af).
- Ajout de pre-commit Husky et contrainte sur les dépendances au template [#bac59af](https://github.com/etalab-ia/skills/commit/bac59af).
- Traduction des instructions en anglais et ajout des sections Tests/Skills aux templates [#2887eab](https://github.com/etalab-ia/skills/commit/2887eab).
- Correction du nom de `datagouv-apis` en `datagouv` [#63efcff](https://github.com/etalab-ia/skills/commit/63efcff).
- Correction de la description de la skill rgaa dans le README [#d2e67cb](https://github.com/etalab-ia/skills/commit/d2e67cb).
- Correction d'un copyright erroné [#96dc4f8](https://github.com/etalab-ia/skills/commit/96dc4f8).

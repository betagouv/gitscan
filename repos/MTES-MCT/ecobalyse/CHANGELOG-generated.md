## Changelog : ecobalyse (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois-ci, ecobalyse a connu une expansion significative de sa base de données avec l'ajout de nouveaux objets (moteurs électriques, batteries, ingrédients Koch) et une amélioration de la gestion des données de consommation. L'interface utilisateur a été enrichie par un nouvel éditeur pour les éléments de production et une meilleure visibilité des masses unitaires. Parallèlement, la stabilité technique a été renforcée via des optimisations de l'API et une mise à jour de l'infrastructure de déploiement.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités et améliorations de l'interface**
  - Introduction d'un nouvel éditeur modal pour les éléments des articles de production ([#2849](https://github.com/MTES-MCT/ecobalyse/issues/2849))
  - Affichage de la masse unitaire pour les articles de production ([#2766](https://github.com/MTES-MCT/ecobalyse/issues/2766))
  - Chargement d'exemples par défaut pour le simulateur ([#2782](https://github.com/MTES-MCT/ecobalyse/issues/2782))
  - Rendu des partages d'éléments de ligne de composants ([#2772](https://github.com/MTES-MCT/ecobalyse/issues/2772))
  - Amélioration du rapport de hiérarchie des ingrédients ([#2787](https://github.com/MTES-MCT/ecobalyse/issues/2787))
  - Ajout de la définition des consommations par catégories ([#2798](https://github.com/MTES-MCT/ecobalyse/issues/2798))
- **Enrichissement des données**
  - Ajout de nouveaux objets : moteurs électriques ([#2846](https://github.com/MTES-MCT/ecobalyse/issues/2846)), batteries alcalines ([#2828](https://github.com/MTES-MCT/ecobalyse/issues/2828)), ingrédients Koch ([#2836](https://github.com/MTES-MCT/ecobalyse/issues/2836)) et assemblages de laits végétaux ([#2800](https://github.com/MTES-MCT/ecobalyse/issues/2800))
- **Corrections de bugs**
  - Correction de la gestion des noms d'articles personnalisés dans l'interface ([#2855](https://github.com/MTES-MCT/ecobalyse/issues/2855))
  - Correction du réinitialisation systématique des processus ([#2785](https://github.com/MTES-MCT/ecobalyse/issues/2785))
  - Correction de l'exposition des détails d'étapes désactivées dans l'API textile ([#2812](https://github.com/MTES-MCT/ecobalyse/issues/2812))

### Évolutions techniques
- **API et Backend**
  - Introduction d'une nouvelle API ([#2792](https://github.com/MTES-MCT/ecobalyse/issues/2792))
  - Optimisation des performances via l'utilisation de traitements par lots (batch) pour les insertions en base de données ([#2790](https://github.com/MTES-MCT/ecobalyse/issues/2790))
  - Ajout d'un script de comparaison Volca ([#2783](https://github.com/MTES-MCT/ecobalyse/issues/2783))
  - Mise en place d'un flag "betauser" pour le déploiement de fonctionnalités ([#2832](https://github.com/MTES-MCT/ecobalyse/issues/2832))
- **Infrastructure et Sécurité**
  - Mise en conformité et compatibilité avec les versions Scalingo 22 et 26 ([#2801](https://github.com/MTES-MCT/ecobalyse/issues/2801), [#2776](https://github.com/MTES-MCT/ecobalyse/issues/2776))
  - Mise à jour de sécurité de Maildev vers la v3.x ([#2771](https://github.com/MTES-MCT/ecobalyse/issues/2771))
  - Mise à jour de l'outil de gestion de versions `uv` ([#2794](https://github.com/MTES-MCT/ecobalyse/issues/2794))
- **Refactoring**
  - Refactorisation du formatage JSON ([#2754](https://github.com/MTES-MCT/ecobalyse/issues/2754))

### Autres changements
- **Documentation**
  - Documentation sur les compléments ([#2833](https://github.com/MTES-MCT/ecobalyse/issues/2833))
  - Guide pour l'ajout d'un nouveau scope ([#2839](https://github.com/MTES-MCT/ecobalyse/issues/2839))
- **Maintenance des données et configuration**
  - Mise à jour des types de matériaux et des processus de recyclage pour les batteries ([#2825](https://github.com/MTES-MCT/ecobalyse/issues/2825))
  - Automatisation de l'inférence des types de matériaux via la taxonomie ([#2779](https://github.com/MTES-MCT/ecobalyse/issues/2779))
  - Nettoyage des fichiers de métadonnées obsolètes ([#2831](https://github.com/MTES-MCT/ecobalyse/issues/2831))
  - Ajustements de données : masse par unité pour l'eau ([#2799](https://github.com/MTES-MCT/ecobalyse/issues/2799)) et gestion des anomalies de hiérarchie ([#2652](https://github.com/MTES-MCT/ecobalyse/issues/2652))
  - Mise à jour du snippet d'analyse Plausible ([#2819](https://github.com/MTES-MCT/ecobalyse/issues/2819))

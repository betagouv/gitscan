## Changelog : ultra11y (30 derniers jours, au 13 septembre 2026)

### Résumé
Ce mois-ci, ultra11y a franchi une étape majeure dans l'automatisation des audits d'accessibilité, particulièrement pour le référentiel RGAA. Les évolutions se concentrent sur une précision accrue des jugements de l'IA, une richesse de reporting nettement améliorée (détails par page et par critère) et une optimisation des coûts et de la performance lors des exécutions en continu (CI). L'outil passe d'un simple mode de détection à une capacité de proposition de réparations.

### Évolutions fonctionnelles
- **Amélioration du reporting et de l'annotation** :
    - Introduction de rapports compacts et de résumés par page, optimisés pour les commentaires de Pull Request.
    - Regroupement des non-conformités par critère pour une lecture plus claire.
    - Publication du taux de conformité officiel du référentiel dans les rapports de conformité.
- **Renforcement de l'audit RGAA** :
    - Extension de la couverture automatique pour les critères du RGAA.
    - Meilleure gestion des critères "non applicables" ou indécidables.
- **Capacités de correction** :
    - Introduction d'une phase de vérification capable de proposer des réparations de code au lieu de simplement signaler des refus.
- **Précision des sondes (probes)** :
    - Amélioration de la détection des indicateurs de focus (notamment dans les pseudo-éléments).
    - Fiabilisation de la détection des pièges au clavier en utilisant de véritables cycles de tabulation.

### Évolutions techniques
- **Optimisation de l'IA et des coûts** :
    - Réduction significative des coûts d'adjudication par l'IA via une meilleure gestion des lots (batches) et des budgets de jetons (tokens).
    - Refactorisation de l'adjudication pour la rendre agnostique au transport et unifier les règles de verdict.
- **Fiabilité et performance de la CI** :
    - Introduction d'un "browser tier" dédié pour les exécutions dans GitHub Actions, garantissant un environnement de navigation complet.
    - Optimisation du crawling : meilleure gestion des erreurs 404, des URLs canoniques et des doublons d'adresses.
    - Mise en place d'un système de "replay" du ledger pour rendre les audits exhaustifs plus rapides et reproductibles.
- **Robustesse du moteur** :
    - Amélioration de la gestion des timeouts et de la concurrence lors des exécutions de tests.

### Autres changements
- Mise à jour régulière des sources de référence (WCAG et RGAA) intégrées au moteur.
- Amélioration de la documentation technique (README, guides de configuration CI et documentation des compétences IA).

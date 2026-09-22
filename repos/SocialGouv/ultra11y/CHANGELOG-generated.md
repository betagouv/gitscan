## Changelog : ultra11y (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, ultra11y a franchi une étape importante dans la qualité de ses rapports et la précision de ses audits. L'outil propose désormais des formats de comptes rendus adaptés aux différents profils (métier vs technique) et améliore significativement la couverture des critères RGAA. Les capacités d'analyse par intelligence artificielle ont également été affinées pour offrir un raisonnement plus robuste et une meilleure gestion des coûts.

### Évolutions fonctionnelles
- **Nouveaux formats de rapports** : Introduction d'un compte rendu synthétique destiné aux profils métier, avec les détails techniques placés en annexe [#38](https://github.com/SocialGouv/ultra11y/pull/38).
- **Amélioration de la couverture RGAA** : Extension de la couverture automatique des critères et rendu de l'audit plus exhaustif.
- **Précision des audits** : Correction de plusieurs faux positifs et négatifs, notamment sur la détection des indicateurs de focus, des pièges au clavier et des éléments animés.
- **Meilleure visibilité des résultats** : Les non-conformités sont désormais regroupées par critère dans les sorties CI, et de nouveaux résultats compacts par page sont disponibles.
- **Gestion des référentiels** : Possibilité de sélectionner un standard spécifique (WCAG ou RGAA) de manière globale pour l'ensemble des commandes.

### Évolutions techniques
- **Optimisation de l'IA** : Amélioration du raisonnement des agents IA (tier "agent") et intégration de la capacité de décision critère par critère via l'interface Claude Code.
- **Optimisation des coûts et performances** : Réduction des coûts d'adjudication par critère et optimisation du traitement des lots pour l'IA.
- **Amélioration de la CI/CD** : Simplification des vérifications automatiques et ajout d'options pour un reporting granulaire par critère dans GitHub Actions.
- **Refactoring de l'architecture** : Rendre le moteur d'adjudication agnostique vis-à-vis du transport utilisé pour les appels LLM.
- **Correction du processus de release** : Correction du flux de publication pour s'assurer que les releases proviennent du dépôt principal et non d'un fork [#39](https://github.com/SocialGouv/ultra11y/pull/39).

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les limites de la couverture déterministe du RGAA et le fonctionnement des nouveaux rapports.
- **Maintenance des standards** : Mises à jour régulières des sources de référence WCAG et RGAA intégrées au projet.

## Changelog : ultra11y (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois-ci, ultra11y a franchi une étape importante dans la communication des résultats d'audit. L'outil propose désormais des rapports différenciés, permettant aux décideurs de consulter une synthèse métier tandis que les experts disposent d'annexes techniques détaillées. Parallèlement, la précision des audits a été renforcée par une meilleure détection des indicateurs de focus et une réduction des faux positifs, tout en stabilisant les processus de publication et de gestion des coûts d'IA.

### Évolutions fonctionnelles
- **Nouveaux formats de rapports** : Introduction d'un compte rendu structuré comprenant une synthèse pour les profils métier et une annexe technique détaillée [#38](https://github.com/SocialGouv/ultra11y/pull/38).
- **Flexibilité des analyses** : Distinction entre les rapports détaillés (via Claude) et les rapports compacts optimisés pour les environnements CI.
- **Amélioration de la précision des audits** :
    - Meilleure détection du focus clavier (gestion des animations et des pseudo-éléments).
    - Correction de faux positifs de conformité dans les rapports et les sondes.
    - Utilisation du taux de conformité officiel du référentiel dans les rapports.
    - Correction de la règle RGAA 10.1.
- **Nouveautés GitHub Actions** : Publication de résultats de statut compacts par page pour un suivi rapide.

### Évolutions techniques
- **Optimisation de la CI/CD** :
    - Simplification des vérifications automatiques.
    - Meilleure gestion du budget d'adjudication par IA (limitation des coûts par lot et par clé).
    - Réduction de la taille des artefacts pour les rapports compacts.
- **Stabilité et Release** :
    - Correction du processus de publication pour utiliser le dépôt principal au lieu d'un fork [#39](https://github.com/SocialGouv/ultra11y/pull/39).
    - Verrouillage (re-pin) des moteurs d'audit intégrés pour garantir la reproductibilité des tests.
- **Amélioration du moteur** :
    - Renforcement de la complétude de l'adjudication et optimisation du passage à l'échelle.
    - Optimisation du processus de build (gestion des chunks `dist/`).

### Autres changements
- Mise à jour régulière des sources de référence pour les normes WCAG et RGAA.

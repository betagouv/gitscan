## Changelog : mon-entreprise (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois-ci, le projet franchit une étape majeure avec l'introduction d'un outil de comparaison de modèles permettant d'évaluer différentes structures juridiques. Parallèlement, une mise à jour profonde des règles de calcul a été déployée pour intégrer les spécificités de Mayotte (Lodeom et statut salarié). Enfin, la qualité du développement est renforcée par l'intégration d'une revue de code automatisée par IA.

### Évolutions fonctionnelles
- **Nouveau comparateur de modèles** : 
    - Possibilité de comparer plusieurs modèles (ex: SASU, EI) sur des critères de revenus et de charges.
    - Ajout de la gestion des périodes de calcul (mensuel ou annuel) et des objectifs d'imposition (IR/IS).
    - Amélioration de l'expérience utilisateur avec des info-bulles explicatives et des cartes de statut.
- **Mise à jour pour Mayotte** :
    - Intégration complète des spécificités locales pour les simulateurs "Salarié" et "Lodeom" (application du PSS mahorais, règles de cotisations chômage, maladie et allocations familiales).
    - Correction des règles d'exonération et des taux de cotisations spécifiques à la zone.
- **Améliorations des simulateurs** :
    - Correction du calcul des dividendes pour le modèle TI.
    - Ajustement des unités d'exonération pour le modèle SASU.
    - Optimisation de l'affichage des questions et des boutons de navigation.

### Évolutions techniques
- **CI/CD & Qualité** :
    - Mise en place d'une revue de code automatique par IA sur les Pull Requests pour accélérer les retours et améliorer la cohérence du code.
- **Refactoring & Architecture** :
    - Refonte majeure du module de gestion des montants (`Montant`) pour une meilleure robustesse et lisibilité des opérations mathématiques.
    - Optimisation de la logique de simulation Lodeom et simplification des composants de calcul.
- **Accessibilité (a11y) & UI** :
    - Correction de plusieurs problèmes d'accessibilité (labels ARIA, IDs non uniques) pour une meilleure compatibilité avec les lecteurs d'écran.
    - Correction de bugs d'affichage et d'espacement dans les formulaires de saisie.

### Autres changements
- **Documentation** :
    - Mise à jour complète de la documentation de l'API et des guides d'intégration (notamment pour l'usage en Iframe).
    - Ajout de nouveaux documents d'architecture (ADR) concernant la conception du comparateur de modèles.
    - Clarification des étapes pour reproduire un calcul spécifique.

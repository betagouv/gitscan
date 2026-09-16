## Changelog : mon-entreprise (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois-ci, mon-entreprise franchit une étape majeure avec l'introduction d'un comparateur de modèles permettant de mettre en balance différents statuts juridiques. Le projet intègre également les spécificités sociales de Mayotte et bénéficie d'une automatisation accrue de la qualité de code grâce à l'intégration de l'intelligence artificielle et de nouveaux environnements de test automatiques.

### Évolutions fonctionnelles
- **Nouveau comparateur de modèles** : Permet de comparer différents statuts (ex: SASU vs EI) avec gestion des périodes de calcul (mensuel/annuel), des objectifs fiscaux (IR/IS, versement libératoire) et des résultats déficitaires.
- **Mise à jour Mayotte** : Intégration complète des spécificités sociales pour les salariés à Mayotte (Plafond de Sécurité Sociale, CSG-CRDS, allocations familiales, cotisations chômage, etc.).
- **Améliorations des simulateurs** :
    - **Lodeom** : Correction de plusieurs questions de formulaire, de l'affichage des récapitulatifs et de la régularisation annuelle.
    - **Travailleur Indépendant (TI)** : Amélioration du calcul basé sur les dividendes sans rémunération brute.
    - **SASU** : Correction de l'unité des exonérations de cotisations sur la fiche de paie.
- **Expérience utilisateur** : Ajout d'info-bulles sur les champs de chiffre d'affaires et de charges dans le comparateur.

### Évolutions techniques
- **Automatisation de la qualité (CI/CD)** :
    - Mise en place d'une revue de code automatique par IA (Claude) sur les Pull Requests.
    - Déploiement automatique d'environnements de test temporaires (review apps) via Clever Cloud pour chaque Pull Request.
- **Refactoring et architecture** :
    - Refonte majeure de la logique de gestion des montants (récurrents et ponctuels) pour améliorer la précision et la robustesse des calculs.
    - Optimisation des performances via le chargement à la demande (lazy loading) de certains composants.
    - Nettoyage du code (suppression de composants, de hooks et de règles métier inutilisés).
- **Accessibilité** : Amélioration du nommage des champs de date pour une meilleure compatibilité avec les lecteurs d'écran.

### Autres changements
- **Documentation** : Mise à jour complète de la documentation de l'API (liens d'intégration, exemples de reproduction de calcul, traductions et URLs des modèles).

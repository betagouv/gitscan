## Changelog : mon-entreprise (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci est marqué par une évolution majeure : l'introduction d'un comparateur de modèles permettant d'opposer différentes situations de gestion. Le projet intègre également les spécificités sociales et fiscales de Mayotte et renforce ses processus de développement grâce à l'automatisation des tests et des déploiements de révision.

### Évolutions fonctionnelles
- **Nouveau comparateur de modèles** : 
    - Mise en place d'un outil permettant de comparer plusieurs simulations.
    - Ajout de questions spécifiques, de cartes de statut et d'info-bulles pour faciliter la saisie du CA et des charges.
    - Gestion des résultats déficitaires et des objectifs fiscaux (IR/IS, versement libératoire).
    - Possibilité de définir une période de calcul (mensuelle ou annuelle).
- **Prise en compte de Mayotte** : Mise à jour complète des règles pour les salariés et employeurs mahorais (plafond de sécurité sociale, cotisations chômage, CSG-CRDS, allocations familiales, etc.).
- **Corrections de simulateurs** :
    - **Lodeom** : Résolution de problèmes liés aux questions "fantômes", correction de l'affichage des tooltips et de la régularisation annuelle.
    - **TI (Travailleur Indépendant)** : Amélioration du calcul basé sur les dividendes et correction des liens entre le CA/charges et la rémunération brute.
    - **SASU** : Correction des unités d'exonération de cotisations sur les fiches de paie.
- **Accessibilité** : Amélioration du nommage des champs de date pour une meilleure compatibilité avec les lecteurs d'écran.

### Évolutions techniques
- **CI/CD et DevOps** :
    - Mise en place de "Review Apps" sur Clever Cloud : chaque Pull Request génère désormais un environnement de test déployé automatiquement.
    - Introduction d'une revue automatique par IA pour les Pull Requests.
- **Performance** : Optimisation du chargement de l'interface via le chargement à la demande (*lazy loading*) de certains composants.
- **Refactoring** : 
    - Refonte de la gestion des montants (distinction entre montants récurrents et ponctuels) pour plus de robustesse.
    - Nettoyage et restructuration du code du comparateur.

### Autres changements
- **Documentation** : Mise à jour importante de la documentation de l'API, des liens d'intégration (Iframe) et des guides de reproduction de calcul pour les développeurs.
- **Nettoyage** : Suppression de l'assistant transitoire pour le complément CMG et de certaines règles de calcul obsolètes.

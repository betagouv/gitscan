## Changelog : mon-entreprise (30 derniers jours, au 29 septembre 2026)

### Résumé
Ce mois a été marqué par des évolutions majeures, notamment le lancement d'un outil permettant de comparer différents statuts juridiques, une refonte visuelle de la page d'accueil et l'intégration complète des spécificités de cotisations sociales pour Mayotte. Le projet améliore également sa qualité de développement grâce à l'introduction d'une revue de code automatisée par intelligence artificielle.

### Évolutions fonctionnelles
- **Nouveau comparateur de modèles** : Ajout d'une fonctionnalité permettant de comparer plusieurs statuts (ex: SASU vs EI) pour aider au choix du statut juridique, incluant la gestion des périodes de calcul et des objectifs fiscaux.
- **Prise en compte de Mayotte** : Mise à jour complète des simulateurs (Salarié et Lodeom) pour intégrer les règles spécifiques à Mayotte (cotisations chômage, maladie, plafonds de sécurité sociale, etc.).
- **Refonte de la page d'accueil** : Nouvelle structure de la page d'accueil avec l'ajout de sections "Qui sommes-nous", "Explorer les statuts" et un module de recherche/création.
- **Nouveaux simulateurs** : Intégration des simulateurs dédiés aux profils Artisan et Commerçant.
- **Améliorations du simulateur Lodeom** : Corrections de calculs, optimisation du parcours de questions et amélioration de l'affichage des répartitions.
- **Documentation utilisateur** : Mise à jour des guides d'intégration (Iframe) et de la documentation de l'API pour les développeurs.

### Évolutions techniques
- **Revue de code par IA** : Intégration d'un agent de revue automatique (Claude) dans le workflow de CI/CD pour analyser les Pull Requests.
- **Refonte de la gestion des montants** : Refactorisation majeure de la logique métier liée aux montants (`Montant`) pour améliorer la précision et la lisibilité des calculs.
- **Optimisation de la CI/CD** : Amélioration de la gestion des environnements de prévisualisation (*review apps*) et de leur cycle de vie.
- **Migration et stabilité Next.js** : Diverses optimisations liées à l'utilisation de Next.js, incluant la correction de problèmes de rendu côté serveur (SSR) et de gestion des dépendances avec Turbopack.

### Autres changements
- **Documentation technique** : Rédaction de plusieurs documents d'architecture (ADR) concernant le fonctionnement du comparateur de modèles.
- **Nettoyage du code** : Suppression de composants obsolètes et de règles de calcul non utilisées.

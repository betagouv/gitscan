## Changelog : mon-service-securise (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du moteur de risque, l'ajout de nouvelles fonctionnalités liées aux thématiques et porteurs de mesures, ainsi que des corrections et optimisations techniques, notamment concernant la gestion des JWT et la migration vers TypeScript. L'interface utilisateur a également été améliorée avec l'ajout d'informations contextuelles et des corrections de présentation.

### Évolutions fonctionnelles
- Ajout de la thématique des mesures, visible dans le tiroir, le filtre de la liste de mesures et le tableau des mesures. (#8134712, #a77cf33, #2df6eda, #b794add, #c4b6511)
- Ajout de la possibilité d'afficher les porteurs singuliers des mesures dans le tiroir et dans l'export CSV. (#67abfac, #d20987f, #a7c818f)
- Amélioration de l'affichage des informations de service dans les PDF d'annexes (criticité, exposition, caractéristiques). (#496b6a3, #b87ac30, #9bd5c7e, #28323e4, #0daf728, #df48328, #eeec0e3)
- Ajout de la transcription dans le tampon d'homologation. (#fc0c2f4, #bbffba8, #06d70fa)
- Amélioration de la gestion des erreurs et des messages d'alerte. (#e727082, #eab3ad2)
- Correction de l'affichage du bouton "Effacer les filtres". (#f2a1083)

### Évolutions techniques
- Migration progressive du code vers TypeScript pour une meilleure maintenabilité et robustesse. (#cea0c50, #e1098bc, #f25ec61, #b8e662c, #a4750ba, #d3811bb, #49dc473, #17adfd0, #0495d1c, #79b4c2b, #5a16ee4, #bd82aef, #b59c9e5, #9480a6e, #55b18f6)
- Refonte de la gestion des JWT : révision de la logique de révocation, stockage des jetons révoqués, synchronisation front/back, et amélioration de la sécurité. (#bef7270, #cc49fee, #8e060e2, #76104a0, #252e517, #1393cf4, #779c665, #28fd81a, #42d6ce8)
- Amélioration du moteur de risque : intégration des vecteurs, objectifs visés, vraisemblance des risques, et utilisation des données de référence. (#ddf1107, #4443f34, #d0476d3, #67f7c39, #3f01251, #817ea68, #1be467e, #03115cf, #f3faaed, #c03cc81, #6698304)
- Mise à jour des dépendances : express (vers la version 5), knex, knex-pglite, axios, jsonwebtoken, express-rate-limit. (#67e1591, #f58eda5, #f2c0092, #cd11bde, #189eec6, #9a5a137)
- Optimisation de la gestion des erreurs et des requêtes. (#7e82beb, #60817b0)

### Autres changements
- Ajout de tests et d'améliorations de la qualité du code (ESLint, Jest, Vitest).
- Amélioration de la documentation et des commentaires.
- Corrections de coquilles et d'incohérences. (#9e5e06b)
- Suppression de code inutile et nettoyage du codebase.
- Mise à jour du référentiel des mesures V2. (#a79dcda)
- Suppression de l'invalidation de cache chez Baleen. (#0f8d7f7)
- Modification du wording concernant les parties responsables des mesures. (#31f1bc1)

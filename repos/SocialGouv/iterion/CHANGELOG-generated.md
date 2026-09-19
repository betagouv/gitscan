## Changelog : iterion (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois a été marqué par une transition majeure vers le profil **DSL v2**, impactant la manière dont les workflows et les bots sont définis et exécutés. Le catalogue de bots a été considérablement enrichi, et l'expérience utilisateur a été affinée avec une refonte de l'interface Studio et une meilleure visibilité sur les coûts et les capacités des agents IA.

### Évolutions fonctionnelles
- **Migration du catalogue de bots :** Déploiement progressif de plusieurs vagues de bundles de bots utilisant le nouveau profil DSL v2 (incluant `app-dev`, `copilot`, `secured-renovacy`, etc.) [#1344, #1369, #1361].
- **Refonte de l'interface Studio :** Nouvelle structure de navigation avec le Studio déplacé sous `/studio` et une page d'accueil dédiée au produit [#1433].
- **Nouvelles capacités d'agents :** Publication de la boucle de revue adversaire en tant que compétence (*skill*) utilisable par les agents [#1372].
- **Amélioration de la revue de PR :** Interface dédiée pour le reviewer Claude [#1388] et lecture automatique des issues liées aux Pull Requests [#1017].
- **Gestion des secrets et identités :** Possibilité pour une équipe de nommer les workloads financés via ses propres clés LLM [#1370] et support des tokens Claude pour l'authentification [#948].
- **Identité visuelle :** Mise à jour de la marque avec l'intégration de la mascotte Iterion sur les avatars, favicons et logos [#794].

### Évolutions techniques
- **Évolution du DSL (v2) :** Migration profonde du langage de description incluant la validation en mode "dry-run", de nouveaux mécanismes de binding et une gestion améliorée des erreurs de syntaxe [#1292, #1276, #1336].
- **Optimisation du Runtime & Sandbox :** 
    - Renforcement de l'isolation des bundles de subbots [#1195].
    - Amélioration de la fiabilité des mécanismes de "checkpoint" et de "banking" des commits lors des exécutions [#988, #556].
    - Gestion plus robuste de l'annulation des processus de groupe [#935].
- **Sécurité et Audit :** Amélioration du scanner de sécurité (*deep scan*) avec un meilleur reporting de couverture et une gestion optimisée des timeouts [#1347, #1321, #1104].
- **Observabilité et Coûts :** 
    - Mise en place d'un suivi précis des coûts (tokens, budgets) par exécution et par identité [#1069, #1105].
    - Introduction de l'option de tracing Sentry pour les transactions API et les appels LLM [#463].
- **Infrastructure :** Optimisation des déploiements Kubernetes (gestion des `resource requests` et du `node spread` pour les pods) [#694, #802].

### Autres changements
- **Documentation :** Mise à jour importante des guides sur le nouveau DSL, les processus d'audit et les politiques de comparaison de produits [#1342, #1231, #1142].
- **CI/CD :** Accélération des pipelines de test grâce à la parallélisation des suites de tests E2E [#880].
- **Nettoyage :** Refactorisation de la logique interne des bots de revue pour une meilleure maintenance [#1241].

## Changelog : oidc2fer (30 derniers jours, au 13 avril 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent sur l'ajout de nouvelles entités SIRET pour une meilleure compatibilité avec les établissements d'enseignement, ainsi que sur des corrections mineures de configuration et de syntaxe pour améliorer la stabilité et la qualité du code.

### Évolutions fonctionnelles
- Ajout de l'entité FUN MOOC au mapping SIRET, permettant une intégration avec ce service. [#8d4d5a4](https://github.com/proconnect-gouv/oidc2fer/commit/8d4d5a4)
- Correction de l'EntityID pour l'établissement ens2m, améliorant ainsi l'identification et l'authentification. [#aef51f3](https://github.com/proconnect-gouv/oidc2fer/commit/aef51f3)
- Ajout de nouvelles entités au mapping SIRET, étendant la compatibilité avec davantage d'établissements. [#0afd27e](https://github.com/proconnect-gouv/oidc2fer/commit/0afd27e)

### Évolutions techniques
- Correction de la syntaxe `cp` dans les fichiers de configuration CI/CD pour assurer un fonctionnement correct des tests. [#8ad2d45](https://github.com/proconnect-gouv/oidc2fer/commit/8ad2d45)
- Utilisation des secrets de staging pour le linting de l'environnement de production, améliorant la sécurité et la cohérence. [#c1efc43](https://github.com/proconnect-gouv/oidc2fer/commit/c1efc43)
- Correction de la syntaxe `cp` dans le linter. [#db18300](https://github.com/proconnect-gouv/oidc2fer/commit/db18300)

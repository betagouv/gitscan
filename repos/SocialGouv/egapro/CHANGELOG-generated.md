## Changelog : egapro (30 derniers jours)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout de nouvelles fonctionnalités comme la gestion des entreprises et du profil utilisateur, ainsi que sur l'amélioration de la robustesse de l'application avec des corrections de bugs et des améliorations de l'infrastructure CI/CD. L'authentification et la gestion des sessions ont également été optimisées.

### Évolutions fonctionnelles
- Ajout de la page "Mes entreprises" (#2850)
- Ajout de la page "Mes déclarations" (#2852)
- Ajout de la page "Mon profil" (#2839)
- Ajout d'un menu dans l'espace personnel ("Mon espace") (#2833)
- Ajout d'une page de connexion (#2823)
- Implémentation de la déclaration (#2825)
- Ajout des pages d'erreurs 404 et 500 (#2832)
- Amélioration de la page d'accueil avec les retours du designer (#2831)

### Évolutions techniques
- Amélioration du workflow CI/CD pour la génération de rapports avec CLAUDE
- Ajout de tests E2E pour la page de connexion (#2849)
- Amélioration du workflow CI/CD avec l'ajout de tests d'accessibilité (a11y)
- Ajout de workflows GitHub Actions pour l'analyse de code avec Claude
- Optimisation du temps de build Docker via le caching (#2795)
- Ajout de la configuration Vitest pour les tests avec DSFR (#2794)
- Mise en place de la nouvelle version de l'application (#2797)
- Correction de problèmes liés à l'environnement de développement ProConnect (#2770)
- Correction de problèmes liés à la configuration de l'URL NEXTAUTH (#2796)
- Correction de problèmes de migration Drizzle (#2819)
- Ajout de linting et de formatage du code dans le CI/CD (#2803)

### Autres changements
- Mise à jour de la documentation (README) (#2830)
- Utilisation de l'anglais comme langue principale pour les noms des composants et les commentaires (#2820)
- Nettoyage de fichiers de configuration (#2782)
- Ajout du job `review-auto` à chaque nouvelle branche dans le CI/CD (#2789)
- Correction de problèmes de cache et de paramètres invalides (#2776)
- Correction d'un problème de non-diffusibilité en production (#2774)
- Publication de la version 3.15.2 (#2774)

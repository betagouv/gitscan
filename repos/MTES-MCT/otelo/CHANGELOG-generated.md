## Changelog : otelo (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, l'accent a été mis sur l'amélioration de l'accompagnement utilisateur grâce à l'introduction d'un nouvel assistant de simulation (wizard) et d'un système de tutoriel interactif. La sécurité de la plateforme a été considérablement renforcée (authentification à deux facteurs, protection contre les abus) et de nouveaux outils d'analyse, comme la pyramide des âges et la fonctionnalité Docurba, ont été intégrés.

### Évolutions fonctionnelles
- **Accompagnement et tutoriels** : Mise en place d'un assistant (wizard) guidant l'utilisateur de la configuration aux résultats (incluant les documents d'urbanisme et la décomposition des estimations) et déploiement d'un nouveau mode tutoriel interactif couvrant les étapes de création.
- **Analyses et graphiques** : Ajout de la pyramide des âges et corrections des graphiques de taux EPCI concernant la largeur automatique et les données démographiques [#69](https://github.com/MTES-MCT/otelo/pull/69).
- **Nouvelles fonctionnalités** : Intégration de la fonctionnalité "Docurba" et ajout de l'authentification à deux facteurs (2FA).
- **Gestion des données et exports** : Correction des noms de groupes lors des fusions d'EPCI [#68](https://github.com/MTES-MCT/otelo/pull/68), détection des doublons d'exports PowerPoint [#64](https://github.com/MTES-MCT/otelo/pull/64) et corrections sur les exports Excel.
- **Administration et suivi** : Refonte de l'interface d'administration et mise en place du suivi d'usage via Matomo et base de données.

### Évolutions techniques
- **Sécurité renforcée** : Implémentation de la politique de sécurité du contenu (CSP), des en-têtes de sécurité, de la limitation de débit (rate limiting) sur les routes sensibles et de la résolution d'IP CIDR [#66](https://github.com/MTES-MCT/otelo/pull/66).
- **Architecture et Code** : Refactorisation du registre des étapes du parcours de scénario pour une meilleure gestion des flux et validation des variables d'environnement via Zod.
- **Infrastructure et CI/CD** : Optimisation des processus de build (gestion du cache Next.js, support monorepo) et ajustements de la configuration de la CI.

### Autres changements
- Corrections de typographies et ajustements mineurs de l'interface utilisateur (bouton de signalement, modale de bienvenue).

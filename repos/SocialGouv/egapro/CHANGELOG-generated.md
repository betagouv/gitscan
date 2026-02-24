## Changelog : egapro (30 derniers jours)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de la qualité du code, l'ajout de tests automatisés, l'optimisation des performances et la correction de bugs liés à l'authentification et à la configuration de l'environnement. Des améliorations ont également été apportées au processus de CI/CD pour garantir une meilleure qualité des déploiements.

### Évolutions fonctionnelles
- Amélioration de la gestion de l'authentification et de la sélection d'organisation, notamment en corrigeant des problèmes de redirection et de nettoyage de session. (#2796)
- Ajout de la possibilité de se déconnecter avant de sélectionner une organisation.
- Correction de l'affichage des cartes et des paramètres de cache. (#2776)

### Évolutions techniques
- Mise en place d'une nouvelle version du projet. (#2797)
- Ajout de tests Vitest avec support du DSFR pour une meilleure couverture des tests unitaires. (#2794)
- Optimisation du temps de build Docker via le caching. (#2795)
- Ajout de workflows GitHub Actions pour l'analyse de l'accessibilité (a11y) et l'évaluation de la qualité du code avec Claude.
- Ajout de jobs de `review-auto` à chaque nouvelle branche pour une revue de code automatisée. (#2789)
- Amélioration de la configuration de l'environnement de développement avec Proconnect. (#2770)
- Ajout de Lighthouse pour vérifier la qualité des déploiements. (#2818)
- Ajout de `lint` et `format` au processus CI pour garantir la qualité du code. (#2803)

### Autres changements
- Nettoyage des fichiers de configuration. (#2782)
- Mise à jour des informations d'identification Proconnect. (#040a098)
- Correction de la version de l'application (3.15.2).

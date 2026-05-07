## Changelog : plusfraisautravail (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure vers une infrastructure plus robuste et automatisée, avec l'adoption d'OpenTofu pour la gestion de l'infrastructure et l'intégration de workflows de déploiement via GitHub Environments.  Parallèlement, des améliorations significatives ont été apportées à l'affichage des alertes et des vigilances, ainsi que des mises à jour du contenu des questionnaires et des thèmes.

### Évolutions fonctionnelles
- **Alertes et Vigilances :** Ajout de l'affichage des vigilances, avec refactorisation de l'API et déploiement associé.
- **Alert Widget :** Amélioration de l'affichage des alertes avec ajout de liens vers les sources d'information, des tooltips détaillés par tag et une vue par phénomène. Possibilité de tester le widget en mode démo avec différents scénarios.
- **Contenu des questionnaires :** Plusieurs mises à jour et corrections du contenu des questionnaires et des thèmes ont été effectuées [#124afd0](https://github.com/incubateur-ademe/plusfraisautravail/pull/16), [#0dedd43](https://github.com/incubateur-ademe/plusfraisautravail/pull/17), [#458c4e8](https://github.com/incubateur-ademe/plusfraisautravail/pull/15), [#cb68fba](https://github.com/incubateur-ademe/plusfraisautravail/pull/14), [#c304144](https://github.com/incubateur-ademe/plusfraisautravail/pull/13), [#98cbe95](https://github.com/incubateur-ademe/plusfraisautravail/pull/12).
- **API :** Ajout de la prise en charge des alertes RTE Ecowatt pour l'électricité et refonte de l'API météo pour gérer plusieurs phénomènes.

### Évolutions techniques
- **Infrastructure :** Migration vers OpenTofu pour la gestion de l'infrastructure.
- **CI/CD :** Intégration de workflows de déploiement via GitHub Environments pour une meilleure gestion et automatisation des déploiements.
- **Scaleway :** Complétion de la configuration de déploiement sur Scaleway et suppression du préfixe de région de l'ID du conteneur.
- **CORS :** Configuration de la variable d'environnement `CORS_ORIGINS` pour l'API afin de gérer les origines autorisées.
- **Monorepo :** Passage à une structure de monorepo.
- **Linting :** Application du linter Ruff pour améliorer la qualité du code.
- **Pré-commit hooks :** Ajout de hooks pré-commit pour automatiser les vérifications de code.
- **Gestion des secrets :** Amélioration de la gestion des secrets pour les environnements de déploiement.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Nettoyage du code :** Suppression du cache de Vite du `.gitignore`.
- **Traduction :** Ajout de traductions.

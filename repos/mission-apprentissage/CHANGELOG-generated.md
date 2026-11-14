# Synthèse d'activité : mission-apprentissage (du 01/07 au 13/11)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une amélioration significative de l'expérience utilisateur et de la fiabilité des services. Les utilisateurs bénéficient de fonctionnalités enrichies, comme la classification des contacts dans [tableaudebord-lab](/repos/mission-apprentissage/tableaudebord-lab), une recherche plus performante dans [voeux-affelnet](/repos/mission-apprentissage/voeux-affelnet), et des outils de modération et d'accessibilité accrus pour [labonnealternance](/repos/mission-apprentissage/labonnealternance). 

Parallèlement, l'organisation franchit des étapes clés dans l'automatisation de ses processus de développement et l'optimisation de ses services de données. Le lancement du mode Sandbox dans [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) et l'intégration de nouveaux modèles d'apprentissage automatique dans [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) témoignent d'une volonté de moderniser l'offre technologique pour les partenaires et les développeurs.

## Sécurité
- Renforcement de la gestion des secrets par l'adoption de SOPS et la mise en place de la rotation des clés dans [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin), [mongodb](/repos/mission-apprentissage/mongodb) et [infra](/repos/mission-apprentissage/infra).
- Application de correctifs de sécurité critiques et protection des données personnelles (Sentry/JWT) dans [labonnealternance](/repos/mission-apprentissage/labonnealternance).
- Mise à jour des environnements (Node.js, Next.js) et suppression des secrets GitHub pour sécuriser [bal](/repos/mission-apprentissage/bal).
- Sécurisation des jetons d'accès via l'intégration du type d'environnement dans [api-apprentissage](/repos/mission-apprentissage/api-apprentissage).
- Développement de capacités d'audit de sécurité automatisées via [mna-skills](/repos/mission-apprentissage/mna-skills).

## Autres changements notables
- **Infrastructure et déploiement** : Déploiement du nouveau socle d'infrastructure avec isolation réseau et optimisation de la CI/CD dans [infra](/repos/mission-apprentissage/infra). Migration de l'environnement de recette vers un staging pour [bal](/repos/mission-apprentissage/bal).
- **Modernisation technique** : Montée de version majeure de MongoDB dans [mongodb](/repos/mission-apprentissage/mongodb), migration vers Mongoose 9 dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage) et passage à Node 26 dans [api-apprentissage](/repos/mission-apprentissage/api-apprentissage).
- **Automatisation des workflows** : Développement d'outils pour automatiser la gestion des issues, des pull requests et des sprints GitHub via [mna-skills](/repos/mission-apprentissage/mna-skills) et [lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp).
- **Optimisation des données** : Amélioration de la gestion des index Elasticsearch dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage) et optimisation des processus d'entraînement de modèles dans [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Évolutions fonctionnelles majeures, accessibilité et sécurité.
- [infra](/repos/mission-apprentissage/infra) : Mise en place du nouveau socle d'infrastructure et optimisation des processus de déploiement.
- [mna-skills](/repos/mission-apprentissage/mna-skills) : Création et refactorisation de compétences d'automatisation pour GitHub.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Amélioration du modèle de classification et de la gestion de la CI/CD.
- [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) : Lancement de nouveaux modes de test et migrations de l'infrastructure logicielle.

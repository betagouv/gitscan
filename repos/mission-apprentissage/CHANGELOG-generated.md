# Synthèse d'activité : mission-apprentissage (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une amélioration significative de l'expérience utilisateur et de l'accessibilité, notamment via [labonnealternance](/repos/mission-apprentissage/labonnealternance) qui propose de nouveaux modules de recherche et une mise en conformité RGAA. Les outils de gestion de données et de communication progressent également avec [bal](/repos/mission-apprentissage/bal) et [tableaudebord-lab](/repos/mission-apprentissage/tableaudebord-lab), offrant de meilleures fonctionnalités de suivi et de classification.

En parallèle, un effort important est porté sur l'automatisation des processus de développement et la robustesse de l'infrastructure. Cela se traduit par le déploiement d'un nouveau socle dans [infra](/repos/mission-apprentissage/infra) et la création de nouveaux outils de gestion de projet et de workflows dans [mna-skills](/repos/mission-apprentissage/mna-skills) et [lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp).

## Sécurité
- **Gestion des secrets et accès** : Adoption généralisée de SOPS pour le chiffrement et la gestion des secrets dans [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin), [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) et [infra](/repos/mission-apprentissage/infra), accompagnée de nouveaux outils de rotation de clés.
- **Protection des données et des flux** : Renforcement de l'isolation réseau, de la gestion des clés OpenPGP dans [infra](/repos/mission-apprentissage/infra), et sécurisation des jetons (JWT) dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) et [api-apprentissage](/repos/mission-apprentissage/api-apprentissage).
- **Corrections de vulnérabilités** : Résolution d'une vulnérabilité critique (CVE) sur Vitest dans [bal](/repos/mission-apprentissage/bal) et rotation du secret principal SOPS dans [mongodb](/repos/mission-apprentissage/mongodb).
- **Audit** : Introduction d'une nouvelle compétence d'audit de sécurité automatisé via [mna-skills](/repos/mission-apprentissage/mna-skills).

## Autres changements notables
- **Infrastructure et CI/CD** : Déploiement du nouveau socle d'infrastructure dans [infra](/repos/mission-apprentissage/infra) et optimisation des processus de déploiement et de la pile de logs.
- **Modernisation des stacks techniques** : Montées de version majeures incluant Node 26 pour [api-apprentissage](/repos/mission-apprentissage/api-apprentissage), TypeScript 7 et Next.js 16.3 pour [bal](/repos/mission-apprentissage/bal), ainsi que MongoDB 8.2 pour [mongodb](/repos/mission-apprentissage/mongodb).
- **Intelligence Artificielle et Recherche** : Intégration d'un nouveau modèle de classification dans [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab), prototype de modération par IA dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) et refonte de l'architecture du moteur de recherche.
- **Migrations et Optimisations** : Migration vers Mongoose 9 pour [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage) et optimisation des index Elasticsearch.

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Évolutions majeures de l'interface, de l'accessibilité et de la recherche.
- [infra](/repos/mission-apprentissage/infra) : Mise en place du nouveau socle d'infrastructure et renforcement de la sécurité réseau.
- [mna-skills](/repos/mission-apprentissage/mna-skills) : Développement de nouveaux outils d'automatisation des workflows GitHub.
- [bal](/repos/mission-apprentissage/bal) : Modernisation de la stack technique et amélioration de la gestion des listes de diffusion.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Amélioration des modèles d'apprentissage et de la CI/CD.

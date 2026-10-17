# Synthèse d'activité : mission-apprentissage (du 01/07 au 08/07)

## Résumé de l'activité
L'activité de la période est marquée par une amélioration significative de l'expérience utilisateur et des fonctionnalités métier. Les plateformes de recherche et de gestion bénéficient de nouvelles options, comme le module "offres 100% libres" et une recherche optimisée dans [labonnealternance](/repos/mission-apprentissage/labonnealternance). Parallèlement, la gestion des listes de diffusion dans [bal](/repos/mission-apprentissage/bal) et la classification des contacts dans [tableaudebord-lab](/repos/mission-apprentissage/tableaudebord-lab) ont été enrichies pour offrir un suivi plus précis et intuitif.

Ces évolutions visent à rendre les outils plus performants et accessibles, tout en intégrant des expérimentations prometteuses comme la modération automatique par IA dans [labonnealternance](/repos/mission-apprentissage/labonnealternance).

## Sécurité
- **Gestion des secrets :** Adoption généralisée de SOPS pour le chiffrement et la rotation des clés dans [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin), [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) et [mongodb](/repos/mission-apprentissage/mongodb).
- **Protection des données :** Renforcement de la sécurité des jetons (JWT) et protection des données sensibles dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) et [api-apprentissage](/repos/mission-apprentissage/api-apprentissage).
- **Corrections et infrastructure :** Résolution d'une vulnérabilité critique (CVE) dans [bal](/repos/mission-apprentissage/bal) et sécurisation des runners GitHub via l'importation de clés OpenPGP dans [infra](/repos/mission-apprentissage/infra).

## Autres changements notables
- **Infrastructure et Automatisation :** Mise en œuvre d'un réseau privé pour isoler la production et déploiement de runners auto-hébergés dans [infra](/repos/mission-apprentissage/infra). Parallèlement, l'automatisation des workflows GitHub a été renforcée via de nouveaux outils dans [mna-skills](/repos/mission-apprentissage/mna-skills) et [lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp).
- **Intelligence Artificielle :** Amélioration des capacités de classification des offres grâce à l'intégration de nouveaux modèles dans [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) et mise en place d'un prototype de modération par IA dans [labonnealternance](/repos/mission-apprentissage/labonnealternance).
- **Modernisation des stacks techniques :** Migrations majeures vers de nouvelles versions de langages et frameworks, notamment Node 26 dans [api-apprentissage](/repos/mission-apprentissage/api-apprentissage), TypeScript 7/Next.js 16.3 dans [bal](/repos/mission-apprentissage/bal) et Mongoose 9 dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Évolutions majeures de l'interface, de la recherche et mise en conformité RGAA.
- [mna-skills](/repos/mission-apprentissage/mna-skills) : Développement intensif d'outils d'automatisation des processus GitHub.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Améliorations techniques liées au machine learning et à la CI/CD.
- [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) : Optimisations de l'API et mise à jour de l'environnement d'exécution.
- [infra](/repos/mission-apprentissage/infra) : Travaux structurels sur l'isolation réseau et l'automatisation.

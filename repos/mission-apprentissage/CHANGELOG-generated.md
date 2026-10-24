# Synthèse d'activité : mission-apprentissage (du 01/07 au 07/07/2026)

## Résumé de l'activité
L'activité de cette période est marquée par une forte progression de l'expérience utilisateur et de l'accessibilité, notamment avec la mise en conformité RGAA et l'amélioration des outils de recherche dans [labonnealternance](/repos/mission-apprentissage/labonnealternance). Les fonctionnalités de gestion sont également enrichies, avec l'ajout de la classification de contacts dans [tableaudebord-lab](/repos/mission-apprentissage/tableaudebord-lab) et un meilleur suivi des listes de diffusion dans [bal](/repos/mission-apprentissage/bal).

Sur le plan opérationnel, l'organisation renforce son efficacité grâce à une automatisation accrue des processus de développement. Le déploiement de nouveaux outils de gestion de workflow dans [mna-skills](/repos/mission-apprentissage/mna-skills) et [lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp) permet une gestion plus fluide des projets, tandis que l'introduction d'un mode "Sandbox" dans [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) sécurise les phases de test.

## Sécurité
- **Gestion des secrets et accès** : Adoption généralisée du pilote SOPS pour sécuriser les secrets dans [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin), [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) et [mongodb](/repos/mission-apprentissage/mongodb), accompagnée de nouveaux outils de rotation de clés.
- **Protection des données et authentification** : Renforcement de la sécurité des jetons et de la protection des données dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) et [api-apprentissage](/repos/mission-apprentissage/api-apprentissage).
- **Maintenance corrective** : Correction de vulnérabilités critiques (CVE) dans [bal](/repos/mission-apprentissage/bal).
- **Sécurisation de l'infrastructure** : Mise en place de runners GitHub auto-hébergés et sécurisés via l'importation de clés OpenPGP dans [infra](/repos/mission-apprentissage/infra).

## Autres changements notables
- **Modernisation de l'infrastructure** : Déploiement d'un réseau privé pour isoler la production dans [infra](/repos/mission-apprentissage/infra) et mise à niveau majeure de l'instance MongoDB dans [mongodb](/repos/mission-apprentissage/mongodb).
- **Évolutions des stacks techniques** : Migrations importantes vers de nouvelles versions de Node.js ([api-apprentissage](/repos/mission-apprentissage/api-apprentissage), [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas)), TypeScript/Next.js ([bal](/repos/mission-apprentissage/bal)) et Mongoose 9 ([catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage)).
- **Optimisation des performances** : Refonte du moteur de recherche dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) et optimisation de l'indexation Elasticsearch dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Évolutions majeures sur l'accessibilité, la recherche et l'introduction de l'IA.
- [mna-skills](/repos/mission-apprentissage/mna-skills) : Développement intensif de compétences d'automatisation pour la gestion des issues et des pull requests.
- [infra](/repos/mission-apprentissage/infra) : Travaux importants sur l'isolation réseau et l'automatisation CI/CD.
- [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) : Améliorations de l'administration, de la stabilité et mise en place du mode Sandbox.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Optimisation des modèles de classification et de la chaîne de déploiement.

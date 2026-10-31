# Synthèse d'activité : mission-apprentissage (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de la période est marquée par une montée en puissance des services utilisateurs et une consolidation majeure de l'infrastructure. Les efforts se sont concentrés sur l'amélioration de l'expérience et de l'accessibilité de [labonnealternance](/repos/mission-apprentissage/labonnealternance), ainsi que sur la création de nouveaux outils d'automatisation pour optimiser les flux de travail des développeurs ([mna-skills](/repos/mission-apprentissage/mna-skills), [lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp)). 

L'écosystème devient plus robuste et sécurisé grâce à une modernisation des stacks techniques et à une meilleure gestion des secrets et des réseaux. Ces évolutions permettent d'offrir des services plus fiables, une meilleure gestion des données et une capacité d'automatisation accrue pour l'organisation.

## Sécurité
- **Gestion des secrets** : Adoption de SOPS pour renforcer le chiffrement et le contrôle d'accès aux secrets ([mongodb](/repos/mission-apprentissage/mongodb), [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin), [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab)).
- **Protection des accès** : Mise en œuvre de la rotation des clés et sécurisation des jetons (JWT et claims d'environnement) ([mongodb](/repos/mission-apprentissage/mongodb), [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin), [api-apprentissage](/repos/mission-apprentissage/api-apprentissage), [labonnealternance](/repos/mission-apprentissage/labonnealternance)).
- **Isolation réseau** : Déploiement d'une infrastructure sur réseau privé pour isoler les services de production ([infra](/repos/mission-apprentissage/infra)).
- **Maintenance corrective** : Résolution d'une vulnérabilité critique (CVE) sur Vitest ([bal](/repos/mission-apprentissage/bal)).

## Autres changements notables
- **Intelligence Artificielle & Data** : Intégration d'un nouveau modèle de classification des offres ([labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab)) et lancement d'un prototype de modération automatique par IA ([labonnealternance](/repos/mission-apprentissage/labonnealternance)).
- **Automatisation des workflows** : Développement de "skills" pour automatiser la gestion des issues et des audits de sécurité ([mna-skills](/repos/mission-apprentissage/mna-skills)) et amélioration de la gestion dynamique des sprints GitHub ([lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp)).
- **Modernisation des stacks techniques** : Montées de version majeures des frameworks et langages (Node.js, TypeScript, Next.js) ([api-apprentissage](/repos/mission-apprentissage/api-apprentissage), [bal](/repos/mission-apprentissage/bal)) et migration vers Mongoose 9 ([catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage)).
- **Infrastructure & DevOps** : Mise en place de runners GitHub auto-hébergés ([infra](/repos/mission-apprentissage/infra)), mise à niveau de MongoDB ([mongodb](/repos/mission-apprentissage/mongodb)) et unification des environnements de développement ([flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas)).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Évolutions majeures de l'interface, de la recherche et mise en conformité RGAA.
- [mna-skills](/repos/mission-apprentissage/mna-skills) : Développement intensif de nouveaux outils d'automatisation pour les processus GitHub.
- [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) : Lancement du mode Sandbox et modernisation de l'infrastructure.
- [lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp) : Optimisation de la gestion des projets et des sprints via l'API.
- [infra](/repos/mission-apprentissage/infra) : Sécurisation du réseau et automatisation de la CI/CD.

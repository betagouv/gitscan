## Changelog : bal (30 derniers jours, au 11 novembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité du système et la modernisation de l'infrastructure, notamment avec la transition vers un nouvel environnement de staging. Une amélioration concernant la gestion des mots de passe a également été déployée.

### Évolutions fonctionnelles
- Amélioration de la gestion des mots de passe [#568](https://github.com/mission-apprentissage/bal/pull/568)

### Évolutions techniques
- **Sécurité** :
    - Mise à jour de Node.js (versions 26.12.1 et 26.13.1) pour intégrer les correctifs de sécurité d'octobre et novembre [#565](https://github.com/mission-apprentissage/bal/pull/565), [#569](https://github.com/mission-apprentissage/bal/pull/569).
    - Application des correctifs de sécurité pour Next.js [#562](https://github.com/mission-apprentissage/bal/pull/562).
    - Renforcement de la sécurité par la suppression des secrets GitHub [#561](https://github.com/mission-apprentissage/bal/pull/561).
- **Infrastructure** :
    - Migration de l'environnement de recette vers un environnement de staging [#563](https://github.com/mission-apprentissage/bal/pull/563), [#564](https://github.com/mission-apprentissage/bal/pull/564).
    - Optimisation de la configuration Docker, incluant la suppression de la génération automatique du fichier `docker-compose.yml` [#567](https://github.com/mission-apprentissage/bal/pull/567) et la mise à jour de l'image Metabase [#566](https://github.com/mission-apprentissage/bal/pull/566).

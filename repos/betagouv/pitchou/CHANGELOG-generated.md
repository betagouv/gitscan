## Changelog : pitchou (30 derniers jours, au 25 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la modernisation des outils de build et l'optimisation de l'environnement de développement. Des corrections de sécurité importantes ont été apportées, notamment concernant le chiffrement et la gestion des accès. L'infrastructure de build a été migrée vers Vite pour plus de performance et l'utilisation de pnpm a été adoptée pour la gestion des dépendances.

### Évolutions fonctionnelles
- Autorisation des routes d'écriture et de suppression via CAP. [#565](https://github.com/betagouv/pitchou/issues/565)

### Évolutions techniques
- **Migration de l'outil de build:** Rollup a été remplacé par Vite pour améliorer la vitesse et l'efficacité du build. [#564](https://github.com/betagouv/pitchou/issues/564)
- **Gestion des dépendances:** Passage à pnpm pour une gestion plus performante des dépendances. [#561](https://github.com/betagouv/pitchou/issues/561)
- **Amélioration du CI:** Le CI a été amélioré en utilisant `just` en local et dans les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- **Sécurité:**
    - Implémentation d'un IV aléatoire pour le chiffrement, accompagné de tests unitaires. [#560](https://github.com/betagouv/pitchou/issues/560)
    - Durcissement de la connexion et du code d'accès pour renforcer la sécurité. [#557](https://github.com/betagouv/pitchou/issues/557)
- **Tests:** Ajout de Vitest et de tests pour la fonction `manipulationStrings`. [#559](https://github.com/betagouv/pitchou/issues/559)
- **Migrations:** Correction de l'utilisation de Knex dans les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)

### Autres changements
- **Environnement de développement:** Ajout d'un shell de développement Nix et configuration de Direnv pour faciliter le développement local. [#558](https://github.com/betagouv/pitchou/issues/558)
- **Qualité du code:** Ajout et application de Prettier pour uniformiser le style du code. [#555](https://github.com/betagouv/pitchou/issues/555)

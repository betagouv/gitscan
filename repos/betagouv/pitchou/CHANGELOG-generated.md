## Changelog : pitchou (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, l'équipe a réalisé une refonte technique majeure de l'application, passant de Fastify et Rollup à SvelteKit et Vite.  Cette migration vise à améliorer les performances, la maintenabilité et l'expérience de développement. Des améliorations de sécurité ont également été apportées, notamment au niveau du chiffrement et de la gestion des accès. Enfin, des corrections ont été implémentées pour améliorer la synchronisation des données et la gestion des pièces jointes.

### Évolutions fonctionnelles

- Ajout d'un bandeau d'identification sur l'environnement de *staging* pour une meilleure distinction. [#574](https://github.com/betagouv/pitchou/issues/574)
- Autorisation des opérations d'écriture et de suppression via le *capability access point* (CAP). [#565](https://github.com/betagouv/pitchou/issues/565)
- Correction de la gestion des entreprises *null* lors de la synchronisation des dossiers. [#569](https://github.com/betagouv/pitchou/issues/569)
- Correction du rattachement des pièces jointes partagées entre dossiers lors de la synchronisation. [#570](https://github.com/betagouv/pitchou/issues/570)
- Ajout d'un *seed* de développement pour permettre la connexion locale avec un compte prédéfini. [#563](https://github.com/betagouv/pitchou/issues/563)

### Évolutions techniques

- **Refonte de l'architecture :** Migration complète vers SvelteKit (SPA) en remplacement de Fastify. [#566](https://github.com/betagouv/pitchou/issues/566)
- **Optimisation du build :** Remplacement de Rollup par Vite pour un processus de construction plus rapide et efficace. [#564](https://github.com/betagouv/pitchou/issues/564)
- **Gestion des dépendances :** Passage à pnpm pour une gestion plus performante des dépendances. [#561](https://github.com/betagouv/pitchou/issues/561)
- **Amélioration du CI/CD :** Utilisation de *just* en local et dans les GitHub Actions pour simplifier et améliorer le processus d'intégration continue. [#562](https://github.com/betagouv/pitchou/issues/562)
- **Sécurité :** Implémentation d'un vecteur d'initialisation (IV) aléatoire pour le chiffrement et ajout de tests associés. [#560](https://github.com/betagouv/pitchou/issues/560)
- Durcissement de la connexion et du code d'accès pour renforcer la sécurité. [#557](https://github.com/betagouv/pitchou/issues/557)
- Utilisation du paramètre `knex` lors des migrations pour une meilleure gestion de la base de données. [#556](https://github.com/betagouv/pitchou/issues/556)
- Configuration de `pgdata` en volume nommé dans Docker pour éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Suppression du service *tooling* dans Docker. [#572](https://github.com/betagouv/pitchou/issues/572)

### Autres changements

- Ajout de Prettier pour formater automatiquement le code et assurer une meilleure cohérence. [#555](https://github.com/betagouv/pitchou/issues/555)
- Ajout de Vitest et de tests pour la fonction `manipulationStrings`. [#559](https://github.com/betagouv/pitchou/issues/559)
- Configuration d'un *dev shell* Nix et de Direnv pour un environnement de développement plus isolé et reproductible. [#558](https://github.com/betagouv/pitchou/issues/558)
- Correction de la seed script et correction de l'origine. [#575](https://github.com/betagouv/pitchou/issues/575)

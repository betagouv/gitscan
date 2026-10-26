## Changelog : formulaire-qf (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par une importante mise à jour de l'infrastructure technique, notamment le passage à Ruby 4.0. Des améliorations significatives ont été apportées à la fiabilité des déploiements et des tests automatiques, tout en renforçant la protection des données des usagers.

### Évolutions fonctionnelles
- **Protection de la vie privée** : les détails personnels des utilisateurs et les réponses d'API ne sont plus transmis à l'outil de suivi d'erreurs Sentry lors des erreurs API.
- **Fiabilité des données** : la version du quotient familial est désormais gérée sous forme de chaîne de caractères pour garantir la cohérence des données.

### Évolutions techniques
- **Mise à jour majeure de l'environnement** : montée de version vers Ruby 4.0.9 [#414](https://github.com/etalab/formulaire-qf/issues/414).
- **Amélioration de la CI/CD** : correction du cycle de tests pour qu'ils s'exécutent systématiquement à chaque nouveau commit sur une pull request [#397](https://github.com/etalab/formulaire-qf/issues/397).
- **Optimisation du déploiement** : résolution de problèmes de déploiement via la mise à jour de Sprockets pour assurer la compatibilité avec JSON 3 [#398](https://github.com/etalab/formulaire-qf/issues/398).
- **Refactoring et nettoyage** :
    - Suppression de la dépendance Spring [#413](https://github.com/etalab/formulaire-qf/issues/413).
    - Mise à jour et nettoyage des migrations pour GoodJob [#392](https://github.com/etalab/formulaire-qf/issues/392).
    - Centralisation des paramètres Logstasher dans un fichier de configuration dédié [#396](https://github.com/etalab/formulaire-qf/issues/396).
- **Amélioration du workflow de développement** : ajout de scripts pour faciliter l'utilisation de `git worktree` avec des bases de données et des ports isolés [#394](https://github.com/etalab/formulaire-qf/issues/394).

### Autres changements
- **Documentation** : création du fichier `CLAUDE.md` récapitulant les commandes et les conventions du dépôt.
- **Correction technique** : résolution d'un problème de clé de version en double dans le format JSON 3 [#391](https://github.com/etalab/formulaire-qf/issues/391).

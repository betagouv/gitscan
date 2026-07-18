## Changelog : Resultats-Elections-FPT (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette version apporte des corrections et améliorations concernant l'affichage des scrutins, des collectivités et des données dans les tableaux et cartes. Des ajustements ont également été effectués pour améliorer l'expérience utilisateur et corriger des bugs liés à l'affichage et à la récupération des données.

### Évolutions fonctionnelles
- Correction de l'affichage des scrutins organisés dans la création de scrutin [#62](https://github.com/betagouv/Resultats-Elections-FPT/pull/62).
- Correction de l'affichage des scrutins liés à la création dans la cartographie des scrutins [#63](https://github.com/betagouv/Resultats-Elections-FPT/pull/63).
- Amélioration de l'affichage des badges pour les collectivités : ils ne s'affichent plus s'ils sont vides, et un nouveau type de badge "erreur" a été ajouté [#52](https://github.com/betagouv/Resultats-Elections-FPT/pull/52).
- Correction de la récupération des données de la table pour les éditeurs [#53](https://github.com/betagouv/Resultats-Elections-FPT/pull/53).

### Évolutions techniques
- Suppression de la dépendance `npm-run-all` [#60](https://github.com/betagouv/Resultats-Elections-FPT/pull/60).
- Mise à jour de plusieurs dépendances (lodash, qs, postcss, follow-redirects, shell-quote) via Dependabot.

### Autres changements
- Préparation de la version MEP v1.14 et v1.15.
- Ajout de versions "staging" pour les déploiements.

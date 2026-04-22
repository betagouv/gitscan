## Changelog : zacharie (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'améliorations significatives en termes de sécurité, de correction de bugs et d'expérience utilisateur. Les efforts se sont concentrés sur l'amélioration des flux de création et de gestion des fiches, ainsi que sur l'optimisation des routes et de l'administration. De nouvelles fonctionnalités, comme le tableau de bord public avec la matrice d'impact, ont également été ajoutées.

### Évolutions fonctionnelles
- Amélioration du flux de création de fiches, notamment pour l'ajout de carcasses [#281](https://github.com/betagouv/zacharie/issues/281).
- Ajout de filtres par premier détenteur et CCG sur le tableau de bord [#267](https://github.com/betagouv/zacharie/issues/267).
- Nouveau tableau de bord public avec matrice d'impact [#272](https://github.com/betagouv/zacharie/issues/272).
- Amélioration de l'interface utilisateur pour la gestion des fiches (liste, création, examinateur) [#301](https://github.com/betagouv/zacharie/issues/301), [#305](https://github.com/betagouv/zacharie/issues/305), [#306](https://github.com/betagouv/zacharie/issues/306), [#311](https://github.com/betagouv/zacharie/issues/311), [#302](https://github.com/betagouv/zacharie/issues/302).
- Correction d'un bug empêchant l'affichage des carcasses lorsque seul un groupe était présent [#287](https://github.com/betagouv/zacharie/issues/287).
- Amélioration de l'UX de la page des statistiques [#273](https://github.com/betagouv/zacharie/issues/273).
- Ajout d'une nouvelle interface pour la création d'une FEI [#219](https://github.com/betagouv/zacharie/issues/219).
- Correction de l'invitation [#309](https://github.com/betagouv/zacharie/issues/309).

### Évolutions techniques
- Refonte des routes pour améliorer la performance et la maintenabilité [#308](https://github.com/betagouv/zacharie/issues/308), [#295](https://github.com/betagouv/zacharie/issues/295), [#293](https://github.com/betagouv/zacharie/issues/293).
- Amélioration de la sécurité avec l'ajout de headers de sécurité (CSP, connect-src) et la correction de vulnérabilités npm audit [#278](https://github.com/betagouv/zacharie/issues/278), [#275](https://github.com/betagouv/zacharie/issues/275), [#259](https://github.com/betagouv/zacharie/issues/259), [#235](https://github.com/betagouv/zacharie/issues/235), [#300](https://github.com/betagouv/zacharie/issues/300).
- Mise en place de `npm-ci` pour une meilleure sécurité des builds [#285](https://github.com/betagouv/zacharie/issues/285).
- Suppression d'une route API inutilisée [#260](https://github.com/betagouv/zacharie/issues/260).
- Amélioration du router SVI [#296](https://github.com/betagouv/zacharie/issues/296).
- Correction de problèmes liés au rafraîchissement de la FEI [#250](https://github.com/betagouv/zacharie/issues/250).
- Amélioration des logs pour n'afficher que ceux des utilisateurs connectés [#261](https://github.com/betagouv/zacharie/issues/261).

### Autres changements
- Amélioration du design des boutons pour respecter les standards DSFR [#268](https://github.com/betagouv/zacharie/issues/268).
- Correction de problèmes d'accessibilité (alt sur les iframes) [#274](https://github.com/betagouv/zacharie/issues/274).
- Correction du wording sur certaines parties de l'application [#286](https://github.com/betagouv/zacharie/issues/286).
- Suppression de Claude [#2868afb].
- Corrections diverses de layout et d'UI [#313](https://github.com/betagouv/zacharie/issues/313), [#310](https://github.com/betagouv/zacharie/issues/310).

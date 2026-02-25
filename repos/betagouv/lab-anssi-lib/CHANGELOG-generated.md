## Changelog : lab-anssi-lib (30 derniers jours)

### Résumé
Cette nouvelle version de la librairie `lab-anssi-lib` (2.1.5) apporte des mises à jour de sécurité importantes pour plusieurs dépendances, notamment `axios`, `express-ipfilter`, `qs` et `express`. Une option a également été ajoutée pour faciliter la publication sur npm.

### Évolutions techniques
- Mise à jour de `express` en version 5 pour bénéficier des dernières améliorations et correctifs de sécurité.
- Mise à jour de `axios` suite à une alerte de sécurité dependabot (#13).
- Mise à jour de `express-ipfilter` suite à une alerte de sécurité dependabot concernant la dépendance `lodash` (#8).
- Mise à jour de `qs` suite à une alerte de sécurité dependabot (#7).
- Ajout du paramètre `--no-git-checks` pour permettre la publication sur npm sans vérification de l'état du dépôt git.

### Autres changements
- Passage à la version 2.1.4 puis 2.1.5.

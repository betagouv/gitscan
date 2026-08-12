## Changelog : aides-jeunes (30 derniers jours, au 7 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilisation des simulations grâce à des améliorations du moteur de calcul et la résolution d'incidents de production. Parallèlement, une maintenance importante des contenus a été réalisée pour corriger de nombreux liens obsolètes et mettre à jour les informations relatives aux différentes aides proposées.

### Évolutions fonctionnelles
- Ajout d'un système d'identification de dispositifs spécifiques pour Paris Cité [#5160](https://github.com/betagouv/aides-jeunes/issues/5160).
- Maintenance et correction de nombreux liens rompus ou obsolètes concernant diverses aides (BAFA, Pass, stages, mobilité, etc.) [#5165-5190](https://github.com/betagouv/aides-jeunes/issues/5165).
- Correction des liens pour les bourses du secteur sanitaire et social en région Grand Est [#5173](https://github.com/betagouv/aides-jeunes/issues/5173).

### Évolutions techniques
- **Améliorations du moteur Openfisca** :
  - Prise en compte des résultats pour les usagers déclarant un taux d'incapacité [#5212](https://github.com/betagouv/aides-jeunes/issues/5212).
  - Optimisation du calcul budgétaire sur les tracés selon leur coût réel [#5211](https://github.com/betagouv/aides-jeunes/issues/5211).
  - Fiabilisation des chemins d'erreur et limitation de la durée des calculs [#5205](https://github.com/betagouv/aides-jeunes/issues/5205).
- **Stabilité et infrastructure** :
  - Résolution d'incidents de production (erreurs 504) suite à une mise à jour du moteur de calcul [#5204](https://github.com/betagouv/aides-jeunes/issues/5204).
  - Correction de l'authentification par jeton pour les appels échouant dans une iframe [#5210](https://github.com/betagouv/aides-jeunes/issues/5210).
  - Mise à jour des outils de test et de communication (Cypress, Nodemailer, MJML) [#5148](https://github.com/betagouv/aides-jeunes/issues/5148), [#5146](https://github.com/betagouv/aides-jeunes/issues/5146).

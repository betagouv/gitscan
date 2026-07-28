## Changelog : aides-jeunes (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette mise à jour comprend principalement des corrections de liens vers des aides et opportunités pour les jeunes, qui étaient devenus obsolètes ou pointaient vers des ressources privées. Des mises à jour de dépendances et des améliorations des tests et de l'envoi d'emails ont également été intégrées. Une amélioration de la recherche a été apportée en ajoutant le code départemental aux suggestions d'institutions.

### Évolutions fonctionnelles
- Correction de liens cassés pour plusieurs aides et opportunités :
  - Bourse du secteur sanitaire et social (région grand est) [#5173](https://github.com/betagouv/aides-jeunes/issues/5173)
  - Pass Pass mensuel et annuel pour les moins de 26 ans [#5172](https://github.com/betagouv/aides-jeunes/issues/5172), [#5171](https://github.com/betagouv/aides-jeunes/issues/5171)
  - Stages à l'étranger (post-bac) [#5170](https://github.com/betagouv/aides-jeunes/issues/5170)
  - Sas jeunes : orientation active vers l'emploi [#5169](https://github.com/betagouv/aides-jeunes/issues/5169)
  - Bourses pour les formations sanitaires et sociales [#5168](https://github.com/betagouv/aides-jeunes/issues/5168)
  - Prêt d’un vélo Freevélo’v [#5167](https://github.com/betagouv/aides-jeunes/issues/5167)
  - Fonds d'aide à la mobilité vers l'emploi [#5166](https://github.com/betagouv/aides-jeunes/issues/5166)
  - Un Parrain, un Emploi [#5165](https://github.com/betagouv/aides-jeunes/issues/5165)
- Amélioration de la recherche : Ajout du code du département aux suggestions d'institution [#5130](https://github.com/betagouv/aides-jeunes/issues/5130)

### Évolutions techniques
- Mise à jour de Cypress pour améliorer les tests [#5148](https://github.com/betagouv/aides-jeunes/issues/5148)
- Mise à jour de `nodemailer` et `mjml` pour l'envoi d'emails [#5146](https://github.com/betagouv/aides-jeunes/issues/5146)
- Mise à jour de la dépendance `openfisca-france` dans `/openfisca` [#5164](https://github.com/betagouv/aides-jeunes/issues/5164) et [#5162](https://github.com/betagouv/aides-jeunes/issues/5162)
- Mise à jour de la dépendance `js-yaml` dans `/contribuer` [#5161](https://github.com/betagouv/aides-jeunes/issues/5161)
- Mise à jour de la dépendance `next` dans `/contribuer` [#5179](https://github.com/betagouv/aides-jeunes/issues/5179)
- Mise à jour de dépendances diverses via Dependabot.

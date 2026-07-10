## Changelog : aides-jeunes (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette mise à jour améliore l'expérience utilisateur en permettant de filtrer les institutions par code département lors de la contribution, corrige des bugs liés au tri des ressources et à la gestion des erreurs réseau, et met à jour les données de l'aide permis de conduire pour les demandeurs d'emploi.

### Évolutions fonctionnelles
- Amélioration de l'outil de contribution simplifié : ajout de la possibilité de sélectionner une institution lors de la contribution, avec affichage du code département associé. [#5133](https://github.com/betagouv/aides-jeunes/pull/5133)
- Mise à jour des données de l'aide "Permis de conduire pour les demandeurs d'emploi". [#5151](https://github.com/betagouv/aides-jeunes/pull/5151)

### Évolutions techniques
- Correction d'un bug qui provoquait une mutation inattendue du tableau réactif lors du tri des ressources. [#5155](https://github.com/betagouv/aides-jeunes/pull/5155)
- Correction d'une erreur réseau non gérée lors du préchargement des paramètres OpenFisca. [#5157](https://github.com/betagouv/aides-jeunes/pull/5157)
- Ajout du code du département aux suggestions d'institution pour faciliter la contribution. [#5130](https://github.com/betagouv/aides-jeunes/pull/5130)

### Autres changements
- Mise à jour de la dépendance `js-yaml` dans le répertoire `/contribuer`. [#5161](https://github.com/betagouv/aides-jeunes/pull/5161)
- Mise à jour de la dépendance `openfisca-france` dans le répertoire `/openfisca`. [#5152](https://github.com/betagouv/aides-jeunes/pull/5162)

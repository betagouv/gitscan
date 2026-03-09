## Changelog : mon-service-securise (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la refonte du moteur de risque et l'intégration des nouvelles données de référentiel V2. De nombreuses améliorations ont été apportées à l'interface utilisateur pour faciliter la gestion des risques, des mesures et des services, notamment l'ajout de filtres et d'informations supplémentaires. Des corrections de bugs et des optimisations ont également été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les services et brouillons. [#990b104](https://github.com/betagouv/mon-service-securise/commit/990b104)
- Ajout de la possibilité de supprimer les brouillons de service depuis le tiroir. [#cc883e7](https://github.com/betagouv/mon-service-securise/commit/cc883e7)
- Affichage de la thématique et des porteurs singuliers dans le tableau des mesures. [#c4b6511](https://github.com/betagouv/mon-service-securise/commit/c4b6511), [#34d082c](https://github.com/betagouv/mon-service-securise/commit/34d082c)
- Ajout de la partie responsable dans le filtrage et l'affichage. [#cb89feb](https://github.com/betagouv/mon-service-securise/commit/cb89feb), [#6ae94f4](https://github.com/betagouv/mon-service-securise/commit/6ae94f4)
- Amélioration de l'affichage des filtres. [#f2a1083](https://github.com/betagouv/mon-service-securise/commit/f2a1083)
- Ajout de la transcription dans le tampon d'homologation. [#fc0c2f4](https://github.com/betagouv/mon-service-securise/commit/fc0c2f4)
- Ajout des caractéristiques du service (criticité, exposition) dans l'export CSV et le PDF. [#eeec0e3](https://github.com/betagouv/mon-service-securise/commit/eeec0e3), [#df48328](https://github.com/betagouv/mon-service-securise/commit/df48328)

### Évolutions techniques
- Migration vers Express 5. [#67e1591](https://github.com/betagouv/mon-service-securise/commit/67e1591)
- Refonte du moteur de risque avec intégration des données V2 et calcul de la vraisemblance et de la gravité. [#d0476d3](https://github.com/betagouv/mon-service-securise/commit/d0476d3), [#eab3ad2](https://github.com/betagouv/mon-service-securise/commit/eab3ad2)
- Conversion de nombreux modèles de données en Typescript pour une meilleure typage et maintenabilité. [#cea0c50](https://github.com/betagouv/mon-service-securise/commit/cea0c50) et beaucoup d'autres commits commençant par "[SOIN]".
- Suppression du code lié à l'authentification legacy (mot de passe, réinitialisation). [#ee9fc4e](https://github.com/betagouv/mon-service-securise/commit/ee9fc4e) et commits suivants.
- Mise à jour de plusieurs dépendances : `bcrypt`, `knex`, `knex-pglite`, `axios`, `jsonwebtoken`. [#7513c41](https://github.com/betagouv/mon-service-securise/commit/7513c41), [#f58eda5](https://github.com/betagouv/mon-service-securise/commit/f58eda5), [#cd11bde](https://github.com/betagouv/mon-service-securise/commit/cd11bde), [#189eec6](https://github.com/betagouv/mon-service-securise/commit/189eec6)
- Ajout de `svelte-check` dans la CI et correction des erreurs associées. [#4ebb5a1](https://github.com/betagouv/mon-service-securise/commit/4ebb5a1)

### Autres changements
- Suppression du composant et de la page "Ui Kit". [#38854ca](https://github.com/betagouv/mon-service-securise/commit/38854ca)
- Ajout de métadonnées. [#f0e0c97](https://github.com/betagouv/mon-service-securise/commit/f0e0c97)
- Nettoyage de code et suppression de code mort. [#f9f660b](https://github.com/betagouv/mon-service-securise/commit/f9f660b) et plusieurs autres commits commençant par "[SOIN]".
- Correction de plusieurs bugs mineurs et améliorations de la lisibilité du code.

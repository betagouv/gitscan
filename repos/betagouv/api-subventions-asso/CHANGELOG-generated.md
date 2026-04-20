## Changelog : api-subversions-asso (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données des programmes de financement (notamment Chorus FSE), la correction de bugs liés aux notifications et à l'encodage des noms de fichiers, ainsi que des refactorings internes pour une meilleure maintenabilité du code. Une nouvelle version (v0.83.0) a été publiée.

### Évolutions fonctionnelles
- Correction d'un bug dans les notifications de dépôt de renouvellement [#3822](https://github.com/betagouv/api-subventions-asso/issues/3822).
- Amélioration de la gestion des programmes Chorus FSE, incluant la mise à jour des codes et descriptions [#3867](https://github.com/betagouv/api-subventions-asso/issues/3867) et [#3875](https://github.com/betagouv/api-subventions-asso/issues/3875).
- Possibilité de restreindre le parsing des données à des exercices spécifiques [#3873](https://github.com/betagouv/api-subventions-asso/issues/3873) et [#3884](https://github.com/betagouv/api-subventions-asso/issues/3884).
- Changement d'instance Matomo pour le suivi analytique [#3825](https://github.com/betagouv/api-subventions-asso/issues/3825) et [#3881](https://github.com/betagouv/api-subventions-asso/issues/3881).
- Correction d'un problème d'encodage des noms de fichiers lors de l'envoi de fichiers multipart [#3872](https://github.com/betagouv/api-subventions-asso/issues/3872) et [#3876](https://github.com/betagouv/api-subventions-asso/issues/3876).

### Évolutions techniques
- Refactoring du code pour renommer les dossiers et fichiers afin de respecter les conventions du projet [#3802](https://github.com/betagouv/api-subventions-asso/issues/3802) et [#3879](https://github.com/betagouv/api-subventions-asso/issues/3879).
- Introduction de "ports to adapters" pour améliorer l'architecture et la testabilité [#3803](https://github.com/betagouv/api-subventions-asso/issues/3803) et [#3877](https://github.com/betagouv/api-subventions-asso/issues/3877).
- Refactoring du code Chorus [#3837](https://github.com/betagouv/api-subventions-asso/issues/3837) et [#3866](https://github.com/betagouv/api-subventions-asso/issues/3866).
- Amélioration de la documentation Swagger pour une meilleure compréhension de l'API [#3847](https://github.com/betagouv/api-subventions-asso/issues/3847) et [#3878](https://github.com/betagouv/api-subventions-asso/issues/3878).
- Corrections de configurations ESLint et TypeScript pour éviter les erreurs.

### Autres changements
- Initialisation du cron Scdl.
- Publication des versions v0.82.0 et v0.83.0.

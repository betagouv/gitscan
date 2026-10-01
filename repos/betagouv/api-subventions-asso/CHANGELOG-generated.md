## Changelog : api-subventions-asso (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois-ci, les travaux ont porté sur l'amélioration de la fiabilité des données associatives (notamment pour les contacts et les coordonnées bancaires) et sur la modernisation technique de l'interface et des processus de traitement. Ces évolutions permettent une gestion plus performante et plus précise des informations issues du RNA et de Sirene.

### Évolutions fonctionnelles
- Correction de l'affichage des données BODACC sur l'interface web.
- Amélioration de la gestion des documents du Répertoire National des Associations (RNA) lors des mises à jour après le premier import [#4034](https://github.com/betagouv/api-subventions-asso/issues/4034).
- Correction des structures de données concernant les contacts et les coordonnées bancaires (RIB) [#4033](https://github.com/betagouv/api-subventions-asso/issues/4033).

### Évolutions techniques
- Modernisation de l'interface utilisateur via la migration des composants vers la syntaxe "runes" de Svelte [#3969](https://github.com/betagouv/api-subventions-asso/issues/3969) ([#4011](https://github.com/betagouv/api-subventions-asso/issues/4011)).
- Optimisation du pipeline de données Sirene (unités légales) par l'intégration du format Parquet [#4038](https://github.com/betagouv/api-subventions-asso/issues/4038).
- Optimisation du flux de données en privilégiant l'utilisation des collections RNA et Sirene avant l'API associations [#4021](https://github.com/betagouv/api-subventions-asso/issues/4021).
- Ajout de scripts permettant l'exécution manuelle des tâches automatisées (cron) liées au RNA et à Sirene.

### Autres changements
- Nettoyage des tests de l'API (suppression de mocks d'environnement inutiles).

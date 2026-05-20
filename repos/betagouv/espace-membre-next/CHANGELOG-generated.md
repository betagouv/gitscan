## Changelog : espace-membre-next (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité, la correction de bugs et l'optimisation de la gestion des phases et des emails. Des améliorations de la recherche ont également été apportées, ainsi qu'un nettoyage du code et de la configuration.

### Évolutions fonctionnelles
- **Recherche:** Ajout d'un champ de recherche combiné pour les startups [#1324](https://github.com/betagouv/espace-membre-next/issues/1324).
- **Phases:** Amélioration de la gestion des phases, incluant des contraintes sur les noms [#1304](https://github.com/betagouv/espace-membre-next/issues/1304) et [#1356](https://github.com/betagouv/espace-membre-next/issues/1356).
- **Emails:** Correction d'un bug empêchant la création d'emails lorsque l'adresse email principale n'est pas définie [#1342](https://github.com/betagouv/espace-membre-next/issues/1342). Amélioration de la synchronisation des emails avec un timeout augmenté [#1372](https://github.com/betagouv/espace-membre-next/issues/1372).
- **Mise à jour d'un utilisateur:** Renforcement de la sécurité en vérifiant l'autorisation avant de mettre à jour les informations d'un événement [#1357](https://github.com/betagouv/espace-membre-next/issues/1357).

### Évolutions techniques
- **Accessibilité (RGAA):** Améliorations significatives de l'accessibilité, incluant l'ajout d'attributs `lang` sur les balises `<html>` [#1361](https://github.com/betagouv/espace-membre-next/issues/1361), la correction de problèmes liés aux labels orphelins [#1363](https://github.com/betagouv/espace-membre-next/issues/1363), l'amélioration de l'accessibilité clavier des éléments cliquables [#1364](https://github.com/betagouv/espace-membre-next/issues/1364) et l'activation du preset recommandé jsx-a11y [#1355](https://github.com/betagouv/espace-membre-next/issues/1355).
- **Composants DSFR:** Utilisation du composant `DataVisualization` au lieu d'un asset SVG supprimé [#1351](https://github.com/betagouv/espace-membre-next/issues/1351).
- **Migration MJML:** Migration du système d'emails MJML [#1350](https://github.com/betagouv/espace-membre-next/issues/1350).
- **Architecture:** Simplification du routage et utilisation accrue du rendu côté serveur (SSR) [#1326](https://github.com/betagouv/espace-membre-next/issues/1326).
- **Configuration:** Nettoyage de la configuration, suppression de variables d'environnement inutiles [#1329](https://github.com/betagouv/espace-membre-next/issues/1329) et suppression de configurations liées à Mattermost [#1325](https://github.com/betagouv/espace-membre-next/issues/1325).

### Autres changements
- Nettoyage de code et suppression de code legacy lié aux emails [#1375](https://github.com/betagouv/espace-membre-next/issues/1375).
- Suppression de TODO liés à l'authentification [#1354](https://github.com/betagouv/espace-membre-next/issues/1354).
- Suppression de la possibilité de supprimer des comptes Matomo/Sentry [#1322](https://github.com/betagouv/espace-membre-next/issues/1322).
- Correction de divers bugs et améliorations mineures [#1337](https://github.com/betagouv/espace-membre-next/issues/1337), [#1338](https://github.com/betagouv/espace-membre-next/issues/1338), [#1339](https://github.com/betagouv/espace-membre-next/issues/1340), [#1331](https://github.com/betagouv/espace-membre-next/issues/1331).
- Renommage et documentation de la tâche `phase-reminder` [#1374](https://github.com/betagouv/espace-membre-next/issues/1374).
- Nettoyage de l'environnement de développement avec la suppression de `dotenv` [#1339](https://github.com/betagouv/espace-membre-next/issues/1339).

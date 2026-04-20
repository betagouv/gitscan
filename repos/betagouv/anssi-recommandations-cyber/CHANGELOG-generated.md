## Changelog : anssi-recommandations-cyber (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, l'ajout de nouvelles fonctionnalités de recherche et d'analyse de documents, ainsi que des corrections de sécurité et de typos. L'intégration de la collection "Jeopardy" est une nouveauté notable, offrant des capacités de recherche supplémentaires.

### Évolutions fonctionnelles
- Ajout de la recherche dans la collection "Jeopardy" et possibilité de récupérer les chunks originaux associés. [#3d3781f](https://github.com/betagouv/anssi-recommandations-cyber/pull/3d3781f)
- Possibilité de lister les documents d'une collection via leurs noms dans un dataframe. [#c6d9763](https://github.com/betagouv/anssi-recommandations-cyber/pull/c6d9763)
- Affichage d'un lien "En savoir plus" pour les sources documentaires de type page HTML. [#ec98247](https://github.com/betagouv/anssi-recommandations-cyber/pull/ec98247)
- Amélioration du prompt pour le rendre plus permissif. [#6146aae](https://github.com/betagouv/anssi-recommandations-cyber/pull/6146aae)
- Affichage des données d'une collection. [#b7994ff](https://github.com/betagouv/anssi-recommandations-cyber/pull/b7994ff)
- Analyse d'une collection avec les documents sans chunks. [#6228e7a](https://github.com/betagouv/anssi-recommandations-cyber/pull/6228e7a)
- La reformulation est désormais obligatoire. [#f7faff0](https://github.com/betagouv/anssi-recommandations-cyber/pull/f7faff0)

### Évolutions techniques
- Séparation des environnements de développement et de production. [#98f19aa](https://github.com/betagouv/anssi-recommandations-cyber/pull/98f19aa)
- Vérification de la présence des variables d'environnement nécessaires au démarrage du serveur. [#56b68b9](https://github.com/betagouv/anssi-recommandations-cyber/pull/56b68b9)
- Gestion améliorée des erreurs : retour d'une erreur HTTP 500 en cas d'échec de communication avec Albert, remontée du message d'erreur original. [#e584866](https://github.com/betagouv/anssi-recommandations-cyber/pull/e584866), [#7de59b3](https://github.com/betagouv/anssi-recommandations-cyber/pull/7de59b3), [#a0f01fe](https://github.com/betagouv/anssi-recommandations-cyber/pull/a0f01fe)
- Utilisation d'une base de données mémoire et d'un Sentry mémoire pour les tests. [#4c17719](https://github.com/betagouv/anssi-recommandations-cyber/pull/4c17719)
- Renommage de `ErreurRechercheGuidesAnssi` en `ErreurRechercheDocuments`. [#15648b8](https://github.com/betagouv/anssi-recommandations-cyber/pull/15648b8)
- Récupération des collections par ordre de création chronologique décroissant. [#1320bdf](https://github.com/betagouv/anssi-recommandations-cyber/pull/1320bdf)

### Autres changements
- Correction d'une typo ("appriécé" -> "apprécié"). [#6b65b01](https://github.com/betagouv/anssi-recommandations-cyber/pull/6b65b01)
- Correction du chiffrement de l'identifiant d'interaction envoyé à Metabase. [#88ceae4](https://github.com/betagouv/anssi-recommandations-cyber/pull/88ceae4)
- Correction d'une typo dans la clef de la variable d'environnement du sel de hachage. [#f4d0915](https://github.com/betagouv/anssi-recommandations-cyber/pull/f4d0915)
- Mise à jour des dépendances de sécurité : `dompurify`, `requests`, `svelte` suite aux alertes Dependabot. [#834cf57](https://github.com/betagouv/anssi-recommandations-cyber/pull/834cf57), [#727abc4](https://github.com/betagouv/anssi-recommandations-cyber/pull/727abc4), [#3949883](https://github.com/betagouv/anssi-recommandations-cyber/pull/3949883)
- Nettoyage du notebook d'interaction avec Albert et ajout d'un champ de saisie pour la clef d'API. [#afc013d](https://github.com/betagouv/anssi-recommandations-cyber/pull/afc013d), [#8b1d84a](https://github.com/betagouv/anssi-recommandations-cyber/pull/8b1d84a)
- Ajout de logs au démarrage pour expliciter la configuration utilisée. [#f6e9bf3](https://github.com/betagouv/anssi-recommandations-cyber/pull/f6e9bf3)
- Modification du wording. [#c91c5e7](https://github.com/betagouv/anssi-recommandations-cyber/pull/c91c5e7)

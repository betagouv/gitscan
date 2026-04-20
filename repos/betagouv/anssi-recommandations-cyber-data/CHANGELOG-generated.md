## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 17 mai 2026)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives dans l'automatisation de la génération de questions (jeopardy) à partir des documents indexés, ainsi que dans l'ajout de nouvelles sources de données, notamment des rapports et recommandations du CERT-FR et de la CNIL. Des améliorations ont également été apportées à l'infrastructure de déploiement et à la gestion des logs.

### Évolutions fonctionnelles
- Ajout de la possibilité de générer des questions (jeopardy) à partir d'une liste de documents, via une nouvelle route API. [#f3cc453](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f3cc453)
- Implémentation d'un client Albert pour la recherche de documents par leur nom. [#0b536f9](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/0b536f9)
- Ajout de la possibilité d'ajouter des chunks (morceaux de texte) à un document existant. [#9c26ac6](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/9c26ac6)
- Intégration de nouvelles sources de données : rapports et fiches réflexes du CERT-FR, documents de la CNIL, recommandations et durcissements du CERT-FR, documents du LAB et panorama de la menace 2025. [#c26c996](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/c26c996), [#6298740](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/6298740), [#2796f44](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/2796f44), [#23e19d7](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/23e19d7), [#01bc121](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/01bc121)
- Amélioration du prompt utilisé pour la génération de questions (jeopardy). [#a757000](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/a757000), [#d5e33a2](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/d5e33a2)

### Évolutions techniques
- Refactoring du code pour extraire un service dédié à la génération de questions (jeopardy). [#f084a46](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f084a46)
- Séparation des environnements de développement et de production. [#feefdae](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/feefdae)
- Mise en place d'une CI/CD pour automatiser le déploiement depuis GitHub. [#88e903f](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/88e903f)
- Correction d'un problème de déploiement lié à une dépendance manquante (pilote Postgres). [#6350851](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/6350851)
- Amélioration de la gestion des logs, notamment pour le suivi de la génération de questions. [#ff086df](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/ff086df)
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité : `aiohttp`, `requests`, `flatted`, `pyasn1`. [#36ec6c4](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/36ec6c4), [#80e1ec3](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/80e1ec3), [#792fad4](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/792fad4), [#01ed8ed](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/01ed8ed)

### Autres changements
- Ajout de documentation sur la réflexion autour de la solution de génération de questions. [#1dbfffd](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1dbfffd)
- Mise à jour de la documentation HyDE. [#3f539f1](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/3f539f1)
- Ajout d'un script `pre-run` pour builder le front-end. [#f3f2df2](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f3f2df2)
- Correction de bugs mineurs et améliorations de la robustesse du code. [#435fabb](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/435fabb), [#6774fc1](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/6774fc1), [#dae30ff](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/dae30ff)

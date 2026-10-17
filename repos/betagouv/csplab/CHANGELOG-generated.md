## Changelog : csplab (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'amélioration significative de la gestion des candidatures (ajout de notes, historique d'activité et interface plus fluide) et l'introduction d'un système de messagerie collaborative pour faciliter les échanges. Le processus d'importation de données a également été enrichi pour mieux intégrer les informations provenant de Talentsoft, tandis que l'architecture technique a été modernisée pour garantir une meilleure stabilité et évolutivité du système.

### Évolutions fonctionnelles
- **Gestion des candidatures** : 
    - Ajout de la possibilité de rédiger et consulter des notes sur une candidature [#1805](https://github.com/betagouv/csplab/issues/1805).
    - Intégration de l'historique d'activité et des dernières actions directement dans le panneau de candidature [#1668](https://github.com/betagouv/csplab/issues/1668).
    - Amélioration de l'ergonomie avec un nouveau panneau de candidature (sous forme de modale) accessible depuis la liste ou le kanban [#1569](https://github.com/betagouv/csplab/issues/1569), [#1477](https://github.com/betagouv/csplab/issues/1477).
    - Ajout d'un garde-fou demandant un motif avant de refuser une candidature [#1506](https://github.com/betagouv/csplab/issues/1506).
- **Messagerie collaborative** : 
    - Mise en place complète du système de messagerie : création de conversations, envoi de messages et possibilité de joindre des fichiers [#1678](https://github.com/betagouv/csplab/issues/1678), [#1666](https://github.com/betagouv/csplab/issues/1666).
    - Possibilité de répondre directement à une conversation depuis le panneau d'une candidature [#1664](https://github.com/betagouv/csplab/issues/1664).
- **Interface Recruteur** : 
    - Nouvelles capacités d'assignation de responsables de recrutement en lot [#1483](https://github.com/betagouv/csplab/issues/1483).
    - Amélioration de la visibilité des documents et des détails des candidats pour les agents autorisés [#1475](https://github.com/betagouv/csplab/issues/1475), [#1462](https://github.com/betagouv/csplab/issues/1462).
    - Optimisations visuelles : en-tête de page fixe (sticky), harmonisation des composants et alignement des données dans les tableaux [#1892](https://github.com/betagouv/csplab/issues/1892), [#1575](https://github.com/betagouv/csplab/issues/1575), [#1857](https://github.com/betagouv/csplab/issues/1857).
- **Ingestion de données** : 
    - Enrichissement des données importées depuis Talentsoft (emails des candidats, contacts de l'offre, dates de vacance de poste) [#1946](https://github.com/betagouv/csplab/issues/1946), [#1936](https://github.com/betagouv/csplab/issues/1936), [#1812](https://github.com/betagouv/csplab/issues/1812).
    - Francisation des champs et des réponses de l'API d'ingestion pour une meilleure lisibilité [#1852](https://github.com/betagouv/csplab/issues/1852), [#1847](https://github.com/betagouv/csplab/issues/1847).

### Évolutions techniques
- **Architecture (ADR-009)** : Refonte majeure de plusieurs services clés (identité, recrutement, organismes) pour s'aligner sur le nouveau standard architectural du projet [#1877](https://github.com/betagouv/csplab/issues/1877), [#1940](https://github.com/betagouv/csplab/issues/1940), [#1916](https://github.com/betagouv/csplab/issues/1916), [#1808](https://github.com/betagouv/csplab/issues/1808).
- **Sécurité & Identité** : 
    - Renforcement de la protection contre les abus via la limitation du débit (rate limiting) sur les requêtes anonymes et les clés d'API [#1964](https://github.com/betagouv/csplab/issues/1964), [#1807](https://github.com/betagouv/csplab/issues/1807).
    - Amélioration de la traçabilité avec le log des tentatives de connexion et de la création de profils [#1660](https://github.com/betagouv/csplab/issues/1660), [#1641](https://github.com/betagouv/csplab/issues/1641).
- **Infrastructure & Stockage** : 
    - Mise en place du stockage objet S3 pour la gestion des documents et fichiers des candidats [#1472](https://github.com/betagouv/csplab/issues/1472).
    - Optimisation du processus d'ingestion (gestion optionnelle de Qdrant, pagination des API, fiabilisation de l'archivage) [#1955](https://github.com/betagouv/csplab/issues/1955), [#1967](https://github.com/betagouv/csplab/issues/1967).

### Autres changements
- **Documentation** : 
    - Ajout de pages d'aide et de contact dans la documentation de l'API [#1920](https://github.com/betagouv/csplab/issues/1920).
    - Mise à jour des guides de correspondance technique pour l'ingestion des données Talentsoft [#1789](https://github.com/betagouv/csplab/issues/1789).
- **Tooling** : Modernisation de la chaîne de développement avec le remplacement de `pre-commit` par `hk` [#1654](https://github.com/betagouv/csplab/issues/1654).

## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 13 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'enrichissement de l'API avec des informations sur les services numériques de la transition écologique, l'amélioration de l'intégration avec la plateforme "Mon Éco Condition" (MEC) et des corrections de bugs pour stabiliser les tests et les performances. Le tableau de bord de la transition écologique (TE) a également été amélioré avec de nouveaux filtres et des informations plus détaillées sur les projets.

### Évolutions fonctionnelles
- Ajout de logos pour les services numériques via l'API. [#507](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/507)
- Génération automatique de descriptions et de classifications pour les services numériques.
- Intégration des questionnaires, recommandations et catalogue de services numériques dans l'API.
- Amélioration de la prédiction des leviers pour les projets MEC.
- Ajout d'endpoints pour exposer les sites, interventions et leviers MEC via l'API de qualification.
- Ajout de filtres multi-valeurs pour les départements, les sources et les EPCI dans le tableau de bord TE.
- Classification scorée des projets dans le détail du tableau de bord TE.
- Possibilité de filtrer les projets par EPCI dans le tableau de bord TE.
- Ajout d'un verdict "annulé" pour révoquer les décisions dans le contrat de décisions v2.
- Schéma `decisions_humaines` pour journaliser les décisions humaines.

### Évolutions techniques
- Refonte de la documentation d'intégration MEC.
- Implémentation d'une doctrine d'accès aux données (data_scopes) pour une meilleure gestion des permissions.
- Ajout d'un endpoint miroir pour les plans territoriaux (sens TeT).
- Amélioration de la gestion des erreurs Undici et stabilisation des tests.
- Configuration d'un limiteur de débit (throttler) configurable pour la suite de tests e2e.
- Correction de problèmes liés à la surcharge de l'ingestion de données par les partenaires.
- Amélioration de la gestion des erreurs d'assertion non rattrapées.
- Optimisation des tests e2e pour éviter les courses inter-suites.

### Autres changements
- Documentation de la provenance des leviers et de la limite v1 pour l'intégration MEC.
- Signalement de la clé `nom_propre` possible sur `llmSites`.
- Clarification de la portée des filtres et du sens du total dans la documentation.
- Suppression de `dataScopes` de l'attente du create de service context.
- Correction des attentes des specs services après l'ajout de `data_scopes`.
- Formattage du fichier `dashboard-te.service.ts` avec Prettier.
- Ajout d'IDs des traces DGCL non contractuels pour l'intégration MEC.
- Publication des versions 0.1.96 à 0.1.103.

## Changelog : autometa (30 derniers jours, au 30/09/2026)

### Résumé
Autometa a considérablement élargi ses capacités d'analyse et de connexion. Ce mois-ci, l'outil intègre de nouvelles sources de données (Datadog, Mon Récap), renforce ses capacités statistiques grâce à l'ajout de modèles bayésiens, et améliore l'expérience utilisateur avec un système de notifications plus complet et une interface de gestion des sources de données simplifiée.

### Évolutions fonctionnelles
- **Nouvelles sources de données** : Intégration de Datadog [#211](https://github.com/gip-inclusion/autometa/issues/211) et [#223](https://github.com/gip-inclusion/autometa/issues/223), de l'application Mon Récap [#239](https://github.com/gip-inclusion/autometa/issues/239), et support de la source raw_rdvi [#229](https://github.com/gip-inclusion/autometa/issues/229).
- **Capacités d'analyse statistique** : Ajout d'un arsenal de statistiques fréquentistes et bayésiennes (via `statsmodels`, `bambi` et `pymc-marketing`) pour permettre des analyses de marché et des modélisations plus complexes [#222](https://github.com/gip-inclusion/autometa/issues/222) [#212](https://github.com/gip-inclusion/autometa/issues/212).
- **Amélioration de l'expérience utilisateur (UX/UI)** :
    - Création d'une page dédiée à la gestion des sources de données [#201](https://github.com/gip-inclusion/autometa/issues/201).
    - Affichage des filtres sur les vues de tableaux de bord (TDB) publiés [#210](https://github.com/gip-inclusion/autometa/issues/210).
    - Système de notifications enrichi (alertes de fin de traitement, échecs, et changements d'état) avec indicateurs visuels (favicon) et sonores.
    - Possibilité de modifier les tableaux de bord d'autres utilisateurs, avec un système de confirmation et d'avertissement [#241](https://github.com/gip-inclusion/autometa/issues/241).
    - Meilleure clarté sur les erreurs rencontrées par les tâches automatisées (crons) [#214](https://github.com/gip-inclusion/autometa/issues/214).
- **Gestion de contenu** : Possibilité de modifier la base de connaissance Zendesk directement depuis l'interface Autometa [#220](https://github.com/gip-inclusion/autometa/issues/220).

### Évolutions techniques
- **Résilience et Intelligence Artificielle** : 
    - Mise en place d'un basculement automatique vers d'autres moteurs d'IA en cas d'épuisement des quotas Claude [#218](https://github.com/gip-inclusion/autometa/issues/218).
    - Réduction des risques d'hallucination sur les sources de données [#227](https://github.com/gip-inclusion/autometa/issues/227).
- **Performance et Stabilité** :
    - Accélération du chargement des pages de tableaux de bord et des tâches cron [#207](https://github.com/gip-inclusion/autometa/issues/207).
    - Sécurisation des appels vers les services externes pour éviter le blocage des workers web en cas d'indisponibilité [#215](https://github.com/gip-inclusion/autometa/issues/215).
    - Migration du stockage de MinIO vers RustFS [#242](https://github.com/gip-inclusion/autometa/issues/242).
- **Infrastructure et Automatisation** :
    - Mise en place d'un processus nocturne pour la mise à jour automatique des embeddings des conversations [#184](https://github.com/gip-inclusion/autometa/issues/184).
    - Optimisations du pipeline CI/CD, de la gestion des images Docker et des déploiements [#226](https://github.com/gip-inclusion/autometa/issues/226) [#216](https://github.com/gip-inclusion/autometa/issues/216) [#204](https://github.com/gip-inclusion/autometa/issues/204).
- **Qualité logicielle** : Amélioration de l'indépendance des tests de configuration Ollama [#233](https://github.com/gip-inclusion/autometa/issues/233) et optimisation du linting [#221](https://github.com/gip-inclusion/autometa/issues/221).

### Autres changements
- Mise à jour de l'URL Matomo pour le site "Les emplois de l'inclusion" [#231](https://github.com/gip-inclusion/autometa/issues/231).
- Correction de la synchronisation des webinaires (Grist) en cas d'absence d'ID d'événement [#240](https://github.com/gip-inclusion/autometa/issues/240).

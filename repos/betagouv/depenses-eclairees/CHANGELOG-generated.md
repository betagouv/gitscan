## Changelog : depenses-eclairees (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'extraction d'informations des documents financiers (avenants, DC4, etc.) grâce à des ajustements des prompts d'IA, l'ajout de post-traitements pour une meilleure qualité des données, et l'amélioration de la robustesse de l'application. Des améliorations significatives ont également été apportées à la gestion des engagements et à la pipeline de synthèse des données.

### Évolutions fonctionnelles
- **Avenants :** Ajout d'un front-end pour la gestion des avenants [#132](https://github.com/betagouv/depenses-eclairees/issues/132). Amélioration de l'extraction et du post-traitement des informations des avenants, incluant la normalisation des booléens et l'enrichissement des données extraites [#131](https://github.com/betagouv/depenses-eclairees/issues/131), [#126](https://github.com/betagouv/depenses-eclairees/issues/126).
- **RIB :** Prise en compte des IBAN étrangers dans le post-traitement des RIB [#139](https://github.com/betagouv/depenses-eclairees/issues/139). Amélioration de la logique de post-traitement des RIB et conservation du numéro de compte [#129](https://github.com/betagouv/depenses-eclairees/issues/129), [#127](https://github.com/betagouv/depenses-eclairees/issues/127).
- **Engagements :** Refactorisation des modèles de données pour les engagements (DataEngagement -> Engagement, DataBatch -> EngagementTag) [#122](https://github.com/betagouv/depenses-eclairees/issues/122). Ajout du champ `external_created_at` pour une meilleure synchronisation des données [#133](https://github.com/betagouv/depenses-eclairees/issues/133).
- **Synthèse :** Implémentation d'une pipeline de synthèse des données avec un script d'exécution de bout en bout [#106](https://github.com/betagouv/depenses-eclairees/issues/106). Ajout de fonctions de test pour la synthèse.
- **DC4 :** Amélioration de la précision du prompt pour l'extraction de la date de dernière signature. Correction du schéma DC4 [#125](https://github.com/betagouv/depenses-eclairees/issues/125).

### Évolutions techniques
- **Qualité des données :** Ajout de fonctions pour lister les erreurs par type (faux positifs, faux négatifs) et intégration dans les tests E2E [#124](https://github.com/betagouv/depenses-eclairees/issues/124), [#123](https://github.com/betagouv/depenses-eclairees/issues/123).
- **Monitoring :** Ajout de métriques pour le comptage des tokens et la date de traitement [#128](https://github.com/betagouv/depenses-eclairees/issues/128).
- **Robustesse :** Gestion des erreurs de décodage JSON dans le client LLM avec une logique de retry [#123](https://github.com/betagouv/depenses-eclairees/issues/123).
- **Schémas :** Refactorisation de la définition des schémas de données [#120](https://github.com/betagouv/depenses-eclairees/issues/120).
- **Prompt Engineering :** Refactorisation des prompts pour les champs communs entre différents types de documents (AE, CCAP, DC4, Devis) [#130](https://github.com/betagouv/depenses-eclairees/issues/130), [#126](https://github.com/betagouv/depenses-eclairees/issues/126).

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Suppression de tests redondants.
- Paramétrage JSON strict [#121](https://github.com/betagouv/depenses-eclairees/issues/121).
- Corrections mineures et ajustements divers.

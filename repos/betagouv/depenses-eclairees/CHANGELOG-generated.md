## Changelog : depenses-eclairees (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'extraction et le post-traitement des données financières, notamment pour les avenants, les RIB et les contrats. Des efforts ont été faits pour améliorer la qualité des données extraites grâce à des ajustements des prompts d'IA et l'ajout de règles de post-traitement. L'infrastructure et les tests ont également été renforcés.

### Évolutions fonctionnelles
- **Avenants :** Ajout d'une interface utilisateur pour la gestion des avenants et amélioration de l'extraction des informations ([#132](https://github.com/betagouv/depenses-eclairees/issues/132), [#131](https://github.com/betagouv/depenses-eclairees/issues/131), [#127](https://github.com/betagouv/depenses-eclairees/issues/127)).
- **RIB :** Prise en charge des IBAN étrangers et amélioration du post-traitement des informations bancaires ([#139](https://github.com/betagouv/depenses-eclairees/issues/139)).
- **Contrats :** Amélioration de l'extraction des informations des contrats (CCAP, devis, etc.) et ajout de règles de post-traitement pour les noms de sociétés.
- **Synthèse :** Implémentation d'un pipeline de synthèse pour extraire des informations à partir des pièces jointes ([#106](https://github.com/betagouv/depenses-eclairees/issues/106)).
- **Dates :** Amélioration de la gestion et de la propagation des dates, notamment pour les engagements ([#136](https://github.com/betagouv/depenses-eclairees/issues/136), [#138](https://github.com/betagouv/depenses-eclairees/issues/138)).
- **Champs :** Augmentation de la longueur maximale des champs de formulaire pour éviter les erreurs de validation ([#135](https://github.com/betagouv/depenses-eclairees/issues/135)).

### Évolutions techniques
- **Modèles de données :** Renommage des modèles `DataEngagement` et `DataBatch` en `Engagement` et `EngagementTag` pour une meilleure clarté ([#122](https://github.com/betagouv/depenses-eclairees/issues/122)).
- **Gestion des erreurs :** Ajout d'une logique de nouvelle tentative pour gérer les erreurs de décodage JSON dans le client LLM ([#123](https://github.com/betagouv/depenses-eclairees/issues/123)).
- **Schémas :** Refonte de la définition des schémas de données pour une meilleure organisation et maintenabilité ([#120](https://github.com/betagouv/depenses-eclairees/issues/120)).
- **Métriques :** Ajout de métriques pour suivre le nombre de tokens utilisés et la date de traitement ([#128](https://github.com/betagouv/depenses-eclairees/issues/128)).
- **Tests :** Ajout de fonctions de test et d'un script d'exécution de bout en bout pour vérifier la qualité des données extraites.
- **Sécurité :** Ajout d'en-têtes transférés et de paramètres de sécurité pour une meilleure protection.

### Autres changements
- **Documentation :** Clarification des règles d'extraction dans le code.
- **Prompts IA :** Amélioration des prompts utilisés pour l'extraction d'informations par l'IA pour différents types de documents (AE, CCAP, DC4, devis).
- **Post-traitement :** Ajout de règles de post-traitement pour améliorer la qualité des données extraites (noms de sociétés, numéros de compte).
- **Configuration :** Ajout d'un paramètre pour activer le mode JSON strict.
- **Correction :** Correction de bugs et d'incohérences dans le code.

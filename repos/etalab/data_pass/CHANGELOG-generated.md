## Changelog : data_pass (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois a été marqué par une extension significative des services pour le secteur de la petite enfance (EAJE) et une refonte majeure de la gestion des données INSEE pour garantir une meilleure stabilité. Les processus de demande pour les API Entreprise et Particulier ont également été simplifiés et enrichis de nouveaux éditeurs.

### Évolutions fonctionnelles
- **Parcours EAJE (Petite Enfance) :** Intégration complète du parcours, incluant de nouvelles options de préfiltrage, la gestion de nouveaux éditeurs (CapCreche, Osmia Projects, optiCreche, etc.) et l'ajustement des paliers de volumétrie FICOBA [#1720](https://github.com/etalab/data_pass/issues/1720) [#1777](https://github.com/etalab/data_pass/issues/1777) [#1779](https://github.com/etalab/data_pass/issues/1779).
- **Gestion des API :** 
    - Ajout de nouveaux éditeurs pour l'API Particulier [#1796](https://github.com/etalab/data_pass/issues/1796).
    - Simplification des demandes pour l'API Entreprise avec la suppression de l'obligation de renseigner un responsable de traitement [#1764](https://github.com/etalab/data_pass/issues/1764).
- **Notifications et Information :** 
    - Information des demandeurs sur la durée de disponibilité des données [#1798](https://github.com/etalab/data_pass/issues/1798).
    - Automatisation des notifications vers le support HubEE lors de la validation de certaines demandes (FQF, DataPass) [#1766](https://github.com/etalab/data_pass/issues/1766).
- **Améliorations de l'interface :** Correction de bugs d'affichage sur les modèles de messages [#1800](https://github.com/etalab/data_pass/issues/1800), personnalisation des titres de pages selon l'API et corrections de diverses coquilles textuelles.

### Évolutions techniques
- **Fiabilisation de la synchronisation INSEE :** Refonte complète de l'intégration pour éviter les échecs de service. Mise en place d'une file d'attente dédiée, d'un mécanisme de "circuit breaker" (coupe-circuit), d'une gestion optimisée du débit (250 appels/min) et d'une meilleure gestion des jetons d'authentification [#1771](https://github.com/etalab/data_pass/issues/1771) [#1772](https://github.com/etalab/data_pass/issues/1772) [#1773](https://github.com/etalab/data_pass/issues/1773) [#1774](https://github.com/etalab/data_pass/issues/1774) [#1789](https://github.com/etalab/data_pass/issues/1789) [#1791](https://github.com/etalab/data_pass/issues/1791).
- **Sécurité et Authentification :** 
    - Sécurisation de la connexion pour éviter l'écrasement accidentel des informations de compte par des valeurs vides.
    - Amélioration de la validation des adresses IP publiques.
    - Attribution automatique du scope `read_webhooks` pour les nouvelles clés API.
- **Infrastructure et CI/CD :** Optimisation des cibles de déploiement dans les workflows GitHub Actions [#1778](https://github.com/etalab/data_pass/issues/1778).

### Autres changements
- **Documentation :** Mise à jour de la documentation concernant la synchronisation des profils à la connexion et les prévisualisations du catalogue Lookbook.
- **Nettoyage :** Suppression de l'ancien plan DataGouv et vérification de l'absence de doublons dans les formulaires.

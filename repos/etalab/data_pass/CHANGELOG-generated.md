## Changelog : data_pass (30 derniers jours, au 12 octobre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la fiabilité des synchronisations de données (notamment avec l'INSEE) et par le déploiement de nouveaux parcours utilisateurs, particulièrement pour le secteur de la petite enfance (EAJE). L'outil est également devenu plus transparent sur ses processus de contribution et sur ses engagements en matière d'accessibilité.

### Évolutions fonctionnelles
- **Parcours EAJE (Petite enfance) :** Intégration de nouvelles options de préfiltrage, ajout de nouveaux éditeurs référencés (CapCreche, Osmia Projects, optiCreche) et personnalisation de l'affichage des formulaires.
- **Gestion des éditeurs et API :** 
    - Référencement de nouveaux éditeurs pour l'API Particulier [#1796](https://github.com/etalab/data_pass/issues/1796).
    - Simplification des demandes API Entreprise par la suppression du champ "responsable de traitement".
- **Expérience utilisateur et interface :**
    - Renommage du "contact technique" en "RSSI" dans les formulaires pour plus de clarté [#1802](https://github.com/etalab/data_pass/issues/1802).
    - Correction de l'invisibilité de certains documents après sauvegarde [#1801](https://github.com/etalab/data_pass/issues/1801).
    - Amélioration de la gestion des erreurs sur les modèles de messages [#1800](https://github.com/etalab/data_pass/issues/1800).
    - Information des demandeurs sur la durée de disponibilité des services [#1798](https://github.com/etalab/data_pass/issues/1798).
- **Données :** Activation des bilans BDF et des liasses fiscales sur l'ADE aides publiques.

### Évolutions techniques
- **Fiabilisation de l'intégration INSEE :** Refonte majeure de la synchronisation pour augmenter la résilience : mise en place d'un circuit breaker (coupe-circuit), utilisation d'une file d'attente dédiée, gestion optimisée des limites de débit (250 appels/min) et meilleure gestion des erreurs en cas d'indisponibilité du service [#1771](https://github.com/etalab/data_pass/issues/1771), [#1772](https://github.com/etalab/data_pass/issues/1772), [#1773](https://github.com/etalab/data_pass/issues/1773), [#1774](https://github.com/etalab/data_pass/issues/1774).
- **Optimisation des tests :** Refonte complète et optimisation du système de génération de données de test (*seeds*) pour améliorer la performance et la couverture des tests [#1793](https://github.com/etalab/data_pass/issues/1793).
- **Audit et traçabilité :** Amélioration du suivi des modifications (ajout de champs ou de documents) pour mieux identifier les changements lors de la réouverture d'une demande.
- **Sécurité :** Renforcement de la validation des étapes mémorisées en cookies et des adresses IP publiques.
- **Correction de bugs :** Empêche l'annulation d'une étape de production sans avoir préalablement validé l'étape "bac à sable" [#1804](https://github.com/etalab/data_pass/issues/1804).

### Autres changements
- **Documentation :** Formalisation des règles de contribution technique pour l'équipe [#1787](https://github.com/etalab/data_pass/issues/1787).
- **Accessibilité :** Publication du plan d'action d'accessibilité du service.

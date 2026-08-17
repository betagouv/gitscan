## Changelog : doctorat-gouv (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois a été marqué par l'intégration majeure du flux EURAXESS. Cette évolution permet à la plateforme de diffuser automatiquement les offres de thèse vers ce réseau international via un flux XML standardisé, tout en garantissant la sécurité et la fiabilité des données transmises.

### Évolutions fonctionnelles
- **Exportation vers EURAXESS** : Mise en place de la génération et de la publication automatique des offres de thèse au format XML pour la plateforme EURAXESS.
- **Accessibilité du flux** : Mise à disposition d'un point d'accès public sécurisé pour permettre la consultation des offres par les services tiers.

### Évolutions techniques
- **Moteur de génération XML** : Implémentation de la technologie JAXB et intégration du schéma XSD officiel pour garantir la conformité du flux EURAXESS.
- **Sécurisation** : Protection du flux de données via l'utilisation d'une clé API dédiée.
- **Fiabilité et robustesse** :
    - Correction de la conversion des dates pour assurer la compatibilité avec le format XML.
    - Amélioration de la gestion des cas particuliers (réponse HTTP 204 en cas d'absence d'offres et logs d'alerte en cas de flux vide).
- **Qualité et tests** :
    - Ajout de tests d'intégration complets (services et contrôleurs).
    - Mise en place de tests de validation de schéma (XSD) et de mapping des données.
    - Configuration d'une base de données H2 pour les environnements de test.

### Autres changements
- **Maintenance** : Préparation et mise à jour des versions pour la release 0.3.9.

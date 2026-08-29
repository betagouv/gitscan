## Changelog : doctorat-gouv (30 derniers jours, au 14 août 2026)

### Résumé
Le développement récent a été quasi exclusivement consacré à l'intégration du flux international EURAXESS. La plateforme est désormais capable de générer et d'exporter automatiquement les offres de thèse au format XML requis, tout en sécurisant cet accès pour les partenaires externes.

### Évolutions fonctionnelles
- **Exportation internationale** : Mise en place de la génération automatique du flux XML pour les offres de thèse vers le réseau EURAXESS.
- **Accessibilité du flux** : Création d'un point d'accès public permettant la consultation des offres via un endpoint dédié.

### Évolutions techniques
- **Moteur d'intégration EURAXESS** :
    - Implémentation de la génération de flux XML via JAXB et intégration du schéma de données officiel.
    - Développement du moteur de mapping pour la conversion des offres de thèse vers le format EURAXESS.
    - Sécurisation de l'endpoint de flux par une clé API dédiée.
    - Optimisation de la gestion des réponses (retour d'un code 204 en cas d'absence d'offres) et ajout de logs de suivi pour les flux vides.
    - Correction de la gestion des formats de date pour assurer la conformité avec les standards XML.
- **Qualité et tests** :
    - Ajout de tests d'intégration pour les services et contrôleurs EURAXESS.
    - Mise en place de la validation automatique des schémas (XSD) et des mappings de données.
    - Configuration d'un environnement de test avec une base de données H2.

### Autres changements
- **Gestion des versions** : Préparation et déploiement de la version 0.3.9 via les pull requests [#51](https://github.com/betagouv/doctorat-gouv/pull/51), [#52](https://github.com/betagouv/doctorat-gouv/pull/52) et [#53](https://github.com/betagouv/doctorat-gouv/pull/53).

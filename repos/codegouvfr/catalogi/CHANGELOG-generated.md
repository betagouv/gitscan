## Changelog : catalogi (30 derniers jours, au 19 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement des outils d'administration et l'optimisation de l'importation de données. L'interface utilisateur est désormais plus flexible grâce à une nouvelle gestion de sa configuration, tandis que la fiabilité des données importées (HAL, Wikidata, GitHub) et la documentation de l'API ont été significativement améliorées.

### Évolutions fonctionnelles
- **Administration** : Introduction d'un éditeur de configuration de l'interface utilisateur (UI) via l'API d'administration, permettant de modifier l'apparence et le comportement de l'interface directement depuis la base de données.
- **Administration** : Ajout d'un raccourci pour la création de logiciels et mise en place de restrictions d'accès à cette fonctionnalité.
- **API** : Mise à disposition d'une documentation interactive (Swagger UI) pour l'export public v2, facilitant l'intégration par des tiers.
- **Données** : Ajout de la mention de la date de dernière importation sur les sources de données.

### Évolutions techniques
- **Optimisation des imports** : Amélioration des performances pour les imports massifs, notamment pour les données Zenodo et via une optimisation globale des processus ([#516](https://github.com/codegouvfr/catalogi/issues/516)).
- **Fiabilisation de l'ingestion de données** : Correction de nombreux bugs lors de l'importation de données externes (HAL, Wikidata, GitHub) concernant la gestion des identifiants, des organisations et des URLs ROR.
- **API & Sécurité** :
    - Correction du préfixe de documentation lors de l'utilisation de proxys.
    - Sécurisation des URLs pour empêcher la déclaration d'URLs exécutables ou d'instances non autorisées.
    - Refactorisation pour assurer la stricte conformité des schémas publics avec les types de logiciels originaux.
- **Tests** : Amélioration de la robustesse des tests unitaires sur les schémas générés et la gestion des données de test pour la configuration de l'UI.

### Autres changements
- Maintenance technique : Correction du nom du build, réorganisation des migrations de base de données et mises à jour de version.

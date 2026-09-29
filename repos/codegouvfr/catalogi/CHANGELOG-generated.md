## Changelog : catalogi (30 derniers jours, au 25 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'ergonomie de l'interface et la simplification de la gestion des données. L'ajout de nouvelles commandes en ligne de commande facilite l'importation de références, tandis que la documentation de l'API a été renforcée pour offrir une meilleure visibilité aux développeurs utilisant les exports de données.

### Évolutions fonctionnelles
- **Interface utilisateur** : l'écran d'accueil est désormais plus épuré lorsqu'aucun cas d'usage n'est défini et le logo a été corrigé.
- **Outils en ligne de commande (CLI)** : ajout de fonctionnalités permettant d'importer et de mettre à jour des références via la ligne de commande [#577](https://github.com/codegouvfr/catalogi/issues/577).
- **Documentation API** : mise à disposition d'une interface Swagger UI autonome pour documenter l'export public v2.

### Évolutions techniques
- **API & Logique métier** :
  - Correction du mécanisme de résolution des identifiants de projet GitLab [#575](https://github.com/codegouvfr/catalogi/issues/575).
  - Amélioration de la gestion des préfixes de documentation lors de l'utilisation de proxys.
  - Renforcement de la validation du schéma public par rapport aux types de logiciels originaux.
  - Sécurisation pour empêcher les déclarations exécutables et les URLs d'instance.
- **Tests & Qualité** :
  - Optimisation de la suite de tests de l'API, notamment la vérification des schémas générés sans nécessiter de serveur HTTP.
  - Amélioration de la gestion et de l'isolation des données de test (fixtures) pour la configuration de l'interface et le catalogue public.

### Autres changements
- Correction de la configuration de build concernant le nom du projet.

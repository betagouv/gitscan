## Changelog : docs (30 derniers jours, au 14 août 2026)

### Résumé
Les récentes mises à jour améliorent l'expérience de présentation, permettant notamment de lancer des présentations directement depuis un bloc ou une diapositive spécifique. Le projet a également bénéficié d'une consolidation technique majeure, incluant la montée de version de l'infrastructure et l'optimisation des outils de développement et de qualité de code.

### Évolutions fonctionnelles
- ✨ Amélioration des fonctionnalités de présentation : possibilité de lancer une présentation depuis un bloc spécifique et de partager des liens pointant vers une diapositive précise.
- ✨ Ajout de notifications par email conditionnelles pour l'API serveur à serveur.
- 💄 Harmonisation visuelle des couleurs de mise en évidence pour les cellules et les déplacements.
- 🐛 Correction de la gestion des épingles (pins) lors de la suppression et de la restauration de documents.
- 🐛 Correction de l'export d'images utilisant des URLs relatives.

### Évolutions techniques
- 🏗️ Mise à jour de l'infrastructure : passage à Python 3.14 dans Docker et amélioration de la gestion des erreurs de base de données dans les déploiements Helm.
- ⚙️ Optimisation du backend : gestion insensible à la casse des métadonnées de stockage d'objets et refactorisation des dépendances (pydantic-ai).
- ⚙️ Qualité de code : mise à jour des outils de linting (Ruff 0.16, Pylint 4.0.6) et stabilisation des tests E2E sur les langues.
- 🔒 Sécurité et configuration : correction des variables d'environnement pour Keycloak en auto-hébergement et résolution d'avertissements de sécurité JavaScript.
- 🛠️ Adaptation du frontend au kit UI v0.28.

### Autres changements
- 📝 Mise à jour de la documentation du README [#2508](https://github.com/suitenumerique/docs/issues/2508).

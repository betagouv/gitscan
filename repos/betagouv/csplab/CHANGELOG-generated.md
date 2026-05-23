## Changelog : csplab (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion de données, notamment avec l'ajout de la gestion des webhooks TalentSoft et l'archivage des offres. L'interface utilisateur a également été enrichie avec l'ajout de pages statiques (mentions légales, confidentialité, accessibilité) et l'amélioration de l'affichage des informations sur les offres et les CV. Des optimisations et des corrections de bugs ont été apportées à l'ensemble du projet.

### Évolutions fonctionnelles
- Ajout de la gestion des webhooks TalentSoft pour l'ingestion d'offres d'emploi [#500](https://github.com/betagouv/csplab/issues/500).
- Implémentation de l'archivage des offres [#455](https://github.com/betagouv/csplab/issues/455).
- Ajout d'une entité "Source" et d'une API pour lister les sources de données [#574](https://github.com/betagouv/csplab/issues/574).
- Affichage de l'organisation ou du ministère sur les cartes et dans les détails des offres [#443](https://github.com/betagouv/csplab/issues/443).
- Ajout de pages statiques pour les mentions légales, la politique de confidentialité et l'accessibilité [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#227](https://github.com/betagouv/csplab/issues/227).
- Amélioration de l'affichage du CV dans l'interface utilisateur [#441](https://github.com/betagouv/csplab/issues/441).
- Possibilité de fermer le tiroir modal depuis la navigation du navigateur [#444](https://github.com/betagouv/csplab/issues/444).
- Ajout de la vectorisation pour les métiers [#551](https://github.com/betagouv/csplab/issues/551).
- Ajout d'un usecase pour récupérer le détail d'une opportunité avec les métiers associés [#487](https://github.com/betagouv/csplab/issues/487).

### Évolutions techniques
- Refactor de l'archive offer pour utiliser les paramètres du corps de la requête et des noms en français [#580](https://github.com/betagouv/csplab/issues/580).
- Mise en place d'un mécanisme de logging [#578](https://github.com/betagouv/csplab/issues/578).
- Standardisation des noms de méthodes pour la récupération de données (get\_xxxx) [#568](https://github.com/betagouv/csplab/issues/568).
- Amélioration de la robustesse du mapping des ministères [#548](https://github.com/betagouv/csplab/issues/548).
- Mise à jour des dépendances pour `web` et `ingestion` [#571](https://github.com/betagouv/csplab/issues/571), [#570](https://github.com/betagouv/csplab/issues/570).
- Utilisation de `python-dateutil` pour la gestion des dates relatives dans l'archivage des offres [#477](https://github.com/betagouv/csplab/issues/477).
- Suppression de code inutilisé et refactoring de la configuration [#459](https://github.com/betagouv/csplab/issues/459).
- Amélioration de la gestion des erreurs dans l'ingestion pour éviter le blocage du processus [#509](https://github.com/betagouv/csplab/issues/509).
- Refactor de l'implémentation des tests et ajout de tests E2E avec Playwright [#490](https://github.com/betagouv/csplab/issues/490), [#460](https://github.com/betagouv/csplab/issues/460), [#461](https://github.com/betagouv/csplab/issues/461), [#462](https://github.com/betagouv/csplab/issues/462), [#463](https://github.com/betagouv/csplab/issues/463).
- Mise en place de la documentation de l'API [#396](https://github.com/betagouv/csplab/issues/396).

### Autres changements
- Ajout de Git hooks pour l'application des règles de qualité du code [#472](https://github.com/betagouv/csplab/issues/472).
- Mise à jour du CHANGELOG pour la version 0.1.8 et 0.1.9 [#485](https://github.com/betagouv/csplab/issues/485).
- Amélioration de la documentation pour les commandes de chargement [#481](https://github.com/betagouv/csplab/issues/481).
- Correction de la configuration de la version de Python [#501](https://github.com/betagouv/csplab/issues/501).
- Ajout de tests de couverture et parallélisation des tests E2E [#494](https://github.com/betagouv/csplab/issues/494).
- Correction de problèmes liés aux caractères non encodés dans les signatures [#506](https://github.com/betagouv/csplab/issues/506).
- Correction de la lecture des délais d'expiration dans les en-têtes de requête [#505](https://github.com/betagouv/csplab/issues/505).
- Ajout de la documentation pour les webhooks TalentSoft [#503](https://github.com/betagouv/csplab/issues/503).
- Ajout d'un mécanisme pour éviter que les documents en échec restent en attente [#452](https://github.com/betagouv/csplab/issues/452).
- Amélioration du logging avec l'utilisation d'interpolation de chaînes paresseuses [#412](https://github.com/betagouv/csplab/issues/412).
- Correction du chemin de génération du schéma en CI [#581](https://github.com/betagouv/csplab/issues/581).
- Exécution de `djlint` dans la CI [#584](https://github.com/betagouv/csplab/issues/584).
- Ajout d'un test pour vérifier que les filtres actifs sont bien reflétés dans l'interface utilisateur [#380](https://github.com/betagouv/csplab/issues/380).
- Suppression de la fonctionnalité de recherche de corps de métiers obsolète [#437](https://github.com/betagouv/csplab/issues/437).
- Correction d'un bug lié au chemin de l'interpréteur Python dans VSCode [#439](https://github.com/betagouv/csplab/issues/439).
- Mise à jour des dépendances pour les notebooks, l'OCR et Tycho [#497](https://github.com/betagouv/csplab/issues/497), [#496](https://github.com/betagouv/csplab/issues/496), [#495](https://github.com/betagouv/csplab/issues/495).

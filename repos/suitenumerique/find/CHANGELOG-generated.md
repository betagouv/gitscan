## Changelog : find (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une phase de nettoyage et de refonte technique importante. Des fonctionnalités expérimentales comme la recherche hybride et l'application d'évaluation ont été supprimées pour se concentrer sur la recherche BM25. L'infrastructure a été modernisée avec des mises à jour de dépendances et l'ajout d'outils d'analyse de code pour améliorer la qualité du code.

### Évolutions fonctionnelles
- Suppression de la recherche par embedding/hybride, maintenant uniquement la recherche BM25 est disponible.
- Suppression de l'application d'évaluation.

### Évolutions techniques
- Mise à jour de Pydantic vers la version 2.13.4.
- Mise à jour de Redis vers la version 6.
- Mise à jour de Django vers la version 6.0.5 (incluant des correctifs de sécurité).
- Mise à jour de plusieurs dépendances (OpenSearch-py, drf-spectacular-sidecar, psycopg, etc.).
- Suppression du code mort identifié par l'outil Vulture.
- Suppression d'un service Docker inutilisé.
- Ajout de hooks pre-commit pour améliorer la qualité du code.
- Simplification du fichier CHANGELOG.md pour la publication initiale.
- Autorisation de l'utilisation de constantes en majuscules pour les paramètres Django dans Pylint.
- Unification des indices de recherche avec la portée du service.
- Renforcement des assertions de tests pour plus de clarté.

### Autres changements
- Suppression des dépendances inutilisées url-normalize et factory_boy.
- Correction de fautes de frappe dans la documentation.
- Epinglage des dépendances pour une meilleure stabilité.
- Séparation des Pull Requests de dépendances Python.
- Mises à jour de sécurité pour Django, Requests, PyJWT, pytest et langchain-text-splitters.

## Changelog : agreste-crawler (30 derniers jours, au 30 mars 2026)

### Résumé
Ce mois-ci, le projet agreste-crawler a connu une évolution majeure avec l'implémentation d'un nouveau crawler basé sur Playwright, permettant une navigation plus robuste et l'interaction avec des pages web dynamiques.  De nombreuses améliorations ont été apportées pour l'extraction et la gestion de documents, incluant la lecture de fichiers associés, l'ajout de métadonnées et la création d'une structure de blog pour les présenter. L'accent a été mis sur la robustesse du processus d'extraction et la gestion des erreurs.

### Évolutions fonctionnelles
- Implémentation d'un nouveau crawler basé sur Playwright pour une meilleure interaction avec les pages web et la possibilité de cliquer sur des liens pour trouver des données. [#1](https://github.com/betagouv/agreste-crawler/pull/1)
- Ajout de la possibilité de spécifier des champs à extraire via des flags, permettant une extraction plus ciblée des données.
- Ajout de la possibilité de lire les informations à partir d'un fichier CSV contenant une liste d'URLs.
- Création d'un script pour préfixer les noms de fichiers avec un identifiant Disaron.
- Mise en place d'un système de "sanity checks" pour valider l'intégrité des données extraites et identifier les erreurs.
- Ajout de la possibilité de télécharger des documents associés aux pages web et de les intégrer dans un blog.
- Création d'un script pour effacer les entrées du blog existantes.
- Ajout de champs pour les thèmes, les années de référence et le niveau géographique.
- Génération automatique de slugs pour les pages.

### Évolutions techniques
- Refonte du processus d'extraction pour utiliser un format de fichier d'entrée plus simple (une URL par ligne).
- Amélioration de la gestion des erreurs avec l'ajout de retries en cas d'échec de chargement d'une page.
- Amélioration de la journalisation (logging) pour faciliter le débogage et le suivi de l'exécution du crawler.
- Conversion du contenu extrait en Markdown grâce à l'utilisation de la librairie markitdown.
- Modification de l'architecture pour séparer la configuration Django et le setup.
- Ajout d'un flag `--scalingo-env` pour configurer l'environnement Scalingo.

### Autres changements
- Ajout de fichiers de données de test pour faciliter le développement et les tests.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
- Organisation des fichiers de résultats et ajout d'un fichier `.gitignore` pour exclure les fichiers temporaires.
- Ajout d'un flag `--no-concurrency` pour désactiver l'exécution concurrente du crawler.

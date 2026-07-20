## Changelog : abrege (30 derniers jours, au 18 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'outil abrege, notamment l'ajout de nouvelles fonctionnalités comme la génération de questions/réponses (QA), la possibilité de scraper du contenu web, et une gestion améliorée des tâches asynchrones. Des corrections de bugs et des mises à jour de configuration ont également été implémentées pour améliorer la stabilité et la sécurité.

### Évolutions fonctionnelles
- Ajout de la génération de questions/réponses (QA) pour les documents, accessible via l'interface utilisateur et l'API. [#29961b5](https://github.com/IA-Generative/abrege/commit/29961b5)
- Implémentation du scraping de contenu web pour l'analyse de documents en ligne. [#8f95fab](https://github.com/IA-Generative/abrege/commit/8f95fab)
- Ajout de la fonctionnalité de suppression de tâches. [#51cb85f](https://github.com/IA-Generative/abrege/commit/51cb85f)
- Ajout d'une vue de détail pour les tâches, permettant de suivre leur progression. [#74cb9c9](https://github.com/IA-Generative/abrege/commit/74cb9c9)
- Amélioration des modèles de résultats OCR avec des structures pour pages, boîtes englobantes et cases à cocher. [#3b5bd6e](https://github.com/IA-Generative/abrege/commit/3b5bd6e)
- Modification du libellé de l'en-tête des tâches dans l'interface utilisateur pour plus de clarté ("Mes tâches"). [#d5c66e9](https://github.com/IA-Generative/abrege/commit/d5c66e9)

### Évolutions techniques
- Mise à jour des variables d'environnement et des configurations pour Redis, MinIO et OpenAI. [#4f0b7fd](https://github.com/IA-Generative/abrege/commit/4f0b7fd)
- Amélioration de la configuration de Langfuse pour une intégration plus flexible. [#d978a8d](https://github.com/IA-Generative/abrege/commit/d978a8d)
- Correction d'un bug lié à la suppression en cascade avec l'OCR. [#506ebe5](https://github.com/IA-Generative/abrege/commit/506ebe5)
- Correction d'un bug lié au mot de passe Redis Sentinel. [#3a6b13a](https://github.com/IA-Generative/abrege/commit/3a6b13a)
- Correction de la valeur par défaut de QA. [#ca2b122](https://github.com/IA-Generative/abrege/commit/ca2b122)
- Correction d'un bug d'importation dans les tests. [#59962e3](https://github.com/IA-Generative/abrege/commit/59962e3)
- Correction d'un problème de sécurité. [#2122bbb](https://github.com/IA-Generative/abrege/commit/2122bbb)

### Autres changements
- Intégration de OWUI. [#99b4d01](https://github.com/IA-Generative/abrege/commit/99b4d01)
- Mise à jour des noms de variables d'environnement de S3_BUCKET_NAME à AWS_BUCKET_NAME dans la configuration et la documentation. [#9ae1aee](https://github.com/IA-Generative/abrege/commit/9ae1aee)
- Publication des versions 3.0.0, 3.1.0, 3.1.1, 3.1.2, 3.2.0, 3.3.0, 3.3.1 et 3.3.2.

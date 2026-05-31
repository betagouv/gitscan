## Changelog : ocr-api (30 derniers jours, au 26 mai 2026)

### Résumé
Cette version apporte des améliorations à la documentation de l'API, notamment avec l'ajout de sections sur la classification, l'extraction d'entités et les modèles. Des corrections ont également été apportées au traitement des tâches OCR et à la gestion des versions pour les branches de développement. Enfin, des améliorations de la robustesse et de la configuration ont été implémentées.

### Évolutions fonctionnelles
* **Documentation:** Ajout de nouvelles sections à la documentation concernant la classification, l'extraction d'entités et les modèles, améliorant ainsi la compréhension et l'utilisation de ces fonctionnalités. ([6958a4c](https://github.com/IA-Generative/ocr-api/commit/6958a4cba009a9f6ec4ec1e2afa64168347bf2cc))

### Évolutions techniques
* **Traitement des tâches:** Optimisation du traitement des tâches OCR en supprimant le découpage (chunking) des documents, améliorant potentiellement la performance et la simplicité du code. ([de1d318](https://github.com/IA-Generative/ocr-api/commit/de1d31809f9f225b39bcd76bb1cb4e8d8cc07969))
* **Versioning:** Amélioration de la stratégie de gestion des versions pour la branche de développement, assurant une meilleure cohérence et automatisation du processus de publication. ([a318f90](https://github.com/IA-Generative/ocr-api/commit/a318f903d525f7c30322f58ff8bfa18e7a56ad33))
* **Docker:** Ajout de vérifications de l'état de santé (healthchecks) pour les services MinIO, Redis et ocr_backend dans le fichier Docker Compose, améliorant la fiabilité du déploiement en conteneurs. ([f5dbba1](https://github.com/IA-Generative/ocr-api/commit/f5dbba1249f770a3a25ba4eb961feaec7ebf37bc))
* **Configuration:** Ajout de la prise en charge de la vérification SSL avec le client httpx pour le chunker. ([ffb7b8c](https://github.com/IA-Generative/ocr-api/commit/ffb7b8c12f5f4aa908e8761f4c166163a33baef6))
* **OpenAI:** Ajout de délais d'attente (timeout) et de tentatives maximales (max retries) aux configurations du client OpenAI pour améliorer la robustesse. ([2cce948](https://github.com/IA-Generative/ocr-api/commit/2cce948042d7615993a3a9c77410c9f738816177))

### Autres changements
* **Documentation:** Amélioration du formatage de la table des matières dans la documentation pour une meilleure lisibilité. ([8bfb680](https://github.com/IA-Generative/ocr-api/commit/8bfb680311d7239f7d1983616c097938b480f213))
* **Import:** Déplacement de l'import `OpenAIClipModel` vers un bloc conditionnel pour éviter des erreurs d'importation dans certains contextes. ([09a40d4](https://github.com/IA-Generative/ocr-api/commit/09a40d4178c3e6f8c9c301a6ec7fb86656aa524c))
* **Tasks:** Ajout de la méthode `fetchTaskPageImage` et mise à jour de l'OcrViewer pour charger les images des pages. ([f5dbba1](https://github.com/IA-Generative/ocr-api/commit/f5dbba1249f770a3a25ba4eb961feaec7ebf37bc))
* **Tasks:** Ajout de la prise en charge de `OCR_TASK_ONLY` dans la fonction `upload_file`. ([5074ad4](https://github.com/IA-Generative/ocr-api/commit/5074ad4daf4d84b65a24efe0eba0a171a6ccbcf6))

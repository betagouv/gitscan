## Changelog : ComparIA (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de modèles de langage supportés, avec l'ajout de nouveaux modèles comme GPT-5.5, DeepSeek V4 et Kimi K2.6, ainsi que la mise à jour et l'archivage de modèles existants. Des efforts importants ont également été consacrés à la lutte contre le spam et à l'amélioration de la robustesse de la plateforme, notamment en bloquant des techniques d'injection de prompts. Enfin, des améliorations techniques ont été apportées à la gestion de la base de données et à l'infrastructure, avec l'introduction d'un outil CLI pour faciliter l'administration et la maintenance.

### Évolutions fonctionnelles
- Ajout des modèles de langage GPT-5.5 et GPT-5.5 Pro [#460](https://github.com/betagouv/ComparIA/pull/460).
- Ajout des modèles de langage DeepSeek V4 Pro et Flash [#456](https://github.com/betagouv/ComparIA/pull/456), [#455](https://github.com/betagouv/ComparIA/pull/455).
- Ajout du modèle de langage Kimi K2.6 [#420](https://github.com/betagouv/ComparIA/pull/420).
- Mise à jour et archivage de plusieurs modèles de langage, incluant Grok 4.20, Qwen 3.6 Plus, MiniMax M2.7 et LFM2 24B A2B [#449](https://github.com/betagouv/ComparIA/pull/449).
- Amélioration de la détection et du filtrage du spam, notamment en bloquant les messages avec des préfixes d'ID de session falsifiés et les tentatives d'injection de prompts via des caractères hexadécimaux [#468](https://github.com/betagouv/ComparIA/pull/468), [#472](https://github.com/betagouv/ComparIA/pull/472), [#467](https://github.com/betagouv/ComparIA/pull/467), [#453](https://github.com/betagouv/ComparIA/pull/453).
- Amélioration de l'accessibilité avec l'utilisation d'une couleur violette accessible pour les boutons principaux [#461](https://github.com/betagouv/ComparIA/pull/461).
- Mise à jour du lien vers le formulaire de facilitation des duels [#459](https://github.com/betagouv/ComparIA/pull/459).

### Évolutions techniques
- Introduction d'un outil en ligne de commande (CLI) pour l'administration de la base de données, incluant des commandes pour l'archivage, la correction et la maintenance des données [#454](https://github.com/betagouv/ComparIA/pull/454).
- Refactorisation et amélioration de la gestion de la base de données, incluant la suppression de colonnes obsolètes et l'optimisation des requêtes.
- Suppression de la journalisation des requêtes SQL pour améliorer la performance et la sécurité [#454](https://github.com/betagouv/ComparIA/pull/454).
- Utilisation d'OpenRouter pour l'analyse des LLM, remplaçant Vertex AI [#454](https://github.com/betagouv/ComparIA/pull/454).
- Correction de bugs liés à l'inférence de type de données Polars et à la gestion des intervalles de confiance dans le classement des modèles [#470](https://github.com/betagouv/ComparIA/pull/470), [#469](https://github.com/betagouv/ComparIA/pull/469).
- Mise à jour des dépendances (npm, pip) [#472](https://github.com/betagouv/ComparIA/pull/472), [#440](https://github.com/betagouv/ComparIA/pull/440), [#424](https://github.com/betagouv/ComparIA/pull/424).

### Autres changements
- Mise à jour de la documentation et du fichier README avec la feuille de route du projet [#458](https://github.com/betagouv/ComparIA/pull/458).
- Corrections de traductions et mises à jour de la localisation (Weblate) pour l'italien et le norvégien.
- Améliorations de la configuration et du build Docker pour simplifier l'installation [#429](https://github.com/betagouv/ComparIA/pull/429).

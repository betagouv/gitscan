## Changelog : ComparIA (30 derniers jours, au 2026-05-15)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes d'infrastructure et de gestion des instances, notamment avec une refonte de la configuration pour supporter plusieurs instances (française et danoise).  De nouveaux modèles de langage ont été ajoutés au catalogue, tandis que d'autres ont été archivés. Des efforts importants ont été faits pour améliorer la robustesse du système, notamment en matière de détection de spam et de gestion des données corrompues.

### Évolutions fonctionnelles
- Ajout des modèles de langage GPT-5.5, DeepSeek V4 Pro et Flash, Kimi K2.6, Grok 4.20, Qwen 3.6 Plus, MiniMax M2.7 et LFM2 24B A2B. [#455](https://github.com/betagouv/ComparIA/pull/455), [#456](https://github.com/betagouv/ComparIA/pull/456), [#461](https://github.com/betagouv/ComparIA/pull/461)
- Archivage de plusieurs modèles de langage obsolètes. [#458](https://github.com/betagouv/ComparIA/pull/458)
- Amélioration de la détection de spam grâce à la reconnaissance de schémas d'injection d'identifiants de session et de messages génériques. [#467](https://github.com/betagouv/ComparIA/pull/467), [#468](https://github.com/betagouv/ComparIA/pull/468), [#472](https://github.com/betagouv/ComparIA/pull/472), [#473](https://github.com/betagouv/ComparIA/pull/473)
- Correction d'un problème de calcul des intervalles de confiance pour le classement des modèles. [#470](https://github.com/betagouv/ComparIA/pull/470)
- Correction d'un problème d'inférence de type dans les jobs de linting Polars. [#469](https://github.com/betagouv/ComparIA/pull/469)

### Évolutions techniques
- Refonte de l'infrastructure pour supporter plusieurs instances (française et danoise) avec une configuration simplifiée et une meilleure gestion des variables d'environnement (utilisation de Keepass). [#430](https://github.com/betagouv/ComparIA/pull/430)
- Suppression de l'utilisation de Vertex AI pour l'analyse LLM, au profit d'OpenRouter.
- Amélioration de la gestion des clés d'API et des secrets.
- Simplification et uniformisation des paramètres d'export vers Hugging Face.
- Suppression de la base de données locale PostgreSQL au profit d'un projet dédié.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout d'outils CLI pour la gestion de la base de données (archivage, correction de données corrompues, etc.).
- Amélioration de la gestion des logs et ajout de logs plus détaillés.
- Mise à jour des dépendances (pip et npm).

### Autres changements
- Mise à jour de la documentation et du fichier README.
- Corrections de traductions dans Weblate (Italien, Norvégien Bokmål, Norvégien Nynorsk).
- Amélioration de l'accessibilité (contraste des couleurs).
- Mise à jour du lien vers le formulaire de kit facilitateur.
- Corrections de formatage et de style du code.

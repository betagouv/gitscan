## Changelog : ComparIA (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de modèles de langage supportés, avec l'ajout de Gemini 3.5 Flash, Grok 4.3, GPT-5.5 et DeepSeek V4. Des corrections de sécurité ont été apportées pour contrer les tentatives de spam et de jailbreak, et l'infrastructure a été revue pour supporter plus facilement de multiples instances et améliorer la gestion des secrets. L'accessibilité a également été améliorée avec une meilleure gestion du contraste des couleurs.

### Évolutions fonctionnelles
- Ajout des modèles de langage Gemini 3.5 Flash et Grok 4.3 [#484](https://github.com/betagouv/ComparIA/pull/484).
- Ajout des modèles de langage GPT-5.5 et DeepSeek V4 [#456](https://github.com/betagouv/ComparIA/pull/456), [#455](https://github.com/betagouv/ComparIA/pull/455).
- Mise à jour du modèle Trinity Large Preview vers Trinity Large Thinking [#487](https://github.com/betagouv/ComparIA/pull/487).
- Amélioration de la gestion des modèles obsolètes : archivage de 6 modèles et suppression du tag "nouveau" pour les modèles de plus de deux mois [#479](https://github.com/betagouv/ComparIA/pull/479).
- Mise à jour du lien vers le formulaire de facilitation des duels [#459](https://github.com/betagouv/ComparIA/pull/459).
- Amélioration de l'accessibilité avec l'utilisation d'une couleur violette accessible pour les boutons d'action principaux [#460](https://github.com/betagouv/ComparIA/pull/460).

### Évolutions techniques
- Refonte de l'infrastructure pour supporter plus facilement plusieurs instances (française et danoise) et améliorer la gestion des secrets (utilisation de Keepass) [#430](https://github.com/betagouv/ComparIA/pull/430).
- Simplification et uniformisation des paramètres d'export vers Hugging Face [#482](https://github.com/betagouv/ComparIA/pull/482).
- Correction de problèmes de type dans les jobs de linting backend [#471](https://github.com/betagouv/ComparIA/pull/471).
- Amélioration de la gestion des clés Redis en les namespaceant par instance/portail [#483](https://github.com/betagouv/ComparIA/pull/483).
- Correction de problèmes liés à la configuration de l'URL du backend en mode développement [#462](https://github.com/betagouv/ComparIA/pull/462).
- Mise à jour des dépendances : litellm, typescript, npm et pip.
- Correction de problèmes de confiance dans le calcul du classement des modèles [#469](https://github.com/betagouv/ComparIA/pull/469).

### Autres changements
- Corrections de sécurité pour bloquer des tentatives de spam et de jailbreak (patterns d'injection, ID de session, etc.) [#473](https://github.com/betagouv/ComparIA/pull/473), [#467](https://github.com/betagouv/ComparIA/pull/467), [#468](https://github.com/betagouv/ComparIA/pull/468).
- Mises à jour des traductions italienne, danoise et norvégienne via Weblate.
- Mise à jour de la documentation et de la feuille de route dans le README.md [#458](https://github.com/betagouv/ComparIA/pull/458).
- Suppression de l'utilisation de Vertex AI dans litellm.
- Correction d'un problème de conversion de NaN en entier dans le calcul du classement.
- Ajout de paramètres requis pour l'estimation des coûts pour GPT-5.5.

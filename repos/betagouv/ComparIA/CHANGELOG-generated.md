## Changelog : ComparIA (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de modèles de langage disponibles, avec l'ajout de GPT-5.5, GPT-5.5 Pro et DeepSeek V4. Des corrections de sécurité ont été apportées pour contrer les tentatives de spam et de jailbreak, et l'infrastructure a été revue pour supporter plus facilement de nouvelles instances et améliorer la configuration. L'accessibilité a également été améliorée avec l'ajustement des couleurs pour une meilleure lisibilité.

### Évolutions fonctionnelles
- Ajout des modèles de langage GPT-5.5 et GPT-5.5 Pro [#456](https://github.com/betagouv/ComparIA/pull/456)
- Ajout des modèles de langage DeepSeek V4 Pro et DeepSeek V4 Flash [#455](https://github.com/betagouv/ComparIA/pull/455)
- Amélioration de l'accessibilité en ajustant les couleurs du CTA principal pour un meilleur contraste [#460](https://github.com/betagouv/ComparIA/pull/460)
- Mise à jour du lien vers le formulaire de kit facilitateur pour les duels [#459](https://github.com/betagouv/ComparIA/pull/459)
- Suppression du tag "nouveau" des modèles de plus de deux mois [#430](https://github.com/betagouv/ComparIA/pull/430)
- Correction de la gestion des modèles OpenRouter Nemotron et Trinity, désormais sur la tier payante [#461](https://github.com/betagouv/ComparIA/pull/461)

### Évolutions techniques
- Refonte de l'infrastructure pour supporter plus facilement de multiples instances (française et danoise) et simplifier la configuration. Ceci inclut la séparation des fichiers Docker Compose et des variables d'environnement, l'utilisation de Keepass pour la gestion des secrets, et la configuration de l'URI de la base de données par instance [#480](https://github.com/betagouv/ComparIA/pull/480)
- Simplification et uniformisation des paramètres d'export pour Hugging Face [#481](https://github.com/betagouv/ComparIA/pull/481)
- Suppression de l'utilisation de Vertex AI dans Litellm [#467](https://github.com/betagouv/ComparIA/pull/467)
- Amélioration de la gestion des erreurs et de la précision des intervalles de confiance dans le calcul du classement des modèles [#470](https://github.com/betagouv/ComparIA/pull/470)
- Correction de problèmes de type dans le job de linting Polars [#473](https://github.com/betagouv/ComparIA/pull/473)
- Correction de la gestion des ID de session pour bloquer les tentatives de spam [#468](https://github.com/betagouv/ComparIA/pull/468) et [#473](https://github.com/betagouv/ComparIA/pull/473)
- Correction de la logique de filtrage de spam pour bloquer les salutations triviales et les injections de faux historiques [#473](https://github.com/betagouv/ComparIA/pull/473)

### Autres changements
- Mise à jour de la documentation et du README avec la roadmap d'avril 2026 [#458](https://github.com/betagouv/ComparIA/pull/458)
- Mise à jour des traductions italiennes, norvégien Bokmål et norvégien Nynorsk via Weblate [#443](https://github.com/betagouv/ComparIA/pull/443) et autres commits Weblate.
- Diverses corrections et simplifications de la configuration et du code.
- Mises à jour mineures de dépendances (npm et pip).

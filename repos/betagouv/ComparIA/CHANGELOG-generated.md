## Changelog : ComparIA (30 derniers jours, au 2026-05-15)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes d'infrastructure et de gestion des instances, avec une séparation des environnements français et allemand. De nouvelles fonctionnalités ont été ajoutées concernant les modèles de langage supportés, et des corrections ont été apportées pour améliorer la sécurité (lutte contre le spam) et la robustesse de la plateforme. Des travaux importants ont également été réalisés sur l'archivage et la gestion des données, notamment pour la détection et le traitement des données corrompues.

### Évolutions fonctionnelles
- Ajout des modèles de langage GPT-5.5, DeepSeek V4 Pro et Flash, Kimi K2.6, Grok 4.20, Qwen 3.6 Plus, MiniMax M2.7 et LFM2 24B A2B. [#458](https://github.com/betagouv/ComparIA/pull/458), [#455](https://github.com/betagouv/ComparIA/pull/455), [#461](https://github.com/betagouv/ComparIA/pull/461)
- Amélioration de la détection de spam grâce à la reconnaissance de préfixes d'ID de session frauduleux et de schémas de rôleplay. [#467](https://github.com/betagouv/ComparIA/pull/467), [#468](https://github.com/betagouv/ComparIA/pull/468), [#473](https://github.com/betagouv/ComparIA/pull/473), [#453](https://github.com/betagouv/ComparIA/pull/453)
- Mise à jour de la feuille de route dans le fichier README.md. [#458](https://github.com/betagouv/ComparIA/pull/458)
- Correction du calcul des intervalles de confiance pour le classement des modèles. [#470](https://github.com/betagouv/ComparIA/pull/470)

### Évolutions techniques
- Séparation des instances françaises et allemandes pour une meilleure gestion et scalabilité. [#430](https://github.com/betagouv/ComparIA/pull/430), [#420](https://github.com/betagouv/ComparIA/pull/420)
- Refactorisation de la configuration et simplification de l'infrastructure DevOps.
- Suppression de l'utilisation de Vertex AI pour l'analyse LLM, au profit d'OpenRouter.
- Amélioration de la gestion des secrets avec l'utilisation de Keepass.
- Ajout d'un outil CLI pour la gestion de la base de données (archivage, nettoyage, analyse).
- Amélioration de la gestion des logs et suppression des logs SQL.
- Optimisation des requêtes et des migrations de la base de données.
- Mise en place d'un système d'archivage des données plus robuste et automatisé.
- Amélioration de la gestion des erreurs et des types de données dans le code.

### Autres changements
- Mise à jour des traductions italiennes, norvégiennes Bokmål et Nynorsk.
- Mise à jour des dépendances (npm et pip).
- Corrections mineures et améliorations de la documentation.
- Nettoyage du code et suppression de configurations obsolètes.
- Amélioration de l'accessibilité (couleurs violettes pour les CTA).
- Mise à jour du lien vers le formulaire de kit facilitateur.

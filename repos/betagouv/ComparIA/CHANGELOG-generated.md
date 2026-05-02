## Changelog : ComparIA (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de modèles de langage supportés, avec l'ajout de Gemma 4 (31B et 26B), GPT-5.5, DeepSeek V4 et la mise à jour de Kimi K2.6. Des corrections de bugs et des améliorations de la sécurité ont également été apportées, notamment concernant la détection de spams et la gestion des données. L'infrastructure a été renforcée avec l'ajout d'un outil CLI pour la gestion de la base de données et une simplification du processus d'installation via Docker.

### Évolutions fonctionnelles

*   **Nouveaux modèles de langage :** Ajout de Gemma 4 (31B et 26B) [#418, #425], GPT-5.5 [#461], DeepSeek V4 Pro et Flash [#455].
*   **Mise à jour de modèles existants :** Mise à jour de Kimi K2.6 [#420].
*   **Détection de spam améliorée :** Utilisation du modèle Gemini pour une détection plus précise du spam et du contenu inapproprié, avec persistance de cette information en base de données [#398, #424].
*   **Archivage de modèles :** Archivage de plusieurs modèles obsolètes ou indisponibles (OLMO 3 32B, LFM2 8B A1B, Gemini 3 Pro) pour maintenir la pertinence de la liste [#424, #426, #428].
*   **Amélioration de l'interface utilisateur :** Amélioration de l'accessibilité des boutons principaux avec des couleurs contrastées [#459].

### Évolutions techniques

*   **Outil CLI pour la base de données :** Ajout d'une interface en ligne de commande (CLI) pour faciliter la gestion et la maintenance de la base de données, incluant des commandes pour l'archivage, la correction de données corrompues et l'analyse des données [#423, #424].
*   **Dockerisation simplifiée :** Simplification du processus d'installation avec Docker, incluant un fichier `docker-compose.yml` pour un déploiement plus facile [#429].
*   **Refactoring de la base de données :** Nettoyage et refactoring de la base de données, suppression de colonnes obsolètes et amélioration des requêtes [#424].
*   **Suppression de la journalisation de la base de données :** Suppression de la journalisation des requêtes SQL pour améliorer les performances et la sécurité [#454].
*   **Utilisation d'OpenRouter :** Passage à OpenRouter pour l'analyse LLM, abandonnant Vertex AI [#454].
*   **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (npm, eslint, jsdom, pip) pour bénéficier des dernières corrections de bugs et améliorations de sécurité [#417, #419, #421, #422, #427].

### Autres changements

*   **Documentation :** Amélioration de la documentation concernant l'installation avec Docker et le processus d'initialisation de la base de données.
*   **Traduction :** Mise à jour des traductions en italien, norvégien Bokmål et norvégien Nynorsk via Weblate [#439, #443].
*   **Roadmap :** Mise à jour de la roadmap du projet [#458].
*   **Correction de bugs :** Correction de bugs mineurs liés à la détection de spams et à la gestion des sessions.
*   **Amélioration de la configuration de Dependabot :** Configuration de Dependabot pour des mises à jour moins fréquentes et plus groupées.

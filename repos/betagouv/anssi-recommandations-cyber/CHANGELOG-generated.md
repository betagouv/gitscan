## Changelog : anssi-recommandations-cyber (30 derniers jours, au 16 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la consultation des documents produits par l'IA Albert et sur la robustesse du système. L'expérience utilisateur est enrichie par une meilleure présentation des résultats, tandis que l'infrastructure technique a été renforcée pour permettre une détection et un suivi plus précis des erreurs de communication avec les modèles d'intelligence artificielle.

### Évolutions fonctionnelles
- **Amélioration de la lecture des documents** : Introduction de la pagination pour l'affichage des segments (chunks) de documents issus d'Albert.
- **Enrichissement du contexte** : Les paragraphes issus de la recherche sont désormais enrichis en intégrant les pages adjacentes pour offrir une meilleure compréhension contextuelle.
- **Qualité des réponses** : Stabilisation du formatage des listes Markdown dans les instructions (prompts) envoyées à l'IA.

### Évolutions techniques
- **Observabilité et gestion des erreurs** :
    - Intégration de Sentry via un consommateur dédié au bus d'événements pour une remontée automatique des exceptions.
    - Spécification de types d'erreurs de communication distincts selon l'étape du processus (reformulation, reclassement ou génération) afin de faciliter le diagnostic.
    - Publication systématique d'événements d'erreurs techniques sur le bus lors des échecs de communication avec le modèle.
- **Architecture et Refactoring** :
    - Renforcement de la cohérence du domaine en rendant l'injection du bus d'événements obligatoire pour les services clés (`ServiceAlbert`, `ReclasseurLLM`, `ReformulateurDeQuestion`).
    - Extraction de méthodes explicites pour les appels au LLM afin de clarifier le code.
- **Sécurité** :
    - Correction de vulnérabilités sur plusieurs dépendances critiques (`nanoid`, `pip`, `idna`).

### Autres changements
- **Documentation** :
    - Refonte de la structure documentaire avec la création d'un dossier `docs/` centralisé.
    - Ajout de diagrammes d'architecture complets (modèle C4 via PlantUML).
    - Documentation des conventions de tests et du fonctionnement du bus d'événements.
- **Développement (IA Agents)** :
    - Mise en place de fichiers d'instructions (`AGENTS.md`) et de compétences (`skills`) pour optimiser l'utilisation d'agents de codage (type Claude Code) sur le projet.

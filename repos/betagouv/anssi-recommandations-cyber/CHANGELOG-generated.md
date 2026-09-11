## Changelog : anssi-recommandations-cyber (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans la fiabilité et la précision de ses réponses. Grâce à un enrichissement des données transmises à l'intelligence artificielle et à une meilleure gestion des erreurs de communication, les recommandations sont désormais plus fidèles et mieux sourcées. L'architecture a également été renforcée pour permettre un suivi technique plus efficace et une documentation plus claire.

### Évolutions fonctionnelles
- **Amélioration de la précision des citations** : l'IA utilise désormais des métadonnées contextuelles (sections, codes de recommandation) pour identifier et citer ses sources avec une plus grande fidélité.
- **Fiabilisation du reclassement** : l'intégration de types de blocs et de codes de recommandation permet une catégorisation plus exacte des contenus par le modèle LLM.
- **Stabilisation du formatage** : correction de la génération des listes Markdown dans les prompts pour garantir des réponses plus cohérentes.

### Évolutions techniques
- **Observabilité et gestion des erreurs** :
    - Implémentation d'un bus d'événements pour notifier les erreurs techniques lors des étapes critiques (reformulation, reclassement, génération).
    - Intégration de Sentry pour le suivi et la remontée automatique des exceptions en production.
    - Création d'exceptions spécifiques par étape de traitement pour faciliter le diagnostic des échecs de communication avec les modèles.
- **Optimisation du pipeline IA** :
    - Enrichissement du contexte envoyé au LLM avec des métadonnées de structure (type de bloc, chemin de section, code de recommandation).
    - Refactoring des méthodes d'appel au LLM pour une meilleure modularité du code.
- **Sécurité** :
    - Correction de plusieurs vulnérabilités via la mise à jour de dépendances critiques (notamment `cryptography`, `nanoid`, `idna` et `dompurify`).

### Autres changements
- **Documentation** :
    - Refonte de la documentation technique avec l'introduction de diagrammes d'architecture (modèle C4 en PlantUML).
    - Centralisation de la documentation dans un nouveau dossier dédié (`docs/`).
    - Mise à jour des guides de contribution, des conventions de tests et des instructions pour les agents de développement IA.

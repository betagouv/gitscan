## Changelog : Muffin (30 derniers jours, au 02 novembre 2026)

### Résumé
Ce mois a marqué une transformation majeure de Muffin vers une plateforme véritablement multimodale. L'ajout de fonctionnalités vocales, de la génération et de la retouche d'images, ainsi que d'une analyse avancée de documents (OCR et tableaux) renforce considérablement l'interaction avec l'IA. La plateforme est également devenue plus personnalisée grâce à une gestion améliorée de la mémoire utilisateur et une intégration profonde avec l'écosystème Open WebUI.

### Évolutions fonctionnelles

- **Multimodalité (Voix, Image, Vision) :**
    - Ajout de la dictée vocale, de la transcription et de la lecture à voix haute via des services compatibles OpenAI ([#517](https://github.com/IA-Generative/Muffin/issues/517)).
    - Capacité de générer des images directement dans le chat et de les retoucher via des outils dédiés ([#518](https://github.com/IA-Generative/Muffin/issues/518)).
    - Support de la vision : l'assistant peut désormais lire et analyser les images jointes aux messages ([#512](https://github.com/IA-Generative/Muffin/issues/512)).
- **Intelligence & Mémoire :**
    - L'agent apprend désormais du style de réponse préféré de l'utilisateur en se basant sur les votes 👍/👎 ([#285](https://github.com/IA-Generative/Muffin/issues/285)).
    - Mise en place d'une gestion de la mémoire utilisateur (page "Ma mémoire") permettant d'injecter des informations contextuelles dans les réponses ([#282](https://github.com/IA-Generative/Muffin/issues/282), [#283](https://github.com/IA-Generative/Muffin/issues/283)).
    - Amélioration de l'interface avec la mise en avant des collections habituelles ([#286](https://github.com/IA-Generative/Muffin/issues/286)).
- **Analyse de documents & Tableurs :**
    - Extraction avancée par OCR : détection de la mise en page (layout), lecture des tableaux et reconnaissance de texte sur documents scannés ([#406](https://github.com/IA-Generative/Muffin/issues/406), [#410](https://github.com/IA-Generative/Muffin/issues/410)).
    - Analyse de données tabulaires : interrogation de fichiers Excel/tableurs en SQL et génération de graphiques directement dans les réponses ([#433](https://github.com/IA-Generative/Muffin/issues/433), [#434](https://github.com/IA-Generative/Muffin/issues/434)).
    - Gestion des "documents vivants" avec historique des révisions et verrouillage d'édition.
- **Assistants & Outils :**
    - Les assistants deviennent partageables comme des collections ([#514](https://github.com/IA-Generative/Muffin/issues/514)).
    - Introduction de la recherche d'assistants et support des serveurs d'outils via le protocole MCP ([#343](https://github.com/IA-Generative/Muffin/issues/343), [#531](https://github.com/IA-Generative/Muffin/issues/531)).
- **API & Écosystème :**
    - Exposition d'une API compatible OpenAI sous le point de terminaison `/v1` ([#513](https://github.com/IA-Generative/Muffin/issues/513)).
    - Synchronisation automatique et périodique des groupes, fichiers et collections depuis Open WebUI ([#453](https://github.com/IA-Generative/Muffin/issues/453)).
    - Gestion sécurisée des clés d'API personnelles via une nouvelle interface utilisateur.
- **Contrôle & Sécurité :**
    - Mise en place de "garde-fous" pour contrôler et filtrer les saisies avant qu'elles n'atteignent l'agent ([#516](https://github.com/IA-Generative/Muffin/issues/516)).

### Évolutions techniques

- **Moteur de recherche :** Migration de Meilisearch vers une recherche hybride (dense + BM25) utilisant Qdrant pour de meilleures performances de pertinence ([#355](https://github.com/IA-Generative/Muffin/issues/355)).
- **Architecture & Traitement :**
    - Découpage du pipeline de traitement documentaire en micro-services spécialisés (extraction, enrichissement, import) pour une meilleure scalabilité.
    - Intégration de l'agent directement dans le backend ([#499](https://github.com/IA-Generative/Muffin/issues/499)).
    - Optimisation du traitement des documents longs par fenêtrage et parallélisation.
- **Infrastructure & Sécurité :**
    - Support de l'autoscaling via KEDA pour les composants de la plateforme.
    - Renforcement de la sécurité des secrets avec l'implémentation de Vault Transit et du chiffrement des données sensibles en base.
    - Amélioration des processus de CI/CD et des déploiements Helm.

### Autres changements

- Mise à jour massive de la documentation technique couvrant les nouvelles fonctionnalités (voix, OCR, mémoire, garde-fous, etc.).
- Nettoyage et refactorisation de divers composants frontend et backend pour améliorer la stabilité.

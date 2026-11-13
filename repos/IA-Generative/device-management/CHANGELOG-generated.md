## Changelog : device-management (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois a été marqué par un renforcement significatif des capacités d'intelligence artificielle, notamment avec l'intégration du relais de "reranking" pour les extensions. Le projet a également bénéficié d'une refonte majeure de son système de déploiement pour garantir plus de stabilité, ainsi que de nouvelles options de configuration permettant de distribuer des liens et de gérer plus finement la sécurité des accès aux API locales.

### Évolutions fonctionnelles
- **Intelligence Artificielle :** Ajout du relais de services de "reranking" (POST `/llm/v1/rerank`) pour permettre aux extensions d'utiliser ces capacités ([#56](https://github.com/IA-Generative/device-management/issues/56), [#57](https://github.com/IA-Generative/device-management/issues/57)).
- **Gestion des outils :** Mise en place d'un relais d'outils vers les services MirAI (REST et MCP) incluant la transmission de l'identité de l'utilisateur ([#123](https://github.com/IA-Generative/device-management/issues/123)).
- **Configuration et UX :** 
    - Distribution de liens vers des portails de recherche ou des communautés bêta via la configuration ([#84](https://github.com/IA-Generative/device-management/issues/84)).
    - Gestion des origines d'API locales autorisées pour les extensions ([#60](https://github.com/IA-Generative/device-management/issues/60)).
- **Corrections :**
    - Résolution d'un problème de redirection (302) vers la page de connexion ([#126](https://github.com/IA-Generative/device-management/issues/126)).
    - Correction du processus d'exportation de données pour s'assurer qu'il s'exécute via un worker et avec les secrets appropriés ([#109](https://github.com/IA-Generative/device-management/issues/109)).
    - Correction d'erreurs sur les endpoints `/config` et `/catalog` lors de requêtes sans poste actif.

### Évolutions techniques
- **Déploiement et Helm :** 
    - Refonte complète du Helm Chart pour inclure le service `relay-assistant` et les modèles d'embeddings/rerank.
    - Optimisation de l'ordre de synchronisation avec Argo CD (prérequis $\rightarrow$ migrations $\rightarrow$ pods).
    - Ajustement des stratégies de mise à jour (Recreate) pour les composants API, Admin et Worker.
- **Configuration système :** Introduction de la possibilité de surcharger les clés du fichier `config.json` directement via les valeurs du chart Helm (`DM_CONFIG_OVERRIDES`) ([#129](https://github.com/IA-Generative/device-management/issues/129)).
- **Infrastructure et Observabilité :** 
    - Mise à jour de la stack d'observabilité (Grafana 11.6 et Tempo 2.10) dans les manifestes Kubernetes ([#120](https://github.com/IA-Generative/device-management/issues/120)).
    - Amélioration de la configuration du proxy Nginx (tunnel et profondeur de vérification SSL).
    - Validation de la compatibilité avec PostgreSQL 18 via la CI ([#110](https://github.com/IA-Generative/device-management/issues/110)).
- **CI/CD :** 
    - Déploiement d'un nouveau pipeline de CI/CD (`fabnum-cicd` v0.25.3).
    - Migration de l'environnement de CI vers Node 24.
    - Durcissement des règles de fusion : la branche `main` n'accepte désormais que des Pull Requests provenant de `develop`.

### Autres changements
- **Automatisation :** Mise en place de `release-please` pour automatiser la gestion des versions et la génération du changelog en français.
- **Qualité de code :** Standardisation de la longueur des en-têtes de commit à 120 caractères ([#92](https://github.com/IA-Generative/device-management/issues/92)).

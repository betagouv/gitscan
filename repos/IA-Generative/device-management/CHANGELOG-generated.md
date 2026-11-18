## Changelog : device-management (30 derniers jours, au 15 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes clés dans la sécurisation de la distribution de logiciels grâce à la mise en place d'une chaîne de confiance pour les paquets. L'expérience d'administration a été considérablement enrichie par une meilleure gestion des versions de test (préversions) et l'automatisation de l'importation depuis GitHub. Enfin, l'infrastructure a été consolidée pour supporter plus efficacement les services d'IA et les déploiements Kubernetes.

### Évolutions fonctionnelles
- **Gestion du catalogue et des paquets :**
    - Importation automatique des versions depuis les releases GitHub via l'assistant ([#155](https://github.com/IA-Generative/device-management/issues/155)).
    - Gestion des "Préversions" : annonce des versions candidates et invitation à l'essai pour tester de nouveaux plugins ([#150](https://github.com/IA-Generative/device-management/issues/150), [#156](https://github.com/IA-Generative/device-management/issues/156)).
    - Amélioration du flux de déploiement des campagnes avec un guidage optimisé lors de l'envoi de versions ([#134](https://github.com/IA-Generative/device-management/issues/134)).
    - Possibilité de demander le redémarrage automatique du logiciel après une installation ([#151](https://github.com/IA-Generative/device-management/issues/151)).
- **Administration et API :**
    - Introduction de clés d'API personnelles pour permettre des appels directs au serveur ([#158](https://github.com/IA-Generative/device-management/issues/158)).
    - Relais d'outils vers les services MirAI (REST et MCP) avec transmission de l'identité utilisateur ([#123](https://github.com/IA-Generative/device-management/issues/123)).
    - Distribution de liens vers des portails de recherche ou des communautés bêta via la configuration ([#84](https://github.com/IA-Generative/device-management/issues/84)).
    - Amélioration de l'interface d'administration (gestion des redirections et des gabarits de paquets) ([#136](https://github.com/IA-Generative/device-management/issues/136)).

### Évolutions techniques
- **Sécurité et intégrité :**
    - Implémentation d'une chaîne de confiance pour les paquets : vérification de l'origine, adaptation du paquet et signature par le DM ([#149](https://github.com/IA-Generative/device-management/issues/149)).
    - Assouplissement de l'exigence de signature pour permettre le déploiement de plugins en cours de développement ([#157](https://github.com/IA-Generative/device-management/issues/157)).
    - Correction du routage des paquets pour garantir que les postes pointent toujours vers le DM d'origine ([#135](https://github.com/IA-Generative/device-management/issues/135)).
- **Infrastructure et Déploiement :**
    - Refonte majeure du Helm Chart pour inclure le relais-assistant, les modèles d'embeddings/rerank et la gestion des jetons LLM ([#68](https://github.com/IA-Generative/device-management/issues/68)).
    - Optimisation de l'ordre de synchronisation Argo CD (respect de la séquence : prérequis > migrations > pods) ([#69](https://github.com/IA-Generative/device-management/issues/69)).
    - Amélioration de la gestion des configurations via le chart (possibilité d'overrides via `DM_CONFIG_OVERRIDES`) ([#129](https://github.com/IA-Generative/device-management/issues/129)).
    - Correction de la stratégie de déploiement (gestion des blocs RollingUpdate vs Recreate) ([#72](https://github.com/IA-Generative/device-management/issues/72)).
- **Base de données et Services :**
    - Correction des erreurs de migration de schéma sur les nouvelles bases de données ([#70](https://github.com/IA-Generative/device-management/issues/70)).
    - Validation de la compatibilité avec PostgreSQL 18 ([#110](https://github.com/IA-Generative/device-management/issues/110)).
    - Mise en place du relais de service de reranking pour les extensions ([#56](https://github.com/IA-Generative/device-management/issues/56)).
- **Observabilité et CI/CD :**
    - Mise à jour de la stack d'observabilité (Grafana 11.6 et Tempo 2.10) ([#120](https://github.com/IA-Generative/device-management/issues/120)).
    - Modernisation de la CI (passage à Node 24 et mise à jour du pipeline `fabnum-cicd`).

### Autres changements
- Ajustement de la longueur maximale des en-têtes de commit pour une meilleure lisibilité ([#92](https://github.com/IA-Generative/device-management/issues/92)).

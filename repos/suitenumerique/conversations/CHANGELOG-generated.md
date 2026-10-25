## Changelog : conversations (30 derniers jours, au 24 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilité de l'expérience de chat, notamment via une meilleure gestion des interruptions de réponse et des rechargements de page. Le projet a également renforcé sa posture de confidentialité en garantissant que les messages des utilisateurs ne sont jamais enregistrés dans les logs, tout en enrichissant ses capacités avec l'ajout de l'outil de recherche web Staan.

### Évolutions fonctionnelles
- **Nouveaux outils** : Intégration de l'outil de recherche web Staan et possibilité pour l'utilisateur de forcer l'utilisation du connecteur DataGouv pour une requête spécifique.
- **Expérience de chat** : Amélioration de la gestion des réponses interrompues (meilleure visibilité de l'état de génération et préservation du contenu produit).
- **Navigation et interface** : 
    - Mise en place d'une demande de rechargement automatique lors du déploiement d'une nouvelle version.
    - Affichage de pages d'erreur explicites au lieu de pages blanches.
    - Améliorations cosmétiques (espacement du module d'impact carbone, ajustement des messages de trafic élevé).
- **Gestion de fichiers** : Correction permettant l'acceptation de fichiers Markdown même avec un type MIME manquant.

### Évolutions techniques
- **Observabilité** : Ajout de métriques Prometheus pour mesurer les requêtes de modèles, les flux de chat et les appels sortants, avec intégration de moniteurs Helm (ServiceMonitor/PodMonitor).
- **Sécurité et Confidentialité** : 
    - Garantie technique que les prompts utilisateurs ne sont jamais enregistrés dans les logs ou la télémétrie.
    - Correction de plusieurs vulnérabilités (CVE) sur des dépendances critiques (brotli, certifi, pillow, pydantic-ai, etc.).
    - Restriction des ports de développement Docker à l'adresse localhost uniquement.
- **Infrastructure et Architecture** : 
    - Migration des tâches périodiques vers Celery Beat.
    - Remplacement de MinIO par RustFS pour les environnements de développement et de CI.
    - Remplacement de Maildev par Mailcatcher.
- **Optimisations** : Amélioration des performances via la mise en cache de la configuration au chargement de la page et réduction de la fréquence de rechargement des flags de fonctionnalités.

### Autres changements
- **Documentation** : Ajout de la politique d'usage de l'IA et des procédures de déploiement/release.
- **Internationalisation** : Mise à jour des chaînes de traduction [#769](https://github.com/suitenumerique/conversations/pull/769).

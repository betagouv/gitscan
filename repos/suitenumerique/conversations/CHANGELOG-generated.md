## Changelog : conversations (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilité de l'expérience de chat, notamment grâce à une meilleure gestion des réponses interrompues, et sur le renforcement de la confidentialité des données. De nouvelles capacités de recherche web ont été intégrées et la surveillance du système a été considérablement améliorée pour garantir une meilleure stabilité et une meilleure visibilité des performances.

### Évolutions fonctionnelles
- **Expérience de chat améliorée** : gestion plus fluide des interruptions de réponse, affichage clair des outils en cours d'exécution et meilleure gestion de l'affichage lors des rechargements.
- **Nouvelles capacités** : intégration de l'outil de recherche web Staan et possibilité pour l'utilisateur de forcer l'utilisation du connecteur DataGouv pour un tour de discussion.
- **Interface et robustesse** : amélioration de la gestion des erreurs (affichage d'une page de rechargement au lieu d'un écran blanc), notifications de mise à jour de version et meilleure prise en charge des fichiers Markdown en pièces jointes.
- **Ajustements UI** : affinage de l'interface pour le module d'impact carbone et modification des messages d'alerte en cas de trafic élevé.

### Évolutions techniques
- **Confidentialité et sécurité** : renforcement de la protection des données en garantissant que les prompts des utilisateurs ne sont jamais enregistrés dans les journaux (logs) ou la télémétrie. Correction de plusieurs vulnérabilités (CVE) sur les dépendances.
- **Observabilité** : mise en place de métriques Prometheus pour le suivi précis des requêtes de modèles, des flux de chat et des appels sortants. Configuration ajustable du taux d'échantillonnage des traces Sentry.
- **Infrastructure et développement** : optimisation de l'environnement de développement local (passage à RustFS et Mailcatcher) et automatisation des tâches périodiques via Celery Beat.
- **Optimisations** : amélioration des performances de chargement de la configuration et de la télémétrie.

### Autres changements
- **Documentation** : ajout d'une politique d'utilisation de l'IA et de la procédure détaillée de déploiement.
- **Internationalisation** : mise à jour des chaînes de traduction [#769](https://github.com/suitenumerique/conversations/pull/769).

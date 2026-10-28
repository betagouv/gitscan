## Changelog : conversations (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes en matière de capacités de recherche et de protection de la vie privée. L'ajout de nouveaux outils de recherche (Staan et DataGouv) enrichit l'expérience utilisateur, tandis que de nouvelles mesures garantissent qu'aucun prompt utilisateur n'est enregistré dans les journaux ou la télémétrie. L'interface est également devenue plus robuste, notamment lors des déploiements ou des interruptions de réponses.

### Évolutions fonctionnelles
- **Nouvelles capacités de recherche** : intégration de l'outil de recherche web Staan et possibilité pour l'utilisateur de forcer l'utilisation du connecteur DataGouv.
- **Amélioration de l'expérience de chat** : meilleure gestion des réponses interrompues (affichage de notifications et persistance du texte) et gestion plus fluide des erreurs (page de rechargement au lieu d'une page blanche).
- **Expérience de déploiement** : l'interface incite désormais l'utilisateur à recharger la page lors d'une nouvelle version pour éviter l'utilisation de fichiers obsolètes.
- **Interface et contenu** : mise à jour des traductions ([#769](https://github.com/suitenumerique/conversations/pull/769)), ajustements visuels du module d'impact carbone et amélioration de la gestion des téléchargements de fichiers Markdown.

### Évolutions techniques
- **Sécurité et confidentialité** : renforcement majeur de la protection des données en interdisant l'enregistrement des prompts utilisateurs dans les logs et la télémétrie, et correction de plusieurs vulnérabilités (CVE) via la mise à jour de dépendances critiques.
- **Observabilité** : mise en place de métriques Prometheus pour mesurer les requêtes de modèles, les flux de chat et les appels sortants, avec support Helm (ServiceMonitor/PodMonitor).
- **Architecture et performance** : passage à Celery Beat pour la gestion des tâches périodiques, optimisation de la lecture de la configuration et réduction des rechargements de flags de fonctionnalités.
- **Infrastructure et développement** : remplacement de Maildev par Mailcatcher et sécurisation des ports Docker en environnement de développement.

### Autres changements
- **Documentation** : ajout d'une politique d'utilisation de l'IA et des pull requests, et documentation détaillée des procédures de release et de déploiement.

## Changelog : conversations (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, Conversations a considérablement enrichi ses capacités de recherche grâce à l'intégration de nouveaux outils comme Staan et le connecteur data.gouv. L'expérience utilisateur a été fluidifiée avec une interface plus intuitive et une meilleure gestion des mises à jour du service. Enfin, un effort majeur a été porté sur la protection de la vie privée, garantissant qu'aucune donnée de conversation n'est enregistrée dans les journaux ou la télémétrie.

### Évolutions fonctionnelles
- **Nouveaux outils de recherche** : intégration de l'outil de recherche web Staan et du connecteur data.gouv.
- **Modernisation de l'interface** : remplacement des actions d'entrée par un menu déroulant "+" et amélioration de l'affichage du module d'impact carbone.
- **Amélioration de l'expérience utilisateur** : 
    - Mise en place de notifications pour demander le rechargement de la page après un déploiement.
    - Affichage d'une page d'erreur explicite au lieu d'un écran blanc en cas de problème.
    - Ajustement des messages d'alerte lors de pics de trafic.
    - Possibilité pour l'utilisateur de forcer l'utilisation du connecteur DataGouv.
- **Corrections** : amélioration de la gestion des téléchargements de fichiers Markdown et stabilisation de l'ordre d'affichage de la liste des projets.
- **Internationalisation** : mise à jour des chaînes de caractères traduites [#769](https://github.com/suitenumerique/conversations/pull/769).

### Évolutions techniques
- **Confidentialité et sécurité** : 
    - Garantie que les requêtes des utilisateurs (prompts) ne sont plus enregistrées dans les logs ni transmises à la télémétrie.
    - Correction de vulnérabilités (CVE) sur les dépendances `pydantic-ai` et `handlebars`.
    - Sécurisation des accès Docker en environnement de développement.
- **Architecture et performance** : 
    - Migration des tâches périodiques vers Celery Beat.
    - Optimisation de la lecture de la configuration (cache) et réduction des rechargements de drapeaux de fonctionnalités (feature flags).
- **Infrastructure et CI/CD** : remplacement de MinIO par RustFS pour les environnements de développement local et de CI ; ajustement de la configuration Docker pour la CI.
- **Tests** : amélioration de la robustesse des tests frontend via le mock de composants et le découplage des tests de langue.

### Autres changements
- **Documentation** : ajout d'une politique d'utilisation de l'IA et des pull requests, et documentation détaillée des procédures de déploiement.

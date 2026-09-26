## Changelog : apistration (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a été marqué par des évolutions majeures concernant la sécurité et l'extension des services. L'introduction d'une nouvelle version de l'introspection des jetons, le déploiement de preuves d'attestation vérifiables pour le service EAJE et l'enrichissement du catalogue des services "Associations" sont les points clés. Parallèlement, l'expérience d'administration a été améliorée grâce à une meilleure visibilité des erreurs et une interface plus intuitive.

### Évolutions fonctionnelles
- **Nouvelle version de l'introspection de jetons** : Introduction d'un endpoint d'introspection en version 3, incluant la mise à jour des SDK officiels pour supporter cette nouvelle norme ([#415](https://github.com/datagouv/apistration/pull/415)).
- **Attestations EAJE** : Mise en place d'un système de preuve d'attestation vérifiable, permettant le rendu de PDF signés et la possibilité de demander une preuve via un en-tête HTTP.
- **Extension du service Associations** : Ajout de nouveaux points de terminaison pour les ressources "Associations" et mise à jour des SDK (v0.4.0).
- **Améliorations de l'interface (Back-office & Portails)** :
    - Optimisation visuelle du tableau de bord (succès affichés en vert).
    - Amélioration des formulaires de requêtes manuelles : intégration de menus déroulants pour les valeurs énumérées OpenAPI et gestion facilitée des paramètres d'en-tête.
    - Meilleure lisibilité des verdicts de vérification et alignement des champs de saisie.
- **Transparence des erreurs** : Amélioration de la précision des messages d'erreur lors des échecs d'authentification (notamment pour les services INSEE et les jetons invalides) et affichage des réponses brutes des fournisseurs dans le back-office pour faciliter le diagnostic.

### Évolutions techniques
- **Gestion de l'authentification** : Automatisation de la rotation des mots de passe pour le service INSEE et amélioration de la gestion des jetons par environnement.
- **Architecture et compatibilité** : Mise à jour pour la compatibilité avec JSON 3 et ajustements des dépendances liées à Rails.
- **DevOps et CI/CD** :
    - Optimisation des workflows GitHub Actions via la variabilisation des cibles de déploiement.
    - Amélioration de l'environnement de développement avec la gestion de bases de données de test via des *worktrees*.
    - Résolution de problèmes de concurrence (race conditions) dans les pipelines de déploiement.
- **Observabilité** : Amélioration du suivi des erreurs via Sentry et enrichissement des logs d'accès avec des codes d'erreur détaillés.

### Autres changements
- **Documentation** : Mises à jour importantes de la documentation technique pour les services INSEE, CNAV, MESRI et DGFiP.
- **Nettoyage** : Suppression de composants obsolètes, ajustement des règles du fichier `robots.txt` pour les environnements hors production et nettoyage des fichiers de configuration.

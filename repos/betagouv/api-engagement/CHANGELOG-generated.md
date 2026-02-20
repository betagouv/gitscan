## Changelog : api-engagement (30 derniers jours)

### Résumé
Cette période a été marquée par des améliorations de l'accessibilité, des corrections de bugs et des optimisations de performance sur l'ensemble de l'application, incluant l'API, le tableau de bord et les widgets. Des refactorings importants ont été effectués pour simplifier l'architecture et améliorer la maintenance du code. Des mises à jour de dépendances ont également été réalisées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles

- Ajout d'un identifiant de publisher comme préfixe d'URL (#807)
- Ajout de l'adresse de la mission dans les informations de modération (#784)
- Amélioration de la gestion des missions et de la modération dans le tableau de bord (plusieurs commits)
- Correction d'un bug empêchant la déconnexion pour l'utilisateur "my-missions" (#799)
- Ajout de la possibilité d'ajouter des attributs personnalisés dans l'écran de suivi en temps réel (#704)
- Amélioration de la gestion des états de modération en batch (#703, #702)
- Correction d'un problème d'affichage des noms de villes et d'organisations dans les widgets (#759)
- Ajout d'un logger pour les widgets (#775)

### Évolutions techniques

- Passage à Node.js version 24 (#802)
- Refactoring de la logique d'agrégation des widgets (#790)
- Refactoring de l'implémentation des recherches dans l'API pour optimiser les performances (#806, #788)
- Migration des activités de mission vers une table de jointure N-N (#757)
- Suppression de l'utilisation de MongoDB (#761)
- Ajout de tests d'intégration pour les endpoints des widgets (#750)
- Amélioration de la gestion des erreurs et ajout de rapports Sentry (plusieurs commits)
- Refactoring de la configuration des conteneurs de widgets (#786)
- Ajout d'un request-id header avec support Sentry (#780)
- Ajout de workflows Claude pour la revue de code (#717)
- Mise à jour de plusieurs dépendances (Express, Next.js, @types/node, @sentry/cli, etc.)

### Autres changements

- Amélioration de l'accessibilité de l'application avec l'utilisation de composants Headless UI conformes RGAA (plusieurs commits)
- Ajout de tests E2E pour le SDK jstag.js (#715)
- Amélioration des logs et du monitoring (plusieurs commits)
- Suppression de jobs et modèles analytics obsolètes (#706, #681)
- Mise à jour de la documentation et du fichier CHANGELOG.md (plusieurs commits)
- Correction de problèmes de performance dans le tableau de bord (#753)
- Correction de problèmes de configuration de l'environnement Metabase (#708)

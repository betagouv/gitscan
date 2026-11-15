## Changelog : signal-logement-sites-conformes (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur l'amélioration de l'accessibilité du site (suite à des audits), l'optimisation de l'expérience utilisateur sur les formulaires et la navigation, ainsi que la stabilisation des processus de déploiement et de sécurité de l'infrastructure.

### Évolutions fonctionnelles
- **Accessibilité** : Corrections majeures suite à l'audit de doctorat.gouv.fr [#631], amélioration des messages de validation de formulaire [#626], ajustements sur les blocs de contenu [#656] et optimisation des filtres et boutons (iCal) sur les pages d'événements [#625].
- **Expérience utilisateur** : Restructuration de la navigation alphabétique des pages d'étiquettes [#649], correction des problèmes de débordement horizontal sur les formulaires [#650], ajout d'une page d'erreur 403 [#644] et amélioration de la saisie via l'autocomplétion des types de champs.
- **SEO & Navigation** : Correction de l'URL canonique [#635] et optimisation de la validation des formulaires pour une meilleure gestion des erreurs par Django [#619].

### Évolutions techniques
- **Infrastructure et Déploiement** : Amélioration du déploiement en un clic [#646], ajout d'un script de rollback [#637] et résolution de problèmes critiques liés à l'environnement Scalingo (CLI et migrations de base de données) [#645, #634]. Optimisation de la configuration par défaut de Gunicorn [#636].
- **Sécurité et Monitoring** : Renforcement de la protection du dépôt contre l'inclusion accidentelle de secrets ou de sauvegardes [#648], correction de correctifs liés à la double authentification (2FA) [#641] et amélioration de la configuration de Sentry [#620].
- **Performance et Internationalisation** : Ajout d'en-têtes de cache public pour les visiteurs anonymes afin d'améliorer la vitesse de chargement [#651] et automatisation de la compilation des fichiers de traduction lors du déploiement [#652].
- **Qualité du code** : Amélioration de la suite de tests [#647] et mise à jour des outils de contrôle de qualité (linting) avec l'intégration de Djlint et prekt [#657, #627].

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les procédures de changement de nom de domaine [#655].

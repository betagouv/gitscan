## Changelog : pass-sport (30 derniers jours, au 19 octobre 2026)

### Résumé
Ce mois-ci, les évolutions majeures concernent l'intégration du nouveau processus CNAF AEEH et l'optimisation du parcours utilisateur via FranceConnect. Le projet renforce également ses outils d'administration avec l'introduction d'un nouveau tableau de bord complet et améliore la résilience du service face aux erreurs techniques pour garantir une expérience plus fluide.

### Évolutions fonctionnelles
- **Nouveau processus métier** : Intégration du processus CNAF AEEH ([#644](https://github.com/betagouv/pass-sport/pull/644)).
- **Amélioration du parcours FranceConnect** : 
    - Optimisation de la gestion des cookies pour sécuriser et fluidifier la connexion ([#639](https://github.com/betagouv/pass-sport/pull/639), [#627](https://github.com/betagouv/pass-sport/pull/627)).
    - Amélioration du flux de relance en incluant la gestion des erreurs 404 ([#641](https://github.com/betagouv/pass-sport/pull/641), [#603](https://github.com/betagouv/pass-sport/pull/603)).
- **Formulaires** : Mise à jour des motifs disponibles dans le formulaire de contact ([#654](https://github.com/betagouv/pass-sport/pull/654)).
- **Règles de gestion** : Mise à jour des règles de correspondance pour les bénéficiaires.

### Évolutions techniques
- **Outils d'administration** : 
    - Mise en place d'un nouveau tableau de bord "fullstack", actuellement activable via un *feature flag* pour un déploiement contrôlé ([#626](https://github.com/betagouv/pass-sport/pull/626)).
    - Ajustement des permissions d'écriture sur les dossiers d'exécution pour les opérateurs.
- **Résilience et performance** :
    - Mise en place de mécanismes de relance automatique en cas d'erreur serveur (500) pour éviter de briser le parcours de l'utilisateur.
    - Optimisation des performances de la base de données via l'ajout d'index ([#608](https://github.com/betagouv/pass-sport/pull/608)).
- **Infrastructure et DevOps** :
    - Refonte de la stack Docker locale pour permettre de tester séparément les configurations avec et sans WAF.
    - Amélioration de la CI (Intégration Continue).
- **Observabilité** : Intégration d'un script Crisp pour le suivi spécifique des utilisateurs rencontrant des situations de "QF non existant" ([#610](https://github.com/betagouv/pass-sport/pull/610)).

### Autres changements
- Mise à jour du sitemap du site.
- Nettoyage de données et de références obsolètes dans le code.
- Mise à jour des fichiers de configuration d'environnement.

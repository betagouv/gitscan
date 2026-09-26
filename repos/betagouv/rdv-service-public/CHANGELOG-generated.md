## Changelog : rdv-service-public (30 derniers jours, au 24 septembre 2026)

### Résumé
Le service a introduit la version initiale (MVP) du système d'invitation pour les usagers. Les agents bénéficient d'une meilleure gestion de leurs comptes via ProConnect et d'un accès étendu aux outils d'administration. La synchronisation des agendas et la gestion des fuseaux horaires ont également été fiabilisées.

### Évolutions fonctionnelles
- **Invitations et rendez-vous**
    - Lancement du parcours d'invitation usager (MVP) [#6626](https://github.com/betagouv/rdv-service-public/issues/6626)
    - Annulation d'invitation [#6722](https://github.com/betagouv/rdv-service-public/issues/6722) et création d'usager via le formulaire d'invitation [#6724](https://github.com/betagouv/rdv-service-public/issues/6724)
    - Amélioration du parcours de rendez-vous par intégration [#6677](https://github.com/betagouv/rdv-service-public/issues/6677)
- **Gestion des agents et administration**
    - Création des comptes administrateurs agents via ProConnect uniquement [#6723](https://github.com/betagouv/rdv-service-public/issues/6723)
    - Accès étendu pour les agents basiques (configuration et liste des agents) [#6684](https://github.com/betagouv/rdv-service-public/issues/6684)
    - Nouveaux filtres et options de gestion des services dans l'administration des espaces [#6650](https://github.com/betagouv/rdv-service-public/issues/6650)
    - Recherche d'espace par SIRET [#6654](https://github.com/betagouv/rdv-service-public/issues/6654)
- **Calendrier et synchronisation**
    - Correction des fichiers de calendrier (ICS) pour une meilleure compatibilité avec Google/Outlook [#6721](https://github.com/betagouv/rdv-service-public/issues/6721)
    - Correction de la gestion des fuseaux horaires pour les récurrences et les événements d'absence [#6708](https://github.com/betagouv/rdv-service-public/issues/6708), [#6696](https://github.com/betagouv/rdv-service-public/issues/6696), [#6695](https://github.com/betagouv/rdv-service-public/issues/6695)
    - Personnalisation (nom et couleur) du calendrier CalDAV [#6620](https://github.com/betagouv/rdv-service-public/issues/6620)
- **Expérience utilisateur**
    - Changement d'adresse email en autonomie par l'usager [#6563](https://github.com/betagouv/rdv-service-public/issues/6563)
    - Corrections d'interface (boutons, menus déroulants, défilement) [#6744](https://github.com/betagouv/rdv-service-public/issues/6744), [#6689](https://github.com/betagouv/rdv-service-public/issues/6689), [#6700](https://github.com/betagouv/rdv-service-public/issues/6700)

### Évolutions techniques
- **Sécurité et Authentification**
    - Gestion des sessions (timeouts SuperAdmin [#6706](https://github.com/betagouv/rdv-service-public/issues/6706), réinitialisation lors de la suppression de compte [#6731](https://github.com/betagouv/rdv-service-public/issues/6731))
    - Authentification OAuth, restriction des accès API [#6547](https://github.com/betagouv/rdv-service-public/issues/6547), [#6694](https://github.com/betagouv/rdv-service-public/issues/6694), [#6649](https://github.com/betagouv/rdv-service-public/issues/6649) et détection d'injections [#6647](https://github.com/betagouv/rdv-service-public/issues/6647)
    - Calcul de la sensibilité des comptes agents [#6707](https://github.com/betagouv/rdv-service-public/issues/6707) et dispositifs de confiance pour la connexion [#6683](https://github.com/betagouv/rdv-service-public/issues/6683)
- **Infrastructure et CI/CD**
    - Mise à jour de l'environnement de test (passage à Ubuntu 26.04) [#6737](https://github.com/betagouv/rdv-service-public/issues/6737)
    - Optimisation des workflows de CI et de la gestion des notifications [#6741](https://github.com/betagouv/rdv-service-public/issues/6741), [#6703](https://github.com/betagouv/rdv-service-public/issues/6703)
    - Nettoyage des fichiers de build et des dépendances inutiles [#6743](https://github.com/betagouv/rdv-service-public/issues/6743), [#6728](https://github.com/betagouv/rdv-service-public/issues/6728)
- **API et Base de données**
    - Ajout d'index sur les rôles d'agents pour les performances [#6660](https://github.com/betagouv/rdv-service-public/issues/6660)
    - Nettoyage du schéma de la base de données (suppression des colonnes CalDAV) [#6729](https://github.com/betagouv/rdv-service-public/issues/6729)
- **Qualité logicielle**
    - Correction de tests instables (flaky tests) dans la suite de tests automatisés [#6752](https://github.com/betagouv/rdv-service-public/issues/6752), [#6715](https://github.com/betagouv/rdv-service-public/issues/6715)

### Autres changements
- **Documentation**
    - Amélioration de l'outillage et de la documentation pour les tests locaux de l'intégration Démarche Numérique [#6725](https://github.com/betagouv/rdv-service-public/issues/6725)

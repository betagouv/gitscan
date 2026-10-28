## Changelog : autometa (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois a été marqué par une extension significative des capacités d'analyse de l'outil. L'ajout de nouvelles sources de données (Airtable et la base "Mon Récap") et l'introduction de tableaux de bord multi-sources permettent une vision plus transverse des indicateurs. L'expérience de recherche a été profondément améliorée grâce à l'intégration de la recherche sémantique, rendant l'exploration des données plus intuitive. Enfin, la robustesse du système a été renforcée, notamment sur la gestion des connexions et la stabilité des tâches automatisées.

### Évolutions fonctionnelles
- **Nouvelles sources de données** : Intégration d'Airtable en lecture seule [#249] et de la base applicative "Mon Récap" comme nouvelle source de données [#239, #250].
- **Amélioration de la recherche et du filtrage** : 
    - Mise en place de la recherche sémantique (via embeddings) avec un repli automatique sur la recherche par mots exacts.
    - Refonte de l'interface de recherche : regroupement des résultats, menu de filtres épuré et ajout de facettes de recherche (ex: filtre "Créé par").
- **Gestion des tableaux de bord** :
    - Support des tableaux de bord multi-sources et introduction de "variantes" pour gérer différentes configurations de données.
    - Possibilité de modifier les tableaux de bord d'autres utilisateurs (avec système de confirmation) [#241].
- **Gestion Zendesk** : Nouvelles capacités de lecture et d'édition des macros avec un système de révision des changements.
- **Interface utilisateur** : 
    - Épinglage du guide de données dans la navigation pour un accès rapide [#234].
    - Affichage direct des résultats de requêtes SQL [#235].
- **Automatisation** : Mise en place de lots (batches) matinaux avec récapitulatifs envoyés sur Slack [#257].

### Évolutions techniques
- **Fiabilité et Résilience** :
    - Refonte majeure de la gestion des timeouts Redis pour éviter le gel des consommateurs en cas de défaillance du serveur.
    - Amélioration de la résilience du système de tâches (runner) pour permettre le démarrage même en cas d'indisponibilité temporaire de Redis.
- **Infrastructure et Stockage** :
    - Remplacement de Minio par RustFS [#242].
    - Optimisation de l'image Scalingo (réduction de la taille) [#266].
    - Corrections liées à la sécurité CSP et à l'adressage virtuel S3 [#256].
- **API et Intégrations** :
    - Ajout de Datadog à l'API des tableaux de bord [#223].
    - Mise à jour de la configuration Matomo [#247, #244].
    - Ajustement de la méthode de connexion pour Metabase (RDVI) [#243].
- **Tests et Qualité** :
    - Accélération des tests unitaires grâce à la parallélisation avec `pytest-xdist`.
    - Amélioration des hooks de pré-push pour garantir l'herméticité des tests.

### Autres changements
- **Documentation** : Mise à jour des guides concernant les tableaux de bord multi-sources et les nouvelles compétences (skills) disponibles.
- **Nettoyage** : Suppression du scrapping RPE [#237] et retrait de la connexion automatique à Sentry [#264].

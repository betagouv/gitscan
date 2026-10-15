## Changelog : hubee (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, hubee a considérablement amélioré la gestion documentaire en permettant aux agents de télécharger et d'archiver les pièces reçues. L'expérience utilisateur a été affinée grâce à des messages d'explication plus clairs en cas de blocage et à une terminologie plus cohérente. Parallèlement, la sécurité et la traçabilité du système ont été renforcées.

### Évolutions fonctionnelles
- **Gestion documentaire** : 
    - Possibilité de télécharger les pièces reçues ([#163](https://github.com/datagouv/hubee/issues/163)).
    - Création d'archives regroupant les pièces reçues pour faciliter la consultation.
    - Possibilité de répondre à un télédossier en y joignant une pièce.
- **Expérience utilisateur (UX)** :
    - Amélioration de l'accompagnement : ajout de messages explicatifs détaillés lorsqu'une action est impossible (ex: téléchargement refusé ou décision bloquée).
    - Mise à jour de la terminologie : utilisation systématique du terme "télédossier" au lieu de "démarche" pour plus de clarté.
    - Ajout d'un bandeau d'information pour orienter les utilisateurs vers le support de la bêta.
- **Interface et corrections** :
    - Amélioration de l'affichage des pages d'erreur (format HTML garanti).
    - Corrections visuelles sur l'alignement des éléments de l'interface et des filtres.

### Évolutions techniques
- **Sécurité et traçabilité** :
    - Renforcement des journaux (logs) : journalisation de l'adresse IP de l'appelant et amélioration de la structure des lignes de requête.
    - Protection des données : masquage des informations sensibles (nonces, adresses) dans les logs.
- **Infrastructure et performance** :
    - Sécurisation des conteneurs : passage à des images Docker "distroless" pour réduire la surface d'attaque.
    - Optimisation de la base de données : limitation du temps de connexion PostgreSQL et configuration pour ne se connecter qu'au nœud primaire.
    - Observabilité : remontée automatique des erreurs des environnements de test (review apps) vers Sentry.
- **Architecture** :
    - Mise à jour majeure des versions de l'API interne (`hub-api-v1`).
    - Refactorisation de la gestion des flux, des états des dossiers et de la signature des événements.

### Autres changements
- **Documentation** : enrichissement de la documentation technique concernant l'authentification et le fonctionnement interne du portail.
- **Maintenance** : nettoyage de code et uniformisation des variables d'environnement dans les processus de test.
